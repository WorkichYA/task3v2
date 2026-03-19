def make_dict(**kwargs):
    reverse = kwargs.pop('reverse', False)
    if reverse:
        try:
            result = {v: k for k, v in kwargs.items()}
            return result
        except TypeError:            
            return None
    else:
        return kwargs

print(make_dict(name='Alice', age=30, city='Moscow'))
# Вывод: {'name': 'Alice', 'age': 30, 'city': 'Moscow'}

print(make_dict(reverse=True, name='Alice', age=30, city='Moscow'))
# Вывод: {'Alice': 'name', 30: 'age', 'Moscow': 'city'}

# Попытка реверса со значениями, которые не могут быть ключами,  (например, список)
print(make_dict(reverse=True, data=[1,2,3]))  # Вернёт None
