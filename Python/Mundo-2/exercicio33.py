#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
opcao = ""
vitoria = 0
pc = random.randint(1,10)


print("-="*20)
print("VAMOS JOGAR IMPAR OU PAR?")
print("-="*20)

num = int(input("Digite um valor entre 0 e 10: "))
while True:
    while num < 0 or num > 10:
        num = int(input("Digite um valor entre 0 e 10: "))

    while opcao != "P" and opcao != "I":
        opcao = str(input("""        *****************
        [  P  ] Para Par
        [  I  ] Para Impar
        *****************
        Escolha sua opcao: """)).upper()[0]   
    
    print("O computador jogou {} e você jogou {} a soma dos dois é {}".format(pc,num,num+pc))

    if opcao == "P":
        if ((pc+num)%2) == 0:
            print("Você venceu pois {} é par".format(num+pc))
            vitoria += 1
            num = -1
            opcao = ""
            pc = random.randint(1,10)
        else:
            print("Você perdeu pois {} é impar\nE perdeu junto a sua invencibilidade de {} jogos".format(num+pc,vitoria))
            pc = random.randint(1,10)
            break
    elif opcao == "I":
        if ((pc+num)%2) == 1:
            print("Você venceu pois {} é impar".format(num+pc))
            vitoria += 1
            num = -1
            opcao = ""
            pc = random.randint(1,10)
        else:
            print("Você perdeu pois {} é par\nE perdeu junto a sua invencibilidade de {} jogos".format(num+pc,vitoria))
            pc = random.randint(1,10)
            break