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
    
    stage_oplmain_to_redshift = StageToRedshiftOperator(
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

    stage_federations_to_redshift = StageToRedshiftOperator(
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

    deduplicate_staging_oplmain = LoadFactOperator(
        task_id='Deduplicate_staging_oplmain',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.staging_oplmain_dedupe_insert,
        target_table='public.staging_oplmain_deduplicated'
    )
    
    load_staging_oplmain_weight_class_table = LoadDimensionOperator(
        task_id='Load_staging_oplmain_weight_class_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.staging_weight_class_table_insert,
        target_table='public.staging_oplmain_weight_class',
        target_columns=None,
        truncate=True
    )
   
    load_dimension_weight_class_tabletable = LoadDimensionOperator(
        task_id='Load_dimension_weight_class_tabletable',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.weight_class_table_insert,
        target_table='public.weight_class',
        target_columns=['federation_meet_key','weight_class_from_inclusive','weight_class_to_exclusive'],
        truncate=True
    )  
     
    load_dimension_lifter_table = LoadDimensionOperator(
        task_id='Load_dimension_lifter_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.lifter_table_insert,
        target_table='public.lifter',
        target_columns=['Name','Sex'],
        truncate=True
    )    

    load_dimension_age_class_table = LoadDimensionOperator(
        task_id='Load_dimension_age_class_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.age_class_table_insert,
        target_table='public.age_class',
        target_columns=['age_class_from','age_class_to'],
        truncate=True
    )

    load_dimension_birth_year_class_table = LoadDimensionOperator(
        task_id='Load_dimension_birth_year_class_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.birth_year_class_table_insert,
        target_table='public.birth_year_class',
        target_columns=['birth_year_class_from','birth_year_class_to'],
        truncate=True
    )    

    load_dimension_federation_meet_table = LoadDimensionOperator(
        task_id='Load_dimension_federation_meet_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.federation_meet_table_insert,
        target_table='public.federation_meet',
        target_columns=None,
        truncate=True
    )  
    
    load_dimension_federation_table = LoadDimensionOperator(
        task_id='Load_dimension_federation_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.federation_table_insert,
        target_table='public.federation',
        target_columns=None,
        truncate=True
    )  
    
    load_dimension_date_table = LoadDimensionOperator(
        task_id='Load_dimension_date_table',
        redshift_conn_id=redshift_conn_id,
        sql_query=SqlQueries.date_table_insert,
        target_table='public.date',
        target_columns=None,
        truncate=True
    )        
    


    # run_quality_checks = DataQualityOperator(
    #     task_id='Run_data_quality_checks',
    #     redshift_conn_id=redshift_conn_id,
    #     data_quality_queries=get_data_quality_queries()
    # )

    end_operator = DummyOperator(task_id='Stop_execution')

    start_operator >> [stage_oplmain_to_redshift,stage_federations_to_redshift]
    
    stage_oplmain_to_redshift >> deduplicate_staging_oplmain
    
    deduplicate_staging_oplmain >> [load_staging_oplmain_weight_class_table,load_dimension_lifter_table,load_dimension_age_class_table,load_dimension_birth_year_class_table,load_dimension_federation_meet_table,load_dimension_date_table]
    
    load_staging_oplmain_weight_class_table >> load_dimension_weight_class_tabletable
    
    stage_federations_to_redshift >> load_dimension_federation_table
    [load_dimension_weight_class_tabletable, load_dimension_lifter_table,load_dimension_age_class_table,load_dimension_birth_year_class_table,load_dimension_federation_meet_table,load_dimension_date_table,load_dimension_federation_table] >> end_operator


