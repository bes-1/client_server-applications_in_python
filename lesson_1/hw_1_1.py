"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип
и содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
"""

VALUE_1 = "разработка"
VALUE_2 = "сокет"
VALUE_3 = "декоратор"


def get_values_and_type(values):
    for item in values:
        print(item)
        print(type(item))
    print('*' * 50)


list_of_values = [VALUE_1, VALUE_2, VALUE_3]
get_values_and_type(list_of_values)

VALUE_UNICODE_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
VALUE_UNICODE_2 = '\u0441\u043e\u043a\u0435\u0442'
VALUE_UNICODE_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

list_of_values_unicode = [VALUE_UNICODE_1, VALUE_UNICODE_2, VALUE_UNICODE_3]

get_values_and_type(list_of_values_unicode)
