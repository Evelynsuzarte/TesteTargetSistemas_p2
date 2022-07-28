#função para cálculo de porcentagem
def porcentagem (total , valor):
    div = valor/total
    porc = round(div * 100)
    return porc


SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53

soma = SP + RJ + MG + ES + outros

#porcentagens por estado
porcentagem_SP = print("SP representa {}% ""do valor total.".format(porcentagem(soma,SP)))
porcentagem_RJ = print("RJ representa {}% ""do valor total.".format(porcentagem(soma,RJ)))
porcentagem_MG = print("MG representa {}% ""do valor total.".format(porcentagem(soma,MG)))
porcentagem_ES = print("ES representa {}% ""do valor total.".format(porcentagem(soma,ES)))
porcentagem_Outros = print("Outros representa {}% ""do valor total.".format(porcentagem(soma,outros)))
