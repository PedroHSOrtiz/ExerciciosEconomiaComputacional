# Programa Termos da PA
# Descrição: Este programa retorna os 10 primeiros termos de uma PA de razão escolhida pelo usuário
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

r = 0.0

a = [0.0]*10

# Entrada de dados

r = float(input("\nQual a razão da Progressão Aritmética? "))

a[0] = float(input("\nQual o primeiro termo da Progressão Aritmética. "))

# Processamento:

for i in range(1, 10):
    a[i] = a[i - 1] + r

# Saída de dados

print(f"Os 10 primeiros termos da Progressão Aritmética escolhida são {a}")