'''
📋 Cenário
 
A empresa DevCorp está fazendo uma análise simples de desempenho dos seus funcionários.
Cada funcionário possui uma nota de desempenho (de 0 a 10).
 
A empresa definiu a seguinte regra:
 
Nota maior ou igual a 7 → Funcionário aprovado
Nota menor que 7 → Funcionário em acompanhamento
 
🔧 O que você deve fazer
 
Criar uma lista com as notas de desempenho dos funcionários
Utilizar o laço for para percorrer a lista
Utilizar um if dentro do for para verificar a nota
Mostrar no console a situação de cada funcionário
 
💻 Exemplo de lista
notas = [8, 5, 9, 6, 7]
 
💻 Exemplo de saída esperada
Nota 8 - Funcionário aprovado
Nota 5 - Funcionário em acompanhamento
Nota 9 - Funcionário aprovado
Nota 6 - Funcionário em acompanhamento
Nota 7 - Funcionário aprovado
 
💡 Dica
 
O for percorre a lista uma nota por vez, e o if decide o que será mostrado para cada valor.
 
✅ Critérios para a atividade estar correta
 
Criar uma lista
Utilizar for
Utilizar if
Exibir a mensagem correta para cada item da lista
 
⭐ Desafio extra (opcional)
 
Contar quantos funcionários foram aprovados[
Contar quantos ficaram em acompanhamento
'''
notas = [9, 4, 7.5, 6, 8, 5.5, 10, 3] 
aprovados = 0
acompanhamento = 0
for nota in notas:
    if nota >= 7:
        print(f"Nota {nota} - Funcionário aprovado")
        aprovados += 1
    else:
        print(f"Nota {nota} - Funcionário em acompanhamento")
        acompanhamento += 1
print(f"\nTotal de aprovados: {aprovados}")
print(f"Total de acompanhamento: {acompanhamento}")
