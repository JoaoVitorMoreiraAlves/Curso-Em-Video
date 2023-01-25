#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formado pela função moeda(), desnevolvida no desafio 108.
from utilidadeCeV import moeda2

p = float(input("Digite o preço R$: "))
print(f"A metade de {moeda2.moeda(p)} é {moeda2.metade(p,True)}")
print(f"O dobro de {moeda2.moeda(p)} é {moeda2.dobro(p,False)}")
print(f"Aumentando 10%, temos {moeda2.aumenta(p,10,False)}")
print(f"Diminuindo 13%, temos {moeda2.diminui(p,13,False)}")