users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
all = len(users)
unique = len(set(users))
dict = {'Общее количество': 0, 'Уникальные посещения': 0}
dict['Общее количество'] = all
dict['Уникальные посещения'] = unique
print(dict)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
