#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adiciona também as docstrings da função.
def notas(*num,sit=False):
    """
    num = notas
    sit = deseja ver a situacao? (boolean)
    return = dicionario com informacoes
    A funcao tem por objetivo aceitar diversas notas seja ela float ou inteiro, e em um dicionário ele adiciona a quantidade de notas, a media das notas, a maior e a menor nota, e caso o usuario escolha ver a situacao então ele vera a situacao das medias
    """
    dic = {"total":0,"maior":0,"menor":0,"média":0}
    dic["total"] = len(num)
    media = 0
    for n,c in enumerate(num):
        media += c
        if n == 0:
            dic["maior"] = c
            dic["menor"] = c
        else:
            if c > dic["maior"]:
                dic["maior"] = c
            elif c < dic["menor"]:
                dic["menor"] = c
    dic["média"] = media / dic["total"]
    if sit == True:
        if dic["média"] > 7:
            dic["sitação"] = "Boa"
        elif dic["média"] > 5:
            dic["situação"] = "Razoável"
        else:
            dic["sitação"] = "Ruim"
    return (dic)


resp = notas(3.5,6.5,2,7,2,4)
print(resp)
