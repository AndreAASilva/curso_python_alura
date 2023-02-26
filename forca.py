
def jogar():
    print('********************************')
    print("***Bem vindo ao jogo da forca***")
    print('********************************')

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_",]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra?")
        chute = chute.strip() #Eliminar espações em branco na hora da pesquisa e não causar erro

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #upper() convente a string em maiúscula 
                letras_acertadas[index] = letra
            index = index + 1
        

        print(letras_acertadas)




    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()