from rest_framework import serializers

from .models import Ticker, Stock

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ['ticker']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['date', 'open', 'high', 'low', 'close', 'volume']