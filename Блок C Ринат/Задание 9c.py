score = float(input("Введите числовой балл экзамена: "))

if score >= 97:
    grade = "A+"
elif score >= 93:
    grade = "A"
elif score >= 90:
    grade = "A-"
elif score >= 87:
    grade = "B+"
elif score >= 83:
    grade = "B"
elif score >= 80:
    grade = "B-"
elif score >= 77:
    grade = "C+"
elif score >= 73:
    grade = "C"
elif score >= 70:
    grade = "C-"
elif score >= 67:
    grade = "D+"
elif score >= 63:
    grade = "D"
elif score >= 60:
    grade = "D-"
else:
    grade = "F"

print(f"Балл: {score} -> Оценка: {grade}")