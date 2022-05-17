"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard»
из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

VALUE_1 = "разработка"
VALUE_2 = "администрирование"
VALUE_3 = "protocol"
VALUE_4 = "standard"

LIST_OF_VAlUES_STR = [VALUE_1, VALUE_2, VALUE_3, VALUE_4]
LIST_OF_VAlUES_BYTE = [str(item).encode('utf-8') for item in LIST_OF_VAlUES_STR]


def conversion_between_str_and_byte(list_values):
    for item in list_values:
        if type(item) == str:
            print(f'тип слова "{item}" = {type(item)}')
            enc_item = item.encode('utf-8')
            print(f'{enc_item} после преобразования тип = {type(enc_item)}')
            print('*' * 50)
        elif type(item) == bytes:
            print(f'тип слова "{item}" = {type(item)}')
            dec_item = item.decode('utf-8')
            print(f'слово "{dec_item}" после преобразования тип = {type(dec_item)}')
            print('*' * 50)
        else:
            print(f'Тип данных "{item}" = {type(item)} ')


conversion_between_str_and_byte(LIST_OF_VAlUES_BYTE)
