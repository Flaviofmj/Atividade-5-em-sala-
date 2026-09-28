# Lê uma frase digitada pelo usuário
frase = input("Digite uma frase: ")

# Cria um contador para as vogais
contador = 0

# Percorre cada caractere da frase
for caractere in frase:

    # Verifica se o caractere é uma vogal
    if caractere.lower() in "aeiouáéióú":

        # Aumenta o contador em 1
        contador += 1

# Exibe a quantidade de vogais
print("A frase possui", contador, "vogais.")