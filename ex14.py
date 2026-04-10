# Programa Distância
# Descrição: Este programa calcula a distância entre dois pontos pela fórmula euclidiana
# Autor: Pedro H. S. Ortiz
# Data: 30/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

x1 = 0

y1 = 0

x2 = 0

y2 = 0

# Entrada de dados

x1 = float(input("Qual a posição do ponto 1 no eixo x?"))

y1 = float(input("Qual a posição do ponto 1 no eixo y?"))

x2 = float(input("Qual a posição do ponto 2 no eixo x?"))

y2 = float(input("Qual a posição do ponto 2 no eixo y?"))

# Processamento:

dist = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

# Saída de dados

print(f"A distância entre o ponto 1 e 2 é de {dist} unidades de distância")