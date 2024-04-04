from django.contrib import admin

from .models import Ticker, Stock

# Register your models here.
admin.site.register(Ticker)
admin.site.register(Stock)