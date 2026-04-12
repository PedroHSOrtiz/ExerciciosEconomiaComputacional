# Programa Par ou ímpar
# Descrição: Este programa retorna se o número inserido é par ou impar
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

num = 0

res = 0

# Entrada de dados

num = int(input("\nInsira o número inteiro que deseja avaliar se é par ou ímpar: "))

# Processamento:

res = num % 2

# Saída de dados

if res == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")