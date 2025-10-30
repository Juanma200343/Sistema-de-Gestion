#Juan Manuel Domínguez García 2ºDAM
import math

opcion = 0

while opcion != 8:
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Módulo")
    print("8. Salir")

    opcion = input("Selecciona una opción (1-8): ")

    # Validar que sea un número entero
    if not opcion.isdigit():
        print(" Error: Debes ingresar un número del 1 al 8.")
        
    else:
        opcion = int(opcion)

    if opcion == 1:
        a = input("Ingresa el primer número: ")
        b = input("Ingresa el segundo número: ")

        if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
            a = float(a)
            b = float(b)
            print(f"El resultado de la suma es: {a + b:.2f}")
        else:
            print(" Error: Solo se permiten números.")

    elif opcion == 2:
        a = input("Ingresa el primer número: ")
        b = input("Ingresa el segundo número: ")

        if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
            a = float(a)
            b = float(b)
            print(f"El resultado de la resta es: {a - b:.2f}")
        else:
            print("Error: Solo se permiten números.")

    elif opcion == 3:
        a = input("Ingresa el primer número: ")
        b = input("Ingresa el segundo número: ")

        if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
            a = float(a)
            b = float(b)
            print(f"El resultado de la multiplicación es: {a * b:.2f}")
        else:
            print("Error: Solo se permiten números.")

    elif opcion == 4:
        a = input("Ingresa el dividendo: ")
        b = input("Ingresa el divisor: ")

        if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
            a = float(a)
            b = float(b)
            if b == 0:
                print(" Error: No se puede dividir entre cero.")
            else:
                print(f"El resultado de la división es: {a / b:.2f}")
        else:
            print(" Error: Solo se permiten números.")

    elif opcion == 5:
        base = input("Ingresa la base: ")
        exponente = input("Ingresa el exponente: ")

        if base.replace('.', '', 1).isdigit() and exponente.replace('.', '', 1).isdigit():
            base = float(base)
            exponente = float(exponente)
            print(f"El resultado de la potencia es: {math.pow(base, exponente):.2f}")
        else:
            print(" Error: Solo se permiten números.")

    elif opcion == 6:
        num = input("Ingresa el número: ")

        if num.replace('.', '', 1).isdigit():
            num = float(num)
            if num < 0:
                print(" Error: No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                print(f"La raíz cuadrada de {num} es: {math.sqrt(num):.2f}")
        else:
            print(" Error: Solo se permiten números.")

    elif opcion == 7:
        a = input("Ingresa el primer número: ")
        b = input("Ingresa el segundo número: ")

        if a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit():
            a = float(a)
            b = float(b)
            if b == 0:
                print(" Error: No se puede calcular el módulo con divisor cero.")
            else:
                print(f"El resultado del módulo es: {a % b:.2f}")
        else:
            print(" Error: Solo se permiten números.")

    elif opcion == 8:
        print(" Saliendo del programa...")
    else:
        print(" Opción no válida. Intenta de nuevo.")