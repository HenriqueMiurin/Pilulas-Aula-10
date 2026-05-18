from notas import converter_notas_conceito


def teste_conceito_a():
    assert converter_notas_conceito(9.0) == 'A'
    assert converter_notas_conceito(10.0) == 'A'

def teste_conceito_b():
    assert converter_notas_conceito(7.0) == 'B'
    assert converter_notas_conceito(8.9) == 'B'

def teste_conceito_c():
    assert converter_notas_conceito(5.0) == 'C'
    assert converter_notas_conceito(6.9) == 'C'

def teste_conceito_d():
    assert converter_notas_conceito(3.0) == 'D'
    assert converter_notas_conceito(4.9) == 'D'

def teste_conceito_f():
    assert converter_notas_conceito(0.0) == 'F'
    assert converter_notas_conceito(2.9) == 'F'

def teste_nota_invalida():
    assert converter_notas_conceito(-1) == 'Nota inválida'
    assert converter_notas_conceito(10.1) == 'Nota inválida'
