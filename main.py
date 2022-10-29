import requests
from tinydb import TinyDB

url = "http://127.0.0.1:8000/add_product/"

db = TinyDB('db.json')
tables = db.tables()

for file_name in tables:
    table = db.table(name=file_name)
    products = table.all()
    for product in products:
        payload = {}
        for key, value in product.items():
            payload[key] = value
        
        r = requests.post(url, data=payload)
        print(r.status_code)