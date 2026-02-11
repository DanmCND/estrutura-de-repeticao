'''
====counter.py====

O que é uma estrutura de repetição ?

Serve para executar um bloco de código várias vezes,
enquanto uma condição específica for verdadeira.

'''

'''#Exemplo de estrutura de repetição usando 'while'
counter = 10
#contagem regressiva de 10 a 0 
while counter >= 0:
    print(counter)
    counter -= 1  # Decrementa o contador em 1
'''

#tabuada do 5
num = float(input("Digite um número para ver sua tabuada: "))
count = 0

while count <= 10:
    print(f"{num} x {count} = {num * count}")
    count += 1  # Incrementa o contador em 1

