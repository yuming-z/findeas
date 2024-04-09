from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404

from rest_framework.decorators import api_view

from django.utils import dateparse

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
    try:
        ticker_data = get_object_or_404(Ticker, ticker=ticker_code)
    except Http404:
        return HttpResponse(status=404, content="Ticker not found.")

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

    # Change the dates to datetime objects
    start_date = dateparse.parse_date(start_date)
    end_date = dateparse.parse_date(end_date)

    if start_date is None or end_date is None:
        return HttpResponse(status=400, content="Invalid date format.")

    # Find the ticker id
    try:
        ticker = get_object_or_404(Ticker, ticker=ticker_code)
    except Http404:
        return HttpResponse(status=404, content="Ticker not found.")

    # Check if the start date exists in record
    earlies_start_date = Stock.objects.filter(ticker=ticker.id).order_by('date').first().date
    if start_date < earlies_start_date:
        return HttpResponse(status=400, content="Start date is earlier than the earliest date in record.")

    # Check if the end date exists the maximum end date in record
    max_end_date = Stock.objects.filter(ticker=ticker.id).order_by('-date').first().date
    if end_date > max_end_date:
        print("End date is later than the latest date in record. The end date is changed to the latest date in record.")
        end_date = max_end_date

    # Query the database for the ticker data
    ticker_data = Stock.objects.filter(ticker=ticker.id, date__range=[start_date, end_date])

    # Serialize the data
    response = StockSerializer(ticker_data, many=True)

    return JsonResponse(response.data, safe=False)