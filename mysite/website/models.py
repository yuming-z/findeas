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

class Indicator(models.Model):

    flags = {
        "Yellow": "In warning",
        "Green": "Safe",
        "Red": "In danger"
    }

    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    # bollinger bands
    sma = models.FloatField()
    sd = models.FloatField()
    ub = models.FloatField()
    lb = models.FloatField()

    macd = models.FloatField()
    macd_signal = models.FloatField()

    gain = models.FloatField()
    loss = models.FloatField()
    avg_gain = models.FloatField()
    avg_loss = models.FloatField()
    rs = models.FloatField()

    rsi = models.FloatField()
    rsi_6 = models.FloatField()
    rsi_12 = models.FloatField()

    weakMACD = models.IntegerField(choices=[-1, 0, 1])

    macd_diff = models.FloatField()

    # Flag determinants
    # Use 0 and 1 --> one-hot-encoding
    # the data will eventually go to the AI engine
    # precausion day = 5
    loss = models.IntegerField(choices=[0, 1])
    causion = models.IntegerField(choices=[0, 1])
    # precausion day = 1
    gain = models.IntegerField(choices=[0, 1])
    safe = models.IntegerField(choices=[0, 1])

    # flag
    flag = models.CharField(max_length=10, choices=flags)