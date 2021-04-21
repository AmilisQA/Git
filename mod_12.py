money = int(input("Введите сумму вклада = "))

#словарь per_cent содержит данные по процентным ставкам вклада
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

per = (list(map(float,per_cent.values())))
deposit = list(map(int,[per[0]*money/100, per[1]*money/100, per[2]*money/100, per[3]*money/100]))

print('Сумма процентов по вкладу: ', deposit)
print('Максимальная сумма от процентов по вкладу за год =', max(deposit))