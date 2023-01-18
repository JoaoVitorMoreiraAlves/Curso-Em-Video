#tipos de Operadores Aritiméticos:
# Soma == +
# Subtração == -
# Divisão == /
# Divisão inteira == //
# Multiplicação == *
# Exponenciação == ** ou pow(base, expoente)
# Resto de Divisão == %

#Ordem de precedência
# 1º == ()
# 2º == **
# 3º == * , / , // , % (Faz o primeiro que aparecer)
# 4º == + , -

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

print('-'*30)
print("A soma vale {}".format(n1+n2))
print('-'*30)
print("A subtração vale {}".format(n1-n2))
print('-'*30)
print("A Multiplicação vale {}".format(n1*n2))
print('-'*30)
print("A Divisão vale {:.2f}".format(n1/n2))
print('-'*30)
print("A Divisão inteira vale {}".format(n1//n2))
print('-'*30)
print("O resto da divisão vale {}".format(n1%n2))
print('-'*30)
print("A Exponenciação vale {}".format(pow(n1,n2)))
print('-'*30)