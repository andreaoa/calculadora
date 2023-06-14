from pandas.core.indexers.objects import VariableOffsetWindowIndexer
def menu():
  print('*****************Calculadora******************')
  print()
  print('Selecione a opção desejada:')
  print()
  print('1 - Soma')
  print('2 - Subtração')
  print('3 - Multiplicação')
  print('4 - Divisão')
  print('0 - Para sair')
  print()
  #operacao = (int(input('Digite a operação: ')))


def operacao(x):
  
  if x == 1:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print (a ,'+', b, '=', a+b)
    print()

  elif x == 2:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print (a ,'-', b, '=', a-b)
    print()

  elif x == 3:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print (a ,'*', b, '=', a*b)
    print()

  elif x == 4:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print (a ,'/', b, '=', a/b)
    print()

  elif x == 0:
    encerrar()

  else:
    print('valor invalido')
    print()

def encerrar():
  zero = 0


while True:
  menu()
  valor = (int(input('Digite a operação: ')))
  print()
  if valor == 0:
    break
  else:
    operacao(valor)
