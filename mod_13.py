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