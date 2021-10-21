import datetime
import random

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
last_price = 1000


@shared_task
def get_stock_data():
    global last_price
    last_price = random.randint(last_price - 5, last_price + 5)
    async_to_sync(channel_layer.group_send)('chart_channel', {'type': 'send_chart', 'last_price': last_price})
