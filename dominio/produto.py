class Produto:
    def __init__(self, id, nome, preco):
        self._id = id
        self._nome = nome
        self._preco = preco

    def mostrar_nome(self):
        return self._nome

    def alterar_nome(self, novo_nome):
        if novo_nome.strip() == '':
            raise ValueError('nome não pode ser vazio')
        self._nome = novo_nome.strip()
    
    def mostrar_id(self):
        return self._id

    def alterar_preco(self, novo_preco): 
        if novo_preco < 0:
            raise ValueError ('preço naão pode ser negativo')
        self._preco = novo_preco

    def mostrar_preco(self):
        return self._preco
    def __repr__(self):
        return f'Produto({self._nome})'

   