import csv


"""
A demonstration how to complicate a trivial task for no reason at all

A simple calculator that allows user to simulate 
currency exchange 

INPUT:
csv file 'currency_value.txt' in format currency_name, exchange_rate
(what is single unit of said currency worth in relation to for example  USD)

OUTPUT:
The amount of money you would receive if you tried to exchange some amount 
of one currency to the other
"""

with open('currency_value.txt') as currency_data:

    # ideally done with dict comprehension(list comprehension for dicts, idk how its called :p
    my_dict = dict()
    for row in currency_data:
        row = row.split(',')
        my_dict[row[0]] = int(row[1])


def money_changer(currency_start, currency_start_amount, currency_end):
    value = currency_start*currency_start_amount/currency_end
    value = str(value)
    currency_start_amount = str(currency_start_amount)

    print(('Po zamianie {} {} --> {} otrzymasz {} {}').format(currency_start_amount,
                                                               currency_start, currency_end, value, currency_end))


def data_cleaner(expected_type, text):
    # obviously ugly, TBD
    #
    data = input(text)
    if data == '':
        return data_cleaner(expected_type, text)
    elif type(data) == expected_type:
        return data
    try:
        return expected_type(data)
    except ValueError:
        print('Coś poszło nie tak')
        return data_cleaner(expected_type, text)


def get_data():
    currency_start = data_cleaner(str, 'Podaj walutę z której chcesz przewalutować ')
    currency_start_amount = data_cleaner(int, 'Ile jej masz? ')
    currency_end = data_cleaner(str, 'Podaj walutę do której chcesz przewalutować ')
    currency_start = my_dict[currency_start]
    currency_end = my_dict[currency_end]
    return currency_start, currency_start_amount, currency_end


def continue_loop():
    """"
    Asks user if they want to keep going or not until they give a proper answer,
    if overused ram iz gonna melt
    """
    inputz = input('Jeszcze raz?(Y/N) ')
    if inputz == 'Y':
        return True
    elif inputz == 'N':
        return False
    else:
        return continue_loop()


def initial_info():
    """
    prints out 10 keys in a row, than goes down a row,
    should be done in 2 lines at worst
    """
    keys = [key for key in my_dict.keys()]
    for i in range(len(keys)):
        if i%9 == 0:
            print('\n')
        print(keys[i], end=',')
    print('\n')


def main():
    initial_info()
    while continue_loop:
        currency_start, currency_start_amount, currency_end = get_data()
        money_changer(currency_start, currency_start_amount, currency_end)
        continue_loop()


main()
