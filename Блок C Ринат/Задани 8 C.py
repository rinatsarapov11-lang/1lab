temp = float(input("Введите температуру: "))

if temp > 0:
    fahrenheit = (temp * 9/5) + 32
    print(f"{temp}°C = {fahrenheit}°F")
else:
    celsius = (temp - 32) * 5/9
    print(f"{temp}°F = {celsius:}°C")