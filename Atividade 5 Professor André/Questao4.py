# Cria uma variável para contar os números pares
contador = 0
# Percorre os números de 1 até 100
for numero in range(1, 101):

    # Verifica se o número é par
    if numero % 2 == 0:
        
        # Aumenta o contador em 1
        contador += 1

# Exibe a quantidade de números pares
print("Quantidade de números pares:", contador)