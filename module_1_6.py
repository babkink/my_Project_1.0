my_dict = {'Paul': 12345, "Mike": 67890, 'Sam': 11111}
print('my dictionary : ', my_dict)
print("Paul's number: ", my_dict['Paul'])
print('access to not existing key returns: ', my_dict.get('Peter'))
my_dict['Peter'] = 22222
print('my dictionary with added "Peter" pair: ', my_dict)
my_dict.update({'Franc': 22222, 'Ana': 33333})
print('Franc and Ana added: ', my_dict)
a = my_dict.pop('Paul')
print('number of deleted Paul: ',a)
print('final version of dictionary : ', my_dict)
my_set={1,1,1,2,2,'DAS', 'DAS', 'IST'}
print('my set is: ', my_set)
my_set.add('Pithon')
my_set.add('Snake')
print('My set with added Python and Snake; ', my_set)
my_set.discard('DAS')
print('My set with removed "DAS": ', my_set)