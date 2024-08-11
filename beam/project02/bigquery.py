import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io.gcp.internal.clients import bigquery


# project-id:dataset_id.table_id
table_spec_text = 'vhm-dataops-prod.VHM_TEMP.data-project-list'
table_spec = bigquery.TableReference(
    projectId='vhm-dataops-prod',
    datasetId='VHM_TEMP',
    tableId='data-project-list')

# with beam.Pipeline() as p:
#     l1 = (p 
#         | 'ReadTable' >> beam.io.ReadFromBigQuery(table=table_spec_text)
#         # | 'Show data' >> beam.Map(print)
#     )
#     result = p.run()
#     result.wait_until_finish()

with beam.Pipeline() as p:
    max_temperatures = (
                p
                | 'QueryTable' >> beam.io.ReadFromBigQuery(
                    query='SELECT max_temperature FROM '\
                        '[apache-beam-testing.samples.weather_stations]')
    # Each row is a dictionary where the keys are the BigQuery columns
    | beam.Map(lambda elem: elem['max_temperature']))