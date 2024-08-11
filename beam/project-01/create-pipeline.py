import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

beam_options = PipelineOptions(
    runner='DataflowRunner',
    project='my-project-id',
    job_name='unique-job-name',
    temp_location='gs://my-bucket/temp',
)

with beam.Pipeline(beam_options) as p:
    pass  # build your pipeline here


pipeline = beam.Pipeline(options=beam_options)
