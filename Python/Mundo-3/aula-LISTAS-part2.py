pessoas2 = [["Pedro",25], ["Maria",19],["João",32]]
print(pessoas2)
print(pessoas2[0][0])
print(pessoas2[1][1])
print(pessoas2[2][0])
print(pessoas2[1])

print("-=="*30)

for p in pessoas2:
    print(f"{p[0]} tem {p[1]} anos de idade.")

print("-=="*30)
teste = list()
teste.append("Gastuvo")
teste.append(48)
galera = list()
galera.append(teste[:])
teste[0] = "Maria"
teste[1] = 22
galera.append(teste[:])
print(galera)

print("-=="*30)
print("Pegando diversos valores")
print("-=="*30)

turma = []
dado = []
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    turma.append(dado[:])
    dado.clear()
for p in turma:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmenor +=1
print(f"Temos {totmaior} maiores de idade e {totmenor} menores de idade")