# Convertendo Celsius para Fahrenheit
# Ela deve receber uma lista e fazera conversão


lista_celsius: float = []

def c_para_f(lista_celsius):
    lista_fahrenheit: float = []
    for c in lista_celsius:
        f = (c* 9/5) + 32
        lista_fahrenheit.append(f)
    return lista_fahrenheit

lista_celsius = [0,1,20.3,45.5]
convercao = c_para_f(lista_celsius)
print(convercao)