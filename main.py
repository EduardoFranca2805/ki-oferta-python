
from dominio.produto import Produto
from dominio.mercado import Mercado

# Python não usa a palavra new para criar objetos

arroz = Produto(12, "Tio João", 23.50)
feijao = Produto(10, "carioca", 10.50)
cafe = Produto(4, "Três Corações", 13.60)

max_atacadista = Mercado(13, "Max atacadista", -23.5135, -46.1843)
assai = Mercado(14, "Assaí Atacadista", -23.5134, -23.5134)

lista_prods = [arroz, feijao, cafe]
lista_mercado = [max_atacadista, assai]

for mercado in lista_mercado:
    print(f"Mercado: {mercado.mostrar_nome()} - Latitude: {mercado._lat} - Longitude: {mercado._lng}")

for produto in lista_prods:
    print(f"Nome: {produto.mostrar_nome()} - Preço: {produto.mostrar_preco()}")

try:
    cafe.alterar_preco(-1)
except ValueError as exc:
    print(f"Erro: {exc}")

print(f"Novo preço do café: {cafe.mostrar_preco()}")