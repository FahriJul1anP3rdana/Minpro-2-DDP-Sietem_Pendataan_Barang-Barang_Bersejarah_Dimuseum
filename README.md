# Minpro-angka-DDP-Sietem_Pendataan_Barang-Barang_Bersejarah_Dimuseum

## Nama: Fahri Julian Perdana
## Nim: 2609116045

## deskripsi singkat program: 
Program ini merupakan program pendataan barang-barang di museum yang memiliki 2 role yaitu admin dan user. Admin memiliki akses penuh untuk mengelola data (tambah, lihat, edit, dan hapus), sedangkan user hanya memiliki akses untuk melihat data barang.

## flowchart:
<img width="1700" height="2772" alt="Untitled Diagram12 drawio" src="https://github.com/user-attachments/assets/23d3a042-4e5c-49e8-bc3d-c461d579b106" />

Flowchart ini menggambarkan alur program yang terbagi menjadi dua role utama, yaitu admin dan user. Pengguna diawali dengan menginput username serta password untuk proses identifikasi hak akses. Jika terverifikasi sebagai user, pengguna hanya diberikan akses untuk melihat daftar barang yang ada di museum. Sementara itu, jika terverifikasi sebagai admin, pengguna mendapatkan hak akses penuh untuk mengelola data barang, meliputi fitur menambah, melihat, mengedit, hingga menghapus barang museum.

## Dokumentasi Program dan Output

<img width="501" height="95" alt="image" src="https://github.com/user-attachments/assets/c8c655d7-ac00-424d-b1de-81d1a95f07b1" />

Disini saya memakai 4 library, yaitu ada prettytable, pwinput, os, dan time

-PrettyTable: saya gunakan untuk merapikan daftar barang yang ada di kodingan saya agar lebih rapih dan enak dipandang

-pwinput: saya gunakan untuk menyembunyikan password agar tidak ketahuan 

-os: saya gunakan untuk tampilan lebih bersih saat saya menjalankan program tersebut

-time: saya gunakan untuk contoh ketika saya salah memasukan password/username, saya bakal diberi peringatan selama 3 detik sebelum saya bisa mengulang Kembali

<img width="695" height="123" alt="image" src="https://github.com/user-attachments/assets/318b3274-e7bc-429e-a9e8-e1f12adc6265" />

Nah untuk list barangnya, saya memakai dictionary dengan di dalamnya ada:

nama: untuk menentukan nama benda sejarah

Asal: tempat dimana benda itu berasal

Kondisi: untuk melihat suatu kondisi barang apakah bagus, baik, atau buruk

Tahun: untuk melihat kapan pertama kali benda itu dibuat

<img width="214" height="59" alt="image" src="https://github.com/user-attachments/assets/6135b638-6d1b-4022-afb4-3215a8650d8e" />

Disini juga saya menggunakan os untuk membersihkan layar, agar output yang nanti akan saya jalankan terlihat lebih rapih dan lebih bersih

<img width="723" height="663" alt="image" src="https://github.com/user-attachments/assets/b8e99f62-a6ce-41e0-9572-c8edfa1b84ca" />

Nah disini ada def tambah barang, yang dimana fungsinya itu untuk menambahkan suatu barang sejarah. Dan di dalamnya, itu saya mengguanakan perulangan while supaya admin harus mengisi inputan tersebut dan jangan dibiarkan kosong. Dan saya juga menggunakan while supaya barang sejarahnya tidak lewat dari 2026 alias tidak ada dari masa depan. Saya juga menggunakan append untuk menambahkan barang.

<img width="823" height="298" alt="image" src="https://github.com/user-attachments/assets/127b288d-1a1e-4e24-a71c-f94c60021fb7" />

Nah, disini ada juga lihat menu dimana, saya menggunakan len untuk menghitung barang yang ada di list, dan kalau barangnya kosong maka akan diberikan peringatan yaitu “barang kosong” nah disini juga saya menggunakan PrettyTable untuk merapikan list.

<img width="789" height="791" alt="image" src="https://github.com/user-attachments/assets/98f8bae9-5429-4be2-9860-24acca955689" />

Nah disini saya membuat edit barang dengan menggunakan len untuk menghitung barang yang ada di list dan saya juga menggunakan perulangan while supaya jika admin mengedit barang dia tidak boleh mengosongkan field. Dan juga disini saya memakai perulangan while untuk tahun juga yang dimana tahunnya ga boleh lebih dari 2026. Dan disini juga, saya menggunakan pilihan apakah anda yakin mau mengedit barang? Jika iya maka barang akan berhasil di edit, jika tidak, maka barang tidak jadi di edit. Oh dan juga disini saya memakai perulangan while dan len supaya jika admin menginputkan nomor kurang dari 1 atau nomor yang melebihi jumlah data yang ada di table maka dia kan muncul peringatan “data yang anda masukan tidak valid”

<img width="493" height="153" alt="image" src="https://github.com/user-attachments/assets/e43889ce-25cb-4768-bce1-e8aaf699bfab" />

Nah disini sama juga kayak di edit, saya menggunakan len untuk menghitung list barang yang ada di dalam table, terus saya juga menggunakan perulangan while dan len supaya admin tidak bisa menginputkan nomor kurang dari 1 atau nomor yang melebihi jumlah data yang ada di dalam tabel. Dan juga saya meakai pilihan, apakah anda yakin ingin menghapus data tersebut? Jika ya maka data akan terhapus dan jika tidak maka datanya tidak jadi di hapus.

<img width="539" height="470" alt="image" src="https://github.com/user-attachments/assets/a461469d-8de3-4a54-bb5a-c0577044bc71" />

Nah disini ada def login, dimana terdapat username dan password untuk masing masing role. Dan juga, saya menggunakan while true agar jika salah memasukan password atau username program tidak terhenti, dan saya juga memakai pwinput untuk menyembunyikan password. Dan, saya memakai time.sleep untuk memberi jeda peringatan agar tidak langsung menghilang, dan yang terakhir saya memakai login() agar memanggil fungsi dari login.

<img width="940" height="246" alt="image" src="https://github.com/user-attachments/assets/7ce581c4-9cd0-4c7d-b6b8-efa15459cfc9" />

Nah, disini ada menu admin yang dimana saya menggunakan perulangan while true, if, elif, dan else, supaya nanti admin bisa menginputkan nomor untuk admin bisa memilih daftar menu dan isinya itu ada 1-5, dan jika admin menginu. Jika mengetik angka 1 maka admin di arahkan ke tambah barang. kalau mengetik angka 2, maka admin akan di arahkan ke melihat barang. Kalau mengetik angka 3, maka admin akan di arahkan ke mengedit barang. Dan jika admin mengetik angka 4 maka dia akan di arahkan ke delete barang. Dan yang terakhir jika admin mengetik angka 5 maka itu akan break alias perulangan selesai. Saya juga menggunakan time.sleep untuk menjeda waktu peringatan agar ga langsung hilang.

<img width="466" height="201" alt="image" src="https://github.com/user-attachments/assets/ef076b6c-5239-4bfc-b01e-50a04488662f" />

Disini ada juga menu user yang saya buat dengan menggunakan perulangan while true sama kayak admin, dan isinya itu ada pilihan 1 dan 2 aja, dimana pilihan 1 user hanya bisa melihat barang dan pilihan ke 2 user keluar, dan jika menginputkan lebih dari 2 maka akan kena peringatan “inputan tidak valid” dan saya juga sama menggunakan time sleep untuk menjeda peringatan agar tidak langsung hilang.

outputnya:
  menu admin:

  <img width="118" height="36" alt="image" src="https://github.com/user-attachments/assets/e8ddd140-1715-43d8-8a2f-ec4db196dde1" />

  output untuk memasukan username dan password (untuk admin)

  <img width="395" height="56" alt="Screenshot 2026-10-06 174414" src="https://github.com/user-attachments/assets/6e2a5085-11b2-4cf0-9371-08e34faf535f" />

  Menu admin

  <img width="482" height="47" alt="Screenshot 2026-10-06 174501" src="https://github.com/user-attachments/assets/1b221fd0-d7bb-41ed-9f84-85464573670e" />

  <img width="375" height="62" alt="Screenshot 2026-10-06 174513" src="https://github.com/user-attachments/assets/4312cb55-4e28-4f4d-8bc0-42d946833393" />

  tambah barang

  <img width="163" height="46" alt="image" src="https://github.com/user-attachments/assets/9023cb20-bd6f-4747-a3df-f38665d08256" />

  Lihat barang

  <img width="318" height="98" alt="Screenshot 2026-10-06 175007" src="https://github.com/user-attachments/assets/d8fab1a4-3584-45bc-97e4-5befda44ae71" />

  <img width="167" height="44" alt="Screenshot 2026-10-06 175029" src="https://github.com/user-attachments/assets/08abb986-785f-476f-b9a7-4e7b36f97077" />

  Edit barang

  <img width="254" height="68" alt="Screenshot 2026-10-06 175100" src="https://github.com/user-attachments/assets/5a01b980-ccf2-4dac-aa32-54b22e4cc0ff" />

  <img width="166" height="39" alt="Screenshot 2026-10-06 175111" src="https://github.com/user-attachments/assets/834158a7-ab66-4aea-825d-a09b2eb0b9c5" />

  Hapus Barang

  <img width="335" height="15" alt="Screenshot 2026-10-06 175123" src="https://github.com/user-attachments/assets/7e0d90b9-6df3-4a2b-972a-9e3b9594924e" />

  Keluar (Break)

  Menu User:

  <img width="107" height="44" alt="image" src="https://github.com/user-attachments/assets/3c8da778-47dc-464a-b6df-51e53115ffbe" />

  output untuk memasukan username dan password (untuk user)

  <img width="98" height="14" alt="image" src="https://github.com/user-attachments/assets/3ee35e30-e0a4-4e22-98cc-7ae70b00650d" />

  Menu user

  <img width="167" height="50" alt="image" src="https://github.com/user-attachments/assets/419d24e4-a72f-4ecd-ba28-bf237abc5dba" />

  menu untuk lihat barang

  <img width="89" height="19" alt="image" src="https://github.com/user-attachments/assets/60274814-333d-4860-93dd-352667c46c73" />

  keluar (break)








  


  


  


  


  


  


  


  
























