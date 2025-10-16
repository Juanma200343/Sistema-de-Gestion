#Juan Manuel Domínguez García 2ºDAM


#Ejercicio 1: Creamos 3 listas de productos

ordenadores = ["Portátil","Sobremesa","Servidor"]
perifericos = ["Raton", "Teclado","Monitor"]
accesorios = ["Funda","Altavoces","Webcam"]

#Ejercicio 2: Creamos una tupla, para crearla tenemos que asignarle un valor entre parentesis.

tupla = (750,1200,2200)

#Ejercicio 3: Creacion de un catálogo.

ordenadores = {
    "Portátil" : "Portátil",
    "Sobremesa" : "Sobremesa",
    "Servidor" : "Servidor"
}

perifericos = {
    "Raton" : "Raton",
    "Teclado" : "Teclado",
    "Monitor" : "Monitor"
}

accesorios = {
    "Funda" : "Funda",
    "Altavoces" : "Altavoces",
    "Webcam" : "Webcam"
}

#Ejercicio 4: Mostrar por pantalla, necesitamos escribir print y dentro del mismo 
# ponemos lo queremos que muestre.

print(ordenadores)
print(perifericos)
print(accesorios)
print(tupla)

#Ponemos Altavoces ya que es el que esta en segundo lugar en la lista.
print(accesorios["Altavoces"])
