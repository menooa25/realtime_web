import datetime

from celery import shared_task


@shared_task
def get_stock_data():
    print(f'{datetime.datetime.now()} + + + + + ++ + + ++ + ')
