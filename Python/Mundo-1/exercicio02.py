#Perguntando a data de nascimento
dia = int(input("Digite o dia: "))
mes = input("Digite o mês: ")
ano = int(input("Digite o ano: "))

print("*"*50)
print ("Você nasceu no dia ",dia," de ", mes ," de ",ano," correto?")
print("*"*50)
print(f"Você nasceu no dia {dia} do mês {mes} do ano {ano}")
print("*"*50)
print("Você nasceu no dia {} do mês {} do ano {}" .format(dia,mes,ano))