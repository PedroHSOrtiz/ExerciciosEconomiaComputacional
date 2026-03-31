# Programa Média Aritmética
# Descrição: Este programa retorna a média aritmética de quatro números informados pelo usuário
# Autor: Pedro H. S. Ortiz
# Data: 30/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

numero1 = 0

numero2 = 0

numero3 = 0

numero4 = 0

# Entrada de dados

numero1 = float(input("Qual o primeiro número?"))

numero2 = float(input("Qual o segundo número?"))

numero3 = float(input("Qual o terceiro número?"))

numero4 = float(input("Qual o quarto número?"))

ponderar = str(input("Deseja fazer uma média ponderada?"))

# Processamento:

mediasimples = (numero1 + numero2 + numero3 + numero4)/4

if ponderar.lower() == "sim":
    peso1 = float(input("Qual o peso do primeiro número?"))
    peso2 = float(input("Qual o peso do segundo número?"))
    peso3 = float(input("Qual o peso do terceiro número?"))
    peso4 = float(input("Qual o peso do quarto número?"))
    mediaponderada = ((peso1 * numero1) + (peso2 * numero2) + (peso3 * numero3) + (peso4 * numero4))/(peso1 + peso2 + peso3 + peso4)

# Saída de dados

if ponderar.lower() == "sim":
    print(f"A média aritmética simples dos números dados é {mediasimples} e a média aritmética ponderada é {mediaponderada}")
else:
    print(f"A média aritmética simples dos números dados é {mediasimples}")