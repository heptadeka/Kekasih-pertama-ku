print("PROGRAM PYTHON UNTUK MENGHITUNG KESELURUHAN NILAI SISWA")
tugas = float (input("/nMasukan Nilai tugas:70"))
uts = float (input("/nMasukan Nilai uts:80"))
uas = float (input("/nMasukan Nilai uas:72"))

na = (0.15 * tugas) + (0.35 * uts) + (0.50 * uas)
if na >= 80:
    indeks = 'A'
elif na >= 70:
    indeks = 'B'
elif na >= 55:
    indeks = 'C'
elif na >= 45:
    indeks = 'D'
else:
    indeks = 'E'

print("\nNilai Akhir = %0.2f" % na)
print("Nilai Indeks = %c" % indeks)
