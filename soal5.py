
# ? Buatlah program untuk menghitung
# ! jumlah huruf vokal di dalam sebuah kata
user = input("Masukkan sebuah kata: ").lower() # ! ubah ke huruf kecil
huruf = []
vokal = ["a", "i", "u", "e", "o"] # ! daftar huruf vokal
for y in user : # ! masukkan ke dalam list
# ? y = b 
# ? y = a TRUE
# ? y = d
# ? y = a TRUE
# ? y = k
    if y in vokal:
        huruf.append(y)
jumVokal = len(huruf) # ! hitung jumlah huruf vokal
print(f"Jumlah huruf vokal pada kata {user} adalah {jumVokal}")
