#Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando laço for.

num = int(input("Digite o valor para ver a tabuada: "))
for i in range(1,11):
    print("{} X {:2} = {:2}".format(num,i,num*i))
