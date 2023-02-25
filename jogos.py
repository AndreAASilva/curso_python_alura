import forca
import jogo_adivinhacao_novo

print('********************************')
print("Bem vindo ao jogo de adivinhação")
print('********************************')

print("(1) Jogo da forca (2) Jogo da adivinhação")

jogo = int(input("Qual o jogo? "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()
elif(jogo == 2):
    print("Jogando adivinhação")
    jogo_adivinhacao_novo.jogar()