from typing import Callable, Optional
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

beam_options = PipelineOptions(
    # runner='DataflowRunner',
    # project='my-project-id',
    # job_name='unique-job-name',
    # temp_location='gs://my-bucket/temp',
)

with beam.Pipeline(options=beam_options) as p:

    # Read the text file[pattern] into a PCollection.
    lines = p | 'Read' >> ReadFromText('./data-temp.txt') \
            | beam.Filter(lambda line: "#" in line)

    # Write the output using a "Write" transform that has side effects.
    # pylint: disable=expression-not-assigned
    output = lines | 'Write' >> WriteToText('./data-out.txt')


    result = p.run()
    result.wait_until_finish()