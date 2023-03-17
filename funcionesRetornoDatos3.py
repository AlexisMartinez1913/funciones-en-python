"""
Elaborar una función que nos retorne el perímetro de un cuadrado pasando como parámetros el valor de un lado
"""
def perimetro_Cuadrado(lado):
    perimetro = lado*4
    return perimetro

#bloque principal
valorLado = int(input("Ingrese el valor del lado del cuadrado para calcular perimetro: "))
resultado = perimetro_Cuadrado(valorLado)
print("El perimetro es igual a: ", resultado)
