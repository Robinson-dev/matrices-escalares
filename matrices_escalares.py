"""
Crear un programa que permita unir la mayoría de los conocimientos adquiridos durante el
semestre. Este algoritmo se llama matrices escalares, y permita multiplicar elementos de
una matriz que hemos definido con filas y columnas ingresadas por el usuario. Se debe
utilizar sentencia While, For, Matrices, Try Except, validaciones y funciones. Se debe
generar un menú de opciones para poder sumar matrices, multiplicar matrices, y un botón
salir.
"""

def suma_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or len(matriz1[0]) != len(matriz2[0]):
        raise ValueError("Las matrices deben tener la misma dimensión para sumarse")

    resultado = []
    for i in range(len(matriz1)):
        fila_resultado = []
        for j in range(len(matriz1[0])):
            fila_resultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(fila_resultado)
    return resultado

def multiplicacion_matriz_escalar(matriz, escalar):
    resultado = []
    for i in range(len(matriz)):
        fila_resultado = []
        for j in range(len(matriz[0])):
            fila_resultado.append(matriz[i][j] * escalar)
        resultado.append(fila_resultado)
    return resultado

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = int(input(f"Ingrese el elemento ({i+1}, {j+1}) de la matriz: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Por favor, ingrese un valor entero válido.")
        matriz.append(fila)
    return matriz

def main():
    while True:
        print("\nMenú")
        print("1. Sumar matrices")
        print("2. Multiplicar matriz por escalar")
        print("3. Salir")
        try:
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
                filas = int(input("Ingrese el número de filas de las matrices: "))
                columnas = int(input("Ingrese el número de columnas de las matrices: "))
                print("Ingrese los elementos de la primera matriz:")
                matriz1 = leer_matriz(filas, columnas)
                print("Ingrese los elementos de la segunda matriz:")
                matriz2 = leer_matriz(filas, columnas)
                resultado = suma_matrices(matriz1, matriz2)
                print("\nResultado de la suma:")
                imprimir_matriz(resultado)
            elif opcion == 2:
                filas = int(input("Ingrese el número de filas de la matriz: "))
                columnas = int(input("Ingrese el número de columnas de la matriz: "))
                print("Ingrese los elementos de la matriz:")
                matriz = leer_matriz(filas, columnas)
                escalar = int(input("Ingrese el valor escalar: "))
                resultado = multiplicacion_matriz_escalar(matriz, escalar)
                print("\nResultado de la multiplicación por escalar:")
                imprimir_matriz(resultado)
            elif opcion == 3:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida, por favor ingrese una opción válida.")
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    main()
