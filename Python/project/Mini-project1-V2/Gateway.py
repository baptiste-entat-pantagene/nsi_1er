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
                raise NameError("id not found !")

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
            return self.dump
        elif self.requestMode == 1:
            return self.dump

    def requestName(self, productName):
        if self.requestMode == 0:
            #urlTest = "https://fr-en.openfoodfacts.org/cgi/search.pl?search_terms=nutella&search_simple=1&action=process&json=true"
            url = 'https://fr-en.openfoodfacts.org/cgi/search.pl?search_terms=' + str(productName) + '&search_simple=1&action=process&json=true'
            getRequests = requests.get(url)
            self.dump = getRequests.json()
            return self.dump
        elif self.requestMode == 1:
            print("search in progress, in local mode(search in the csv file) it can take a long time...")
            for row in self.locaReader:
                if row["product_name"] == productName:
                    self.dump = row
                    return self.dump
            raise ValueError()


    def cleanDump(self, dump=None):
        """
        if dump==None -> use the last dump
        """
        if dump == None:
            if self.dump == None:
                raise NotImplementedError("please initialize dump before clean dump")
            else:
                dump = self.dump

        if self.requestMode == 0:
            if "products" in dump:
                return dump["products"]
            elif "product" in dump:
                return dump["product"]
            else:
                return dump
        elif self.requestMode == 1:
            return dump #no need for modification(already only one article)
    
    def getProductInDump(self, dump, number=0):
        if self.requestMode == 0:
            try:
                return dump[number]
            except:
                return dump
        elif self.requestMode == 1:
            return dump #there is already only one article
    
    def getProductFacts(self, productDump, option=(None)):
        """
        option = ("name", "ingredients")
        """
        buffReturn = {}
        if self.requestMode == 0:
            if "name" in option:
                buffReturn["name"] = (productDump["product_name_fr"])
            if "ingredients" in option:
                buffReturn["ingredients"] = (productDump["ingredients_text_fr"])

        elif self.requestMode == 1:
            if "name" in option == True:
                buffReturn["name"] = (productDump["product_name"])
            if "ingredients" in option:
                buffReturn["ingredients"] = (productDump["ingredients_text"])
        
        return buffReturn
            