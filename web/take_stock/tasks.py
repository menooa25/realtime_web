import random
import time
#
# from asgiref.sync import async_to_sync
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()
last_price = 1000
second = 0


@shared_task
def get_take_stocks():
    global last_price
    global second
    second += 1
    last_price = random.randint(last_price - 5, last_price + 5)
    take_stocks = {'last_price': last_price}
    async_to_sync(channel_layer.group_send)('take_stocks_channel', {'type': 'send_stock', 'take_stocks': take_stocks})
