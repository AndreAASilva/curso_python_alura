total = 0
palavra = "André Anderson"
acabou = False

while(not acabou):
    acabou = (total == len(palavra)) #Faz a contagem de caracteres da variável
    total += 1

print(total - 1) #Imprime a quantidade de caracteres da variável