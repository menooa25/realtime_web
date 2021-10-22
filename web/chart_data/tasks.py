import random
import time

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
last_price = 1000
second = 0

@shared_task
def get_stock_data():
    global last_price
    global second
    second += 1
    last_price = random.randint(last_price - 5, last_price + 5)
    last_chart_data = {"last_price": last_price, 'time': second}
    async_to_sync(channel_layer.group_send)('chart_channel', {'type': 'send_chart', 'last_chart_data': last_chart_data})
