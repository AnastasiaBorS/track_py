# TODO Напишите функцию find_common_participants
# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1_str, group2_str, separator=","):
    """ Находит общих участников среди двух групп.
        Args:
            group1_str: строка с участниками первой группы
            group2_str: строка с участниками второй группы
            separator: разделитель между участниками (по умолчанию ",")
        Returns:
            Список общих участников, отсортированный в алфавитном порядке """
    # Шаг 1: Разделяем строки на списки участников
    group1 = group1_str.split(separator)
    group2 = group2_str.split(separator)

    # Шаг 2: Находим общих участников (пересечение множеств)
    common_participants = set(group1) & set(group2)

    # Шаг 3: Преобразуем результат обратно в список и сортируем
    result_list = sorted(list(common_participants))

    return result_list


# Исходные данные
participants_first_group = ["Иванов", "Петров", "Сидоров"]
participants_second_group = ["Петров", "Сидоров", "Смирнов"]

# Шаг 4: Преобразуем списки в строки с разделителем
participants_first_group_str = ",".join(participants_first_group)
participants_second_group_str = ",".join(participants_second_group)

print(f"Первая группа: {participants_first_group_str}")
print(f"Вторая группа: {participants_second_group_str}")

# Шаг 5: Вызываем функцию для поиска общих участников
result = find_common_participants(participants_first_group_str, participants_second_group_str)

# Шаг 6: Выводим результат
print(f"Общие участники: {result}")

# Проверка работы функции с разделителем отличным от запятой
participants_third_group_str = "Иванов;Петров;Сидоров"
participants_fourth_group_str = "Петров;Сидоров;Смирнов"

print(f"\nПервая группа (с разделителем ';'): {participants_third_group_str}")
print(f"Вторая группа (с разделителем ';'): {participants_fourth_group_str}")

result_with_semicolon = find_common_participants(participants_third_group_str, participants_fourth_group_str, ";")
print(f"Общие участники (с разделителем ';'): {result_with_semicolon}")