from django.db import models

from .validators import validate_weakMACD, validate_one_hot_encoding

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

    # Analytic metrics
    flags = {
        "Yellow": "In warning",
        "Green": "Safe",
        "Red": "In danger"
    }

    # bollinger bands
    sma = models.FloatField(blank=True)
    sd = models.FloatField(blank=True)
    ub = models.FloatField(blank=True)
    lb = models.FloatField(blank=True)

    # macd
    macd = models.FloatField()
    macd_signal = models.FloatField()

    # gain/loss
    gain = models.FloatField()
    loss = models.FloatField()
    avg_gain = models.FloatField(blank=True)
    avg_loss = models.FloatField(blank=True)

    # rsi
    rs = models.FloatField(blank=True)
    rsi = models.FloatField(blank=True)
    rsi_6 = models.FloatField(blank=True)
    rsi_12 = models.FloatField(blank=True)

    # Weak MACD
    weakMACD = models.IntegerField(validators=[validate_weakMACD])

    # MACD difference
    macd_diff = models.FloatField()

    # Flag determinants
    # Use 0 and 1 --> one-hot-encoding
    # the data will eventually go to the AI engine

    # precausion day = 5
    isLoss = models.IntegerField(validators=[validate_one_hot_encoding], default=0, null=True)
    isCausion = models.IntegerField(validators=[validate_one_hot_encoding], default=0, null=True)
    # precausion day = 1
    isGain = models.IntegerField(validators=[validate_one_hot_encoding], default=0, null=True)
    isSafe = models.IntegerField(validators=[validate_one_hot_encoding], default=0, null=True)

    # flag
    flag = models.CharField(max_length=10, choices=flags)