import random

from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

class TakeStock:
    def __init__(self, name, _min, _max):
        self.name = name
        self._min = _min
        self._max = _max
        self.__high = -1
        self.__low = -1
        self.__open = -1
        self.__close = -1
        self.__deference = 0

    def order(self, price):
        if self._min <= price <= self._max:
            self.__set_price(price)

    def __set_price(self, price):
        if self.__open == -1:
            self.__initial_price(price)
        else:
            self.__deference = price - self.__close
            self.__close = price
            if price > self.__low:
                self.__high = price
            elif price < self.__high:
                self.__low = price

    def __initial_price(self, price):
        self.__open = price
        self.__close = price
        self.__low = price
        self.__high = price

    def __str__(self):
        return str({"name": self.name,
                    "open": self.__open,
                    "min": self._min,
                    "max": self._max,
                    "low": self.__low,
                    "high": self.__high,
                    "close": self.__close,
                    "deference": self.__deference})

    def as_dict(self):
        return {"name": self.name,
                "open": self.__open,
                "min": self._min,
                "max": self._max,
                "low": self.__low,
                "high": self.__high,
                "close": self.__close,
                "deference": self.__deference}


fulad = TakeStock('فولاد', 125, 135)
verazi = TakeStock('ورازی', 200, 210)
shalord = TakeStock('شلرد', 390, 400)
zagros = TakeStock('زاگرس', 500, 510)


def generate_order(stocks):
    updated_stock = []
    for stock in stocks:
        stock.order(random.randint(stock._min, stock._max))
        updated_stock.append(stock.as_dict())
    return updated_stock



@shared_task
def get_take_stocks():
    async_to_sync(channel_layer.group_send)('take_stocks_channel', {'type': 'send_stock', 'take_stocks': generate_order([fulad, verazi, shalord, zagros])})
