### Project Setup Guide:

* Import the docker image of the application for `Linux` using the following command
```
docker pull aaravjn/stock-server
```

* Run a container from the docker image using the below command.
```
docker run -it -p 8000:8000 stock-server
```

The application will download and insert the past `5` days stock data from BSE. The number was kept limited to `5` because it takes a lot of time to process data because of a large number of entries.


### Usage guide
* A GET route for the top `n` stocks.
Example:-
```
http://0.0.0.0:8000/bsestox/top-stocks?n=10
```

Output:-
```
"Message": "[{\"name\": \"KSPL281022\", \"value\": 1147000.0, \"date\": \"18-01-2024\"}, {\"name\": \"MSFL31022\", \"value\": 1139690.0, \"date\": \"24-01-2024\"}, {\"name\": \"ECE30922A\", \"value\": 1113500.0, \"date\": \"24-01-2024\"}]"
```


* A GET route to find stocks by name.
Example:-
```
http://0.0.0.0:8000/bsestox/find-stock?name=ABB LTD.
```

* A GET route to get stock price history list
```
http://0.0.0.0:8000/bsestox/get-stock-history?name=ABB LTD.
```

Output:-
```
"Message": "4731.00 4771.80 4755.80 4819.65 4710.65"
```

* A POST route to add a stock to favourites.
Example:-
```
http://0.0.0.0:8000/bsestox/add-to-fav

PARAMETERS: name=ABB LTD.
```

* A GET route to see favourite stocks.
Example:-
```
http://0.0.0.0:8000/bsestox/delete-from-fav

PARAMETERS: name=ABB LTD.
```

* A GET route to see favourite stocks.
Example:-
```
http://0.0.0.0:8000/bsestox/favourite-stocks
```

Output:-
```
"Message": "[ANDHRA PETRO]"
```