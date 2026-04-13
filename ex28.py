# Programa Cinco Quadrados
# Descrição: Este programa lê cinco números e retorna o quadrado de cada um
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

x = [0.0]*5

y = [0.0]*5 

# Entrada de dados

for i in range(5):
    x[i] = float(input(f"\nDigite um número: "))

# Processamento:

for i in range(5):
    y[i] = x[i]**2

# Saída de dados

for i in range(5):
    print(f"\nO quadrado de {x[i]} é {y[i]}.\n")