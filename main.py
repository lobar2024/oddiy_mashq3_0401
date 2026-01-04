students = {
    "Ali": 85,
    "Vali": 92,
    "Hasan": 78,
    "Husan": 90
}

print("O‘rtacha:", sum(students.values()) / len(students))
print("Eng yuqori:", max(students, key=students.get))

print("85 dan yuqorilar:")
print({k: v for k, v in students.items() if v > 85})
