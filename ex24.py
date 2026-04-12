# Programa IMC
# Descrição: Este programa classifica a pessoa de acordo com o IMC calculado a partir de peso e altura informados
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

peso = 0.0

altura = 0.0

imcs = {"Excessivamente magro" : (0, 18.5),
        "Peso Normal" : (18.5, 25),
        "Sobrepeso" : (25, 30),
        "Obeso" : (30, 2500)}

imc = 0.0

match = False

# Entrada de dados

peso = float(input("\nQual o seu peso em quilos? "))

altura = float(input("\nQual a sua altura em metros? Use o ponto como separador decimal. "))

# Processamento:

imc = peso / (altura ** 2)

# Saída de dados

for condição, (min, max) in imcs.items():
    if min <= imc < max:
        print(f"Seu IMC é {imc} e sua condição é {condição}")