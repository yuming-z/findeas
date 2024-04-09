from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view

from .models import Ticker, Stock
from .serializer import TickerSerializer, StockSerializer

@api_view(['GET'])
def validate(request):
    '''This function is used to validate the connection to the database.'''

    success = "The connection for data fetching is successful."

    return HttpResponse(status=200, content=success)

@api_view(['GET'])
def query_ticker(request):
    '''
    This function is used to query the database for the ticker data.
    '''

    # Get the parameter value
    ticker_code = request.GET.get('ticker')

    # Switch the ticker code to uppercase
    ticker_code = ticker_code.upper()

    # Query the database for the ticker data
    ticker_data = Ticker.objects.filter(ticker=ticker_code)

    # Serialize the data
    response = TickerSerializer(ticker_data, many=True)

    return JsonResponse(response.data, safe=False)


@api_view(['GET'])
def query_stock(request):
    '''
    This function is used to query the database for stock data.
    '''

    # Get the parameters
    ticker_code = request.GET.get('ticker')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    # Switch the ticker code to uppercase
    ticker_code = ticker_code.upper()

    # Find the ticker id
    ticker = Ticker.objects.get(ticker=ticker_code)

    # Query the database for the ticker data
    ticker_data = Stock.objects.filter(ticker=ticker.id, date__range=[start_date, end_date])

    # Serialize the data
    response = StockSerializer(ticker_data, many=True)

    return JsonResponse(response.data, safe=False)