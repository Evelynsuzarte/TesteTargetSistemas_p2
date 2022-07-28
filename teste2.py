ultimo = 0
penultimo = 1
achou = 0

n = int(input("Digite um número pra gerar a sequência Fibonacci: "))
encontra = int(input("Que número você quer encontrar na sequência? "))

if (n == 0) or (n == 1):
    print("1")
else:
    contador = 2
    while contador <= n:
        item = ultimo + penultimo
        penultimo = ultimo
        ultimo = item
        contador += 1
        if item == encontra:
            achou = item

    print("------- RESULTADO -------")

    if achou == 0:
        print("O número {} NÃO EXISTE na sequência!\n\n".format(encontra))
    if achou == encontra:
        print("O número {} EXISTE na sequência!".format(encontra))
        
    print("O Fibonacci de {} é {}".format(n, item))
