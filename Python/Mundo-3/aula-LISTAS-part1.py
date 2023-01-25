num = [2,5,9,1]
print(f"Lista: {num}")
num[2] = 3 #Trocando valor 9 por 3
print(f"Trocando o valor 9 por 3\nLista: {num}")

num.append(7) #Adicionando o 7 no final
print(f"Adicionando o 7 no final\nLista: {num}")

num.sort() #Colocar em ordem
print(f"Colocando em ordem crescente\nLista: {num}")

num.sort(reverse=True) #Colocar em ordem descrescente
print(f"Colocando em ordem Descrescente\nLista: {num}")

print(f"Essa lista tem {len(num)} elementos")

num.insert(2,0) #Inserindo o valor 0 na posição 2
print(f"Inserindo um valor no meio da lista\nLista: {num}")

num.pop() #Esclue o ultimo elemento da lista
print(f"Excluindo ultimo elemento\nLista: {num}")

num.pop(2) #Esclue o elemento da posição 2 da lista
print(f"Excluindo um elemento no meio da lista\nLista: {num}")

num.insert(2,2) #Inserindo um valor repetido
print(f'Inserindo um valor repetido\nLista: {num}')

num.remove(2) #Removendo um valor q tem mais de 1x na lista (Ele só remove a primera ocorrência do valor)
print(f"Removendo um valor repetido na lista\nLista: {num}")

if 4 in num:
    num.remove(4)
else:
    print(f"Não achei o número 4 na lista: {num}")

valores = [] #criando lista vazia

valores.append(5)
valores.append(9)
valores.append(4)

for v, c in enumerate(valores):
    print(f"Na posição {v} encontrei o valor {c}")

comida = [] 
print("Pegando diversos valores pra lista através do for")
for cont in range(0,5):
   comida.append(str(input("Digite a comida: ")))
print(comida)


a = [2,3,4,7]
b = a

print(f"Lista A: {a}")
print(f"Lista B: {b}")

print("Atribui a lista B o valor 8")
b[2] = 8

print(f"Lista A: {a}")
print(f"Lista B: {b}")
print("Ambas as listas mudaram")

c = a[:]
c[1] = 8
print("Mas, então como eu modifico o valor de uma e não da outra? simplesmente utilizando o [:] veja a seguir:")
print(f"Lista C: {c}")
print(f"Lista A: {a}")