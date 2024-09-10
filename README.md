PWS : https://yemima-clara31-luxuryglow.pbp.cs.ui.ac.id/

# 1. Cara Implementasi Checklist secara step by step : 
1. Membuat repositori baru di GitHub dengan nama Luxury-Glow dan membuat berkas README dalam direktori lokal proyek.
2. Menghubungkan repositori lokal dengan repositori di github. 
3. Melakukan cloning repositori ke komputer lokal dengan url clone eccomerce.
4. Membuat dan mengaktifkan virtual environment pada command prompt.
5. Membuat berkas requirements.txt dan menambahkan beberapa dependencies, seperti berikut : 
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    Pillow
6. Melakukan instalasi terhadap dependencies dan membuat proyek django bernama Luxury_Glow.
7. Mengkonfigurasi proyek dan menjalankan server dengan menambahkan string pada ALLOWED HOSTS di settings.py untuk keperluan deployment, seperti berikut : 
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
8. Menambahkan berkas .gitignore untuk menentukan berkas dan direktori yang harus diabaikan oleh Git.
9. Membuat aplikasi main dalam proyek Luxury-Glow dan mendaftarkan aplikasi main ke dalam proyek. 
10. Mencoba membuka berkas HTML di peramban web.
11. Menambahkan atribut atribut yang diperlukan pada eccomerce Luxury Glow pada berkas models.py, yaitu :  name, price, description, image, shade_name, dan stock quantity.
12. Membuat migrasi model dengan perintah "python manage.py makemigrations" dan menerapkan migrasi ke dalam basis data lokal dengan perintah "python manage.py migrate".
13. Mengintegrasikan komponen MVT dengan menambahkan baris import di paling atas berkas views.py dengan menambahkan berkas dan menambahkan fungsi show_main di bawah impor.
14. Memodifikasi template main.html dan mengisi dengan atribut yang diperlukan pada eccomerce dan menyesuaikan peletakkan judul dan isiannya serta melakukan setting di warna tulisan dan backgroundnya.
15. Mengonfigurasi routing url pada aplikasi main pada berkas urls.py di dalam direktori main.
16. Mengonfigurasi routing url proyek untuk menghubungkan ke tampilan main dengan mengimpor fungsi include pada berkas urls.py yang bukan di direktori aplikasi main.
17. Menjalankan django dengan perintah "python manage.py runserver" dan membukanya pada peramban web.
18. Melakukan deployment dengan menambahkan URL deployment PWS pada ALLOWED HOSTS dengan username sso dan nama proyek.
19. Melakukan push dengan perintah "git push pws master" dan menununggu status running hingga successful, kemudian project yang sudah dibuat sudah dapat diakses.

# 2. Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan penjelasan kaitan antara urls.py, views.py, models.py, dan berkas html.
![alt text](<Bagan PBP-3.jpeg>)

# 3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Beberapa fungsi utama Git dalam pengembangan perangkat lunak :
1) Melacak setiap perubahan yang dibuat pada kode sumber selama pengembangan. Setiap perubahan dapat direkam dalam bentuk commit, yang berisi informasi tentang perubahan tersebut, seperti apa yang diubah, oleh siapa, dan kapan.
2) Git memfasilitasi kolaborasi antar anggota tim pengembang dengan mengizinkan beberapa orang untuk bekerja pada bagian yang sama dari sebuah proyek secara bersamaan. 
3) Git sering digunakan bersama dengan alat Continuous Integration/Continuous Deployment (CI/CD). Setiap kali ada perubahan kode yang dikirim ke repositori, pengujian otomatis dan proses build dapat dijalankan untuk memastikan kualitas dan konsistensi kode.
4) Git memungkinkan pengembang untuk membuat berbagai versi kode secara paralel menggunakan branching. Ini memudahkan pengelolaan fitur baru, perbaikan bug, dan eksperimen tanpa mengganggu kode utama (main branch). Setelah fitur atau perbaikan selesai, mereka dapat digabungkan kembali ke branch utama.

# 4. Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya, Framework Django dijadikan permulaan pembelajaran dikarenakan Kemudahan penggunaan karena dokumentasiya lengkap dan berkualitas dan memiliki arsitektur yang terorganisir dengan baik (MVT - Model - View - Template) yang terstruktur dengan baik sehingga pemula dapat memahami bagaimana komponen aplikasi web berinteraksi satu sama lain. Django juga memiliki komunitas user dan developer yang aktif sehingga pemula dapat mudah menemukan jawaban atas pertanyaan mereka. Django juga memungkinkan pemula yang ingin menjadi developer untuk membuat aplikasi web fungsional dengan cepat dikarenakan kerangka kerjanya dilengkapi panel admin otomatis yang memungkinkan pengembang untuk mengelola data aplikasi tanpa menulis banyak kode. 

# 5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut sebagai ORM dikarenakan memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python dan metode, tanpa perlu menulis query SQL. Django ORM akan secara otomatis menerjemahkan operasi yang dilakukan pada objek Python menjadi perintah SQL yang setara. Django disebut ORM juga karena menyediakan interface berbasis python untuk melakukan operasi CRUD (Create, Read, Uodate, Delete) pada data dalam database. 