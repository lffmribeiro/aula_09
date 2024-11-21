## Criando uma funcao
from pydantic import validate_call

@validate_call
def soma(x: float,y: float,z: float):
    '''Essa é uma função para somar três parâmetros ela deve receber inteiros e/ou floats'''
    print(x+y+z)
    return x+y+z

soma(1,2,3)