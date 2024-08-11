from typing import Callable, Optional
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText


def split_element_1(text):
    a = []
    for word in text.split(','):
        a.append(word)
    return a

def split_element_2(text):
    for word in text.split(','):
        yield word
    
with beam.Pipeline() as p:
    plants = (
        p | 'Gardening plants' >> beam.Create([
            '🍓Strawberry,🥕Carrot,🍆Eggplant',
            '🍅Tomato,🥔Potato',
            ])
        | 'Split words' >> beam.ParDo(split_element_1)
        | beam.Map(print)
    )

    p2 = (  p |  'Gardening plants 2' >> beam.Create([
            '🍓Strawberry,🥕Carrot,🍆Eggplant',
            '🍅Tomato,🥔Potato',
            ])
        | 'Split words 2' >> beam.ParDo(split_element_2)
        | 'print 2' >> beam.Map(print))