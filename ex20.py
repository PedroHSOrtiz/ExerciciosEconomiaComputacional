# Programa Cinema
# Descrição: Este programa lê o nome e idade da pessoa e verifica se a pessoa tem idade para assistir a um filme para maiores de 18 anos
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

nome = ""

idade = 0

resposta = ""

# Entrada de dados

nome = input("\nQual o seu nome? ")

idade = int(input("\nQuantos anos você tem? "))

# Processamento:

if idade < 18:
    resposta = "%s não pode assistir a este filme" % (nome)
else:
    resposta = "%s pode assistir a este filme" % (nome)

# Saída de dados

print (resposta)