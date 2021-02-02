"""
02 Fev 2020
Entat
Baptiste
"""
#EX 185 - 186 p. 220


class DataBase:
    #base
    def __init__(self) -> None:
        self.m_data = [{
            'réf.': '18635',
            'désignation': 'lot crayons HB',
            'prix': '2.30',
            'qté': '1'
        }, {
            'réf.': '15223',
            'désignation': 'stylo rouge',
            'prix': '1.50',
            'qté': '3'
        }, {
            'réf.': '20112',
            'désignation': 'cahier petits carreaux',
            'prix': '3.50',
            'qté': '2'
        }]

    #set
    def set_purge(self) -> None:
        self.m_data = [block for block in self.m_data if int(block["qté"]) > 0]
    
    #get
    def get_presence(self) -> bool:
        for block in self.m_data:
            if int(block["qté"]) < 0:
                return False
        return True

    def get_numberOf(self, ref:str) -> int:
        """
        take a reference and return a number of products in stock
        """
        for block in self.m_data:
            if block["réf."] == ref:
                return int(block["qté"])
        return -1

    def get_totalCost(self) -> float:
        totalCost = 0
        for block in self.m_data:
            if int(block["qté"]) > 0:
                totalCost += (int(block["qté"]) * float(block["prix"]))
        return totalCost

base = DataBase()

base.set_purge()
print(base.m_data)
