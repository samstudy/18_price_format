import re


def format_price(price):
    if type(price) is int:
        updated_price = "{:,}".format(price)
        return (updated_price.replace(',',' '))
    if type(price) is float:
        updated_price = ('%f' % price).rstrip('0').rstrip('.')
        if re.findall(r'\.', updated_price):
            formated_price = "{:,}".format(float(updated_price))
            return (formated_price.replace(',',' '))
        else:
            formated_price = "{:,}".format(int(updated_price))
            return(formated_price.replace(',',' '))
    else:
        raise ValueError('Incorrect value')