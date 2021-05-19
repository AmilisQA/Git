#Вам дан словарь per_cent с распределением процентных ставок по вкладам в различных банках 
#Напишите программу, в результате которой будет сформирован список deposit значений — накопленные средства за год вклада в каждом из банков. 
#На вход программы с клавиатуры вводится сумма money, которую человек планирует положить под проценты.

money = int(input("Введите сумму вклада = "))

#словарь per_cent содержит данные по процентным ставкам вклада
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

per = (list(map(float,per_cent.values())))
deposit = list(map(int,[per[0]*money/100, per[1]*money/100, per[2]*money/100, per[3]*money/100]))

print('Сумма процентов по вкладу: ', deposit)
print('Максимальная сумма от процентов по вкладу за год =', max(deposit))


#Для онлайн-конференции необходимо написать программу, которая будет подсчитывать общую стоимость билетов. Программа должна работать следующим образом:
#В начале у пользователя запрашивается количество билетов и возраст посетителей
#        Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
#        От 18 до 25 лет — 990 руб.
#        От 25 лет — полная стоимость 1390 руб.
# Если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
#В результате программы выводится сумма к оплате. 

price=0
n = int(input("Сколько билетов Вам потребуется? "))
Age = [int(input("Введите возраст посетителя :")) for i in range(1,n+1)]
#print('\nКоличество приобретаемых билетов:',n,'\nВозраст посетителей, лет:',Age)
for i in Age:
    if 18 <= i < 25:
        price+=990
    elif i >= 25:
        price+=1390
if n>3:
    price*=0.9
print('\nСумма к оплате: ',price,' руб.')

