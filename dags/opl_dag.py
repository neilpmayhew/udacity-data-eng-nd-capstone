from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries,get_data_quality_queries

# AWS_KEY = os.environ.get('AWS_KEY')
# AWS_SECRET = os.environ.get('AWS_SECRET')

default_args = {
    'owner': 'NeilPMayhew',
    'start_date': datetime(2018, 11, 1),
    'depends_on_past':False,
    'retries':3,
    'retry_delay': timedelta(minutes=5),
    'catchup':False,
    'email_on_retry':False
}

redshift_conn_id = 'redshift'
s3_region='eu-west-2'
s3_bucket='udacity-dend-nm'
aws_credentials_id='aws_credentials'

# use context manager for dag
with DAG('opl_dag',
          default_args=default_args,
          description='Stage data into redshift, transform and load into dimensional model',
          schedule_interval=None,
          catchup=False,
        ) as dag:
    
    start_operator = DummyOperator(task_id='Begin_execution',  dag=dag)
    
    stage_events_to_redshift = StageToRedshiftOperator(
        task_id='Stage_oplmain',
        s3_region=s3_region,
        s3_bucket=s3_bucket,
        s3_key='opl_data/openpowerlifting-2020-01-03.csv',
        redshift_conn_id=redshift_conn_id,
        aws_credentials_id=aws_credentials_id,
        s3_format='CSV',
        s3_format_args="IGNOREHEADER 1",
        staging_table='staging_oplmain'
    )

    stage_songs_to_redshift = StageToRedshiftOperator(
        task_id='Stage_federations',
        s3_region=s3_region,
        s3_bucket=s3_bucket,
        s3_key='federation_data/federations.csv',
        redshift_conn_id=redshift_conn_id,
        aws_credentials_id=aws_credentials_id,
        s3_format='CSV',
        s3_format_args="IGNOREHEADER 1",
        staging_table='staging_federation'
    )

    Deduplicate_data_staging_oplmain = LoadFactOperator(
        task_id='Deduplicate_data_staging_oplmain',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.staging_oplmain_dedupe_insert,
        target_table='public.staging_oplmain_deduplicated'
    )

    load_user_dimension_table = LoadDimensionOperator(
        task_id='Load_lifter_dim_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.lifter_table_insert,
        target_table='public.lifter(Name,Sex)',
        truncate=True
    )

    # load_song_dimension_table = LoadDimensionOperator(
    #     task_id='Load_song_dim_table',
    #     redshift_conn_id=redshift_conn_id,
    #     sql_query=SqlQueries.song_table_insert,
    #     target_table='public.songs',
    #     truncate=True
    # )

    # run_quality_checks = DataQualityOperator(
    #     task_id='Run_data_quality_checks',
    #     redshift_conn_id=redshift_conn_id,
    #     data_quality_queries=get_data_quality_queries()
    # )

    end_operator = DummyOperator(task_id='Stop_execution')

    start_operator >> [stage_events_to_redshift,stage_songs_to_redshift,Deduplicate_data_staging_oplmain]

    [stage_events_to_redshift,stage_songs_to_redshift,Deduplicate_data_staging_oplmain] >> load_user_dimension_table
    
    load_user_dimension_table >> end_operator


