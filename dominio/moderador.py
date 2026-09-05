from dominio.usuario import Usuario
class Contribuidor(Usuario):
    def pode_moderar(self):
        return True