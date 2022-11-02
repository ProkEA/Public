ticket = int(input("Введите количество билетов, которое Вы хотите приобрести на мероприятие:"))
cost = ""
amount = 0
for i in range(ticket):
    i += 1
    age = int(input(f"Какого возраста посититель билета №{i}?"))
    if 18 <= age <= 25:
        cost = 990
        amount = amount + cost
        print(f"Стоимость Вашего билета - {cost} руб.")
    elif age >= 26:
        cost = 1390
        amount = amount + cost
        print(f"Стоимость Вашего билета - {cost} руб.")
    else:
        print("Посещение мероприятия лицам до 18 лет - бесплатно!")
if ticket > 3:
    amount = amount - ((amount * 10) / 100)
    print(f'Сумма к оплате с учетом 10% скидки {amount} руб.')
else:
    print(f'Сумма к оплате {amount} руб.')
