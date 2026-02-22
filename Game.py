import time
import sys

def slow_text(teks, delay=0.04):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def save_ending(ending):
    with open("ending.txt", "a") as file:
        file.write(ending + "\n")

def tampilkan_endings():
    try:
        with open("ending.txt", "r") as file:
            endings = file.readlines()
            if endings:
                print("\n=== ENDING YANG KAMU DAPAT ===")
                for idx, ending in enumerate(endings, 1):
                    print(f"{idx}. {ending.strip()}")
            else:
                print("=== BELUM DAPAT ENDING ===")
    except FileNotFoundError:
        print("=== BELUM DAPAT ENDING ===")

game_over = False

print ("===WELCOME===")

while True:
    slow_text(
    "===MISI PENANGKAPAN===\n"
    "1. MULAI GAME\n"
    "2. ENDINGS\n"
    "3. KELUAR\n"
    ) 
    
    pilihan = input("pilih dari menu(1,2,3): ")

    

    if pilihan == "1":
        while True:
            name = input("Masukkan nama (bukan angka): ")
            try:
                name = int(name)
                print("Input tidak valid! Jangan masukkan angka.")
            except ValueError:
                print(f"Input diterima: {name}\n")
                break
    elif pilihan == "2":
        tampilkan_endings()
        input("\nTekan ENTER untuk kembali ke menu...")
        continue

    slow_text( 
    "GAME STORY : MISI PENANGKAPAN ROBERT\n"
    "Tekan ENTER untuk mulai...\n"
    )
    input()

    print("================================================================================\n")
    
    slow_text(

    "Anda adalah seorang detektif yang mendapatkan misi untuk menangkap seorang penjahat berbahaya.\n"
    "targetmu adalah Robert, seorang penjahat yang dikenal licik, sadis dan sangat berbahaya.\n"
    "kau harus kau akan masuk ke dalam pesta yang di rayakan oleh Robert, kau harus menyamar, dan menangkap dia sebelum dia menyadari keberadaanmu.\n"
    )
    input()
    print("=================================================================================\n")

    while True:
        slow_text(
        f"CAPTAIN RAYLE : hey {name}, kamu sudah siap dengan misimu kan?\n"
        "Tekan ENTER untuk menjawab..."
            )
        input()        

        jawab = input("\nJAWAB (ya/tidak): ").lower()

        if jawab == "ya":
            slow_text(
                "CAPTAIN RAYLE : bagus, kamu akan menyamar menjadi tamu di pesta.\n"
                "Nama samaranmu adalah Andrew.\n"
                "CAPTAIN RAYLE : kau harus harus bisa menangkap Robert sebelum pestanya selesai.\n"
                f"Semoga beruntung, tuan {name}!\n"
                "Tekan ENTER untuk lanjut..."
                )
            input()
            break

        elif jawab == "tidak":
            print(
                "CAPTAIN RAYLE : kalau begitu kamu tidak akan pernah menangkap Robert.\n"
                "Selamat tinggal!\n"
            )
            save_ending("ENDING PENGANGGURAN: KAMU DIPECAT KARENA MENOLAK MISI\n")
            print("=== KAMU MENDAPAT 'SECRET ENDING (3/3)' ===\n")
            game_over = True
            break

        else:
            slow_text(
                f"Pilih 'ya' atau 'tidak', tuan {name}!\n"
                "Tekan ENTER untuk menjawab ulang..."
            )
    if game_over:
        continue

    slow_text(
        "PENJAGA PINTU MASUK : selamat datang di pesta Robert, siapa namamu? \n"
        f"({name} / Andrew) : nama saya Andrew\n"
        "PENJAGA PINTU MASUK : silahkan masuk Tuan Andrew, semoga anda menikmati pestanya.\n"
        f"({name} / Andrew) : terima kasih.\n"
    )
    input()

    slow_text(
    f"{name} : (baiklah apa yang aku harus lakukan sekarang?) \n"
    "CAPTAIN RAYLE : (ada beberapa ruangan yang hanya bisa di akses oleh tamu VIP dan staff.)\n"
    "CAPTAIN RAYLE : (cari kartu akses staff dan masuk ke ruangan cctv. lalu hack sistem cctv, agar orang-orang di markas bisa membantu)\n"
    "CAPTAIN RAYLE : (ingat, jangan sampai melakukan tindakan mencurigakan, atau kau akan diusir dari pesta.)\n"
    )
    input()

    slow_text(
    "saat kau sedang berkeliling di pesta, kau melihat ada staff security yang sedang lemas, dan kau melihat celah untuk mengambil kartu akses staff.\n"
    "tetapi ini tempat yang ramai, jadi sedikit sulit untuk mengambil kartu akses itu.\n"
    )
    input()

    slow_text(
                f"{name} / Andrew : maaf, apakah anda baik - baik saja?\n"
                "STAFF SECURITY : ahh.. iya, saya merasa sedikit pusing karena tempat ini terlalu bising.\n"
                f"{name} / Andrew : ayo, saya bantu ke belakang gedung."
                "kamu pun membawa staff security itu ke tempat yang lebih sepi dan sunyi, setelah memastilkan tidak ada orang di sekitar, kamu langsung memukulnya dari belakang sampai pingsan dan mengambil kartu aksesnya, dan menyembunyikan tubuhnya di tempat sampah.\n"
            "----kamu mendapatkan kartu akses staff----\n"
        )
    input()
        
    slow_text(
            f"{name} : (captain saya sudah mendapatkan kartu akses staff.\n)"
            f"CAPTAIN RALEY : (bagus {name}, sekarang pergilah ke ruangan cctv dan hack sistemnya agar tim di markas bisa membantumu memantau pergerakan Robert dan bawahannya).\n"
            f"{name} : (baik captain)"
        )
    input()

    slow_text(
            "kamu pun pergi keruangan cctv dan menggunakan kartu akses staff untuk masuka ke ruangan itu.\n"
            "dan saat kamu masuk kamu melihat ada security yang memantau cctv sedang tidur di bangkunya."
            "TEKAN ENTER UNTUK MEMBUAT ORANG ITU PINGSAN"
        )
    input()

    slow_text(
            "kamu berhasil membuat orang itu pingsan, dan kamu langsung menghack sistem cctv agar tim di markas bisa membantu."
            "setelah beberapa saat, tim di markas berhasil masuk kedalam sistem cctv"
        )
    input()

    slow_text(
            f"KHAI: (halo {name}, apa kau bisa mendengar suaraku? Aku akan membantumu untuk melacak Robert dan bawahannya)\n"
            f"{name} : (iya, aku bisa mendengarmu dengan jelas, terima kasih Khai!)\n"
            "KHAI: (tidak masalah, tetap waspada!)\n"
        )
    input()

    slow_text(
            "setelah kau keluar dari ruangan cctv, kau langsung pergi ke tempat pesta lagi untuk mencari Robert.\n"
        )
    input()

    slow_text(
            f"KHAI: ({name}, aku melihat Robert ada di ruangan khusus VIP, kau bisa masuk dengan menyamar menjadi salah satu security khusus VIP, ada salah satu securty VIP yang sedang di toilet khusus staff, masuk diam diam dan ambil bajunya.)\n"
            f"{name} : (baik, terikasih atas informasinya.)\n"
            f"KHAI: (ingat jangan sampai ada yang melihat mu)\n"
        )
    input()

    slow_text(
            "kamu pun pergi ke toilet staff secara diam - diam, dan menyerang security VIP itu dari belakang sampai pingsan, dan kamu langsung mengambil baju security VIP itu, dan menyembunyikan di salah satu kamar toilet.\n"
            "setelah menggunakan baju security, kau masuk ke ruangan VIP dengan hati-hati dan waspada.\n"
        )
    input()

    slow_text(
            "ROBERT : hai kau yang di sana."
            f"{name} : <sial apa aku ketahuan?>"
            "ROBERT : hey kau cepat kesini jangan diam saja"
            f"{name} : siap bos."
            "ROBERT : aku tidak pernah melihat wajah mu, apa kau pekerja baru?"
            f"{name} : iya bos saya pegawai baru di sini."
            "ROBERT : oh beitu, jadi William menambah karyawan baru lagi, yah sudah lah."
            f"{name} : jadi bos memanggil saya untuk melakukan apa."
            "ROBET : aku memanggil mu untuk membantu ku mengeksekusi seseorang, apa kau bisa anak baru?"
            f"{name} : saya akan usahakan bos."
            "ROBERT : bagus, sekarang cepat ikuti aku."
        )
    input()

    slow_text(
            "kau pun mengikuti Robert sampai ke suatu tempat, terlihat seperti basement atau penjara bawah tanah.\n"
            "kau mencium bau busuk seperti bangkai, dan itu hampir membuat mu muntah.\n"
            "kalian berhenti di depan pintu besi.\n"
        )
    input()

    slow_text(
            "ROBERT : baik kita sudah sampai.\n"
            f"{name} : tempat apa ini?"
            "ROBERT : ini tempat untuk mengurung/mengeksekusi penghianat dan mata - mata.\n"
            f"{name} : memangnya ada apa sampai bos membawa saya kesini.\n"
            "ROBERT : aku ingin kau membunuh seseorang untuk ku, dia mata - mata yang di kirim oleh para FBI 1 bulan yang lalu.\n"
            f"{name} : (mata - mata yang dikirim anngota FBI?)\n"
            "ROBERT : baiklah aku sudah membuka pintuny, ayo masuk dan kau bunuh orang itu saat aku selesai bicara dengannya.\n"
        )
    input()

    slow_text(
        "saat kau masuk kedalam ruangan itu besama Robert, kau melihat mata - mata FBI itu sudah memiliki luka yang sanagat parah dan terlihat seperti orang yang telah disiksa dalam waktu yang lama.\n"
        "kau merasa ketakutan dan ingin kabur dari tempat itu tetapi kau tidak bisa karena misimu.\n"
        "sementara itu Robert berbicara dengan orang itu walaupun dia tidak di gubris.\n"
    )

    input()

    slow_text(
        "ROBERT : baiklah nak aku sudah selesai berbicara dengannya, kau bisa membunuhnya sekarang menggunakan pisau yang ada di meja.\n"
        f"{name} : baiklah . . . (kau hanya berdiri diam sambil memegang pisau)\n"
        "ROBERT : apa yang kamu tunggu nak? cepat lakukan!"
        "apa yang akan kamu lakukan?"
        "[1. SERANG ROBERT]\n"
        "[2. BUNUH MATA - MATA FBI]\n"
    )
    input()

    while True:

        pilihan == input("\npilih 1 atau 2")

        if pilihan("1"):
            slow_text(
                "kau langsung menyerang Robert dengan pisau itu, dan berhasil menusuk bahunya.\n"
                "saat robert mau berteriak kau langsung menutup mulutnya dan mencekek Robert sampai pingsan.\n"
                "saat Robert sudah pingsan, kau langsung menghubungi captain dan minta tolong untuk dijemput ke markas.\n"
                "setelah itu, kau keluar dari tempat itulewat jalan keluar rahasia yang sempat kau lhat saat menuju ke ruang bawah tanah.\n"
                "beberapa hari kemudian, berita Robert sudah tertangkap tersebar ke seluruh dunia, dan tim militer juga di kirim ke tempat pesta untuk menyelamatkan para korban yang sudah di culik oleh Robert.\n"
                "beberapa bawahan Robert menyerahkan diri ke polisi, sedangkan sisanya menjadi criminal yang dicari polisi.\n"
            )
            input()
            save_ending("MISION SUCCESS! ENDING : KAU BERHASIL MENANGKAP ROBERT")
            print("=== KAMU MENDAPATKAN 'GOOD ENDING (2/3)' ===")
            game_over = True
            break
            

        elif pilihan("2"):
            slow_text(
                "kau langsung membunuh mata - mata tersebut.\n"
                f"{name} : sudah ku bunuh bos!\n"
                "ROBERT : bagus! Kamu sangat bagus sebagai pemula di sini."
                f"{name} : hehe, terima kasih bos!\n"
                "kamu pun menjadi bawahannya Robert.\n"
                "tiba - tiba, tim di markas datang dan mengetahui bahwa kamu sudah menjadi bawahannya Robert dan kau di bunuh.\n"
            )
            input()
            save_ending("MISION FAILED, ENDING : KAMU GAGAL")
            print("=== KAMU MENDAPATKAN 'BAD ENDING (1/3)' ===")
            game_over = True
            break
            

        if game_over:
            continue

