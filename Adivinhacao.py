print ("*********************************")
print ("Bem vindo ao jogo de Adivinhação!")
print ("*********************************")

#parâmetros do jogo
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

#condições do jogo
while (rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    #entrada do chute
    chute_str = input("Digite o seu número: ")

    print("Você digitou ", chute_str)

    chute = int(chute_str)
    #condições de vitória
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou, seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Você errou, seu chute foi menor do que o número secreto!")

    rodada = rodada + 1        

print ("Fim de jogo")    
