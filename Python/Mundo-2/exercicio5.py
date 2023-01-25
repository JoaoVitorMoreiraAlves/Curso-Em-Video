#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if (media < 5.0):
    print("Você está REPROVADO\nSua média foi de {:.1f}".format(media))
elif (media < 6.9):
    print("Você está de RECUPERAÇÃO\nSua média foi {:.1f}".format(media))
else:
    print("Você está APROVADO\nSua média foi de {:.1f}".format(media))