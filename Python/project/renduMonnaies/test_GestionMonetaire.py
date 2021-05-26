from systemeMonetaire import *


def test_compte_setAndGet():
    gestEur = GestionMonetaire()
    assert gestEur.get_compte() == {1: 0, 2: 0,
                                    5: 0, 10: 0, 20: 0, 50: 0, 100: 0}

    gestEur.set_compte_exemple()
    assert gestEur.get_compte() == {1: 100, 2: 100,
                                    5: 100, 10: 100, 20: 100, 50: 100, 100: 100}

    gestEur.set_compte_all({1: 0, 2: 0, 5: 0, 10: 0, 20: 0, 50: 0, 100: 0})
    assert gestEur.get_compte() == {1: 0, 2: 0,
                                    5: 0, 10: 0, 20: 0, 50: 0, 100: 0}


def test_compte_afterCalc():
    gestEur = GestionMonetaire()
    gestEur.set_compte_exemple()

    assert gestEur.renduMonnaies(48) == {20: 2, 5: 1, 2: 1, 1: 1}

    compte = gestEur.get_compte()
    assert compte[20] == 98
    assert compte[5] == 99
    assert compte[2] == 99
    assert compte[1] == 99


def test_rendu_calcule():
    gestEur = GestionMonetaire()
    gestEur.set_compte_exemple()

    assert gestEur.renduMonnaies(48) == {20: 2, 5: 1, 2: 1, 1: 1}
    assert gestEur.renduMonnaies(
        888) == {100: 8, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1}
    assert gestEur.renduMonnaies(1) == {1: 1}

    gestEur.set_compte_exemple()
    assert gestEur.renduMonnaies(
        18800) == {100: 100, 50: 100, 20: 100, 10: 100, 5: 100, 2: 100, 1: 100}


def test_rendu_overflow():
    gestEur = GestionMonetaire()
    gestEur.set_compte_exemple()
    gestEur.renduMonnaies(18800)

    try:
        gestEur.renduMonnaies(1)
    except Exception as exp:
        #Exception("out of money")
        assert exp.args == ("out of money",)  # , <--!


def test_check_IDinCompte():
    gestEur = GestionMonetaire()
    assert gestEur.check_IDinCompte(100) == False
    assert gestEur.check_IDinCompte(50) == False
    assert gestEur.check_IDinCompte(20) == False
    assert gestEur.check_IDinCompte(10) == False
    assert gestEur.check_IDinCompte(5) == False
    assert gestEur.check_IDinCompte(2) == False
    assert gestEur.check_IDinCompte(1) == False

    gestEur.set_compte_exemple()  # all ID to 100
    assert gestEur.check_IDinCompte(100) == True
    assert gestEur.check_IDinCompte(50) == True
    assert gestEur.check_IDinCompte(20) == True
    assert gestEur.check_IDinCompte(10) == True
    assert gestEur.check_IDinCompte(5) == True
    assert gestEur.check_IDinCompte(2) == True
    assert gestEur.check_IDinCompte(1) == True
