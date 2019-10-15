"""
A demonstration how to complicate a trivial task for no reason at all

A simple calculator that allows user to simulate 
currency exchange 

INPUT:
csv file 'currency_value.txt' in format <currency_name>,<exchange_rate>,
Users Data, not case sensitive,
(exchange_rate is a single unit of said currency worth in relation to for example  USD)

OUTPUT:
The amount of money you would receive if you tried to exchange some amount 
of one currency to the other
'Po zamianie <start_currency_name> <start_currency_amount> --> <end_currency_name> otrzymasz <end_currency_amount> <end_currency_name>'
"""


with open('currency_value.txt') as currency_data:
    # TBD redundant multiple split operations
    currency_value_dict = {row.split(',')[0]: int(row.split(',')[1])for row in currency_data}


def money_changer(args):
    value = currency_value_dict[args[0]]*args[1]/currency_value_dict[args[2]]
    print('Po zamianie {} {} --> {} otrzymasz {} {}'.format(args[1], args[0], args[2], value, args[2]))


def data_cleaner(expected_type, text):
    # A simple input data validator
    data = input(text).upper()
    if data == '':
        print('Podaj odpowiedź')
        return data_cleaner(expected_type, text)
    if data not in currency_value_dict and expected_type == str:
        print('Niewłaściwe dane poczatkowe')
        return data_cleaner(expected_type, text)
    try:
        return expected_type(data)
    except ValueError:
        print('Pamiętaj oby dane były w formacie {}'.format(expected_type))
        return data_cleaner(expected_type, text)


def get_data():
    cleaned_data = list()

    texts = ['Podaj walutę z której chcesz przewalutować ',
            'Ile jej masz? ',
            'Podaj walutę do której chcesz przewalutować ']

    types = [str, int, str]

    for expected_type, message in zip(types, texts):
        cleaned_data.append(data_cleaner(expected_type, message))
    return cleaned_data


def continue_loop():
    """"
    Asks user if they want to keep going or not until they give a proper answer,
    if overused ram iz gonna melt
    """
    inputz = input('Jeszcze raz?(Y/N) ').upper()
    if inputz == 'Y':
        return True
    elif inputz == 'N':
        return None
    return continue_loop()


def initial_info():
    """
    TBD prints out 10 keys in a row, than goes down a row,
    """
    currency_list = list(currency_value_dict.keys())
    print(currency_list)


def main():
    initial_info()
    while continue_loop:
        money_changer(get_data())
        continue_loop()

main()
