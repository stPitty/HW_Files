from pprint import pprint
import os
cook_book = {}

with open('recipes.txt','r') as recipes:
    space = ' '
    while space:
        key = recipes.readline().strip('\n')
        cook_book[key] = []
        length = int(recipes.readline())
        for count in range(length):
            line = recipes.readline().strip('\n').split(' | ')
            cook_book[key] += [{'ingredient_name':line[0],'quantity':line[1],'measure':line[2]}]
        space = recipes.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    dish_name_in = []
    dish_name_out = []
    for dish in dishes:
        if dish in cook_book:
            dish_name_in += [dish]
            for items in cook_book[dish]:
                if items['ingredient_name'] in shop_list:
                    shop_list[items['ingredient_name']]['quantity'] += int(items['quantity']) * person_count
                else:
                    shop_list[items['ingredient_name']] = {'measure':items['measure'],'quantity':int(items['quantity']) * person_count}
        else:
            dish_name_out += [dish]
    if dish_name_out:
        print(f'Мы не смогли найти {", ".join(dish_name_out)} в нашем списке блюд', end='\n\n\n')
    if dish_name_in:
        print(f'Для того, чтобы приготовить {", ".join(dish_name_in)} для {person_count} человек '
              f'\n необходимо купить следующие ингридиенты:', end='\n\n')
    if shop_list:
        return shop_list
    else:
        return None

def write_files(new_file_name):
    files_dict = {}
    keys_dict = {}
    for files in os.listdir():
        if files.endswith('.txt') and files != new_file_name and files != 'recipes.txt':
            with open(files) as file:
                files_dict[files] = file.readlines()
                keys_dict[files] = len(files_dict[files])
    sorted_keys = sorted(keys_dict, key = keys_dict.get)
    with open(new_file_name,'w+') as file:
        for file_name in sorted_keys:
            file.write(f'{file_name}\n'
                       f'{len(files_dict[file_name])}\n'
                       f'{" ".join(files_dict[file_name])} \n\n')

write_files('Answer.txt')
# pprint(cook_book)
# pprint(get_shop_list_by_dishes(['Омлет', 'asdsada', 'Запеченный картофель'], 10))