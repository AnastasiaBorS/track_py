# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        # Используем DictReader для автоматического использования первой строки как заголовков
        reader = csv.DictReader(csv_file)

        # Преобразуем OrderedDict в обычные dict для сериализации в JSON
        data = [dict(row) for row in reader]

    # Сериализуем данные в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")