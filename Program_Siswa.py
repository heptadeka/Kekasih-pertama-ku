print("PROGRAM PENGHITUNG KESELURUHAN NILAI SISWA")
tugas = float(input("\nMasukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

na =  (0.3 * uas) + (0.35 * uts) +  (0.50 * uas)
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