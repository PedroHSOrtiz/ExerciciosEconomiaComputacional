# Programa Salário Líquido
# Descrição: Este programa calcula o salário líquido de um empregado
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

tabela = {(0, 1000): 0,
          (1000, 2500) : 0.1,
          (2500, 5000) : 0.2,
          (5000, 9999999999999999999) : 0.35}

percentual = {0 : "0%",
              0.1 : "10%",
              0.2 : "20%",
              0.35 : "35%"}

salario = 0.0

salarioliquido = 0.0

# Entrada de dados

salario = float(input("\nQual o seu salário bruto? Digite apenas o número e use . como separador decimal: "))

# Processamento:

for (min, max), aliquota in tabela.items():
    if min <= salario < max:
        salarioliquido = salario*(1-aliquota)
        break

# Saída de dados

print(f"\nSeu salário líquido é de R${salarioliquido} e sua alíquota de imposto de renda é de {percentual[aliquota]}.\n")