import apache_beam as beam

durations = ['annual', 'biennial', 'perennial']

def by_duration(plant, num_partitions):
    return durations.index(plant['duration'])

with beam.Pipeline() as pipeline:
    annuals, biennials, perennials = (
        pipeline
        | 'Gardening plants' >> beam.Create([
            {'icon': '🍓', 'name': 'Strawberry', 'duration': 'perennial'},
            {'icon': '🥕', 'name': 'Carrot', 'duration': 'biennial'},
            {'icon': '🍆', 'name': 'Eggplant', 'duration': 'perennial'},
            {'icon': '🍅', 'name': 'Tomato', 'duration': 'annual'},
            {'icon': '🥔', 'name': 'Potato', 'duration': 'perennial'},
        ])
        | 'Partition' >> beam.Partition(by_duration, len(durations))
    )

    annuals | 'Annuals' >> beam.Map(lambda x: print('annual: {}'.format(x)))
    biennials | 'Biennials' >> beam.Map(
        lambda x: print('biennial: {}'.format(x)))
    perennials | 'Perennials' >> beam.Map(
        lambda x: print('perennial: {}'.format(x)))
