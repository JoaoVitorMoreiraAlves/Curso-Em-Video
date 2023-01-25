#Crie um programa que tenha uma função chamada vota() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoas tem voto NEGADO, OPCIONAL ou OBRIGÁTÓRIO nas eleições.
from datetime import date
def vota(nasc):
    idade = date.today().year-nasc
    if idade >= 18 and idade < 70:
        return "Votação Obrigatória"
    elif idade < 17:
        return "é muito novo para votar"
    else:
        return "tem voto facultativo, podendo escolher se vota ou não vota"



print("-="*30)
nascimento = int(input("Digite a data de nascimento: "))
print(f"Como você tem {date.today().year-nascimento} anos você: {vota(nascimento)}")