pessoas = {"Nome": "João","Idade": 19,"Sexo": "M"}
print("-="*30)
print(pessoas.keys())
print("-="*30)
print(pessoas.values())
print("-="*30)
print(pessoas.items())
print("-="*30)
print(f"O {pessoas['Nome']} tem {pessoas['Idade']}")
print("-="*30)
for k in pessoas.keys():
    print(f"{k}, ",end="")
print("")
print("-="*30)
for k in pessoas.values():
    print(f"{k}, ",end="")
print("")
print("-="*30)
for k,v in pessoas.items():
    print(f"{k} = {v}")
print("-="*30)
del pessoas["Sexo"]

pessoas["Nome"] = "Gustavo"
print(pessoas)
print("-="*30)
pessoas["Peso"] = 100
print(pessoas)

print("-="*30)
print("CRIANDO DICIONARIO DENTRO DE LISTA")
print("-="*30)

estado1 = {"uf": "Rio de Janeiro", "sigla": "RJ"}
estado2 = {"uf": "São Paulo", "sigla": "SP"}
brasil = list()
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]["uf"],brasil[0]["sigla"])
print(brasil[1]["uf"],brasil[1]["sigla"])
print("-="*30)

estado = dict()
brasil = list()
for c in range(0,3):
    estado["uf"] = str(input("Digite a Unicade Federativa: "))
    estado["sigla"] = str(input("Digite a sigla do Estado: "))
    brasil.append(estado.copy())
for e in (brasil):
    for k,v in e.items():
        print(f"O campo {k} tem valor {v}")
print("-="*30)
for e in brasil:
    for v in e.values():
        print(v,end="")