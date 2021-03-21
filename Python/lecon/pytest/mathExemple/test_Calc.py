import time
import mathLib


def test_div():
    assert mathLib.div(2, 2) == 1
    assert mathLib.div(2, 0) == 0
    assert mathLib.div(0, 2) == 0
