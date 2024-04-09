from rest_framework import serializers

from .models import Ticker, Stock

class TickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticker
        fields = ['ticker']