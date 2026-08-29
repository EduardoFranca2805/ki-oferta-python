<<<<<<< HEAD
from dominio.produto import Produto
from dominio.mercado import Mercado
from dominio.oferta import oferta

# pyhton não usa a palavra new para criar objetos 

arroz = Produto(12, "Tio João", 23.50)
feijao = Produto(10, "carioca", 10.50)
cafe = Produto(4, "Três Corações", 13.60)

max = Mercado(13, "Max atacadista", -23.5135, -46.1843)
assai = Mercado(14, "Assaí Atacadista", -23.5134, -23.5134)

lista_prods = [arroz, feijao, cafe]
lista_mercado = [max, assai]

for aux in lista_mercado:
    print(f"Mercado: {aux._nome} - Latitude: {aux._lat} - Long {aux._log}")

for i in lista_prods:
    print (f" Nome: {i._nome} Preço: {i._preco}")

resultado = cafe.alterar_preco(23.80)
=======
from dominio.produto import Produto
from dominio.mercado import Mercado
from dominio.oferta import oferta

# pyhton não usa a palavra new para criar objetos 

arroz = Produto(12, "Tio João", 23.50)
feijao = Produto(10, "carioca", 10.50)
cafe = Produto(4, "Três Corações", 13.60)

max = Mercado(13, "Max atacadista", -23.5135, -46.1843)
assai = Mercado(14, "Assaí Atacadista", -23.5134, -23.5134)

lista_prods = [arroz, feijao, cafe]
lista_mercado = [max, assai]

for aux in lista_mercado:
    print(f"Mercado: {aux._nome} - Latitude: {aux._lat} - Long {aux._log}")

for i in lista_prods:
    print (f" Nome: {i._nome} Preço: {i._preco}")

resultado = cafe.alterar_preco(23.80)
>>>>>>> 9cbc862a24453bd644b3e9dd238192f9a9003d91
print (f"Novo preço do café {cafe.mostrar_preco()}")