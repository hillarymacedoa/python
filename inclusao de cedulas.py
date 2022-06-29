import getpass
import os


while True:
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
            'value': 4000,
            'adimn': False
        },
        '0001-03': {
            'password1': '24681012',
            'name1': 'Fulano de Souza',
            'value': 1000,
            'adimn': False
        },
        '0131-04': { 
            'password1': '232425',
            'name1': 'Fulano da Costa',
            'value': 14000,
            'adimn': True
        }
    }

    money_slips = {
        '25': 5,
        '57': 5,
        '140': 5,
        

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('****************************************')
        print('*** School of Net - Caixa Eletronico ***')
        print('****************************************')
        print('1 - saldo')
        if accounts_list[account_typed]['admin'] == True:
            print('10 - Incluir cedulas')
        option_typed = input('Escolha uma das opções acima: ')
        if option_typed == '1':
            print('Seu saldo é: $s' % accounts_list[account_typed]['valu'])
        elif option_typed == '10' ad accounts_list[account_typed]['admin']:
            amount_typed = input('Digite a quantidade de cedulas: ')
            money_bill_typed = input('Digite a cedula a ser incluida: ')
            money_slips[money_bill_typed] = money_slips[money_bill_typed] + int(amount_typed)
            print(money_slips)
        
    else:
        print('Conta invalida')

    input('Pressione <Enter> para continuar...') #pause do programa

    if os.name == 'nt': #windowa
        os.system('cls')
    else:
        os.system('clear')
