# client = bigquery.Client()
# dataset_id = 'my_dataset'
dataset_ref = client.dataset(dataset_id)
job_config = bigquery.LoadJobConfig()
job_config.autodetect = True
job_config.skip_leading_rows = 1
# The source format defaults to CSV, so the line below is optional.
job_config.source_format = bigquery.SourceFormat.CSV

load_job = client.load_table_from_uri(
    'gs://case-fitbit/sample-user-data-casefitbit.csv',
    dataset_ref.table('us_states'),
    job_config=job_config)  # API request

assert load_job.job_type == 'load'

load_job.result()  # Waits for table load to complete.

assert load_job.state == 'DONE'
assert client.get_table(dataset_ref.table('new_table')).num_rows == 50