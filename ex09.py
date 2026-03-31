# Programa Equação Quadrática
# Descrição: Este programa resolve a equação quadrática ax^2 + bx + c = 0
# Autor: Pedro H. S. Ortiz
# Data: 24/03/2026
# Versão: 0.0.2
# Notas da versão: Correção do if e do cálculo das raízes

# Alocação de Memória

a = 0

b = 0

c = 0

delta = 0

raizdelta = 0

real = 0

imag = 0

x1 = 0

x2 = 0

# Entrada de dados

a = float(input("Qual o coeficiente quadrático?"))

b = float(input("Qual o coeficiente linear?"))

c = float(input("Qual a constante?"))

# Processamento:

if a == 0:
    x1 == x2 == c/b
else:
    delta = b**2 - 4*a*c
    if delta >= 0:
        raizdelta = (delta)**(1/2)
        x1 = (-b + raizdelta)/(2*a)
        x2 = (-b - raizdelta)/(2*a)
    else:
        raizdelta = (-delta)**(1/2)
        real = -b/(2*a)
        imag = raizdelta/(2*a)
        x1 = complex(real, imag)
        x2 = complex(real, -imag)

# Saída de dados
if a ==0:
    print(f"Este é um problema linear e sua raíz é {c/b}")
else:
    print(f"As soluções de ax^2 + bx + c = 0 são {x1} e {x2}")