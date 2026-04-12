# Programa Capitais
# Descrição: Este programa informa se a cidade informada é capital de um estado da região sul do Brasil
# Autor: Pedro H. S. Ortiz
# Data: 11/04/2026
# Versão: 0.0.1
# Notas da versão:

# Alocação de Memória

estados = []
cidades = []

rs = "Rio Grande do Sul"
sc = "Santa Catarina"
pr = "Paraná"

poa = "porto alegre"
flo = "florianópolis"
cur = "curitiba"

cidade = ""
resposta = ""

estados.append(rs)
estados.append(sc)
estados.append(pr)

cidades.append(poa)
cidades.append(flo)
cidades.append(cur)

match = False

i = 0

# Entrada de dados

cidade = input("\nInforme uma cidade: ")

# Processamento:

while i < len(cidades):
    if cidades[i] == cidade.lower():
        match = True
        break
    i += 1

if match:
    resposta = f"\n{cidade} é a capital do estado de {estados[i]}.\n"
else:
    resposta = f"\n{cidade} não é capital de nenhum estado da região sul do Brasil. Verifique se digitou corretamente.\n"

# Saída de dados

print(resposta)