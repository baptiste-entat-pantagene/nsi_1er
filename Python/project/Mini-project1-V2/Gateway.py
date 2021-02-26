import requests
import json

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

        self.dump = {}
    
    def requestID(self, productId):
        if self.requestMode == 0:
            url = 'https://fr-en.openfoodfacts.org/api/v0/product/' + str(productId) + '.json'
            request = requests.get(url)
            #https://global.openfoodfacts.org
            self.dump = request.json()

        if self.requestMode == 1:
            pass

        stat = self.dump["status_verbose"]
        if stat != "product found":
            raise NameError()
        #["product_name_en"]
        name = self.dump["product"]["product_name_fr"]
        #generic_name_fr
        print(stat)
    
