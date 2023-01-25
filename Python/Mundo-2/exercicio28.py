

print("-=" * 12)
print("Sequencia de Fibonacci")
print("-=" * 12)

termo = int(input("Digite quantos termos você quer mostrar: "))
cont = 0
aux = 0
t1 = 0
t2 = 1
t3 = t2 + t1
print("~" * 40)

print("{} -> {} ->".format(t1,t2), end="")
while cont < termo:
    cont += 1
    print(" {} -> ".format(t3),end="")
    t1 = t2
    t2 = t3
    t3 = t2+t1
print("FIM")
print("~" * 40)