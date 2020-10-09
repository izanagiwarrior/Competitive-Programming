format = input()
jam = format[:2]
jam = float(jam)
while jam > 11:
    jam = jam - 12
menit = format[3:]
menit = float(menit)
jam = (jam * 30)
jam = jam + (menit*0.5)
menit = menit * 6

Hasil = menit - jam

if Hasil < 0:
    Hasil = Hasil*-1

Hasil2 = 360 - Hasil
if Hasil2 > Hasil:
    print(Hasil)
else:
    print(Hasil2)