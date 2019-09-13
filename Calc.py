# Para hacer pruebas sólo con este programa descomentar las líneas de abajo
# Se comentaron para realizar las pruebas con el pytest


def calc(a, b):
    if ((a.isalpha()) | (b.isalpha())):
        return -100
    elif int(a) < int(b):
        return -100
    else:
        suma = int(a)+int(b)
        resta = int(a)-int(b)
        mult = int(a)*int(b)
        print("suma,resta,multiplicacion")
        return suma, resta, mult
# x = input("Digite el primer numero: ")
# y = input("Digite el segundo numero: ")
# calc(x, y)
# print (calc(x, y))
# k = input("presione una tecla para salir")
