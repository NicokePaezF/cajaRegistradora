import datetime
import logging
# {}: dictionary
# []: list


logging.basicConfig(filename='cajaRegistradora.log', encoding='utf-8', level=logging.DEBUG)
logging.info('This is our first log and it will be saved in the file CajaRegistradora.log')

invoice = {}
rut_customer = input("Enter RUT customer, to associate them with their points:")
mail_customer = input("Enter customer email for your virtual ticket:")
date_now = datetime.date.today()
invoice['rut_customer'] = rut_customer
invoice['mail_customer'] = mail_customer
invoice['date_now'] = date_now
invoice['details'] = []
print('Start product entry: ')

state = True
while state:
    code_product = input('Enter the product code: ')
    name_product = input('Enter the product name: ')
    category = input('Enter the product category: ')
    price = int(input('Enter the product price: '))
    quantity = int(input('Enter the product quantity: '))
    details = {
        'code_product': code_product,
        'name_product': name_product,
        'category': category,
        'price': price,
        'quantity': quantity
    }
    invoice.get('details').append(details)
    answer = input('do you wish to continue? yes/no')

    if answer == 'no':
        state = False

print(f'customer: {invoice.get("rut_customer")}')
print(f'mail: {invoice.get("mail_customer")}')
print(f'date: {invoice.get("date_now")}')
total = 0

for product in invoice.get('details'):
    print(f'{product["code_product"]} {product["name_product"]} {product["quantity"]} {product["price"]} {product["quantity"] * product["price"]}')
    total += product["quantity"] * product["price"]
print(f'Total to pay: {total}')

with open('invoice.txt', 'w') as file:
    file.write(f'customer: {invoice.get("rut_customer")}\n')
    file.write(f'mail: {invoice.get("mail_customer")}\n')
    file.write(f'date: {invoice.get("date_now")}\n')
    for product in invoice.get('details'):
        file.write(f'{product["code_product"]} {product["name_product"]} {product["quantity"]} {product["price"]} {product["quantity"] * product["price"]} \n')
    file.write(f'Total to pay: {total}\n')