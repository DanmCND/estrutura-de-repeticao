'''
📋 Enunciado
 
Você deve criar um programa em Python que gere a tabuada de um número escolhido pelo usuário, indo até um limite também definido pelo usuário.
 
Diferente do exemplo visto em sala (onde a tabuada era fixa), agora o programa deve ser dinâmico, permitindo diferentes valores.
 
🔧 Requisitos do programa
 Pedir ao usuário:
O número da tabuada
Até qual número a tabuada deve ir
Utilizar a estrutura while
Mostrar o cálculo no formato:
5 x 3 = 15
Encerrar quando atingir o limite informado
 
 
✅ Critérios para a atividade estar correta
Utilizar input() para receber os valores
Utilizar while corretamente
Exibe a tabuada no formato correto
 
⭐⭐ Desafio extra (opcional) ⭐⭐
Não permitir números negativos
Perguntar ao final se o usuário deseja gerar outra tabuada

'''
num = int(input("Digite um número para ver sua tabuada: "))
mult = int(input("Digite até qual número a tabuada deve ir: "))
count = 0
if num < 0 or mult <0:
    print("Insira apenas números positivos.")
else:
     while count <= mult:
         print(f"{num} x {count} = {num * count}")
         count += 1  # Incrementa o contador em 1
resposta = input("Deseja gerar outra tabuada? (s/n): ").lower()
if resposta == "s":
     num = int(input("Digite um número para ver sua tabuada: "))
     mult = int(input("Digite até qual número a tabuada deve ir: "))
     count = 0
if num < 0 or mult <0:
    print("Insira apenas números positivos.")
else:
    while count <= mult:
        print(f"{num} x {count} = {num * count}")
        count += 1  # Incrementa o contador em 1
        

