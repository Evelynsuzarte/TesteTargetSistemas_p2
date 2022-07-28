import json

diasSup = 0
diasMedia = 0
soma = 0
mediaMensal = 0

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

menor = dados[0]['valor']
maior = dados[0]['valor']

#verificação de menor e maior valor de faturamento
for i in dados:
    if i['valor'] < menor and i['valor']!= 0 :
        menor = i['valor']
    if i['valor'] > maior and i['valor']!= 0 :
        maior = i['valor']

#média mensal
for i in dados:
    if i['valor']!= 0:
        soma = soma + i['valor']
        diasMedia = diasMedia + 1
mediaMensal = soma/diasMedia

#dias com faturamento diário superior
for i in dados:
    if i['valor'] > mediaMensal:
        diasSup = diasSup + 1


print("O menor valor de faturamente ocorrido em um dia do mês: R$ {}".format(menor))
print("O maior valor de faturamento ocorrido em um dia do mês: R$ {}".format(maior))
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {}".format(diasSup))


