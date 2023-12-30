# portfolio/views.py
from django.shortcuts import render
from .models import Stock
import requests

def stock_list(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'portfolio/stock_list.html', context)

def add_stock(request):
    if request.method == 'POST':
        symbol = request.POST['symbol']
        # Use Alpha Vantage API to get real-time stock data
        # Example: https://www.alphavantage.co/documentation/#quote
        api_key = 'YOUR_ALPHA_VANTAGE_API_KEY'
        api_url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(api_url)
        data = response.json()
        stock_data = data.get('Global Quote', {})
        if stock_data:
            stock = Stock(
                symbol=symbol,
                name=stock_data.get('01. symbol', ''),
                quantity=request.POST['quantity'],
                purchase_price=request.POST['purchase_price'],
                purchase_date=request.POST['purchase_date']
            )
            stock.save()
    return render(request, 'portfolio/add_stock.html')
from django.shortcuts import render

# Create your views here.
