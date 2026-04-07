import pytest
from src.logic import calcular_imc

def test_calculo_correto():
    # Pessoa de 70kg e 1.75m deve ter IMC ~22.86 (Peso normal)
    valor, cat = calcular_imc(70, 1.75)
    assert valor == 22.86
    assert cat == "Peso normal"

def test_obesidade():
    # Pessoa de 100kg e 1.70m
    _, cat = calcular_imc(100, 1.70)
    assert cat == "Obesidade"

def test_erro_entrada_invalida():
    with pytest.raises(ValueError):
        calcular_imc(70, 0)
