'''
#lista para armazenar os nomes dos alunos
nome_aluno = ["Seu Antonio", "Idalguinho", "Fefe", "Uilian", "Estefhania", "Luzkinha", "Rapaizinho de rosa", "Titi", "Leandrinho do grau", "Lele"  ]

# o for é uma estrutura de repetição que percorre cada elemento de uma coleção.
for nome in nome_aluno:
    print(nome) # Imprime cada nome da lista nome_aluno

# Exemplo de uso do for com um range
for i in range(8): # O range(5) gera uma sequência de números de 0 a 4
    print(i) # Imprime cada número gerado pelo range
'''

veiculos = ["Fusca", "Doblo", "Marea Turbo", "Tiggo", "Uno", "Gol bolinha", "Chevette", "Celta do Felipe", "Corsa", "Civic"]

for veiculo in veiculos:
    if veiculo in ["Fusca", "Doblo", "Marea Turbo"]:
        print(f"{veiculo} é um carro antigo.")
    elif veiculo in ["Tiggo", "Uno", "Gol bolinha"]:
        print(f"{veiculo} é um carro popular.")
    else:
        print(f"{veiculo} é um carro moderno.")
           