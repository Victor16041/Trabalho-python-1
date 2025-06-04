senha2 = "1604"


for tentativa in range(5):
    senha = input("Digite a senha (Você tem 5 tentativas): ")
    if senha == senha2:
        print("Acesso liberado")
        break
    else:
        print("Tente novamente")


else:
    print("Falhou todas")

