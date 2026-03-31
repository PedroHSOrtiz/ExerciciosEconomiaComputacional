# Programa Progressão Aritmética
# Descrição: Este programa calcula o n-ésimo termo e a soma dos termos de uma Progressão Aritmética
# Autor: Pedro H. S. Ortiz
# Data: 24/03/2026
# Versão: 0.0.3
# Notas da versão: Corrigido str() por float()

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

termo = float(primeiro + n * r - r)

soma = float(((primeiro + termo) * n)/2)

# Saída de dados

print(f"O termo número {n} da Progressão Aritmética é {termo} e a soma dos termos é {soma}")