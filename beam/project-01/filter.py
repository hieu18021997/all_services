import apache_beam as beam

def is_perennial(plant):
    return plant['duration'] == 'perennial'

with beam.Pipeline() as pipeline:
    perennials = (
        pipeline
        | 'Gardening plants' >> beam.Create([
            {
                'icon': '🍓', 'name': 'Strawberry', 'duration': 'perennial'
            },
            {
                'icon': '🥕', 'name': 'Carrot', 'duration': 'biennial'
            },
            {
                'icon': '🍆', 'name': 'Eggplant', 'duration': 'perennial'
            },
            {
                'icon': '🍅', 'name': 'Tomato', 'duration': 'annual'
            },
            {
                'icon': '🥔', 'name': 'Potato', 'duration': 'perennial'
            },
        ])
        | 'Filter perennials' >> beam.Filter(is_perennial)
        )
    
    show = (perennials
            | beam.Map(print))
    
    filter2 = (perennials
            | 'Filter lamda' >> beam.Filter(lambda x : x['name'] == 'Eggplant')
            | 'print 2'  >> beam.Map(print))

