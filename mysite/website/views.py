from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404

from rest_framework.decorators import api_view

from django.utils import dateparse

from .models import Ticker, Stock
from .serializer import TickerSerializer, StockSerializer, StockSimplifiedSerializer

def is_exist_ticker(ticker_code):
    '''
    This function is used to validate whether the given ticker code exists in the data storage.

    Parameters:
    - ticker_code: str

    Returns:
    - the Ticker object if the ticker code exists
    '''

    # Convert the ticker code to uppercase
    ticker_code = ticker_code.upper()

    # Query the database for the ticker data
    try:
        ticker_data = get_object_or_404(Ticker, ticker=ticker_code)
    except Http404:
        return HttpResponse(status=404, content="Ticker not found.")
    return ticker_data

def is_valid_date_range(start_date, end_date, ticker: Ticker):
    '''
    This function is used to validate the date range for the stock data.

    Parameters:
    - start_date: str
    - end_date: str
    - ticker: Ticker

    Exceptions:
    - If the date format is invalid
    - If the start date is earlier than the earliest date in record
    '''

    # Convert the dates to datetime objects
    start_date = dateparse.parse_date(start_date)
    end_date = dateparse.parse_date(end_date)

    if start_date is None or end_date is None:
        return HttpResponse(status=400, content="Invalid date format.")

    # Check if the start date exists in record
    earlies_start_date = Stock.objects.filter(ticker=ticker.id).order_by('date').first().date
    if start_date < earlies_start_date:
        return HttpResponse(status=400, content="Start date is earlier than the earliest date in record.")

    # Check if the end date exists the maximum end date in record
    # If the end date exceeds the maximum end date, change the end date to the maximum end date
    max_end_date = Stock.objects.filter(ticker=ticker.id).order_by('-date').first().date
    if end_date > max_end_date:
        print("End date is later than the latest date in record.")
        print("The end date is changed to the latest date in record.")
        end_date = max_end_date

    return start_date, end_date

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

    # Get the ticker object
    ticker_data = is_exist_ticker(ticker_code)

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
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')

    # Get the Ticker object
    ticker = is_exist_ticker(ticker_code)

    # Validate the date range
    is_valid_date_range(start_date, end_date, ticker)

    # Query the database for the ticker data
    ticker_data = Stock.objects.filter(ticker=ticker.id, date__range=[start_date, end_date])

    # Serialize the data
    response = StockSimplifiedSerializer(ticker_data, many=True)

    return JsonResponse(response.data, safe=False)

@api_view(['GET'])
def query_stock_analytic_data(request):
    '''
    This function is used to fetch the analytic data processed for the stock.

    The web request will take in the ticker code and the date range,
    and return the analytic data for the stock in that date range.

    The analytic data includes:
    - Bollinger Bands
    - MACD
    - RSI
    - Weak MACD
    - MACD Difference
    '''

    # Get the parameters
    ticker_code = request.GET.get('ticker')
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')

    # Get the Ticker object
    ticker = is_exist_ticker(ticker_code)

    # Validate the date range
    start_date, end_date = is_valid_date_range(start_date, end_date, ticker)

    # Query the database for the ticker data
    ticker_data = Stock.objects.filter(ticker=ticker.id, date__range=[start_date, end_date])

    # Serialize the data
    response = StockSerializer(ticker_data, many=True)

    return JsonResponse(response.data, safe=False)