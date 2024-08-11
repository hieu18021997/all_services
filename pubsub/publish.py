import os
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='vhm-dataops-prod',
    topic='vhm-real-estate-topic',  # Set this to something appropriate.
)
#publisher.create_topic(name=topic_name)
for i in range(10000):
    future = publisher.publish(topic_name,b'My first message!' )
    print(i) 
    future.result()
