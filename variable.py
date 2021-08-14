print("PROGRAM PYTHON MENENTUKAN NILAI INDEKS MAHASISWA")
tugas = float(input("\nMasukkan nilai Tugas:80 "))
uts = float(input("\nMasukkan nilai UTS:70 "))
uas = float(input("\nMasukkan nilai UAS:90 "))

na =  (0.15 * uas) + (0.35 * uts) +  (0.50 * uas)
if na >= 80:
    indeks = 'A'
elif na >= 70:
    indeks = 'B'
elif na >= 55:
    indeks = 'C'
elif na >= 40:
    indeks = 'D'
else:
    indeks = 'E'

print("\nNilai Akhir  = %0.2f" % na)
print("Nilai Indeks = %c" % indeks)