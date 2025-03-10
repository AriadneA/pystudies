def pega_numero() :
    n = int(input('Digite um número: '))
    return n

def soma(a, b) : 
    return a+b

n1 = pega_numero()
n2 = pega_numero()

print(f'{n1} + {n2} = {soma(n1,n2)}')

print('\nFazendo outra soma:')
print('A soma dos números é:', soma(pega_numero(), pega_numero()))

