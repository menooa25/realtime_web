from django.shortcuts import render


def take_stock_view(request):
    return render(request, 'take_stock/take_stock.html')
