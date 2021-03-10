import Gateway
import csv


def inputSecured(msg, returnType: str):
    """
    returnType: "int", "str", "bool"(yes/no)
    """
    while True:
        print(msg)
        buff = input()

        if returnType == "int":  #int
            if buff == "":
                continue
            try:
                int(buff)
            except:
                continue
            return int(buff)
        elif returnType == "str":  #str
            if buff == "":
                continue
            return buff
        elif returnType == "bool":  #bool
            if buff == "":
                continue
            elif buff == "yes" or buff == "y" or buff == "Y":
                return True
            elif buff == "no" or buff == "n" or buff == "N":
                return False
        else:
            raise NotImplementedError()


def getProduct(name: str, analogNumber=0):
    dump = gateway.requestName(productName=name)
    dump = gateway.cleanDump(dump=dump)
    productN = gateway.getProductInDump(dump=dump, number=analogNumber)
    return productN


def getInfo(productN):
    buff = gateway.getProductFacts(productN, option="all")
    return buff


def createCsv(allProduct) -> None:
    csvFlow = open("product.csv", 'w', encoding='utf-8')
    headerList = [
        "name", "code", "ingredients", "nutriscore_grade", "stores",
        "packaging", "brands", "labels", "quantity", "ecoscore_score",
        "ecoscore_grade"
    ]
    writerFlow = csv.DictWriter(csvFlow, fieldnames=headerList, delimiter=";")
    writerFlow.writeheader()
    for product in allProduct.values():
        #print(product)
        writerFlow.writerow(product)


def cleanProduct(product: dict) -> dict:
    headerList = [
        "name", "code", "ingredients", "nutriscore_grade", "stores",
        "packaging", "brands", "labels", "quantity", "ecoscore_score",
        "ecoscore_grade"
    ]
    cleanProductDict = {}
    for productK in product.values():
        buffDict = {}
        for factsK, factsV in productK.items():
            if factsK in headerList:
                buffDict[factsK] = factsV
        cleanProductDict[productK["name"]] = buffDict
        print(productK["name"])
    return cleanProductDict


gateway = Gateway.Gateway(requestMethod=0)


def finalRechearch(productToShearch, analogProductNumber):
    allProduct = {}
    print("We found a match for : ")
    for number in range(0, analogProductNumber):  #for get analog product
        for name in productToShearch:
            buffProduct = getProduct(name, number)
            buffName = gateway.getProductFacts(buffProduct, option=("name"))
            allProduct[buffName["name"]] = getInfo(buffProduct)
            print("   ->", buffName["name"])
    print(allProduct)
    return allProduct


while True:
    """
    print(
        "Hi, this program allows you to create a valid csv file to do without internet.\n"
        + "The program you are looking for is probably 'main.py'.")
    if inputSecured(msg="continue ? type : yes or no",
                    returnType="bool") == False:
        print("okay, look 'main.py'")
        break

    print(
        "the search for the products can take a long time,\n" +
        "it searches for all the products in the list, also for its anallogues"
    )
    if inputSecured(msg="continue ? type : yes or no",
                    returnType="bool") == False:
        print("okay, look 'main.py'")
        break
    """
    productShearch = ("nutella", "oreo", "jambon", "beurre", "arizona",
                      "orange", "pomme", "jus", "chocolat", "sushi", "prince",
                      "petit écolier", "côte d'or", "lu", "the", "tictac",
                      "patate")
    #productShearch = ("nutella", "oreo")
    dirtyFound: dict = finalRechearch(productShearch, analogProductNumber=4)
    cleanFound: dict = cleanProduct(dirtyFound)
    createCsv(dirtyFound)
    print("total product found ->", len(dirtyFound))
    print("end csv okay")
    break
