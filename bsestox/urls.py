from django.urls import path
import bsestox.views as vi


urlpatterns = [
    path("find-stock", vi.checkIfStockExists),
    path("get-stock-history", vi.returnStockHistory),
    path("favourite-stocks", vi.returnFavStocks),
    path("add-to-fav", vi.addCurrStock),
    path("delete-from-fav", vi.deleteFavStock),
    path("top-stocks", vi.getTopStocks)
]