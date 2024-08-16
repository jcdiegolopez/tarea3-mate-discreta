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

celdas = validate_positive_integer(
    input("Ingrese la cantidad de celdas: "),
    "El número de celdas debe ser un entero positivo mayor que 0"
)

initial = [randint(1, 100) for _ in range(celdas)]
memoryArray = [0] * celdas

def hashFunction(x, m):
    return x % m

def saveValue(value):
    index = hashFunction(value, celdas)
    if memoryArray[index] == 0:
        memoryArray[index] = value
    else:
        for i in range(celdas):
            if memoryArray[i] == 0:
                memoryArray[i] = value
                break

def searchValue(value):
    index = hashFunction(value, celdas)
    if memoryArray[index] == value:
        return index
    else:
        for i in range(celdas):
            if memoryArray[i] == value:
                return i
        return -1

for i in initial:
    saveValue(i)

print("Initial: ", initial)
print("Memory: ", memoryArray)

while True:
    value = validate_positive_integer(
        input("Ingrese el valor a buscar (o 0 para salir): "),
        "El valor a buscar debe ser un entero positivo"
    )
    
    if value == 0:
        print("Programa terminado.")
        break
    
    index = searchValue(value)
    if index == -1:
        print("El valor no se encuentra en la memoria")
    else:
        print("El valor se encuentra en la posición:", index + 1)