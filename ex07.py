# Programa Progressão Geométrica
# Descrição: Este programa calcula o n-ésimo termo e a soma dos termos de uma Progressão Geométrica
# Autor: Pedro H. S. Ortiz
# Data: 24/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

primeiro = 0

n = 0

r = 0

termo = 0

soma = 0

# Entrada de dados

primeiro = float(input("Qual o primeiro termo da Progressão Aritmética?"))

r = float(input("Qual a razão da Progressão Aritmética?"))

n = float(input("Qual o número do termo da Progressão Aritmética?"))

# Processamento:

termo = float(primeiro + r**(n-1))

soma = float((primeiro*(r**n - 1))/(n - 1))

# Saída de dados

print(f"O termo número {n} da Progressão Geométrica é {termo} e a soma dos termos é {soma}")