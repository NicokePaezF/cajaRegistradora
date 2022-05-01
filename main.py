import datetime
# {}: dictionary
# []: list

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
    category = input('Enter the product category : ')
    price = input('Enter the product price : ')
    amount = input('Enter the product amount: ')
    details = {
        'code_product': code_product,
        'name_product': name_product,
        'category': category,
        'price': price,
        'amount': amount
    }
    invoice.get('details').append(details)
    answer = input('do you wish to continue? yes/no')

    if answer == 'no':
        state = False

