"""
Elaborar una función que reciba tres enteros y nos retorne el valor promedio de los mismos
"""
def promedioNumeros(num1,num2,num3):
    suma = num1+num2+num3
    promedio=(suma/3)
    return promedio

valor1 = int(input("Ingrese el valor #1: "))
valor2 = int(input("Ingrese el valor #2: "))
valor3 = int(input("Ingrese el valor #3: "))
prom = promedioNumeros(valor1,valor2,valor3)
print("El promedio de los numeros es igual a: ", prom)

