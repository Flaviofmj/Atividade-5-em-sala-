# Pergunta quantos números serão digitados
N = int(input("Quantos números você vai digitar? "))

# Cria uma variável para armazenar a soma
soma = 0

# Repete N vezes
for i in range(N):

    # Lê um número
    numero = float(input("Digite um número: "))

    # Adiciona o número à soma
    soma += numero

# Calcula a média
media = soma / N

# Exibe a média
print("A média aritmética é:", media)