"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

FILE_NAME = 'task_5.txt'

with open(FILE_NAME, 'w') as f:
    digits = input('Введите набор чисел через пробел: ')
    f.write(digits)

with open(FILE_NAME, 'r') as f:
    digits_str = f.read()
    print(sum([int(digit) for digit in digits_str.split()]))