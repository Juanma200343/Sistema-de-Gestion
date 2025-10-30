#Juan Manuel Domínguez García 2ºDAM

class Autor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

    def MostrarAutor(self):
        print("Autor:", self.nombre, self.apellidos)

# =======================================
# Clase Libro
# =======================================
class Libro:
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.autor = None  # Se añadirá después

    def AñadirAutor(self, autor):
        self.autor = autor

    def MostrarLibro(self):
        print("Título:", self.titulo)
        print("ISBN:", self.isbn)
        if self.autor:
            print("Autor:", self.autor.nombre, self.autor.apellidos)
        else:
            print("Autor: No asignado")
        print("-" * 40)

    def ObtenerTítulo(self):
        return self.titulo

# =======================================
# Clase Biblioteca
# =======================================
class Biblioteca:
    def __init__(self):
        self.ListaLibros = []

    def NumeroLibros(self):
        return len(self.ListaLibros)

    def AñadirLibro(self, libro):
        self.ListaLibros.append(libro)

    def BorrarLibro(self, titulo):
        for libro in self.ListaLibros:
            if libro.ObtenerTítulo().lower() == titulo.lower():
                self.ListaLibros.remove(libro)
                print(" Libro eliminado correctamente.")
                return
        print(" No se encontró un libro con ese título.")

    def MostrarBiblioteca(self):
        if not self.ListaLibros:
            print("📚 La biblioteca está vacía.")
        else:
            print("\n=== LIBROS EN LA BIBLIOTECA ===")
            for libro in self.ListaLibros:
                libro.MostrarLibro()

# =======================================
# Funciones auxiliares
# =======================================

def MostrarMenu():
    print("\n=== MENÚ BIBLIOTECA ===")
    print("1. Añadir libro a la biblioteca")
    print("2. Mostrar biblioteca")
    print("3. Borrar libro de la biblioteca")
    print("4. Mostrar el número de libros")
    print("5. Salir")

def AñadirLibroABiblioteca(biblioteca):
    print("\n=== Añadir nuevo libro ===")
    titulo = input("Introduce el título del libro: ")
    isbn = input("Introduce el ISBN del libro: ")

    nombre = input("Introduce el nombre del autor: ")
    apellidos = input("Introduce los apellidos del autor: ")

    autor = Autor(nombre, apellidos)
    libro = Libro(titulo, isbn)
    libro.AñadirAutor(autor)
    biblioteca.AñadirLibro(libro)
    print(" Libro añadido correctamente.")

def MostrarBibliotecaFuncion(biblioteca):
    biblioteca.MostrarBiblioteca()

def BorrarLibroFuncion(biblioteca):
    titulo = input("Introduce el título del libro que deseas eliminar: ")
    biblioteca.BorrarLibro(titulo)

def NumeroLibrosFuncion(biblioteca):
    print(" Número total de libros en la biblioteca:", biblioteca.NumeroLibros())

# =======================================
# Programa principal
# =======================================
def main():
    biblioteca = Biblioteca()
    opcion = 0

    while opcion != 5:
        MostrarMenu()
        entrada = input("Selecciona una opción (1-5): ")

        if not entrada.isdigit():
            print(" Debes ingresar un número entre 1 y 5.")
            

        opcion = int(entrada)

        if opcion == 1:
            AñadirLibroABiblioteca(biblioteca)
        elif opcion == 2:
            MostrarBibliotecaFuncion(biblioteca)
        elif opcion == 3:
            BorrarLibroFuncion(biblioteca)
        elif opcion == 4:
            NumeroLibrosFuncion(biblioteca)
        elif opcion == 5:
            print("👋 Saliendo del programa...")
        else:
            print(" Opción no válida. Intenta de nuevo.")

# =======================================
# Ejecución del programa
# =======================================
if __name__ == "__main__":
    main()