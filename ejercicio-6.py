import sys
from random import randint

def validate_positive_integer(input_value, error_message):
    try:
        value = int(input_value)
        if value <= 0:
            raise ValueError({"message": error_message, "code": 1})
        return value
    except ValueError as e:
        if isinstance(e.args[0], dict) and e.args[0].get('code') == 1:
            print(e.args[0]['message'])
        else:
            print(error_message)
        sys.exit()

m = validate_positive_integer(
    input("Ingrese el modulo: "),
    "El número de celdas debe ser un entero positivo mayor que 0"
)
a = validate_positive_integer(
    input("Ingrese el multiplicador: "),
    "El número de celdas debe ser un entero positivo mayor que 0"
)
c = validate_positive_integer(
    input("Ingrese el incremento: "),
    "El número de celdas debe ser un entero positivo mayor que 0"
)
s = validate_positive_integer(
    input("Ingrese la semilla: "),
    "El número de celdas debe ser un entero positivo mayor que 0"
)

size = validate_positive_integer(
    input("Ingrese el tamaño de la lista: "),
    "El número de celdas debe ser un entero positivo mayor que 0"
)

randomArray = [0] * size

def generateRandomNumbers(m, a, c, s, size):
    x = (a * s + c) % m
    randomArray[0] = x
    for i in range (1,size):
        randomArray[i] = (a * randomArray[i - 1] + c) % m
    
    return randomArray

print(generateRandomNumbers(m, a, c, s, size))