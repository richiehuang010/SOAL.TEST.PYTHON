nama = input("Masukkan nama : ")
i = 1
total = 0
grade = ""
while i <= 5 :
    user = int(input(f"Masukkan nilai ke-{i} : "))
    total += user
    i += 1
rata2 = total / 5
if rata2 > 92 :
    grade = "A"
elif rata2 > 85 :
    grade = "B"
elif rata2 > 75 :
    grade = "C"
else : grade = "-"
print(f"nilai rata-rata {nama} adalah {rata2} dengan grade {grade}")