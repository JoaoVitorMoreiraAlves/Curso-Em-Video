#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ela ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input("Digite o seu ano de nascimento: "))

ano = date.today().year - ano


if (ano < 18):
    print("Você possui no momento {} anos, ainda não necessita de ir ao exercito e precisará ir daqui a {} anos, seu alistamento será em {}".format(ano,18-ano, (date.today().year + (18 - ano))))
elif (ano == 18):
    print("Você possui no momento {} anos, este é o ano em que você deverá ir ao exercíto".format(ano))
else:
    print("Você possui {} anos e ja se passou {} anos que você foi ao exercíto que foi em {}".format(ano, ano -18, (date.today().year - (ano - 18))))