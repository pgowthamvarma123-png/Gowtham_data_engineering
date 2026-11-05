from google.cloud import bigquery

client = bigquery.Client()
table_id = "product2_dataset.orders"
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV,
    skip_leading_rows=1,
    autodetect=True,        
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

job = client.load_table_from_uri(
    "gs://gowtham_bkt1/orders.csv",
    table_id,
    job_config=job_config
)

job.result()

print("Load completed")
