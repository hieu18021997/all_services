from typing import Callable, Optional
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText

with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | 'Gardening plants' >> beam.Create([
            '🍓Strawberry 🥕Carrot 🍆Eggplant',
            '🍅Tomato 🥔Potato',
        ])
        | 'Split words' >> beam.FlatMap(str.split)
        | beam.Map(print))

print("="*30)
def split_words(text):
    return text.split(',')

with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | 'Gardening plants' >> beam.Create([
            '🍓Strawberry,🥕Carrot,🍆Eggplant',
            '🍅Tomato,🥔Potato',
        ])
        | 'Split words' >> beam.FlatMap(split_words)
        | beam.Map(print))
print("="*30)
with beam.Pipeline() as pipeline:
    plants = (
        pipeline
        | 'Gardening plants' >> beam.Create([
            ['🍓Strawberry', '🥕Carrot', '🍆Eggplant'],
            ['🍅Tomato', '🥔Potato'],
        ])
        | 'Flatten lists' >> beam.FlatMap(lambda elements: elements)
        | beam.Map(print))