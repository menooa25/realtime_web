import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

app = Celery('web')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.beat_schedule = {
    'get_stock_data_1s': {
        'task': 'chart_data.tasks.get_stock_data',
        'schedule': 1,
    }
}
app.autodiscover_tasks()
