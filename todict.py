from pprint import pprint

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ]
  }



def get_shop_list_by_dishes(dishes, person_count):
    shop_dict={}
    for dish in dishes:
        for count in cook_book[dish]:
            if count['ingredient_name'] not in shop_dict:
                shop_dict[count['ingredient_name']]={'measure':count['measure'],'quantity': count['quantity']*person_count}
            else:
                shop_dict[count['ingredient_name']]['quantity']=shop_dict[count['ingredient_name']]['quantity']+count['quantity']*person_count


    return shop_dict


pprint(get_shop_list_by_dishes(['Запеченный картофель','Утка по-пекински'], 2))

