# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными. Пример: 67.82 -> 23; (-0.56) -> 11

num = input('Введите дробное число: ')
sum = 0 
print(num)
for i in num:
    if('.'!= i) and (','!= i):
        sum += int(i)
print(sum)
exit()

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) 
# чисел от 1 до N. Не используйте функцию math.factorial. Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Введите число: '))
fact = 1
for i in range(1,N+1):
    fact = i*fact 
    print(fact,end=' ')
   
      
# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.
# Пример: - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random
N = int(input('Введите число: '))
array = []
for i in range(N):
    array.append(random.randint(-99,100))
print(array)

i=0
for i in range(len(array) - 1, -1, -1):       
    if array[i] < 0:                          
        array.insert(i + 1, 0)                
print(array)


# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. 
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, 
# остальные получили по две монеты. Далее человек, на котором остановился счет, 
# отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. 
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. 
# Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте 
# библиотеку time и используйте оттуда функцию sleep. Определите номер этого человека и количество монет, 
# которые оказались у него в конце игры.

# 4 - (если не получается, то альтернативная задача). Составьте алгоритм нахождения случайного числа 
# без использования библиотеки random.
# https://habr.com/ru/company/vk/blog/574414/ - поможет вам эта статья.

# P.S. рекомендации по выполнению 4-го задания.
# 1. представьте список людей в виде списка индексов: [0,1,2,3,4...];
# 2. работайте одновременно со списком монет;
# 3. не надо писать сложных систем для "Процесс продолжается с места остановки". 
# Достаточно использовать срезы: переместите оставшуюся часть списка вперед
# 4. после каждого выбывшего пусть работает input: хотите продолжать или выйти из цикла игры?

# Остальное - это списки, циклы и условия, поэтому надеюсь, вы справитесь;)

Задание выполнила на 1/2, с монетами не могу связать ((

n = int(input('Кол-во человек в круге: '))            
m = int(input('Число в считалке: '))
print(f'Выходит из круга каждый {m} человек')
list_n = list(range(1, n + 1))
count = 0
while len(list_n) > 1:
    print('Наш круг людей: ', list_n)
    print('Начало счёта с номера:', list_n[count])
    count = (count + m - 1) % len(list_n)
    if list_n[count] == list_n[-1]:
        print('Выходит из круга человек под номером:', list_n.pop(count))
    else:
       print('Выходит из круга человек под номером:', list_n.pop(count))
print('Остался человек под номером:', list_n[0])

