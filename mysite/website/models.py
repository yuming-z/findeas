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
    sma = models.FloatField(blank=True, null=True)
    sd = models.FloatField(blank=True, null=True)
    ub = models.FloatField(blank=True, null=True)
    lb = models.FloatField(blank=True, null=True)

    # macd
    macd = models.FloatField(blank=True, null=True)
    macd_signal = models.FloatField(blank=True, null=True)

    # gain/loss
    gain = models.FloatField(blank=True, null=True)
    loss = models.FloatField(blank=True, null=True)
    avg_gain = models.FloatField(blank=True, null=True)
    avg_loss = models.FloatField(blank=True, null=True)

    # rsi
    rs = models.FloatField(blank=True, null=True)
    rsi = models.FloatField(blank=True, null=True)
    rsi_6 = models.FloatField(blank=True, null=True)
    rsi_12 = models.FloatField(blank=True, null=True)

    # Weak MACD
    weakMACD = models.IntegerField(validators=[validate_weakMACD], blank=True, null=True)

    # MACD difference
    macd_diff = models.FloatField(blank=True, null=True)

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
    flag = models.CharField(max_length=10, choices=flags, default="Green")