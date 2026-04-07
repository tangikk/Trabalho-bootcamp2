def calcular_imc(peso, altura):
    """Calcula o IMC e retorna o valor e a categoria."""
    if altura <= 0 or peso <= 0:
        raise ValueError("Peso e altura devem ser maiores que zero.")

    imc = round(peso / (altura ** 2), 2)

    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif imc < 25:
        categoria = "Peso normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"

    return imc, categoria
