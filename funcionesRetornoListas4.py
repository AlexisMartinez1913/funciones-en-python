"""
En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio.
"""
def cargar_datos():
    lista = []
    for x in range(10):
        sueldos = float(input("Ingrese el salario del empleado: "))
        lista.append(sueldos)
    return lista

def mostrar_sueldos(sueldos):
    print("Sueldos de los empleados: ")
    print(sueldos)

def sueldos_mayores(sueldos):
    mayores = 0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            mayores = mayores+1
    return mayores

def promedio_sueldos(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    promedio = suma/10
    return promedio

def prom(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma + sueldos[x]
    promedio = suma/10
    print("Sueldos por debajo del promedio: ")
    for x in range(len(sueldos)):
        if sueldos[x]< promedio:
            print(sueldos[x])



#bloque principal
lista = cargar_datos()
mostrar_sueldos(lista)
print("La cantidad de empleados que tienen un salario mayor a 4000 son: ", sueldos_mayores(lista))
print("el promedio de sueldos es: ", promedio_sueldos(lista))
prom(lista)

