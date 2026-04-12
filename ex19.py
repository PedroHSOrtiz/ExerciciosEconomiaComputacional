# Programa Múltiplo de 3
# Descrição: Este programa lê um número dado pelo usuário e informa se ele é múltiplo de 3
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

num = 0

res = 0

# Entrada de dados

num = int(input("\nDigite o número cuja multiplicidade você deseja verificar: "))

# Processamento:

res = num % 3

# Saída de dados

if res == 0:
    print(f"{num} é múltiplo de 3.")
else:
    print(f"{num} não é múltiplo de 3")