from zad_1 import return_full_name
from zad_2 import multipy
from zad_3 import is_even
from zad_4 import check_numbers
from zad_5 import s_func
from zad_6 import func

print('Exercise 1')
string = return_full_name('Mikolaj', 'Bialas')
print(string)
print('-'*30)


print('Exercise 2')
print(multipy(2, 2))
print('-'*30)

print('Exercise 3')
entered_number = is_even(5)

if entered_number:
    print("Number is even")
else:
    print('Number is odd')
print('-'*30)


print('Exercise 4')
print(check_numbers(5,2,5))
print('-'*30)

print('Exercise 5')
l = [213, 123, 213, 2]
num = 6

print(s_func(l, num))
print('-'*30)

print('Exercise 6')
print(func([2, 3, 4, 5], [1, 2, 4, 5]))
print('-'*30)


