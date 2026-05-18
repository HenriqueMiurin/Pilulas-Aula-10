from cupons import aplicar_cupom


def test_cupom10_valido():
    assert aplicar_cupom("CUPOM10", 50.0) == 0.10


def test_cupom10_minusculo():
    assert aplicar_cupom("cupom10", 50.0) == 0.10


def test_cupom25_valido_acima_de_100():
    assert aplicar_cupom("CUPOM25", 150.0) == 0.25


def test_cupom25_invalido_abaixo_de_100():
    assert aplicar_cupom("CUPOM25", 50.0) == 0.0


def test_descontovip_valido_acima_de_500():
    assert aplicar_cupom("DESCONTOVIP", 600.0) == 0.35


def test_descontovip_invalido_abaixo_de_500():
    assert aplicar_cupom("DESCONTOVIP", 300.0) == 0.0


def test_cupom_invalido():
    assert aplicar_cupom("CUPOM_FALSO", 1000.0) == 0.0


def test_descontovip_minusculo():
    assert aplicar_cupom("descontovip", 600.0) == 0.35