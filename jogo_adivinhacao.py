print('********************************')
print("Bem vindo ao jogo de adivinhação")
print('********************************')

numero_secreto = 2
total_tentativas = 3
rodada = 1

while(rodada <= total_tentativas):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um númdero: ")
    print("Você digitou:", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 10):
        print("Você deve digitar um número entre 1 e 10")
        continue


    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou! O seu número foi maior do que o número secreto!")
            
        elif(menor):
            print("Você errou! O seu número foi menor do que o número secreto!")

        rodada = rodada + 1



print("Fim de Jogo!")