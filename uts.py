#Nama   : Sepry Handi
#NIM    : 191011400624
#Kelas  : 06TPLM004
#Kondisi IF ELSE

#Ini adalah contoh struktur Kondisi IF
lulus = input("Apakah kamu lulus? [Ya/Tidak] :")

if lulus == "Tidak":
  print("Kamu Harus Ikut Remedial!")

  print("\n")

#Ini adalah contoh struktur kondisi If/Elif (Beberapa kondisi bersyarat)
print("Kapan Negara Indonesia Merdeka? \n");
print("A. 1 Juni 1945 \n");
print("B. 18 Agustus 1945 \n");
print("C. 30 September 1965 \n");
print("D. 17 Agustus 1945 \n");

x = str(input("Jawaban = "))

if (x == 'A') or (x == 'a'):
     print("Ops, 1 Juni 1945 adalah hari lahirnya Pancasila");
elif (x == 'B') or (x == 'b'):
     print("Ops, 18 Agustus 1945 adalah hari pengesahan UUD 1945");
elif (x == 'C') or (x == 'c'):
     print ("Ops, 30 September 1965 adalah hari G30S/PKI");
elif (x == 'D') or (x == 'd'):
     print("Selamat Anda benar");

     print("\n")

#Ini adalah contoh struktur kondisi If/Else (Menentukan Angka Ganjil/Genap)
angka = int(input('Masukan angka :'))

if angka %2 == 0:
  print('angka{}genap'.format(angka))
else:
  print('angka{}ganjil'.format(angka))

  print("\n")


#Ini adalah contoh Struktur Kondisi IF/Elif/Else
nilai = int(input('Masukkan nilai: '))

if nilai >= 90:
  print('Predikat A')
elif nilai >= 80:
  print('Predikat B')
elif nilai >= 60:
  print('Predikat C')
elif nilai >= 40:
  print('Predikat D')
else:
  print('Predikat E')
  
  print("\n")