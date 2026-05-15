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

import requests

def get_weather(city="Sao Paulo"):
    try:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        data = response.json()

        temp = int(data["current_condition"][0]["temp_C"])
        desc = data["current_condition"][0]["weatherDesc"][0]["value"]

        return temp, desc
    except:
        return None, None


def recomendacao_agua(temp):
    if temp is None:
        return "Mantenha-se hidratado ao longo do dia."

    if temp >= 30:
        return "Temperatura alta. Beba bastante agua."
    elif temp >= 25:
        return "Clima quente. Aumente a ingestao de agua."
    elif temp >= 15:
        return "Clima moderado. Continue se hidratando bem."
    else:
        return "Temperatura baixa, mas nao se esqueca de beber agua."
