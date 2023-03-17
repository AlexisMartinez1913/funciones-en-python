"""
Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'
"""
def oracion(mensaje):
    cantidad = 0
    for x in range(len(mensaje)):
        if mensaje[x]=='a' or mensaje[x]=='A':
            cantidad = cantidad+1
    return cantidad

texto = input("Ingrese una oración: ")

print("Cantidad de letras 'a' o 'A' en dicha oración son: ", oracion(texto))

