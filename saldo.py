import getpass

print('****************************************')
print('*** School of Net - Caixa Eletronico ***')
print('****************************************')

account_typed = input('Digite sua conta: ')
password_typed = input('Digite sua senha: ')

## agencia, senha, nome, valor

accounts_list = {
    '0001-02': { 
        'password1': '123456',
        'name1': 'Fulano da Silva',
        'value': 0
    },
    '0001-03': {
        'password1': '24681012',
        'name1': 'Fulano de Souza',
        'value': 1
    }
}

if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
    print('****************************************')
    print('*** School of Net - Caixa Eletronico ***')
    print('****************************************')
    print('1 - saldo')
    option_typed = input('Escolha uma das opções acima: ')
    if option_typed == '1':
        print('Seu saldo é: $s' % accounts_list[account_typed]['valu'])
    
else:
    print('Conta invalida')
    


    
