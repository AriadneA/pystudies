a = 10 
print(a)

a = int(input('digite um numero: '))

print(a)

exemplo = [] #lista vazia //  aspas simples =  posso criar comentarios de blocos   

def func() : 
    """essa é uma função que nao serve para nada""" 
    return 'teste'

obj = ['bola', 'carro' , 21, 21.2, True, "ASpaas"]

print(obj)

print('\n')

for i, objeto in enumerate(obj) :  # enumerando a lista 
    print(i+1,' - ', objeto)


print('Os 3° primeiros: ', obj[0:3])

print( '2a metade: ', obj[len(obj)//2:])


