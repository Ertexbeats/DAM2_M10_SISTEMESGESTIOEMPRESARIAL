print("Primera potencia:")
print("===================================")
base = int(input("Introduzca la base: "))
potencia = int(input("Introduzca la potencia: "))

resultado1 = base

contador = 1

while contador < potencia:
    contador += 1
    resultado1 = resultado1 * base


print("")


print("Segunda potencia:")
print("===================================")
base = int(input("Introduzca la base: "))
potencia = int(input("Introduzca la potencia: "))

resultado2 = base

contador = 1

while contador < potencia:
    contador += 1
    resultado2 = resultado2 * base

print("")


print("El resultado es: ")
print("===================================")
print("La primera potencia da: ", resultado1)
print("La segunda potencia da: ", resultado2)

if resultado1 > resultado2:
    print("La primera potencia es mayor que la segunda")
elif resultado2 > resultado1:
    print("La segunda potencia es mayor que la primera")
else:
    print("Ambas potencias son iguales")

# I AQUEST?


def obtener_tipo(variable):
    return type(variable)


def mostrar_caracteres(cadena):
    for caracter in cadena:
        print(caracter)


nombre = "Juan"
apellido = "Gomez"

# tipado dinamico

print(type(nombre))

# nombre = 90
print(type(nombre))

saludo = f"Hola me llamo {nombre} {apellido}"
print(saludo)

edad = 90
# print(type(edad))
print("El tipo es", obtener_tipo(edad), sep=":")

# nombre_completo = nombre + " " + apellido
nombre_completo = f"{nombre} {apellido}"

# recorrer las letras de nmopbre_completo
num_caracteres = len(nombre_completo)

mostrar_caracteres(nombre_completo)
print("Fin de iteracion")


# I AQUEST?

# input: nombre completo : nombre, apellido1, apellido2 ->

def obtener_iniciales(n_completo):
    nombre_completo_sanitizado = nombre_completo.strip()
    primera_inicial = nombre_completo_sanitizado[0]
    pos_espacio = nombre_completo_sanitizado.index(" ")
    pos_ultimo_espacio = nombre_completo_sanitizado.index(" ", pos_espacio + 1)
    segunda_inicial = nombre_completo_sanitizado[pos_espacio + 1]
    tercera_inicial = nombre_completo_sanitizado[pos_ultimo_espacio + 1]

    return (primera_inicial, segunda_inicial, tercera_inicial)  # tupla


# nombre_completo = "Juan Gomez Lopez" # JGL
nombre_completo = "Ricardo Jaume Albacar"  # JGL
iniciales = obtener_iniciales(nombre_completo)
print(iniciales[0], iniciales[1], iniciales[2], sep="*")
# I AQUEST?
resultado = 0


def calcular():
    global resultado
    resultado = 3 * 4
    print("local " + str(resultado))


calcular()
print(resultado)


# I AQUEST?

def repetir():
    repetir()


repetir()

# I AQUEST?


def imprimir(x):
    if x > 0:
        print(x)
        imprimir(x-1)


imprimir(4)

# I AQUEST?


def factorial(fact):
    if fact > 0:
        valor = fact * factorial(fact - 1)
        return valor
    else:
        return 1


num = int(input("Entre un numero"))
print(f"El factorial de {num} es {factorial(num)}")


# I AQUEST?

def poner_multas(l_conductores, num_multas):
    import random

    listado_multas = dict()  # variable local
    for i in range(num_multas):
        print(i)
        poner_multa(random.choice(l_conductores), listado_multas)

    return listado_multas


def poner_multa(conductor, l_multas):
    if conductor[-1] not in l_multas:
        l_multas[conductor[-1]] = conductor


if __name__ == "__main__":

    conductor = ("A11", "Jaime", "B9090D")  # tupla (inmutable)
    conductores = [
        conductor,
        ("A12", "Jaime", "B9090D"),
        ("A13", "Ana", "B9056F"),
        ("A14", "Jaime", "B787D"),
        ("A15", "Lourdes", "B665A")
    ]

    # test de una accion unitaria
    """
    listado_multas = poner_multa(conductores) #diccionario
    print(listado_multas)
    """

    listado_multas = poner_multas(conductores, 4)
    # print(listado_multas)

    # slicing
    importe_multas = [45.00, 100.00, 25.75, 75.00]
    importe_multas = importe_multas[0:len(
        listado_multas)]  # bypass de repetidos

    multados = list(listado_multas.values())
    print(multados)
    relacion_pagos = list(zip(multados, importe_multas))
    print(relacion_pagos)
