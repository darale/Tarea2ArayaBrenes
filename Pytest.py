from Calc import calc


def test_1():
    assert calc(7, 6) != -100, "Caso éxito"


def test_2():
    assert calc(1, 3) == -100, "Error, a menor que b"


def test_3():
    assert calc("r", 6) == -100, "Error presenta una letra"


def test_4():
    assert calc(5, "y") == -100, "Error presenta una letra"


def test_5():
    assert calc("r", "u") == -100, "Error presenta dos letras "
