faltas = int(input('Digite sua quant. de faltas: '))

if faltas < 25:
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    media = (n1+n2)/2
    if media >= 6 :
        print('Aluno aprovado por média: ', media)
    elif media < 3:
        print('Aluno reprovado com média: ', media)
    else :
        print('Aluno em exame final com média: ', media)
else: 
    print('Aluno reprovado por falta')

