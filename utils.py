import json
from datetime import datetime

def load_operations():
    """
    Загружает данные из файла operations.json
    :return: данные файла
    """
    with open('operations.json', 'r', encoding='utf-8') as file:
        data_operations = json.load(file)
    return data_operations

def select_by_state(data_operations):
    """
    Отбирает операции со статусом 'EXECUTED'
    :param data_operations: данные файла operations.json
    :return: операции со статусом 'EXECUTED'
    """
    executed_operations = []
    for item in data_operations:
        try:
            if item["state"] == 'EXECUTED':
                executed_operations.append(item)
        except KeyError:
            pass
    return executed_operations

def last_executed_operations(executed_operations):
    """
    Сортирует операции со статусом 'EXECUTED' по дате и возвращает последние 5
    :param executed_operations: операции со статусом 'EXECUTED'
    :return: последние 5 операций со статусом 'EXECUTED'
    """
    sort_operations = sorted(executed_operations, key=lambda x: x["date"], reverse=True)
    last_operations = sort_operations[4::-1]
    return last_operations

def hide_digits(account):
    """
    Скрывает цифры счета или карты участвующих в операции
    :param account: счет или карта участвующие в операции
    :return: счет или карта со скрытыми цифрами
    """
    number_of_digits = account.split(' ')[-1]
    if len(number_of_digits) == 20:
        return f'Счет **{number_of_digits[16:]}'
    else:
        card = " ".join(account.split(" ")[:-1])
        return f'{card} {number_of_digits[0:4]} {number_of_digits[4:6]}** **** {number_of_digits[12:]}'

def output(last_operations):
    """
    Выводит 5 последних операций
    :param last_operations: 5 последних операций
    :return: выводит 5 последних операций в соответствии с примером
    """
    for item in last_operations:
        date = datetime.strptime(item['date'][:10], '%Y-%m-%d')
        try:
            from_operations = hide_digits(item['from'])
        except KeyError:
            from_operations = ''
        print(f"""{date} {item['description']}
{from_operations} -> {hide_digits(item['to'])}
{item['operationAmount']['amount']} {item['operationAmount']['currency']['name']}\n""")
