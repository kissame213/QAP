try:
 amount = int(input("Пожалуйста, введите желаемое количество билетов: \n"))
 age = [int(input("Пожалуйста, укажите возраст гостя: \n")) for n in range(amount)]
 price = (0, 990, 1390)

 i = 0
 new_price = 0

 while i < amount:
     if age[i] < 18:
         new_price += price[0]
     elif 18 <= age[i] <= 24:
         new_price += price[1]
     elif age[i] >= 25:
         new_price += price[2]
     i += 1
 if amount > 2:
     new_price = new_price * 0.9
 print("Общая стоимость билетов:", new_price, "руб.")
except ValueError as a:
    print("Количество билетов и возраст гостей должны быть введены цифрами.")