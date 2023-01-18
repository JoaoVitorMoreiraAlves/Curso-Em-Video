#Como por cor \033[style, text, background, m]

#Style podem receber estilos 0,1,4,7
#1 = nada, 1 é Bold, 4 é Underline, 7 é Negative

#Text pode receber 30,31,32,33,34,35,36,37
#30 cinza, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 roxo, 36 azul claro, 37 branco

#BackGround pode receber 40,41,42,43,44,45,46,47
#40 default, 41 vermelho, 42 verde, 43 amarelo, 44 azul, 45 roxo, 46 azul claro e 47 branco

print('\033[0;31;47mOla, Mundo!\033[m')

nome = "João Vitor Moreira Alves"

print("Olá! Muito prazer em te conhecer: {}{}{} !!!!".format("\033[4;37;44m",nome,'\033[m'))

