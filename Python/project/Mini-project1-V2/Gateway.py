import requests
import json
import csv

class Gateway:
    def __init__(self, requestMethod:int) -> None:
        """
        modeRequest = 0 -> web request
        modeRequest = 1 -> local file request
        """
        #check request mode
        if requestMethod != 0 and requestMethod != 1:
            raise NotImplementedError("requestMethod !")
        self.requestMode = requestMethod

        if requestMethod == 1:
            self.locaReader = csv.DictReader(open("fr-openfoodfacts-org-products.csv", "r", encoding="utf8", errors="ignore"), delimiter="\t")
            #open(vocab_path, 'r', encoding='utf8', errors='ignore') #errors="ignore" else raise erorr

    
    def requestID(self, productId):
        if self.requestMode == 0:
            url = 'https://fr-en.openfoodfacts.org/api/v0/product/' + str(productId) + '.json'
            getRequests = requests.get(url)
            #https://global.openfoodfacts.org
            self.dump = getRequests.json()

            #verifie l'existence de l'id
            stat = self.dump["status_verbose"]
            if stat != "product found":
                raise NameError()

        elif self.requestMode == 1:
            print("search in progress, in local mode(search in the csv file) it can take a long time...")
            for row in self.locaReader:
                if row["code"] == productId:
                    self.dump = row
                    break
            if self.dump == None:
                raise ValueError
            

        if self.requestMode == 0:
            #["product_name_en"]
            #generic_name_fr
            print(self.dump)
            print("name ->", self.dump["product"]["product_name_fr"])
        elif self.requestMode == 1:
            print("name ->", self.dump["product_name"])

    def requestName(self, name):
        if self.requestMode == 0:
            urlTest = "https://fr-en.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=breakfast_cereals&tagtype_1=nutrition_grades&tag_contains_1=contains&tag_1=A&additives=without&ingredients_from_palm_oil=without&json=true'"
            #url = 'https://fr-en.openfoodfacts.org/api/v0/product/' + str(productId) + '.json'
            getRequests = requests.get(urlTest)
            
            #https://global.openfoodfacts.org
            self.dump = getRequests.json()
            print(self.dump)



