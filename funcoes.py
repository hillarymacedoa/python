def call_numbers():
    for number in range(0,10):
        print(number)

def call_numbers_wit_limit(limit):
    list = range(0,10)
    for number in list[0:limit]:
        print(number)

call_numbers_wit_limit(5)