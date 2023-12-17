from zad_1 import print_names
from zad_2 import multiply
from zad_3 import print_even
from zad_4 import print_every_other_element

print('zadanie 1')
names = ['Dominika', 'Marta', 'Filip', 'Kacper', 'Mikolaj']
print_names(names)
print('-' * 30)

print('zadanie 2')
list_of_num = [2, 5, 6, 7, 8]
print(multiply(list_of_num))
print('-' * 30)

print('zadanie 3')
list_of_num = [i for i in range(1, 11)]
print_even(list_of_num)
print('-' * 30)

print('zadanie 4')
list_of_num = [i for i in range(1, 20)]
print_every_other_element(list_of_num)
