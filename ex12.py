# Programa Área e Circunferência
# Descrição: Este programa retorna a área e a circunferência de um círculo de raio dado pelo usuário
# Autor: Pedro H. S. Ortiz
# Data: 30/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

raio = 0

area = 0

circ = 0

# Entrada de dados

import math

raio = float(input("Qual o raio da circunferência?"))

# Processamento:

area = math.pi*raio**2

circ = math.pi*raio*2

# Saída de dados

print(f"A área do círculo de raio {raio} é {area} e a circunferência {circ}")