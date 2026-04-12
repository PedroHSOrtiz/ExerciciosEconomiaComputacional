# Programa Notas
# Descrição: Este programa calcula a nota final de um aluno na disciplina de Eco Computacional
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

notas = []
pesos = []
avaliações = ["Primeiro Teste", "Segundo Teste", "Prova"]

teste1 = 0.0
teste2 = 0.0
prova = 0.0
parcial = 0.0
rec = 0.0
final = 0.0

peso_teste1 = 0.15
peso_teste2 = 0.15
peso_prova = 0.7
peso_rec = 0.6
peso_parcial = 0.4

i = 0

resposta = ""

notas.append(teste1)
notas.append(teste2)
notas.append(prova)

pesos.append(peso_teste1)
pesos.append(peso_teste2)
pesos.append(peso_prova)

soma = 0.0
somapesos = 0.0

# Entrada de dados

while i < len(notas):
    notas[i] = float(input(f"\nQual a sua nota em {avaliações[i]}? "))
    i+=1

# Processamento:

for i in range(len(notas)):
    soma += notas[i] * pesos[i]
    somapesos += pesos[i]

parcial = soma / somapesos

if parcial >= 9:
    resposta = f"Sua nota é {parcial} e você está aprovado com conceito A.\n"
elif parcial >= 7.5:
    resposta = f"Sua nota é {parcial} e você está aprovado com conceito B.\n"
elif parcial >= 6:
    resposta = f"Sua nota é {parcial} e você está aprovado com conceito C.\n"
else:
    rec = float(input(f"\nSua nota é {parcial} e você está em recuperação. Insira sua nota na recuperação: "))
    final = ((peso_rec * rec) + (peso_parcial * parcial)) / (peso_rec + peso_parcial)
    if final >= 9:
        resposta = f"Sua nota final é {final} e você está aprovado com conceito A.\n"
    elif final >= 7.5:
        resposta = f"Sua nota final é {final} e você está aprovado com conceito B.\n"
    elif final >= 6:
        resposta = f"Sua nota final é {final} e você está aprovado com conceito C.\n"
    else:
        resposta = f"Sua nota final é {final} e você está reprovado com conceito D.\n"

# Saída de dados
print(resposta)