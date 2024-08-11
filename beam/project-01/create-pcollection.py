import apache_beam as beam
from apache_beam.io import WriteToText

def show_data(p):
    print(p)
    return p

with beam.Pipeline() as p:
    (p | 'Create words' >> beam.Create(['Hello Beam','It`s introduction'])
        | 'Log words' >> beam.Map(print))

    Pcollection = (p | 'Create numbers' >> beam.Create(range(1, 11))
                    | 'Log numbers' >> beam.Map(show_data))
  
    Pcollection | "write" >> WriteToText('./output')