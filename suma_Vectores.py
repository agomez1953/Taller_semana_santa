from producto_escalar import *
import math
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
    for posicion in range(len(vectores[seleccion1])):
        resultado.append(vectores[seleccion1][posicion]+vectores[seleccion2][posicion])
    print(resultado)
def producto_punto():
    print('Escoja el primer vector')
    mostrar_vectores()
    seleccion1 = input()
    print('Escoja el segundo vector')
    mostrar_vectores()
    seleccion2 = input()
    producto = []
    contador=0
    for posicion in range(len(vectores[seleccion1])):
        producto.append(vectores[seleccion1][posicion] * vectores[seleccion2][posicion])
    for resultado in producto:
        contador=contador+resultado
    print(contador)
def mayor_elemento():
    print('Escoja el vector para ver el mayor elemento')
    mostrar_vectores()
    seleccion=input()
    print(vectores[seleccion])
    contador=0
    for i in vectores[seleccion]:
        if i > contador:
            contador += 1
        respuesta = contador
    print(respuesta)
def menor_elemento():
    print('Escoja el vector para ver el menor elemento')
    mostrar_vectores()
    seleccion = input()
    contador=0
    for i in vectores[seleccion]:
            contador -= 1
            if i <= contador:
                i = vectores[seleccion]
            print(contador)
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
    print('Escoja el vector')
    mostrar_vectores()
    seleccion = input()
    for i in seleccion:
        resultado=math.sqrt((1/len(seleccion)-1)*(vectores[seleccion][i]-promedio())**2)
    print(resultado)

def comparar():
    print('Escoja el primer vector para comparar')
    mostrar_vectores()
    seleccion1 = input()
    print('Escoja el segundo vector para comparar')
    mostrar_vectores()
    seleccion2 = input()
    if vectores[seleccion1] == vectores[seleccion2]:
        print('son iguales')
    else:
        print('No son iguales')
def norma():
    print('Escoja el primer vector para comparar')
    mostrar_vectores()
    seleccion = input()
    contador = 0
    for i in vectores[seleccion]:
        contador = contador+i**2
    print(math.sqrt(contador))
def moda():
    print('Escoja el primer vector para sacar la moda')
    mostrar_vectores()
    seleccion=input()
    contador=0
    for i in vectores[seleccion]:
        if vectores[seleccion][i] > contador:
            contador += i
            print('La moda es',contador)

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
