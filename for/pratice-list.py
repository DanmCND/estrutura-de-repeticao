'''
list = lista
uma coleção de valores que podemos guardar juntos em uma unica variável.

1.Cada item da liesta ocupa uma posição
2.Cada posição tem um indice, que começa do 0
3. Podemos acessar os itens da lista usando o indice

'''
# indice de cada item da lista
#             0           1          2             3                  4 
mochila = ["celular", "carteira", "chave", "fones de ouvido", "garrafa de água"]
#             0        1           2         3        4          5
compras = ["arroz", "feijão", "macarrão", "carne", "frutas", "verduras"]
print("comprar:" + compras[0])
print("comprar:" + compras[4])
print("comprar:" + compras[2])

compras.append("leite") # adiciona um item no final da lista
print(compras)

compras.remove("arroz") # remove um item da lista
print(compras)

print(len(compras)) # conta quantos itens tem na lista ou até mesmo quantos caracteres tem em uma string

compras.count("carne") # conta quantas vezes um item aparece na lista
print(compras.count("carne"))