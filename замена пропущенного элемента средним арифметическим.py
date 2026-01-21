numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

a = sum (x for x in numbers if x is not None)/len(numbers)
b = sum (x for x in numbers if x is not None)
c = len (numbers)
numbers[4] = a
print("сумма чисел:", b)
print("количество чисел:", c)
print("Измененный список:", numbers)
