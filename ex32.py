# Programa Pares 100
# Descrição: Este programa retorna todos os números pares de 1 a 100
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

n = 100

pares = []

# Entrada de dados



# Processamento:

for x in range(1, n+1):
    if x % 2 == 0:
        pares.append(x)

# Saída de dados

print(f"\nOs números pares de 1 a {n} são {pares}")