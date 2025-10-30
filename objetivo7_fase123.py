#Juan Manuel Dominguez Garcia

class Video:
    def __init__(self, titulo, duracion, categoria):
        self.titulo = titulo
        self.duracion = duracion
        self.categoria = categoria

    def mirar_video(self):
        print("Iniciando el video:", self.titulo)
        print("Duración:", self.duracion, "minutos")
        print("Categoría:", self.categoria)

    def detener_video(self):
        print("El video se ha detenido.")


class Audio:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def escuchar_audio(self):
        print("Reproduciendo el audio:", self.titulo)
        print("Artista:", self.artista)

    def detener_audio(self):
        print("El audio se ha detenido.")


class Media(Video, Audio):
    def __init__(self, titulo, duracion, categoria, artista):
        Video.__init__(self, titulo, duracion, categoria)
        Audio.__init__(self, titulo, artista)
        self.titulo = titulo
        self.duracion = duracion
        self.categoria = categoria
        self.artista = artista


# Ejemplo de uso
medio = Media("Documental Musical", 45, "Música", "Carlos Pérez")
medio.mirar_video()
medio.detener_video()
medio.escuchar_audio()
medio.detener_audio()