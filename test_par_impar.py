from par_impar import eh_par

def test_numero_pares():
    assert eh_par(4) is True
    assert eh_par(2) is True
    assert eh_par(22) is True
    assert eh_par(22878) is True

def test_numeros_impares():
    assert eh_par(5) is False
    assert eh_par(573) is False
    assert eh_par(573551) is False
