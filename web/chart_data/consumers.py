import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChartConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('chart_channel', self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard('chart_channel', self.channel_name)

    async def send_chart(self, event):
        print(event)
        last_price = event['last_price']
        context = json.dumps({'last_price': last_price})
        await self.send(context)
