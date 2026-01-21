# TODO Напишите функцию для поиска индекса товара

def find_items (items, product_to_find):
    for i,items in enumerate(items):
        if items == product_to_find:
            return i
    return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_items (items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара {find_item} имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
