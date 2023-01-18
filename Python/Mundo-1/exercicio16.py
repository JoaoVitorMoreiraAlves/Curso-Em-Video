#Conversão de Temperatura
#Celsius para Fahrenheit é (1ºC * 9/5)+32ºF
#Celsius para Kelvin é 1ºC+273,15K

num1 = float(input("Digite o Valor de Celsius: "))
print('-'*60)
print("O valor em Celsius de {}ºC passa a ser {}ºF e {}K".format(num1,(num1*9/5)+32,num1+273.15))