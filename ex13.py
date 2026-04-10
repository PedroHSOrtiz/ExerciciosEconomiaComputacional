# Programa Demanda
# Descrição: Este programa calcula a demanda por um bem dados renda e preço do bem
# Autor: Pedro H. S. Ortiz
# Data: 30/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

renda = 0

preço = 0

# Entrada de dados

renda = float(input("Qual a renda do consumidor?"))

preço = float(input("Qual o preço do bem?"))

# Processamento:

demanda = renda/preço

# Saída de dados

print(f"A quantidade ótima do bem é {demanda}")