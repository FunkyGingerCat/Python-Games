print ("*********************************")
print ("Bem vindo ao jogo de Adivinhação!")
print ("*********************************")

#parâmetros do jogo
numero_secreto = 42
total_de_tentativas = 3
rodada = 1

#condições do jogo
for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    #entrada do chute
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    #condição de entrada
    if (chute <1 or chute >100):
        print ("Você deve digitar um número entre 1 e 100!")
        continue

    #condições de vitória
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou, seu chute foi maior do que o número secreto!")
        elif(menor):
            print("Você errou, seu chute foi menor do que o número secreto!")    

print ("Fim de jogo")    
