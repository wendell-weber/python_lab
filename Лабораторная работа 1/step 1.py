numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers[4] = 0
a = sum(numbers)
b = len(numbers)
average = a/b
numbers[4] = average
print("Измененный список:", numbers)
