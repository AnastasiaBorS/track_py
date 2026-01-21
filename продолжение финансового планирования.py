from pkg_resources import require

salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.05  # Ежемесячный рост цен
need_end = 0

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for months in range (months-1, -1, -1):
    rasod_ = spend * ((1 + increase) ** months)
    need_end = max (0, rasod_ + need_end - salary)
required_capital = round (need_end)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
