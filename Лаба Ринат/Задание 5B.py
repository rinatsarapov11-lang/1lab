a=int(input("Введите цену"))
if a<100:
    print("Скидки нет")
else:
    a=a-a*0.1
    print("Скидка есть")
print(a)