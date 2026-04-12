# Programa Sinal do Número
# Descrição: Este programa verifica se o número é positivo, nulo ou negativo
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

num = 0.0

resposta = ""

# Entrada de dados

num = float(input("\nInforme o número que deseja analisar: "))

# Processamento:

if num < 0:
    resposta = f"O número {num} é negativo."
elif num > 0:
    resposta = f"O número {num} é positivo."
else:
    resposta = f"O número {num} é nulo."

# Saída de dados

print(resposta)