from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stocks, FavStocks, StocksCurrVal
import json


@api_view(["GET"])
def checkIfStockExists(request):
    stock_name = request.GET.get("name")

    if stock_name == None:
        return Response({"Message": "Invalid Request, `name` parameter missing"})

    if Stocks.objects.filter(name=stock_name).exists():
        return Response({"Message": "True"})

    return Response({"Message": "False"})


@api_view(["GET"])
def returnStockHistory(request):
    stock_name = request.GET.get("name")

    if stock_name == None:
        return Response({"Message": "Invalid Request, `name` parameter missing"})

    try:
        stock = Stocks.objects.get(name=stock_name)
        return Response({"Message": stock.val_close})
    except:
        return Response({"Message": "No such stock exists"})


@api_view(["GET"])
def returnFavStocks(request):
    fav_stocks_ref = FavStocks.objects.all()
    fav_stocks_list = []

    for stock in fav_stocks_ref:
        fav_stocks_list.append(stock.name.name)
    return Response({"Message": json.dumps(fav_stocks_list)})


@api_view(["POST"])
def addCurrStock(request):
    stock_name = request.data.get("name")

    if stock_name == None:
        return Response({"Message": "Invalid Request, `name` parameter missing"})

    try:
        stock = Stocks.objects.get(name=stock_name)
        FavStocks.objects.create(name=stock)
    except:
        return Response({"Message": "Some error occured"})
    return Response({"Message": "Stock added succesfully"})


@api_view(["POST"])
def deleteFavStock(request):
    stock_name = request.data.get("name")

    if stock_name == None:
        return Response({"Message": "Invalid Request, `name` parameter missing"})

    try:
        stock = Stocks.objects.get(name=stock_name)
        stock.favstocks.delete()
    except:
        return Response({"Message": "Some error occured"})

    return Response({"Message": "Stock deleted from favourites succesfully"})


@api_view(["GET"])
def getTopStocks(request):
    n = int(request.GET.get("n"))

    cnt = StocksCurrVal.objects.all().count()
    n = min(cnt, n)

    stocks = StocksCurrVal.objects.order_by("-val_curr")[:n]
    top_stocks_info = []
    for stock in stocks:
        top_stocks_info.append(
            {
                "name": stock.name.name,
                "value": stock.val_curr,
                "date": stock.date.strftime("%d-%m-%Y"),
            }
        )

    return Response({"Message": json.dumps(top_stocks_info)})
