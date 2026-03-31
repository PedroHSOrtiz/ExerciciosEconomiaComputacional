# Programa Valor Capitalizado
# Descrição: Este programa calcula o valor capitalizado de um investimento
# Autor: Pedro H. S. Ortiz
# Data: 29/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

montante = 0

taxa = 0

prazo = 0

# Entrada de dados

montante = float(input("Qual o capital inicial? Digite apenas o número sem separador de milhar e usando ponto como separador decimal quando necessário: "))

taxa = float(input("Qual a taxa de juros do investimento? Digite o valor percentual sem o símbolo % (digite 10% como 10, não 0.1), sem separador de milhar e usando ponto como separador decimal quando necessário: "))

prazo = float(input("Qual o prazo de investimento? Use a mesma medida de tempo que usada na taxa, digite apenas o número sem separador de milhar e usando ponto como separador decimal quando necessário: "))

# Processamento:

capitalsimples = montante*prazo*(1 + (taxa/100))

capitalcomposto = montante*(1 + (taxa/100))**prazo

# Saída de dados

print(f"O valor final do seu investimento será R${capitalsimples} com juros simples e {capitalcomposto} com juros compostos")