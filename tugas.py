def mulai_game():
    print ("====SELAMAT DATANG DI GAME RANDOM====")
    nama = input("Masukan nama kamu: ")
    print (f"Kamu adalah seorang anak bernama {nama}")
    print ("Kamu terbangun di sebuah kamar mu yag ada ps5nya")
    print ("Kamu ingin melakuka sesuatu")
    print ("1. Bermain PS5")
    print ("2. Makan sarapan")
    print ("3. Kembali tidur")

    pilihan = input("pilih 1, 2 atau 3: ")
    if pilihan == "1":
        Bermain(nama)
    elif pilihan == "2":
        Sarapan(nama)
    elif pilihan == "3":
        Tidur(nama)
    else:
        print ("Nggak ada pilihan lain, bikin game sendiri kalau mau!!\n")
        mulai_game()

def Bermain(nama):
    print(f"\n{nama}Berjalan ke ps5, lalu main game")
    print("\nsetelah dinyalakan, memilih game")
    print("1. Sonic")
    print("2. Roblox")

    pilihan = input("pilih 1 atau 2 : ")
    if pilihan == "1":
        print(f"\n{nama} bermain Sonic")
        tamat("Baik")
    elif pilihan == "2":
        print(f"\n{nama}bermain Roblox")
        tamat("Ok")
    else:
        print("Tidak ada pilihan\n")
        Bermain(nama)

def Sarapan(nama):
    print(f"\n{nama} berjalan ke dapur")
    print("\nMelihat telur dan Ayam di meja")
    print("1. Makan Ayam")
    print("2. Makan Telur")

    pilihan = input("pilih 1 atau 2 : ")
    if pilihan == "1":
        print(f"\n{nama} makan ayam")
        tamat("Baik")
    elif pilihan == "2":
        print(f"\n{nama} makan telur")
        tamat("ok")
    else:
        print("Tidak ada pilihan\n")
        Sarapan(nama)

def Tidur(nama):
    print(f"\n{nama} jalan ke tempat tidur")
    print("pilih guling atau bantal")

    pilihan = input("pilih 1 atau 2 : ")
    if pilihan == "1":
        print(f"\n{nama} memilih bantal")
        tamat("Netral")
    elif pilihan == "2":
        print(f"\n{nama} pilih guling")
        tamat("Netral")
    else:
        print("Tidak ada pilihan")
        Tidur(nama)

def tamat(akhir):
    print("\n== AKHIR CERITA ===")
    if akhir == "Baik":
        print("Kamu memiliki hidup yang baik")
    elif akhir == "Ok":
        print("Hidupmu terasa ok saja")
    else:
        print("Entah bagaimana menjelaskannya")

        print("Terimakasih sudah bermain")

mulai_game()




