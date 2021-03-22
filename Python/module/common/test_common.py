import common


def test_returnType():

    # Override the Python built-in input method
    common.input = lambda: 'texteStr'
    output = common.entry(returnType="str")
    assert type(output) == type("str")

    common.input = lambda: '12345'
    output = common.entry(returnType="int")
    assert type(output) == type(123)

    common.input = lambda: 'c'
    output = common.entry(returnType="char")
    assert type(output) == type('c')

    common.input = lambda: 'yes'
    output = common.entry(returnType="bool")
    assert type(output) == type(True)

    #restore input()
    common.input = input
