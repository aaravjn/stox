from django.contrib import admin
from .models import Stocks, FavStocks, StocksCurrVal


# Register your models here.
admin.site.register(Stocks)
admin.site.register(FavStocks)
admin.site.register(StocksCurrVal)
