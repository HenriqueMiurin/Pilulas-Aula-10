def aplicar_cupom(codigo_cupom: str, valor_compra: float) -> float:
    codigo = codigo_cupom.upper()

    if codigo == "CUPOM10":
        return 0.10

    elif codigo == "CUPOM25":
        if valor_compra > 100.0:
            return 0.25
        return 0.0

    elif codigo == "DESCONTOVIP":
        if valor_compra > 500.0:
            return 0.35
        return 0.0

    else:
        return 0.0