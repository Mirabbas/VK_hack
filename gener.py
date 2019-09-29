import random

def name_generator(num):
    Surname = {1: 'Veselov', 2: 'Petrov', 3: 'Koryakov',
               4: 'Bagirov', 5: 'Serebryansky', 6: 'Gushin',
               7: 'Rudoyasov', 8: 'Chelnokov', 9: 'Rubzov',
               10: 'Egorov'}

    Sex = {1: 'male', 2: 'female'}

    Initials = {1: 'A.', 2: 'B.', 3: 'C.', 4: 'D.', 5: 'E.',
                6: 'F.', 7: 'G.', 8: 'H.', 9: 'I.', 10: 'J.',
                11: 'K.', 12: 'L.', 13: 'M.', 14: 'N.', 15: 'O.',
                16: 'P.', 17: 'Q.', 18: 'R.', 19: 'S.', 20: 'T.',
                21: 'U.', 22:'V.', 23:'W.', 24: 'X.', 25: 'Y.',
                26: 'Z.'}

    Names_List = []
    for i in range(num):

        name = {'Name':'', 'Sex':''}
        name['Sex'] = Sex[random.randint(1,2)]

        name_string = Surname[random.randint(1,10)]

        if name['Sex'] == 'female':
            name_string += 'a'

        name_string = name_string + ' ' + Initials[random.randint(1,26)] + Initials[random.randint(1,26)]

        name['Name'] = name_string

        Names_List.append(name)

    return Names_List

def date_generator():
    Date = {'day': random.randint(1, 30), 'month': random.randint(1, 12), 'year': random.randint(2000, 2020)}
    return Date

def calculator_total_cost(price_list):

    result = 0

    result += (price_list['bread'] * price_list['bread_price'])
    result += (price_list['milk'] * price_list['milk_price'])
    result += (price_list['yogurt'] * price_list['yogurt_price'])
    result += (price_list['meat'] * price_list['meat_price'])
    result += (price_list['chicken'] * price_list['chicken_price'])
    result += (price_list['cheese'] * price_list['cheese_price'])
    result += (price_list['biscuit'] * price_list['biscuit_price'])
    result += (price_list['cake'] * price_list['cake_price'])
    result += (price_list['coffee'] * price_list['coffee_price'])
    result += (price_list['tea'] * price_list['tea_price'])

    return result

def purchase_history_generator(names):

    Company = {1: 'MirITeam', 2: 'ASE', 3: 'SPAR', 4: 'Avocado'}


    date = date_generator()

    names_num = (len(names))
    buyers_num = random.randint(0, names_num)


    buyers_list = []
    day_list = []
    for i in range(buyers_num):
        while True:
            rand = random.randint(0, (names_num - 1))
            sex = names [rand]['Sex']
            buyer = names[rand]['Name']
            for j in range(len(buyers_list)):
                if (buyers_list[j] == buyer):
                    break
            try:
                j < 0
            except UnboundLocalError:
                buyers_list.append(buyer)
                break

            if (buyers_list[j] != buyer):
                buyers_list.append(buyer)
                break



        Product = {'bread': random.randint(0,20), 'bread_price': 15,
                   'milk': random.randint(0,20), 'milk_price': 50,
                   'yogurt': random.randint(0,20), 'yogurt_price': 55,
                   'meat': random.randint(0,20), 'meat_price': 80,
                   'chicken': random.randint(0,20), 'chicken_price': 180,
                   'cheese': random.randint(0,20), 'cheese_price': 200,
                   'biscuit': random.randint(0,20), 'biscuit_price': 20,
                   'cake': random.randint(0,20), 'cake_price': 300,
                   'coffee': random.randint(0,20), 'coffee_price': 100,
                   'tea': random.randint(0,20), 'tea_price': 30}



        bill = {'name': buyer, 'sex': sex, 'company': Company[random.randint(1,4)],
                'products': Product, 'total_cost': calculator_total_cost(Product), 'date': date}
        day_list.append(bill)


    return day_list

def print_cheque(data):

    print('\n\n\n\n')
    print('{:^16};{:^12}{:^13}\n'.format('Название', 'Кол-во', 'Цена за штуку'))
    if data['products']['bread'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Хлеб', str(data['products']['bread']), str(data['products']['bread_price'])))
    if data['products']['milk'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Молоко', str(data['products']['milk']), str(data['products']['milk_price'])))
    if data['products']['yogurt'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Йогурт', str(data['products']['yogurt']), str(data['products']['yogurt_price'])))
    if data['products']['meat'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Мясо', str(data['products']['meat']), str(data['products']['meat_price'])))
    if data['products']['chicken'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Курица', str(data['products']['chicken']), str(data['products']['chicken_price'])))
    if data['products']['cheese'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Сыр', str(data['products']['cheese']), str(data['products']['cheese_price'])))
    if data['products']['biscuit'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Печенье', str(data['products']['biscuit']), str(data['products']['biscuit_price'])))
    if data['products']['cake'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Торт', str(data['products']['cake']), str(data['products']['cake_price'])))
    if data['products']['coffee'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Кофе', str(data['products']['coffee']), str(data['products']['coffee_price'])))
    if data['products']['tea'] != 0:
        print('{:^16}{:^12}{:^13}\n'.format('Чай', str(data['products']['tea']), str(data['products']['tea_price'])))
    print('\n\n-----------------------------------------\n\n')
    print('ИТОГО:                  ' + str(data['total_cost']) + '\n')
    print('Оплата картой:          ' + str(data['total_cost']) + '\n')
    print('Оплатил(ла):            ' + str(data['name']) + '\n')
    print('Пол:                    ' + data['sex'] + '\n')
    print('Чек выдвн компанией:    ' + data['company'] + '\n')
    print('Дата совершения платежа:' + str(data['date']))
    print('\n\n\n\n')

    print(data)








#result = name_generator(4)
#print(result)

#list = purchase_history_generator(result)

#for data in list:
    #print_cheque(data)

