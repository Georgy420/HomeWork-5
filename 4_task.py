"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1 Two — 2  Three — 3  Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
 числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""

READ_FILE_NAME = 'task_4.txt'
WRITE_FILE_NAME = 'task_4_w.txt'

DIGITS_TRANSLATE = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open(READ_FILE_NAME, 'r') as f:
    lines = f.readlines()
    new_lines = [f'{DIGITS_TRANSLATE[line.split(" - ")[0]]} - {line.split(" - ")[-1]}' for line in lines]

with open(WRITE_FILE_NAME, 'w') as f:
    f.writelines(new_lines)