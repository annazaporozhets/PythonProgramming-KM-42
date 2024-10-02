word = input("Введіть певний перелік предметів через кому:")
things = [thing.strip() for thing in word.split(",") if thing.strip()]
if not things:
    print("Не введено жодного елемента!")
elif len(things) == 1:
    print(things[0])
elif len(things) == 2:
    print(things[0] , "and" , things[1])
else:
    print(", ".join(things[:-1]) , "and" , things[-1])