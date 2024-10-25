#https://airflow.apache.org/docs/docker-stack/build.html
FROM apache/airflow

USER root
COPY ./requirements.txt requirements.txt
COPY --chown=airflow:root ./dags/test_dag.py /opt/airflow/dags

USER airflow
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r ./requirements.txt
USER root
RUN sudo apt-get update \
  && apt-get install -y --no-install-recommends \
         vim \
  && apt-get autoremove -yqq --purge \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER chown -R airflow:airflow /opt/airflow/logs
USER chmod -R 755 /opt/airflow/logs

USER airflow
EXPOSE 8080
EXPOSE 8793
EXPOSE 5555
