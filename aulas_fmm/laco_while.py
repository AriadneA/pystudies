print("Escrevendo de 1 a 10 com o laço while")

i = 20

while i > 0:
    i = i-1
    if i % 2 == 1: continue #não quebra o laço
    print(i, end=' ')
    