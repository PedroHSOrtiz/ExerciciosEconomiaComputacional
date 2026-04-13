# Programa 6 3 3
# Descrição: Este programa retorna o cubo e a raíz cúbica de 6 números informados pelo usuário
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

x = [0.0]*6

y = [0.0]*6

z = [0.0]*6

# Entrada de dados

for i in range(6):
    x[i] = float(input("Insira um número: "))

# Processamento:

for i in range(6):
    y[i] = x[i]**3

for i in range(6):
    z[i] = x[i]**(1/3)

# Saída de dados

print(f"\nA sequência de números inserida é {sorted(x)}, cujos cubos são {sorted(y)} e as raízes cúbicas são {sorted(z)}.\n")