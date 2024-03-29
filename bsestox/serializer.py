from rest_framework import serializers
from .models import Stocks


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = "__all__"
