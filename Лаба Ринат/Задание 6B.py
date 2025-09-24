a=int(input("Введите число:"))
if a%3==0 and a%5==0:
    print(a//3, a//5)
else:
    print("одно из числе не делится")
