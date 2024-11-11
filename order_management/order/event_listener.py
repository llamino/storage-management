import pika
import json
from .models import ProductData

def callback(ch, method, properties, body):
    event = json.loads(body)
    event_type = event['type']
    product_data = event['data']

    if event_type == 'created':
        ProductData.objects.create(
            product_id=product_data['id'],
            name=product_data['name'],
            price=product_data['price']
        )
    elif event_type == 'updated':
        product = ProductData.objects.get(product_id=product_data['id'])
        product.name = product_data['name']
        product.price = product_data['price']
        product.save()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='product_events')
channel.basic_consume(queue='product_events', on_message_callback=callback, auto_ack=True)

print('Waiting for product events...')
channel.start_consuming()