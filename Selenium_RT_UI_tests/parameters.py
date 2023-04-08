valid_names_parameters = {
    'им': 'Минимальное количество символов',
    'имё': 'Минимальное количество символов + 1',
    'имяимяимяимяимяимяимяимяимяимя': 'Максимальное количество символов',
    'имяимяимяимяимяимяимяимяимяим': 'Максимальное количество символов - 1',
    'и-м': 'Два символа с тире между',
    'имя-имя': 'Несколько символов с тире по середине',
    ' имя ': 'Пробелы с краёв',
}

invalid_names_parameters = {
    'п': 'Минимальное количество символов - 1',
    'пэжпэжпэжпэжпэжпэжпэжпэжпэжпэжж': 'Максимальное количество символов + 1',
    'пэжпэжпэжпэжпэжпэжпэжпэжпэжпэжпэж': 'Максимальное количество символов + >1',
    'имя--имя': 'Двойное тире',
    '-имя': 'Тире в начале',
    'имя-': 'Тире в конце',
    'имя имя': 'Пробел в середине',
    'name': 'Латиница',
    'имяqя': 'Кириллица и латиница',
    'имя_имя': 'Нижний слеш',
    'имя,имя': 'Запятая',
    '"имя"': 'Двойные кавычки',
    '\'имя\'': 'Одинарные кавычки',
    '//имя': 'Двойной слэш',
    '!@#$%^&*()_+': 'Другие спец.символы',
    '斯坦尼斯': 'Иерогливы',
    '☻☻☻': 'Смайлы',
}

valid_password_parameters = {
    '!№%?*()_+-\';:">/*qQ1': 'Набор спецсимволов',
    'qwertyu1!Q': 'По всем максимальным требованиям - спецсимвол+цифра',
    'qwertyu!Q': 'Без цифры, но со спецсимволом',
    ' qwertyu1Q': 'Без спецсимвола, но с цифрой',
}

invalid_password_parameters = {
    'qwertyu1!': 'Нет заглавной буквы',
    'qwertyuQ': 'Нет ни цифры, ни спецсимволов',
    'QWERTY!2': 'Нет прописной буквы',
    'qwЖertyu1!Q': 'Есть кириллица',
    'qwe rtyu1!Q': 'Пробел в середине',
    'rtyu1!Q': 'Минимальное количество символов - 1',
    ' qwertyu1!Qqwertyu1!Q7': 'Максимальное количество символов + 1',
}

valid_names = [i for i in valid_names_parameters.keys()]
valid_names_ids = [i for i in valid_names_parameters.values()]

invalid_names = [i for i in invalid_names_parameters.keys()]
invalid_names_ids = [i for i in invalid_names_parameters.values()]

valid_password = [i for i in valid_password_parameters.keys()]
valid_password_ids = [i for i in valid_password_parameters.values()]

invalid_password = [i for i in invalid_password_parameters.keys()]
invalid_password_ids = [i for i in invalid_password_parameters.values()]