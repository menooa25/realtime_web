from django.urls import path

from take_stock.views import take_stock_view

urlpatterns = [
    path('', take_stock_view, name='take_stock')
]
