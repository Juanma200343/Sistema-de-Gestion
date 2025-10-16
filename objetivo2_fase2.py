#Juan Manuel Domínguez García 2ºDAM

#Creamos 3 variables con los siguientes nombres: Nombre y Apellidos , Curso y Grupo.

nombreCompleto = input("Dime tu nombre: ")
curso = input("Dime tu curso: ")
grupo = input("Dime tu grupo: ")
rutaProyecto = input("Inserte la ruta de su proyecto: ")

print(
    "----------------------------------------\n"
    "Ficha del alumnado\n"
    "----------------------------------------\n"
    "Nombre: "+nombreCompleto,"\n"
      "Curso: "+curso,"Grupo: "+grupo ,"\n"
      "Ruta del Proyecto: "+ rutaProyecto 
)
#Para que quede igual que en el ejemplo necesitamos poner detras de lo queramos el salto de linea "\n"