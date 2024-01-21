from datetime import date, timedelta
import requests
from zipfile import ZipFile
import os

HISTORY_LENGTH = 5

def import_data():
    print("Downloading BSE stocks data....")

    count = 0
    i = 1
    while count < HISTORY_LENGTH:
        dt = date.today() - timedelta(i)
        file_name = f"{str(dt.day).zfill(2)}{str(dt.month).zfill(2)}{str(dt.year)[2:]}"
        
        if os.path.exists(f"./bse_stocks_data/EQ{file_name}.CSV"):
            return
        
        url = f'https://www.bseindia.com/download/BhavCopy/Equity/EQ{file_name}_CSV.ZIP'

        # Including headers to make the request look like a browser request
        # BSE blocks all non-browser requests (This is a speculation)
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "TE": "trailers"
        }
        response = requests.get(url=url, headers=header)

        if response.status_code == 200:
            with open(f'./bse_stocks_data/{file_name}.zip', 'wb') as f:
                f.write(response.content)
            print("Succesfully downloaded the file", file_name)
            count += 1

            with ZipFile(f'./bse_stocks_data/{file_name}.zip', 'r') as zObject:
                zObject.extract(f"EQ{file_name}.CSV", path="./bse_stocks_data/")
            
            os.remove(f'./bse_stocks_data/{file_name}.zip')
        else:
            print("Could not import data for:", dt.strftime("%d-%m-%Y"))

        i += 1
    
    print("\n")


def insert_data():
    print("\nInserting data in the database")

