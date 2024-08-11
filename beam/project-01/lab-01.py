

from typing import Callable, Optional
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def run(
    input_text: str,
    beam_options: Optional[PipelineOptions] = None,
    test: Callable[[beam.PCollection], None] = lambda _: None,
) -> None:
    with beam.Pipeline(options=beam_options) as pipeline:
        elements = (
            pipeline
            | "Create elements" >> beam.Create(["Hello", "World!", input_text])
            | "Print elements" >> beam.Map(print)
        )

        # Used for testing only.
        test(elements)
        # run('hoang')
# def func1(p):
#     print(p)
run('hieu Hoang==========')

# ================================
def func1(str):
  print(str)
  return str    

def func2(str):
  print(f'{str} Hoang van hieu')  
  return ['hoang', 'van', 'hieu']

with beam.Pipeline() as p:
  (p | beam.Create(['Hello Beam'])
   | "print data" >> beam.Map(func1)
   | "tranform" >> beam.Map(func2)
   | "print" >> beam.Map(func1)     
   )