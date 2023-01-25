#Crie um programa que leia NOME e DUAS NOTAS de vários alunos e guarde tudo em uma LISTA COMPOSTA. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

aluno = []
opinador = ""
nome = ""
while True:
    nome = str(input("Digite o nome do aluno: ")).capitalize()
    aluno.append(nome)
    aluno.append(float(input("Digite a primeira nota: ")))
    aluno.append(float(input("Digite a segunda nota: ")))
    while opinador != "S" and opinador != "N":
        opinador = (str(input("Deseja continuar? [S/N]: "))).upper()[0]
    if opinador == "N":
        break
    else:
        opinador = ""

print("-="*15)
print("Notas dos Alunos")
print("-="*15)
for i in range(0,len(aluno),3):
    media = (aluno[i+1] + aluno[i+2]) / 2
    if i == 0 or i % 3 == 0:
        print(f"Nome: {aluno[i]}, Media: ",end="")
    print(media)

print("-="*15)
opinador = ""
while True:
    while opinador != "S" and opinador != "N":
        opinador = (str(input("Deseja ver a nota de alguém? [S/N]: "))).upper()[0]
    if opinador == "N":
        break
    else:
        opinador = ""
    nome = str(input("Digite o nome do Aluno: ")).capitalize()
    if nome not in aluno:
        print(f"O aluno {nome} não existe ou foi digitado errado")
    else:
        for i in range(0,len(aluno),3):
            if nome == aluno[i]:
                print(f"Aluno: {aluno[i]}, Primeira nota: {aluno[i+1]}, Segunda Nota: {aluno[i+2]}, Média: {(aluno[i+1]+aluno[i+2])/2} ")   