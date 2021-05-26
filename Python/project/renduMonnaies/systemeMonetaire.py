"""
Entat Baptiste
"""


class GestionMonetaire:
    def __init__(self) -> None:
        self._compte = {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

    def get_compte(self) -> dict:
        return self._compte

    def set_compte_all(self, newCompte) -> None:
        self._compte = newCompte

    def set_compte_exemple(self) -> None:
        self._compte = {1: 100, 2: 100, 5: 100,
                        10: 100, 20: 100, 50: 100, 100: 100}

    def check_IDinCompte(self, id: int) -> bool:
        if self._compte[id] == 0:
            return False
        else:
            return True

    def renduMonnaies(self, somme_a_rendr) -> dict:
        lst_pieces = [1, 2, 5, 10, 20, 50, 100]
        idPiece = len(lst_pieces) - 1
        dictRendu = {}

        while somme_a_rendr > 0:
            print
            if idPiece < 0:
                print("out of money")
                raise Exception("out of money")
            elif self._compte[lst_pieces[idPiece]] == 0:
                idPiece -= 1
            elif somme_a_rendr < lst_pieces[idPiece]:
                idPiece -= 1
            elif somme_a_rendr >= lst_pieces[idPiece]:
                self._compte[lst_pieces[idPiece]] -= 1
                somme_a_rendr -= lst_pieces[idPiece]

                if lst_pieces[idPiece] in dictRendu:
                    dictRendu[lst_pieces[idPiece]] += 1
                else:
                    dictRendu[lst_pieces[idPiece]] = 1
            else:
                raise NotImplementedError()

        return dictRendu
