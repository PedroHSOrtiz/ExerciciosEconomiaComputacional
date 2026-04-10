# Programa Ordenamento
# Descrição: Este programa ordena três números dados pelo usuários
# Autor: Pedro H. S. Ortiz
# Data: 07/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

i = 0

valores = [0.0] * 3

# Entrada de dados

for i in range (3):
    valores[i] = float(input("\nDigite um número que deseja ordenar: "))

# Processamento:

ordenados = sorted(valores)

# Saída de dados

print(f"Os números em ordem crescente são {ordenados}")