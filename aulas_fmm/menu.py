def somar(a, b) :
    return a + b

def subtrair(a, b) :
    return a - b

def multiplicar(a, b) :
    return a * b

def divisao(a, b):
    return a / b

def pega_numero() :
    n = int(input('Digite um número: '))
    return n

while True: 
    n1 = pega_numero()
    n2 = pega_numero()
    
    print('\n ***** MENU *****')
    print('1 - SOMAR')
    print('2 - SUBTRAIR')
    print('3 - MULTIPLICAR')
    print('4 - DIVIDIR')
    print('0 - SAIR')
    
    op = int(input('\nDigite sua opção: '))
    
    if op == 0: break
    elif op == 1 : print(f'{n1} + { n2} = {somar(n1,n2)}')
    elif op == 2 : print(f'{n1} - {n2} = {subtrair(n1,n2)}')
    elif op == 3 : print(f'{n1} * {n2} = {multiplicar(n1,n2)}')
    elif op == 4 : print(f'{n1} / {n2} = {divisao(n1,n2)}')
    else : print('\nOpção inválida!')

    input()

