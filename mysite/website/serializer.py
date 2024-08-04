from rest_framework import serializers

from .models import Ticker, Stock

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ['ticker']

class StockSimplifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['date', 'open', 'high', 'low', 'close', 'volume']

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['date', 'open', 'high', 'low', 'close', 'volume', 'ub', 'lb', 'macd', 'macd_signal', 'rsi', 'weakMACD', 'macd_diff', 'flag']