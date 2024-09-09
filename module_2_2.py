first = input('введите первое число: ')
second = input('введите второе число: ')
third = input('введите третье число: ')
if first == second and second == third and first == third: result = 3
elif first == second or second == third or first == third: result = 2
else:
    result = 0
print(result)