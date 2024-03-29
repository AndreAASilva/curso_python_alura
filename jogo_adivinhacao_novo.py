import random

def jogar():
    print('********************************')
    print("Bem vindo ao jogo de adivinhação")
    print('********************************')

    numero_secreto = round(random.random() *10)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_tentativas = 10
    elif (nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 2

    for rodada in range(1, total_tentativas + 1):
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
            print("Você acertou e fez {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu número foi maior do que o número secreto!")
                
            elif(menor):
                print("Você errou! O seu número foi menor do que o número secreto!")
            #Calculando a pontuação - A pontuação é calculada conforme a diferença entre o valor do chute ao número_secreto

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos




        


    print("Fim de Jogo!")