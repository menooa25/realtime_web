from django.urls import path
from .consumers import ChartConsumer

ws_urlpatterns = [
    path('ws/chart_data/', ChartConsumer.as_asgi(),name='chart_data')
]
