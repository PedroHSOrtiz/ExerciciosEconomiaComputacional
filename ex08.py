# Programa Equação Linear
# Descrição: Este programa resolve a equação linear ax - b = 0
# Autor: Pedro H. S. Ortiz
# Data: 24/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

a = 0

b = 0

x = 0

# Entrada de dados

a = float(input("Qual o coeficiente linear?"))

b = float(input("Qual a constante?"))

# Processamento:

x = b/a

# Saída de dados

print(f"A solução de {a}x = {b} é {x}")