a = int(input("Первое число:"))
b = int(input("Второе число:"))
if a>b:
    print("Первое число больше")
elif b>a:
    print("Второе число больше")
else:
    b = a
    print("Числа равны")