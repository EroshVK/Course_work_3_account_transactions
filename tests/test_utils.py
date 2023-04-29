import utils

def test_select_by_state():
    assert utils.select_by_state([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"state": "CANCELED"}]) == \
                                 [{"state": "EXECUTED"}, {"state": "EXECUTED"}]
    assert utils.select_by_state([{"state": "EXECUTED"}, {"state": "EXECUTED"}, {"st": " "}]) == \
                                 [{"state": "EXECUTED"}, {"state": "EXECUTED"}]

def test_last_executed_operations():
    assert utils.last_executed_operations([{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}, {"date": "2018-06-30T02:08:58.425572"}]) == \
                                          [{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}, {"date": "2018-06-30T02:08:58.425572"}]

def test_hide_digits():
    assert utils.hide_digits("Счет 75106830613657916952") == "Счет **6952"
    assert utils.hide_digits("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert utils.hide_digits("Visa Classic 6831982476737658") == "Visa Classic 6831 98** **** 7658"

def test_output():
    assert utils.output([{"date": "2019-08-26T10:50:58.294041", "description": "Перевод организации",
                          "from": "Maestro 1596837868705199", "to": "Счет 64686473678894779589",
                          "operationAmount": {"amount": "31957.58","currency": {"name": "руб."}}}]) == \
                          ["2019-08-26 00:00:00 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n"]
    assert utils.output([{"date": "2019-08-26T10:50:58.294041", "description": "Перевод организации",
                          "to": "Счет 64686473678894779589",
                          "operationAmount": {"amount": "31957.58","currency": {"name": "руб."}}}]) == \
                          ["2019-08-26 00:00:00 Перевод организации\n -> Счет **9589\n31957.58 руб.\n"]
