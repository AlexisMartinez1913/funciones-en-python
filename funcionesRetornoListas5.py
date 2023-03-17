"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de articulos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
"""


def cargar_articulos():
    articulos = []
    precios = []
    for x in range(5):
        nombre = input("Ingrese el nombre del articulo: ")
        articulos.append(nombre)
        valor = int(input("Ingrese su respectivo precio: "))
        precios.append(valor)
    return [articulos, precios]

def imprimir_articulos(articulos, precios):
    for x in range(len(articulos)):
        print(articulos[x], precios[x])

def producto_mayor(articulos, precios):
    pos = 0
    mayor = precios[0]
    for x in range(1,len(precios)):
        if precios[x]>mayor:
            mayor = precios[x]
            pos = x
    print("El articulo : ", articulos[pos], "es el de mayor precio con el valor de: ",mayor)

def importe(articulos,precios):
    importeP = int(input("Ingrese un valor: "))
    for x in range(len(articulos)):
        if precios[x] < importeP:
            print("Los articulos con un precio menor o igual al valor ingresado son: ", articulos[x], precios[x])


#bloque principal
productos, valores = cargar_articulos()
imprimir_articulos(productos,valores)
producto_mayor(productos,valores)
importe(productos,valores)
