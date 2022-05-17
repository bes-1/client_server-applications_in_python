"""
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.
"""

VALUE_1 = "attribute"
VALUE_2 = "класс"
VALUE_3 = "функция"
VALUE_4 = "type"

LIST_OF_VAlUES = [VALUE_1, VALUE_2, VALUE_3, VALUE_4]

for item in LIST_OF_VAlUES:
    try:
        item.encode('ascii')
    except UnicodeEncodeError:
        print(f'слово "{item}" невозможно записать в байтовом типе')
