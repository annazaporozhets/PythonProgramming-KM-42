try:
    time = int(input("Введіть тривалість розмов(у хвилинах):"))
    if time < 0:
        print("Помилка! Тривалість розмов не може бути від'ємною.")
    else:
        price_plan = 100
    if time <= 50:
        print("До сплати 100 гривень.")
    elif time > 50 and time <= 100:
        print("До сплати 150 гривень.")
    else:
        final_pay = 150 + (time - 100) * 2
        print(f"До сплати {final_pay} гривень.")
except ValueError:
    print("Помилка! Введіть коректне значення.")
    