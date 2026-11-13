print(' ---   Строительный калькулятор  --- ')
print('1. Сложение 2. Вычитание 3. Умножение 4. Деление 5. Деление без остатка 6. Остаток 7. Степень 0. Выход')
choice = int(input('Выберите одно из действий (Цифру): '))
if int(choice) == 0:
    print('ВЫХОДОД')
if choice > 7:
    print('Такого действия нет')
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if int(choice) == 1: 
    print('Ответ:', num1 + num2)
if int(choice) == 2: 
    print('Ответ:', num1 - num2)
if int(choice) == 3: 
    print('Ответ:', num1 * num2)
if int(choice) == 4: 
    print('Ответ:', num1 / num2)
if int(choice) == 5: 
    print('Ответ:', num1 // num2)
if int(choice) == 6: 
    print('Ответ:', num1 % num2)
if int(choice) == 7: 
    print('Ответ:', num1 ** num2)