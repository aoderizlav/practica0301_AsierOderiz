import datetime

def fibonacci_recursiva(numero):
    if numero < 2:
        return numero
    else:
        return fibonacci_recursiva(numero-1) + fibonacci_recursiva(numero-2)

inicio_recursiva = datetime.datetime.now()
print(fibonacci_recursiva(10))
fin = datetime.datetime.now()
print(fin - inicio_recursiva)

def fibonacci_bucles(numero):
    numero1 = 0
    numero2 = 1
    if numero == 1:
        return 0
    elif numero == 2:
        return 1
    for i in range(2,numero):
            total = numero1 + numero2
            numero1 = numero2
            numero2 = total
    return numero2

inicio_bucles = datetime.datetime.now()
print(fibonacci_bucles(40))
fin = datetime.datetime.now()
print(fin - inicio_bucles)



