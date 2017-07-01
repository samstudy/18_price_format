import re
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', type=int and float, help='Inputed price format must be integer or float')
    return parser.parse_args()


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
     

if __name__ == '__main__':
    params = get_args()
    beautiful_price = format_price(params.price)
    print(beautiful_price)