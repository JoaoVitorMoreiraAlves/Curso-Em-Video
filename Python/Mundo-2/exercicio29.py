#Crie o programa que leia vários número inteiros pelo teclado. O programa só vai para quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos número foram digitado e qual foi a soma entre elas(desconsiderando o flag[999])

total = cont = num = 0

while num != 999:
    num = int(input("Digite um número [999 para parar]: "))
    if num != 999:
        total += num
        cont += 1
print("Você digitou {} número e a soma entre eles foi {}".format(cont,total))