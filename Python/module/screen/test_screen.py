import screen


def test_switch():
    tab: list = [1, 2]
    screen.switch(tab, 0, 1)
    assert tab == [2, 1]


def test_tri_selection():
    tab: list = [98, 22, 15, 32, 2, 74, 63, 70]
    buff = tab[:]
    buff.sort()
    screen.tri_selection(tab)

    assert tab == buff
