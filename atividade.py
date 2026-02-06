'''
#===primeira versão===

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
'''

#===segunda versão===

while True:
    num = int(input("Digite um número para ver sua tabuada: "))
    mult = int(input("Digite até qual número a tabuada deve ir: "))
    count = 0
    if num < 0 or mult < 0:
        print("Insira apenas números positivos.")
    else:
        while count <= mult:
            print(f"{num} x {count} = {num * count}")
            count += 1  # Incrementa o contador em 1
    resposta = input("Deseja gerar outra tabuada? (s/n): ").lower()
    if resposta != "s":
        break