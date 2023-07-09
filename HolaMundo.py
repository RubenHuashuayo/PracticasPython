def suma(Valor1, Valor2):
    resultado = Valor1 + Valor2
    return resultado

def resta(Valor1, Valor2):
    resultado = Valor1 - Valor2
    return resultado

def multiplicacion(Valor1, Valor2):
    resultado = Valor1 * Valor2
    return resultado

def division (Valor1, Valor2):
    resultado = Valor1 / Valor2
    return resultado

def potenciacion (Valor1, Valor2):
    resultado = Valor1 ** Valor2
    return resultado

def calculadora():
    print('BIENVENIDO A LA CALCULADORA JUEGOS MACABROS')
    print('-------------------------------------------')
    Valor1 = int(input('Ingresar el primer valor'))
    Valor2 = int(input('Ingresar el segundo valor'))
    print('-------------------------------------------')
    print("1 Suma \n2 Resta \n3 Multiplicar \n4 Dividir \n5 Potencia \n6 Salir")
    print('-------------------------------------------')
    opcion = int(input('Elije tu opcion: '))

    if opcion == 1:
        resultado = suma(Valor1, Valor2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        resultado = resta(Valor1, Valor2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        resultado = multiplicacion(Valor1, Valor2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 4:
        resultado = division(Valor1, Valor2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 5:
        resultado = potenciacion(Valor1, Valor2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 6:
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Por favor, selecciona 1 o 2.")
# Llamada a la funcion calculdara()
calculadora()