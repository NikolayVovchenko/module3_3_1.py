
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print()



# введение данного элемента  по умолчанию меняет заданное значение'b'='строка' на '25'
print_params(b = 25)
print_params(c = [1,2,3])
# введением данного элемента'c' заменяет его значение в выводе с True на c=[1,2,3]
values_list = ['Привет', 72, [7, 5, 2]]
values_dict = {'a': [2, 4, 6], 'b': 'Привет', 'c': 67}
print_params(*values_list)
print_params(**values_dict)

# вводим исходное задание

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)