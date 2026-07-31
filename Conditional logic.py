# if elif else

nama = str(input("Masukan Nama Anda        : "))
umur = int(input("Masukan Umur Anda        : "))
tinggi = float(input("Masukan Tinggi Anda      : "))

print ("")

if nama == "":
    print("Anda tidak memasukan nama anda") 
else:
    print(f"Halo {nama} :)")                

if umur >= 150:
    print("Anda memasukan umur yang salah")
elif umur <= 150:
    print(f"Umur anda adalah : {umur} ")
else:
    print("Jawaban anda salah")     


if tinggi >= 300.0:
    print("Anda memasukan tinggi yang salah")
elif tinggi <= 300.0:
    print(f"Tinggi anda adalah : {tinggi}")
else:
    print("Jawaban anda salah")     