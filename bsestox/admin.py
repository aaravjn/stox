from django.contrib import admin
from .models import Stocks, FavStocks


# Register your models here.
admin.site.register(Stocks)
admin.site.register(FavStocks)