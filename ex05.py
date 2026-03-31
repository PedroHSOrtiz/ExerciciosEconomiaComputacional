# Programa Salário
# Descrição: Este programa calcula o salário de um professor horista na Universidade XYZ
# Autor: Pedro H. S. Ortiz
# Data: 24/03/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

horas = 0

salbruto = 0

salliq = 0

desconto = 0

totaldesconto = 0

valorhora = 0

# Entrada de dados

horas = float(input("Quantas horas você trabalha no mês?"))

desconto = float(30/100)

valorhora = 40

# Processamento:

salbruto = float(horas * valorhora)

totaldesconto = float(desconto * salbruto)

salliq = float(salbruto - totaldesconto)

# Saída de dados

print(f"Seu salário bruto é R${salbruto}, seu desconto total de impostos é R${totaldesconto} e seu salário líquido é R${salliq}")