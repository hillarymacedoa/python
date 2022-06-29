import getpass

account_typed = input('Digite sua conta: ')
password_typed = input('Digite sua senha: ')

#accounts_list = {
#    '0001-02': {
#        'password': '123456',
#        'name' : 'Fulano de Souza',
#        'value': 0
#    },
#    '0002-03': {
#       'password': '246810',
#       'name': 'Fulano da Silva',
#       'value': 1
#   }
#}

#if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
#    print('Conta valida')
#else:
#    print('Conta invalida')


# Resolucao 2

accounts_list = [
     {  'agency': '0001-02',
        'password': '123456',
        'name' : 'Fulano de Souza',
        'value': 0
     },
     {  'agency': '0002-03',
        'password': '246810',
        'name': 'Fulano da Silva',
        'value': 1
     }
]
    
flag = False 
for account in accounts_lisr:
    if account_typed == account['agency'] and password_typed == account['password']:
        flag = True
        print('Conta valida')
if not flag:
    print('Conta Invalida')
