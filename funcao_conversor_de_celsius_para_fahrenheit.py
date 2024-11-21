# Convertendo Celsius para Fahrenheit
# Ela deve receber uma lista e fazera conversão
'''
exemplo de type
from typing import
lista: List[float] = []
'''
from pydantic import validate_call

lista_celsius: float = []

@validate_call
def c_para_f(lista_celsius):
    '''Essa funcao recebe uma lista como parâmetro e converte Celsius em Fahrenheit'''
    lista_fahrenheit: float = []
    for c in lista_celsius:
        f = (c* 9/5) + 32
        lista_fahrenheit.append(f)
    return lista_fahrenheit

lista_celsius = [0,1,20.3,45.5]
convercao = c_para_f(lista_celsius)
print(convercao)