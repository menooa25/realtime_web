import json
import time

from channels.generic.websocket import AsyncWebsocketConsumer


class TakeStocksConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('take_stocks_channel', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('take_stocks_channel', self.channel_name)

    async def send_stock(self, event):
        last_chart_data = event['take_stocks']
        context = json.dumps(last_chart_data)
        await self.send(context)
