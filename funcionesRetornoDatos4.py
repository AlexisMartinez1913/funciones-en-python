"""
Confeccionar una función que calcule la superficie de un rectángulo y la retorne, la función recibe como parámetros los valores de dos de sus lados:
En el bloque principal del programa cargar los lados de dos rectángulos y luego mostrar cual de los dos tiene una superficie mayor.
"""
def retornar_superficie(lado1,lado2):
    superficie = lado1*lado2
    return superficie

lado1 = int(input("Ingrese el valor del lado 1: "))
lado2 = int(input("Ingrese el valor del lado 2: "))
lado3 = int(input("Ingrese el valor del lado 1: "))
lado4 = int(input("Ingrese el valor del lado 2: "))
la1 = retornar_superficie(lado1, lado2)
la2 = retornar_superficie(lado3,lado4)
if la1 >la2:
    print("La superficie del rectangulo 1 es mayor, es igual a: ", la1)
else:
    print("La superficie del rectangulo 2 es mayor, es igual a: ", la2)

