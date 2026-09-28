# Lê um número inteiro informado pelo usuário
numero = int(input("Digite um número não negativo: "))

# Começa o fatorial com 1
fatorial = 1

# Percorre os números de 1 até o número informado
for i in range(1, numero + 1):

    # Multiplica o fatorial pelo valor atual de i
    fatorial *= i

# Mostra o resultado
print("O fatorial de", numero, "é:", fatorial)