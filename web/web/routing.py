from django.urls import path

from chart_data.consumers import ChartConsumer
from take_stock.consumers import TakeStocksConsumer

ws_urlpatterns = [
    path('ws/chart_data/', ChartConsumer.as_asgi(), name='chart_data'),
    path('ws/take_stocks/', TakeStocksConsumer.as_asgi(), name='take_stocks')
]
