money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while True:
    ost = spend - salary
    if ost > money_capital:
        break
    month += 1
    spend = spend + spend * increase
    money_capital -= ost
print("Количество месяцев, которое можно протянуть без долгов:", month)
