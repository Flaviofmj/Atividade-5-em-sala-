# Lê um número inteiro
numero = int(input("Digite um número: "))

# Variável que vai guardar a soma
soma = 0

# Começa a contagem em 1
i = 1

# Enquanto i for menor ou igual ao número informado
while i <= numero:

    # Adiciona i à soma
    soma = soma + i

    # Aumenta i em 1
    i = i + 1

# Exibe o resultado
print("A soma de 1 até", numero, "é:", soma)