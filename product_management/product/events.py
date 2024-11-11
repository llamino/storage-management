import pika
import json

def send_product_event(product_data, event_type):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='product_events')

    event = {
        'type': event_type,  # "created" یا "updated"
        'data': product_data
    }
    channel.basic_publish(exchange='', routing_key='product_events', body=json.dumps(event))
    connection.close()

    import json
    import requests

def send_event(event_type, data):
    # این تابع به سیستم پیام‌رسانی رویداد ارسال می‌کند
    payload = {'event_type': event_type, 'data': data}
    headers = {'Content-Type': 'application/json'}
    # آدرس و پورت پیام‌رسان را وارد کنید
    url = 'http://event-bus-url/events'
    requests.post(url, headers=headers, data=json.dumps(payload))