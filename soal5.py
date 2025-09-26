i = 1
total = 0
grade = ""
while i <= 3 :
    user = int(input(f"Masukkan nilai ke-{i} : "))
    total += user
    i += 1
rata2 = total / 3
if rata2 > 92 :
    grade = "A"
elif rata2 > 80 :
    grade = "B"
elif rata2 > 70 :
    grade = "C"
else : grade = "D"
print(f"nilai rata-ratamu adalah {rata2} dengan grade {grade}")