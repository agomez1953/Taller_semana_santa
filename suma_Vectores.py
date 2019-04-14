from producto_escalar import *

vectores = {}

def ingresar_vector():
    """
    Permite leer un vector del usuario
    :return: list of num el vector ingresado por el usuario
    """
    vector = [input('¿Cual es el nombre de su vector? ')]

    while True:
        num = input('Ingrese su escalar o "s" para terminar ')
        if num.lower() != 's':
            try:
                num = int(num)
                vector.append(num)
            except:
                print(num, 'no es un escalar')
        else:
            break
    print('su vector', vector[0], 'es', vector[1:])
    return vector


def mostrar_vectores():
    for nombre in vectores:
        print(nombre, 'contiene', vectores[nombre])

def op_producto_escalar():
    while True:
        escalar = input('Ingrese su escalar ')
        try:
            escalar = int(escalar)
            break
        except:
            print(escalar, 'no es un escalar')

    print('Cual es el nombre de su vector')
    mostrar_vectores()
    seleccion = input()

    print('El producto escalar es',
          producto_escalar(escalar, vectores[seleccion]))
def suma_vectores():
    print('Escoja el primer vector a sumar')
    mostrar_vectores()
    seleccion1=input()
    print('Escoja el segundo vector a sumar')
    mostrar_vectores()
    seleccion2=input()
    resultado=[]
    contador=0
    for i in range(len(seleccion1)):
        resultado.append(vectores[seleccion1][i] + vectores[seleccion2][i])
        contador+=1
        print(resultado)
def producto_punto():
    print('Escoja el primer vector para hacer el producto punto')
    mostrar_vectores()
    seleccion1 = input()
    print('Escoja el segundo vector para hacer el producto punto')
    mostrar_vectores()
    seleccion2 = input()
    resultado = []
    for i in range(0,len(seleccion1),1):
        print(resultado)
def mayor_elemento():
    resultado=0
    print('Escoja el vector para ver el mayor elemento')
    mostrar_vectores()
    seleccion=input()
    print(vectores[seleccion])
    contador=0
    for arreglo in range(len(seleccion)):
        if arreglo < contador:
            contador += 1
            resultado = contador
    print(resultado)
def menor_elemento():
    resultado = 0
    print('Escoja el vector para ver el mayor elemento')
    mostrar_vectores()
    seleccion = input()
    print(vectores[seleccion])
    contador = 0
    for arreglo in range(len(vectores[seleccion])):
        if arreglo < contador:
            contador += 1
            resultado = contador
    print(resultado)
def promedio():
    print('Seleccione el arreglo para hacer el promedio')
    mostrar_vectores()
    seleccion=input()
    contador=0

    respuesta=0
    for arreglo in vectores[seleccion]:
        contador=contador+arreglo
        respuesta=contador/len(vectores[seleccion])
    print(respuesta)


def desviacion_estandar():
    return 0
def comparar():
    print('Escoja el primer vector para comparar')
    mostrar_vectores()
    seleccion1 = input()
    print('Escoja el segundo vector para comparar')
    mostrar_vectores()
    seleccion2 = input()
def norma():
    return 0
def moda():
    return 0
def principal():

    MENSAJE = '''Seleccione una opcion:
    0. Salir
    1. Ingresar Vector
    2. Mostrar Vectores
    3. Producto escalar
    4. Suma de vectores
    5. Producto Punto
    6. Mayor numero
    7. Menor elemento
    8. Promedio
    9. Desviacion estandar
    10. Comparar
    11. Norma
    12. Moda
    '''

    while True:
        opcion = input(MENSAJE)

        if opcion == '0':
            print('Gracielas')
            break
        elif opcion == '1':
            vector = ingresar_vector()
            vectores[vector[0]] = vector[1:]
        elif opcion == '2':
            mostrar_vectores()
        elif opcion == '3':
            op_producto_escalar()
        elif opcion == '4':
            suma_vectores()
        elif opcion == '5':
            producto_punto()
        elif opcion == '6':
            mayor_elemento()
        elif opcion == '7':
            menor_elemento()
        elif opcion == '8':
            promedio()
        elif opcion == '9':
            desviacion_estandar()
        elif opcion == '10':
            comparar()
        elif opcion == '11':
            norma()
        elif opcion == '12':
            moda()
        else:
            print('Seleccione una opcion valida')


if __name__ == '__main__':
    principal()