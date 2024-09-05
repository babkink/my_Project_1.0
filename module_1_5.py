immutable_var = 1, 2, 3, 4, 5.5, True
immutable_var_2 = (23, 'RBS', True, 843.45)
print(immutable_var)
print(immutable_var_2)
print(immutable_var[1])
print(immutable_var_2[1])
#immutable_var[1] = False - невозможно изменить кортеж
mutable_list = [1, 2, 3, 4, 5.5, True, 'RBS']
print(mutable_list)
mutable_list[-1] = "REV" #можно изменить список
print(mutable_list)
print(type(mutable_list))
mutable_list.extend('845') #можно добавить в конец списка строку, которую метод extend разобъет на символы
print(mutable_list)
mutable_list.__delitem__(0)
print(mutable_list)
#immutable_var.__delitem__(0) невозмжно удалить элемент кортежа
a=immutable_var.__getitem__(-1)
print(a)
mutable_list.append(100)
mutable_list.append('ASD')
mutable_list.insert(1, 'ADDED')
print(mutable_list)