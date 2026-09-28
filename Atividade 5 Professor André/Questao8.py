while True:

    # Pede a senha ao usuário
    senha = int(input("Digite a senha: "))

    # Verifica se a senha está correta
    if senha == 1234:

        # Libera o acesso
        print("Acesso liberado!")

        # Encerra o while
        break

    else:

        # Informa que a senha está incorreta
        print("Senha incorreta")