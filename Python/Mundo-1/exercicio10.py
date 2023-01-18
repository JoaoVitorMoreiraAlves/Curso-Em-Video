#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
# 100 centímetro = 1 metro
# 1000 milimetro = 1 metro


num = float(input("Digite a quantidade de metros: "))
print('-'*50)
print("A quantidade em centímetro é de {} centímetros".format(num*100))
print('-'*50)
print("A quantidade em milimetro é de {} milimetros".format(num*1000))
print('-'*50)