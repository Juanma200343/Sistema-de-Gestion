#Juan Manuel Domínguez García 2ºDAM

#Utilización de bifurcaciones if.

edad = 20

if edad >= 18:
    print("Eres mayor de edad.")

#Utilización de bifurcaciones if…else.

edad = 16

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

#Utilización de bifurcaciones if…elif…else.

nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Bueno")
elif nota >= 60:
    print("Aprobado")
else:
    print("Reprobado")


#Iniciar el uso de lógica condicional dentro de un programa.

edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puedes conducir.")
else:
    print("No puedes conducir.")


#Ampliar los conocimientos previos del Objetivo 2 (Fase 5) con el manejo avanzado de cadenas mediante los métodos startswith() y endswith().
mensaje = "Hola mundo"

if mensaje.startswith("Hola"):
    print("El mensaje empieza con 'Hola'.")