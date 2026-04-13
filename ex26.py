# Programa Polinômio
# Descrição: Este programa calcula o valor de um polinômio de grau e coeficientes informados pelo usuário
# Autor: Pedro H. S. Ortiz
# Data: 12/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

i = 0

grau = 0

x = 0.0

poli = 0.0

# Entrada de dados

grau = int(input("\nQual o grau do polinômio cujo valor deseja calcular? Digite apenas o número do grau: "))

a = [0.0] * (grau + 1)

while i <= grau:
    a[i] = float(input(f"\nDigite o coeficiente {i} do polinômio: "))
    i+=1

x = float(input("\nQual o valor de x desejado? "))

# Processamento:

for i in range(grau + 1):
    poli += a[i] * (x**i)

# Saída de dados

print(f"\nO valor do polinômio para x = {x} é {poli}.\n")