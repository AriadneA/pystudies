def soma (a, b) :
    print(f'A soma de {a} e {b} é: ',{a+b})
    print('A soma de', a, 'e', b, 'é:',a+b)
    print('A soma de %d e %d é: %d' %(a,b,a+b))

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))

soma(n1,n2)