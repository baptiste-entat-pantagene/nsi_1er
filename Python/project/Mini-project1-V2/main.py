import requests
import json


request = requests.get('https://fr-en.openfoodfacts.org/api/v0/product/3017620425035.json')
#https://fr-en.openfoodfacts.org/category/pizzas/1.json
#request.json()

dump = request.json()
stat = dump["status_verbose"]

#name = dump["product_name_en"]
name = dump["product"]["product_name_fr"]
#generic_name_fr



print(name)