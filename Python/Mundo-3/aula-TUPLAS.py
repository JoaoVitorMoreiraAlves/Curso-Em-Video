#TUPLAS SÃO IMUTAVÉIS --- OU SEJA NÃO PODEMOS MODIFICAR OS VALORES DA TUPLA DURANTE O FUNCIONAMENTO DO PROGRAMA

lanche = ("Hambúrger", "Suco", "Pizza", "Pudim")

print(sorted(lanche)) #Ordem alfabética

print(lanche.count("a"))
print(lanche.index("Pizza"))

a = (1,2,3)
b = (3,4,4,5)
c = a+b
d = b+a

print(a)
print(b)
print(c)
print(d)
print("O 4 está na posição {}".format(d.index(4)))