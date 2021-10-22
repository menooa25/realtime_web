
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chart_data.urls')),
    path('take-stock', include('take_stock.urls')),
]
