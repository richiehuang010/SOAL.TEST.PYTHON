user = int(input("Masukkan jumlah pelajaran : "))
i = 1
total = 0
while i <= user :
    nilai = int(input(f"masukkan nilai pelajaran ke-{i} : "))
    total += nilai
    i += 1
print(f"Nilai rata-ratamu adalah {total/user}")