# Programa Metade-Dobro
# Descrição: Este programa lê um número e imprime na tela seu dobro se for menor que 10 e sua metade se for de 10 a 20.
# Autor: Pedro H. S. Ortiz
# Data: 10/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

numero = 0.0

# Entrada de dados

numero = float(input("\nInsira um número: "))

# Processamento:

if numero < 10:
    valor = numero * 2
    
elif 10 < numero < 20:
    valor = numero / 2

else:
    valor = "Número não é válido, por favor, execute novamente o programa."

# Saída de dados
print(valor)
