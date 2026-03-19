def filter_by_value(data, threshold=0):
    new_data = {}
    for key, value in data.items():
        if value >= threshold:
            new_data[key] = value
    return new_data
    
# Исходные данные
scores = {'Alice': 85, 'Bob': 42, 'Charlie': 100, 'Diana': 37}

print(filter_by_value(scores))
# Результат: {'Alice': 85, 'Bob': 42, 'Charlie': 100, 'Diana': 37}

print(filter_by_value(scores, 50))
# Результат: {'Alice': 85, 'Charlie': 100}

print(filter_by_value(scores, 90))
# Результат: {'Charlie': 100}

print(filter_by_value(scores, 42))
# Результат: {'Alice': 85, 'Bob': 42, 'Charlie': 100}
