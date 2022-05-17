"""
2. Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме, с помощью добавления литеры b к текстовому значению,
(т.е. ни в коем случае не используя методы encode, decode или функцию bytes) и определить тип, содержимое и длину
соответствующих переменных.
"""

VALUE_1 = "class"
VALUE_2 = "function"
VALUE_3 = "method"

LIST_OF_VALUES = [VALUE_1, VALUE_2, VALUE_3]

for item in LIST_OF_VALUES:
    value_in_byte = eval(f"b'{item}'")
    print('*' * 50)
    print(f'value = {value_in_byte} \ntype of value: {type(value_in_byte)} \nlength of value = {len(value_in_byte)}')
