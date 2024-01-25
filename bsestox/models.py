from django.db import models

# Create your models here.
class Stocks(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100, primary_key=True)
    
    val_open = models.TextField(null=True)
    val_close = models.TextField(null=True)
    val_high = models.TextField(null=True)
    val_low = models.TextField(null=True)

    def __str__(self):
        return str(self.name)

class FavStocks(models.Model):
    name = models.OneToOneField(Stocks, on_delete=models.CASCADE, primary_key=True)
    def __str__(self):
        return str(self.name)


class StocksCurrVal(models.Model):
    name = models.OneToOneField(Stocks, on_delete=models.CASCADE, primary_key=True)
    val_curr = models.FloatField()
    date = models.DateField()