import json
import time

from channels.generic.websocket import AsyncWebsocketConsumer


class ChartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('chart_channel', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('chart_channel', self.channel_name)

    async def send_chart(self, event):
        last_chart_data = event['last_chart_data']
        context = json.dumps(last_chart_data)
        await self.send(context)
