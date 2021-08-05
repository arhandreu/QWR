def read_file(name):
    with open(name, 'rt', encoding='utf-8') as file:
        book_recipe = {}
        for line in file:
            count_ing = int(file.readline().strip())
            book_recipe[line.strip()] = []
            for ingredient in range(count_ing):
                list_ing = file.readline().strip().split('|')
                book_recipe[line.strip()].append({'ingredient_name': list_ing[0], 'quantity': int(list_ing[1]), 'measure': list_ing[2]})
            file.readline()
    return book_recipe


cook_book = read_file('dish.txt')


def get_shop_list_by_dishes(dishes, person_count):
    products = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            if ing['ingredient_name'] in products:
                products[ing['ingredient_name']]['quantity'] += ing['quantity']
            else:
                products[ing['ingredient_name']] = {'measure': ing['measure'], 'quantity': ing['quantity']}
    print(products)


get_shop_list_by_dishes(['Утка по-пекински', 'Омлет'], 2)
