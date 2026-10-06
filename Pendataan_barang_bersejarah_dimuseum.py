from prettytable import PrettyTable
import pwinput
import os
import time

barang_sejarah = []
barang = [
    {"nama": "katana", "asal": "jepang", "kondisi": "bagus", "tahun": 1454},
    {"nama": "broadsword", "asal": "inggris", "kondisi": "baik", "tahun": 1330}
]

def hapus_layar():
    os.system('cls')


def tambah_barang():
        hapus_layar()
        print("SELAMAT DATANG DI MUSEUM, SILAHKAN PILIH MENU")
        print(barang)
        nama_barang = input("masukan nama barang :") 
        while nama_barang == "":
            print("jangan sampai kosong")
            nama_barang = input("masukan nama barang :") 

        asal_barang = input("masukan asal barang :")
        while asal_barang == "":
            print("isi dengan nama negara, jangan di biarkan kosong") 
            asal_barang = input("masukan asal barang :")

        kondisi_barang = input("masukan kondisi barang :")
        while kondisi_barang == "":
            print("isi dengan rusak/baik/bagus. Jangan dibiarkan kosong")
            kondisi_barang = input("masukan kondisi barang :")

        tahun_barang = int(input("masukan tahun barang :"))
        while tahun_barang > 2026:
            print("isi dengan angka tahun yang valid!")
            tahun_barang = int(input("masukan tahun barang :"))

        barang.append({
            "nama" : nama_barang, 
            "asal" : asal_barang, 
            "kondisi" : kondisi_barang, 
            "tahun" : int(tahun_barang)
            }) 
            
        print("barang berhasil di tambahkan!")
    
def lihat_menu():
    hapus_layar()
    if len(barang) == 0:
            print("barang kosong")
            return
    tabel = PrettyTable()
    tabel.field_names = ["no", "nama","asal", "kondisi", "tahun"]

    nomor = 1
    for item in barang:
        tabel.add_row([nomor, item["nama"], item["asal"], item["kondisi"], item["tahun"]])
        nomor = nomor + 1
    
    print(tabel)

def edit_barang():
        hapus_layar()
        if len(barang) == 0:
            print("barang belum di edit")
            return

        lihat_menu()
        nomor_pilihan = int(input("Masukkan nomor barang yang mau di edit: "))
        while nomor_pilihan < 1 or nomor_pilihan > len(barang):
            print("data yang anda masukan tidak valid")
            nomor_pilihan = int(input("Masukan nomor barang yang mau di edit: "))
            
        index = int(nomor_pilihan) - 1
        nama_barang = input("masukan nama barang :") 
        while nama_barang == "":
            print("jangan sampai kosong")
            nama_barang = input("masukan nama barang :") 

        asal_barang = input("masukan asal barang :")
        while asal_barang == "":
            print("isi dengan nama negara, jangan di biarkan kosong") 
            asal_barang = input("masukan asal barang :")

        kondisi_barang = input("masukan kondisi barang :")
        while kondisi_barang == "":
            print("isi dengan rusak/baik/bagus. Jangan dibiarkan kosong")
            kondisi_barang = input("masukan kondisi barang :")

        tahun_barang = int(input("masukan tahun barang :"))
        while tahun_barang > 2026:
            print("isi dengan angka tahun yang valid!")
            tahun_barang = int(input("masukan tahun barang :"))
        
        
        yakin = input("apakah anda ingin mengedit barang ini? ketik y jika ya dan ketik no jika tidak: ")
        if yakin == "y":
            barang[index] = {
                "nama" : nama_barang, 
                "asal" : asal_barang, 
                "kondisi" : kondisi_barang, 
                "tahun" : tahun_barang
                }
            print("barang berhasil di edit")
        else:
            print("barang tidak jadi di edit")
        

def hapus_barang():
    hapus_layar()
    if len(barang) == 0:
        print("belum ada data yang di hapus")
        return
    lihat_menu()
    nomor_pilihan = int(input("pilih nomor yang mau anda hapus: "))
    while nomor_pilihan < 1 or nomor_pilihan > len(barang):
        print("nomor inputan tidak valid")
        nomor_pilihan = int(input("Masukkan nomor barang yang mau dihapus: "))
    index = int(nomor_pilihan) - 1

    yakin = input("apakah anda ingin menghapus barang ini? ketik y jika ya dan ketik n jika tidak: ")
    if yakin == "y":
        barang.pop(index)
        print("barang berhasil di hapus")
    else:
        print("barang tidak jadi di hapus")

def menu_admin():
    hapus_layar()
    while True:
        pilihan = input("daftar menu, 1. Tambah Barang, 2. Melihat Barang, 3. Mengedit Barang, 4. Menghapus Barang, 5. Break/keluar: ")
        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            lihat_menu()
        elif pilihan == "3":
            edit_barang()
        elif pilihan == "4":
            hapus_barang()
        elif pilihan == "5":
            print("log out dari menu admin")
            break
        else:
            print("pilihan tidak valid, masukan angka 1-5! selain angka 5 tidak valid")
            time.sleep(3)

def menu_user():
    hapus_layar()
    while True:
        pilihan_menu = input("1. Lihat Barang, 2. Keluar")
        if pilihan_menu == "1":
            lihat_menu()
        elif pilihan_menu == "2":
            print("log out dari menu user")
            break
        else:
            print("input tidak valid")
            time.sleep(2)

def login(): 
    admin_user =  "admin"
    admin_pass = "admin123"

    tamu_user = "user"
    tamu_pass = "user123"

    while True: 
        hapus_layar()
        print("sistem manajemen museum")
        input_user = input("masukan username : ")
        input_pass = pwinput.pwinput("masukan password : ")
    
        if input_user == admin_user and input_pass == admin_pass:
            print("selamat anda masuk ke admin")
            menu_admin()
            break
        elif input_user == tamu_user and input_pass == tamu_pass:
            print("selamat anda masuk ke user")
            menu_user()
            break
        else:
            print("password atau username yang anda masukan salah")
            time.sleep(3)
login()


