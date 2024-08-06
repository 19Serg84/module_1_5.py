immutable_var = (15, 2.75, 'текст', True)
print (immutable_var)
print(immutable_var [0])
# immutable_var [0] = 200, при попытке изменить входящий в состав кортежа элемент возникает ошибка. Элементы котежа изменить нельзя.
mutable_list = [15, 2.75, 'текст', True]
print(mutable_list)
mutable_list [0] = 200
print(mutable_list)