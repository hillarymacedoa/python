from file import open_file_bank, write_money_slips, write_bank_accounts
from utils import header

def main():
    header()
    make_money_slips()

def make_money_slips():
    file = open_file_bank('w')
    write_money_slips(file)
    file.close()
    print('Cedulas gravadas com sucesso')

main()
