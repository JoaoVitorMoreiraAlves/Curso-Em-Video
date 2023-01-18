#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

print('-'*30)
print("A média do aluno entre {} e {} é de {:.1f}".format(nota1,nota2,(nota1+nota2)/2))