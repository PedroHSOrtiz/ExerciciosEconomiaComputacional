# Programa 1 100
# Descrição: Este programa mostra todos os números de 1 a 100
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

a = [0.0]*100

a[0] = 1

# Entrada de dados

# Processamento:

for i in range(1, 100):
    a[i] = a[i - 1] + 1

# Saída de dados

print(f"\n{a}\n")