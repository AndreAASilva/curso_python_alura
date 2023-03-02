import random

def imprime_mensagem_abertura():
    print('********************************')
    print("***Bem vindo ao jogo da forca***")
    print('********************************')

def carrega_palavra_secreta():
    
    arquivo = open("palavras.txt", "r") #Abrindo arquivo TXT com as palavras
    palavras = []#lista para as palavras so arquivo

    for linha in arquivo:
        linha = linha.strip()#remover espaços entre as palavras
        palavras.append(linha)

    arquivo.close()#Fechando o arquivo

    #Variável numero criada para as palavras dentro da lista
    numero = random.randrange(0,len(palavras))#Puxar palavras da lista de forma aleatória

    palavra_secreta = palavras[numero].upper()

    return palavra_secreta

def jogar():
    
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = ["_" for letra in palavra_secreta]#Utilizando o FOR dentro da lista, saerá acrescentado o espaço das letras da palavra secreta

    enforcou = False
    acertou = False
    erros = 0 #Variável para a quantidade de tentativas

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper() #STRIP Eliminar espações em branco na hora da pesquisa e não causar erro - UPPER verifica se é maiúscula ou minúscula 

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()): #upper() convente a string em maiúscula 
                    letras_acertadas[index] = letra
                index += 1
            
        else: #Verificar a quantidade de tentativas

            erros += 1 #Contagem de tentativas 
            desenha_forca(erros)
        
        enforcou = erros == 7 #Máximo de tentativas
        acertou = "_" not in letras_acertadas #validação de espaços disponíveis para finalizar o jogo caso não tenha acertado

        print(letras_acertadas)
    
        def desenha_forca(erros):
        
            print("  _______     ")
            print(" |/      |    ")

            if(erros == 1):
                print(" |      (_)   ")
                print(" |            ")
                print(" |            ")
                print(" |            ")

            if(erros == 2):
                print(" |      (_)   ")
                print(" |      \     ")
                print(" |            ")
                print(" |            ")

            if(erros == 3):
                print(" |      (_)   ")
                print(" |      \|    ")
                print(" |            ")
                print(" |            ")

            if(erros == 4):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |            ")
                print(" |            ")

            if(erros == 5):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |            ")

            if(erros == 6):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      /     ")

            if (erros == 7):
                print(" |      (_)   ")
                print(" |      \|/   ")
                print(" |       |    ")
                print(" |      / \   ")

            print(" |            ")
            print("_|___         ")
            print()


    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


    
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()