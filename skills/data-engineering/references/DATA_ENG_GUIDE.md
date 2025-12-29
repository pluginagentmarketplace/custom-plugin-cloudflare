# Data Engineering Guide

## ETL Pipelines

```python
# Airflow DAG
from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG('etl_pipeline', schedule='@daily') as dag:
    extract = PythonOperator(task_id='extract', python_callable=extract_data)
    transform = PythonOperator(task_id='transform', python_callable=transform_data)
    load = PythonOperator(task_id='load', python_callable=load_data)

    extract >> transform >> load
```

## dbt Models

```sql
-- models/staging/stg_users.sql
SELECT
    id,
    name,
    created_at
FROM {{ source('raw', 'users') }}
```

---

*Cloudflare Plugin - Data Engineering Skill*
