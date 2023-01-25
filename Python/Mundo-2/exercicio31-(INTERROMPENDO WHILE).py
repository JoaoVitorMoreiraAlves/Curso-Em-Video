#Crie um programa que leia vários número inteiro pelo teclado. O Programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos número foram digitado e qual foi a soma entre eles (desconsiderando o flag).

total = cont = 0
while True:
    num = int(input("Digite um número ou 999 para parar: "))
    if (num == 999):
        break
    total += num
    cont += 1
print("Ao todo você usou {} números e a soma deles é de {}".format(cont,total))