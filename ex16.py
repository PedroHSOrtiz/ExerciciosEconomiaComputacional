# Programa 
# Descrição: Este programa
# Autor: Pedro H. S. Ortiz
# Data: 30/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

Ri = 0.0

Rf = 0.0

Rm = 0.0

Bi = 0.0

periodo = ""

tempo = ""

# Entrada de dados

Rf = float(input("\nQual o retorno do ativo sem risco? Digite apenas o número da porcentagem sem o sinal: "))

Rm = float(input("\nQual o retorno da carteira de mercado? Digite apenas o número da porcentagem sem o sinal: "))

periodo = input("\nAs taxas informadas são de que tipo: diárias, mensais ou anuais? ")

Bi = float(input("\nQual o coeficiente de sensibilidade do retorno do ativo a variações no prêmio de risco de mercado? "))

# Processamento:

Ri = Rf + Bi * (Rm - Rf)

if periodo.lower() == "diárias":
    tempo = "dia"
elif periodo.lower() == "mensais":
    tempo = "mês"
else:
    tempo = "ano"

# Saída de dados

print(f"O retorno do ativo é de {Ri}% ao {tempo}")