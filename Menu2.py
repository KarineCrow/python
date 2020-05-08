from os import system
from time import sleep

print('''      ........Menu.......\n
    [ 1 ] R$ 1,00 - Coxinha
    [ 2 ] R$ 2,00 - Enroladinho
    [ 3 ] R$ 3,00 - Pastel\n''') 

opcao = int(input('Selecione opção:'))

if opcao == 1:
    print('Coxinha adicionada.')
    valor1 = 1
    pass
elif opcao == 2:
    print('Enroladinho adicionado.')
    valor1 = 2
    pass
elif opcao == 3:
    print('Pastel adicionado.')
    valor1 = 3
    pass
else:
    print('Opção inexistente. Digite outra vez.') 

print('''........Menu bebidas.......\n
    [ 1 ] R$ 1,00 - Refrigerante
    [ 2 ] R$ 1,00 - Suco
    [ 3 ] R$ 2,00 - Suco natural\n''') 

opcao2 = int(input('Selecione opção:'))

if opcao2 == 1:
    print('Refrigerante adicionado.')
    valor2 = 1
    pass
elif opcao2 == 2:
    print('Suco adicionado.')
    valor2 = 1
    pass
elif opcao2 == 3:
    print('Suco natural')
    valor2 = 2
    pass
else:
    print('Opção inexistente. Digite outra vez.') 
    
print('''........Menu bebidas.......\n
    [ 1 ] Valor
    [ 2 ] Fechar\n''') 

opcao3 = int(input('Selecione opção:'))

if opcao2 == 1:
    valor = valor1 + valor2
    print(valor)
    pass
elif opcao2 == 2:
    SystemExit
    pass
else:
    print('Opção inexistente. Digite outra vez.') 

