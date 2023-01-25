#Crie uma TUPLA preenchida com os 20 PRIMEIROS colocados da tabela do campeonato brasileiro de futebol, na ordem de colocação. Depos mostra:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.

tupla = ("Palmeiras", "Internacional", "Fluminense", "Corinthians", "Flamengo", "Athletico-PR", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG", "Botafogo",
"Santos", "Goiás", "Bragantino", "Coritiba", "Cuiabá", "Ceará", "Atletico-GO", "Avaí", "Juventude")
print("=*"*30)
print("Lista dos times do Brasileirão: {}".format(tupla))
print("=*"*30)
print("Os 5 primeiros times são: {}".format(tupla[:5]))
print("=*"*30)
print("Os ultimos 4 times são: {}".format(tupla[-4:]))
print("=*"*30)
print("Times em ordem afabética são: {}".format(sorted(tupla)))
print("=*"*30)
print("O Bragantino está na posição: {}".format(tupla.index("Bragantino")))