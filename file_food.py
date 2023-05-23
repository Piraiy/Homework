from pprint import pprint
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        food_name = i.strip()
        ingredient_count = int(file.readline())
        ingredient = []
        for _ in range(ingredient_count):
            ingredients = {}
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients['ingredient_name'] = ingredient_name
            ingredients['quantity'] = quantity
            ingredients['measure'] = measure
            ingredient.append(ingredients)
        cook_book[food_name] = ingredient
        file.readline()


    # pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    ingr_name_count = {}
    for food_name in dishes:
        for i in cook_book.get(food_name):
            if i['ingredient_name'] in ingr_name_count:
                z = int(i['quantity'])
                ingr_name_count[i['ingredient_name']] = {'measure': i['measure'],
                                       'quantity': ((int(i['quantity'])) + z)*person_count}
            else:
                ingr_name_count[i['ingredient_name']] = {'measure': i['measure'],
                                       'quantity': (int(i['quantity']))*person_count}
    return ingr_name_count

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Фахитос'], 2), sort_dicts=False)

