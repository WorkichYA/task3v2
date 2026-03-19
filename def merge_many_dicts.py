def merge_many_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
d3 = {'c': 5, 'd': 6}



print(merge_many_dicts(d1, d2, d3))
# Вывод: {'a': 1, 'b': 3, 'c': 5, 'd': 6}

print(merge_many_dicts(d1, d3))
# Вывод: {'a': 1, 'b': 2, 'c': 5, 'd': 6}
