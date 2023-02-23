def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default.
    :param collection: Исходный словарь.
    :param key: Ключ возвращаемого значения.
    :param default: Значение по-умолчанию
    :return: Значение по ключу или значение по-умолчанию.
    """
    if key in collection:
        return collection[key]
    else:
        return default
