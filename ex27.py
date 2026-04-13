# Programa Raiz Quadrada Heron
# Descrição: Este programa calcula a raíz quadrada de um número pelo método de Heron
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

raiz = 0.0

i = 0

n = 0

a = 0.0

x1 = 0.0

# Entrada de dados

a = float(input("\nQual é o número cuja raíz você deseja estimar? "))

n = int(input("\nQuantas vezes você deseja iterar a aproximação? "))

x = [0.0]*(n+1)

x1 = float(input("\nDê um número positivo para iniciar a aproximação: "))

# Processamento:

for i in range (n+1):
    if i == 0:
        x[i] = x1
    else:
        x[i] = (x[i-1] + (a / x[i-1]))/2

# Saída de dados

print(f"\nA estimação da raíz quadrada de {a} com {i} aproximações é {x[i]}.\n")