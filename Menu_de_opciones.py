while True:
    print("Menu de Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potenciación")
    print("6. Salir")
    
    opcion = input("Ingresa el número de la opción deseada: ")
    
    if opcion == "1":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 + num2
        print("El resultado de la suma es:", resultado)
    elif opcion == "2":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 - num2
        print("El resultado de la resta es:", resultado)
    elif opcion == "3":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = num1 * num2
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == "4":
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print("El resultado de la división es:", resultado)
        else:
            print("Error: No se puede dividir entre cero.")
    elif opcion == "5":
        num1 = float(input("Ingresa la base: "))
        num2 = float(input("Ingresa el exponente: "))
        resultado = num1 ** num2
        print("El resultado de la potenciación es:", resultado)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, ingresa un número del 1 al 6.")
