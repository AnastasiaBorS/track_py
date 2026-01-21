# TODO решите задачу
import json
import os

def task() -> float:
    # Предполагаем, что файл называется 'input.json' и находится в текущей директории
    # Или можно добавить параметр для имени файла
    filename = 'input.json'

    # Проверяем существует ли файл
    if not os.path.exists(filename):
        print(f"Файл {filename} не найден")
        return 0.0

    # Читаем JSON файл
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Вычисляем сумму произведений score * weight
    total = 0.0
    for item in data:
        # Проверяем, что оба ключа существуют в словаре
        if isinstance(item, dict) and 'score' in item and 'weight' in item:
            try:
                total += float(item['score']) * float(item['weight'])
            except (ValueError, TypeError):
                # Если значения не могут быть преобразованы в числа, пропускаем
                continue

    # Округляем до 3 знаков после запятой
    return round(total, 3)


if __name__ == '__main__':
    result = task()
    print(result)