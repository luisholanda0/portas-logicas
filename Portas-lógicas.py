# Iniciando as variáveis

A = [0,0,1,1]
B = [1,0,1,0]

valor_saida_E = [0,0,0,0]
valor_saida_OU = [0,0,0,0]
valor_saida_NAO = [0,0,0,0]
valor_saida_NAO_E = [0,0,0,0]
valor_saida_NAO_OU = [0,0,0,0]
valor_saida_OU_EXCLUSIVO = [0,0,0,0]

# Começando as portas lógicas

# Porta lógica E:
for var in range(0,4):
    if A[var] == 1 and B[var] == 1:
        valor_saida_E[var] = 1
    else:
        valor_saida_E[var] = 0

print("PORTA LÓGICA E:")
print("A tabela-verdade de A é: " + str(A) + "\nA tabela-verdade de B é: " + str(B) + "\nOs valores de saída da porta lógica E [A.B] são: " + str(valor_saida_E) + "\n")

# Porta lógica OU:
for var in range(0,4):
    if A[var] == 1 or B[var] == 1:
        valor_saida_OU[var] = 1
    else:
        valor_saida_OU[var] = 0

print("PORTA LÓGICA OU:")
print("A tabela-verdade de A é: " + str(A) + "\nA tabela-verdade de B é: " + str(B) + "\nOs valores de saída da porta lógica OU [A+B] são: " + str(valor_saida_OU) + "\n")

# Porta lógica NÃO:
for var in range(0,4):
    if A[var] == 1:
        valor_saida_NAO[var] = 0
    else:
        valor_saida_NAO[var] = 1

print("PORTA LÓGICA NÃO:")
print("A tabela-verdade de A é: " + str(A) + "\nOs valores de saída da porta lógica NÃO são: " + str(valor_saida_NAO) + "\n")

# Porta lógica NÃO E:
for var in range(0,4):
    if valor_saida_E[var] == 1:
        valor_saida_NAO_E[var] = 0
    else:
        valor_saida_NAO_E[var] = 1

print("PORTA LÓGICA NÃO E:")
print("A tabela-verdade de A é: " + str(A) + "\nA tabela-verdade de B é: " + str(B) + "\nOs valores de saída da porta lógica NÃO E são: " + str(valor_saida_NAO_E) + "\n")

# Porta lógica NÃO OU:
for var in range(0,4):
    if valor_saida_OU[var] == 1:
        valor_saida_NAO_OU[var] = 0
    else:
        valor_saida_NAO_OU[var] = 1

print("PORTA LÓGICA NÃO OU:")
print("A tabela-verdade de A é: " + str(A) + "\nA tabela-verdade de B é: " + str(B) + "\nOs valores de saída da porta lógica NÃO OU são: " + str(valor_saida_NAO_OU) + "\n")

# Porta lógica OU EXCLUSIVO:
for var in range(0,4):
    if A[var] == B[var]:
        valor_saida_NAO_OU[var] = 0
    else:
        valor_saida_NAO_OU[var] = 1

print("PORTA LÓGICA OU EXCLUSIVO:")
print("A tabela-verdade de A é: " + str(A) + "\nA tabela-verdade de B é: " + str(B) + "\nOs valores de saída da porta lógica OU EXCLUSIVO são: " + str(valor_saida_NAO_OU) + "\n")