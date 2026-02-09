def mulai_game():
    print ("====SELAMAT DATANG DI GAME RANDOM====")
    nama = input("\nMasukan nama kamu: ")
    print (f"Detektif {nama} mendapatkan sebuah misi menyamar di sebuah pesta mewah")
    print ("\nTargetmu adalah penjahat bernama Robert yang dikenal licik")
    print ("\nDi tengah pesta kamu melihat Robert berdiri sendirian sambil minum")
    print ("\nApa yang akan kamu lakukan?")
    print ("1. Mendekat dan mengajak ngobrol santai")
    print ("2. Mengawasi dari jauh")

    pilihan = input("pilih 1 atau 2: ")
    if pilihan == "1":
        Ngobrol(nama)
    elif pilihan == "2":
        Mengawasi(nama)
    else:
        print ("Nggak ada pilihan lain, bikin game sendiri kalau mau!!\n")
        mulai_game()

def Ngobrol(nama):
    print("======================================================")
    print(f"\n{nama} mendekat dengan tenang dan mulai berbincang.")
    print("\nRobert tersenyum dan terlihat santai")
    print("\nRobert : Pesta yang bagus ya")
    print("\nBagaimana responmu?")
    print("1. Ikut santai dan membangun kepercayaan")
    print("2. Langsung menyinggung soal kejahatan yang ia buat")

    pilihan = input("pilih 1 atau 2 : ")
    if pilihan == "1":
        print("\nPercakapan mulai terasa nyaman dan berjalan lancar")
        Strategi_Santai(nama)
    elif pilihan == "2":
        print("\nPenjahat langsung curiga dan merasa tidak nyaman")
        tamat("Bad")
    else:
        print("Tidak ada pilihan\n")
        Ngobrol(nama)

def Mengawasi(nama):
    print("======================================================")
    print(f"\n{nama} memilih untuk mengawasi dari jauh.")
    print("\nNamun Robert menyadari tatapanmu dan merasa diawasi.")
    print("\nApa yang kamu lakukan?")
    print("1. Tetap mengawasi")
    print("2. Pura-pura tidak peduli dan mendekat secara natural")

    pilihan = input("pilih 1 atau 2 : ")
    if pilihan == "1":
        print("\nRobert merasa panaik dan meninggalkan pesta")
        tamat("Bad")
    elif pilihan == "2":
        print("\nKamu berhasil menyamarkan kecurigaanmu")
        Strategi_Akhir(nama)
    else:
        print("Tidak ada pilihan")
        Mengawasi(nama)

def Strategi_Akhir(nama):
    print("===========================================================")
    print("\nPenyamaran berhasil.")
    print("\nKamu memberi kesempatan untuk memberi sinyal ke pada tim.")
    print("\nApa yang kamu lakukan?")
    print("!. Kirim sinyal diam-diam ke tim.")
    print("2. Mencoba menangkap sendiri saat itu juga.")

    pilihan = input("Pilih 1 atau 2: ")
    if pilihan == "1":
        print("\nTim bergerak dengan cepat dan menangkap penjahat tanpa keributan.")
        tamat("Good")
    elif pilihan == "2":
        print("\nRobert melawan dan berhasil kabur di tengah kekacauan pesta")
        tamat("Bad")
    else:
        print("\nTidak ada pilihan")
        Strategi_Akhir(nama)

def Strategi_Santai(nama):
    print("==================================================")
    print("\nPercakapan semakin mendalam")
    print("\nKamu mengajak Robert untuk keluar ke tempat sepi")
    print("\nApa yang akan kamu lakukan sekarang?")
    print("1. Mengikat tangan Robert")
    print("2. Mencoba melawan")

    pilihan = input("Pilih 1 atau 2: ")
    if pilihan == "1":
        print("Kamu secara cepat mengikat tangan Robert dan membawahnya ke kantor")
        tamat("Good")
    elif pilihan == "2":
        print("Kamu mencoba melawan tetapi kalah kuat dengan Robert, sehingga Robert berhasil melarikan diri.")
        tamat("Bad")
    else:
        print("Tidak ada pilihan")

              

def tamat(akhir):
    print("\n== AKHIR CERITA ===")
    if akhir == "Good":
        print("GOOD ENDING: Penjahat berhasil di amankan, dan kamu mejadi pahlawan dunia")
    else:
        print("BAD ENDING: Operasi gagal, penjahat melarikan diri, dan kamu di pecat")
        print("Terimakasih sudah bermain")

mulai_game()