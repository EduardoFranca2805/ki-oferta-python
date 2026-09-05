from dominio.usuario import Usuario

class contribuidor(Usuario):
    def pode_publicar(self):
        return True
