from rest_framework import serializers
from .models import Stocks, FavStocks


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = "__all__"


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavStocks
        fields = "__all__"