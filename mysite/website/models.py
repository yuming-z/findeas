from django.db import models

# Create your models here.
class Ticker(models.Model):
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker
    
class Stock(models.Model):
    ticker = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    date = models.DateField()
    open = models.FloatField()
    close = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    volume = models.FloatField()
    dividend = models.IntegerField()
    split = models.FloatField()