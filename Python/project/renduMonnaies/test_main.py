from systemeMonetaire import *


def test_compte():
    gestEur = GestionMonetaire()

    assert gestEur.get_compte() == {1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

#static supp
#def test_rendu_static():
#    assert renduMonnaies(49) == [20, 20, 5, 2, 2]


def test_rendu_dynamic():
    gestEur = GestionMonetaire()
    gestEur.set_compte_exemple()

    assert gestEur.renduMonnaies(49) == {20: 2, 5: 1, 2: 2}
    
    for key, val in gestEur._compte.items():
        assert val != 0
