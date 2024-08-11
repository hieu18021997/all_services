from typing import Callable, Optional
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText


with beam.Pipeline() as p:
    input = p | 'Log lines' >> beam.io.ReadFromText('gs://apache-beam-samples/shakespeare/kinglear.txt') \
                | beam.Filter(lambda line: line != "")

    input | 'Log fixed lines' >> beam.combiners.Sample.FixedSizeGlobally(10) \
        | beam.FlatMap(lambda sentence: sentence) \
        | beam.Map(print)
    print("=============")
    words = p | 'Log words' >> beam.io.ReadFromText('gs://apache-beam-samples/shakespeare/kinglear.txt') \
                | beam.Filter(lambda word: not word.isspace() or word.isalnum()) \
                | beam.FlatMap(lambda word: word) \
                | 'Log output words' >> beam.Map(print)