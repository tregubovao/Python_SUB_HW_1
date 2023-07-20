# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = int(input('Введите положительное число не более 100_000: \n' ))

if (0 <= number <= 100000):
    current = 2
    count = 0
    while current < number:
        if number % current == 0:
            count += 1
        current += 1
    if count != 0 or number == 0 or number == 1:
        print(f'Число {number} НЕ является простым')
    else:
        print(f'Число {number}  - ПРОСТОЕ')

else:
    print('Некорректный ввод. Повторите.')
