R = int(input("Введіть рейтинговий бал:"))
if R<=100 and R>=95:
    print("Excellent")
elif R<95 and R>=85:
    print("Very good")
elif R<85 and R>=75:
    print("Good")
elif R<75 and R>=65:
    print("Satisfactory")
elif R<65 and R>=60:
    print("Marginal")
elif R<60 and R>=0:
    print("Unsatisfactory")
elif R>100:
    print("Помилка! Введіть число менше за 100.")
else:
    print("Помилка!Введіть невід'ємне число!")