# @malakanov


# 4.3 - 1 
# Задача 1. Курс от Skillbox-2

# Пользователь покупает курс стоимостью 75 000 рублей. Если денег на счету достаточно, нужно списать деньги и вывести сообщение: «Курс успешно приобретён», — а иначе вывести: «Не хватает денег на счёте». Не забудьте пожелать «Хорошего дня!» в любом случае. Мы же вежливые продавцы.

#Пример:
# Сколько денег на счету? 5000
# Не хватает денег на счету.
# Хорошего дня!

balance = int(input('Сколько денег на счету? '))
course_price = 75000
if balance >= course_price:
  balance -= 75000
  print('Курс успешно приобретён.')
  print('Остаток на балансе:', balance)
else:
  print('Не хватает денег на счёте.')
print('Хорошего дня!')


# 4.3 - 2
# Задача 2. Разминка для мозгов

# Напишите программу, которая проверяет то, как вы умеете складывать два числа в уме. Программа получает на вход два числа и предполагаемую сумму и должна выводить два разных сообщения — на верный и неверный ответ пользователя. В последнем случае надо показывать правильный результат.

# Пример:
# Введите первое число: 3
# Введите второе число: 10
# Сумма этих чисел: 13
# Ответ верный!

# Пример 2:
# Введите первое число: 3
# Введите второе число: 10
# Сумма этих чисел: 14
# Ответ неверный!
print()
print('====================')
print('Проверьте сумму сложения в уме')
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
sum = int(input('Введите сумму первого и второго чисел: '))
if sum == first_num + second_num:
  print('Ответ верный!')
else:
  print('Ответ неверный!')

# 4.3 - 1
# Задача 3. Угадай число 2
# На удивление, отец и сын частенько стали играть в игру «Угадай число», и поэтому папа захотел немного усовершенствовать свою программу, чтобы на экран всегда выводилось нужное сообщение.

# Напишите программу, которая запрашивает число у пользователя, сравнивает его с другим числом и выводит соответствующее сообщение: «Угадал», — если они равны,  и: «Не угадал», — если не равны. В конце выводите фразу: «Конец игры».

# Пример 1:
# Какое число я загадал? 5
# Угадал!
# Конец игры

# Пример 2:
# Какое число я загадал? 6
# Не угадал!
# Конец игры

# Попробуйте решить задачу сначала с помощью одного знака сравнения (==), а затем с помощью другого (!=).
print()
print('====================')
print('Отец загадал число от 1 до 10. Если сын ответит верно, то сможет пойти гулять.')
print('Отец:"Какое число я загадал?"')
fathers_num = 2
sons_num = int(input('Введите число от 1 до 10: '))
# ==
if sons_num == fathers_num:
  print('Угадал!(==)')
else:
  print('Не угадал!(==)')
# !=
if sons_num != fathers_num:
  print('Не угадал!(!=)')
else:
  print('Угадал!(!=)')
print('Конец игры')