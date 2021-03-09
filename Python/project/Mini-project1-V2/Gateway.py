import requests
import json
import csv


class Gateway:
    def __init__(self, requestMethod: int) -> None:
        """
        modeRequest = 0 -> web request
        modeRequest = 1 -> local file request
        """
        #check request mode
        if requestMethod != 0 and requestMethod != 1:
            raise NotImplementedError("requestMethod !")
        self.requestMode = requestMethod

        if requestMethod == 1:
            self.locaReader = csv.DictReader(open(
                "fr-openfoodfacts-org-products.csv",
                "r",
                encoding="utf8",
                errors="ignore"),
                                             delimiter="\t")
            #open(vocab_path, 'r', encoding='utf8', errors='ignore') #errors="ignore" else raise erorr

    def requestID(self, productId):
        if self.requestMode == 0:
            url = 'https://fr-en.openfoodfacts.org/api/v0/product/' + str(
                productId) + '.json'
            getRequests = requests.get(url)
            #https://global.openfoodfacts.org
            self.dump = getRequests.json()

            #verifie l'existence de l'id
            stat = self.dump["status_verbose"]
            if stat != "product found":
                raise NameError("id not found !")

        elif self.requestMode == 1:
            print(
                "search in progress, in local mode(search in the csv file) it can take a long time..."
            )
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
            url = 'https://fr-en.openfoodfacts.org/cgi/search.pl?search_terms=' + str(
                productName) + '&search_simple=1&action=process&json=true'
            getRequests = requests.get(url)
            self.dump = getRequests.json()
            return self.dump

        elif self.requestMode == 1:
            print(
                "search in progress, in local mode(search in the csv file) it can take a long time..."
            )
            self.dump = []
            count = 0
            #.find("welcome")
            for row in self.locaReader:
                if (row["product_name"].find(productName) != -1
                        or row["product_name"].find(
                            productName.capitalize()) != -1):
                    count += 1
                    self.dump.append(row)

                if count >= 3:
                    return self.dump
            #return self.dump
            raise ValueError()

    def cleanDump(self, dump):
        """
        Dumping in on-line and off-line mode produces structures that need to be armonised with this function.
        """
        if dump == None:
            if self.dump == None:
                raise NotImplementedError(
                    "please initialize dump before clean dump")
            else:
                dump = self.dump

        if self.requestMode == 0:  #please clean it !
            if "products" in dump:
                return dump["products"]
            elif "product" in dump:
                return dump["product"]
            else:
                return dump
        elif self.requestMode == 1:
            return dump  #no need for modification(already only one article)

    def getProductInDump(self, dump, number: int = 0):
        """
        return a single product of the dump
        number -> which product take in the dump(like a list)
        """
        if self.requestMode == 0:
            try:
                return dump[number]
            except:
                return dump
        elif self.requestMode == 1:
            return dump[number]

    def getProductFacts(self, productDump, option=(None)):
        """
        for onligne:
            option = ("all", "name", "ingredients", "code", "ecoscore_score", "ecoscore_grade",\n
            "nutriscore_grade", "stores", "packaging", "quantity", "brands", "labels")
        for of-ligne:
            option = ("all", "name", "ingredients", "code")

        implementation in progress:
            None
        """
        buffReturn = {}
        if self.requestMode == 0:

            codeMachine = ("code", "ingredients_text_fr", "nutriscore_grade",
                           "stores", "packaging", "brands", "labels",
                           "quantity")
            codeHuman = ("code", "ingredients", "nutriscore_grade", "stores",
                         "packaging", "brands", "labels", "quantity")
            for n in range(len(codeMachine)):
                if codeHuman[n] in option or "all" in option:
                    try:
                        buffReturn[codeHuman[n]] = productDump[codeMachine[n]]
                    except:
                        buffReturn[codeHuman[n]] = "error"

            #not implemented in the for
            if "name" in option or "all" in option:
                try:
                    buffReturn["name"] = productDump["product_name_fr"]
                except:
                    try:
                        buffReturn["name"] = productDump["product_name"]
                    except:
                        buffReturn["name"] = "error"
            if "ecoscore_score" in option or "all" in option:
                try:
                    buffReturn["ecoscore_score"] = productDump[
                        "ecoscore_data"]["score"]
                except:
                    buffReturn["ecoscore_score"] = "error"
            if "ecoscore_grade" in option or "all" in option:
                try:
                    buffReturn["ecoscore_grade"] = productDump[
                        "ecoscore_data"]["grade"]
                except:
                    buffReturn["ecoscore_grade"] = "error"

        elif self.requestMode == 1:
            """
            codeMachine = ("product_name", "code", "ingredients_text")
            codeHuman = ("name", "code", "ingredients")
            """
            codeHuman_Machine = {
                "name": "product_name",
                "code": "code",
                "ingredients": "ingredients_text"
            }
            for humanCode, machineCode in codeHuman_Machine.items():
                if humanCode in option or "all" in option:
                    try:
                        buffReturn[humanCode] = productDump[machineCode]
                    except:
                        buffReturn[humanCode] = "error"

        return buffReturn