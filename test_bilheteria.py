from bilheteria import definir_preco_ingresso,PRECO_INTEIRA ,PRECO_MEIA, PRECO_ISENTO

def test_ingresso_isento():
    assert definir_preco_ingresso(1) == PRECO_ISENTO
    assert definir_preco_ingresso(2) == PRECO_ISENTO
    assert definir_preco_ingresso(3) == PRECO_ISENTO
    
def test_ingresso_jovem():
    for i in range(4,19):
        assert definir_preco_ingresso(i) == PRECO_MEIA

def test_ingresso_adulto():
    for i in range(19,60):
        assert definir_preco_ingresso(i) == PRECO_INTEIRA

def test_ingresso_idoso():
    assert definir_preco_ingresso(60) == PRECO_MEIA
    assert definir_preco_ingresso(75) == PRECO_MEIA
    assert definir_preco_ingresso(94) == PRECO_MEIA
