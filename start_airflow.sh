docker run -d -p 8080:8080 -v ./dags:/usr/local/airflow/dags -v ./plugins:/usr/local/airflow/plugins -v ./requirements.txt:/requirements.txt --name airflow puckel/docker-airflow webserver
