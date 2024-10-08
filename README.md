PWS : http://yemima-clara31-luxuryglow.pbp.cs.ui.ac.id

<details>
<summary>Tugas 2</summary>
<p><strong>**Cara Implementasi Checklist secara step by step**</strong></p>
<ol>
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

**Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan penjelasan kaitan antara urls.py, views.py, models.py, dan berkas html.**
![alt text](<Bagan PBP-3.jpeg>)

**Jelaskan fungsi git dalam pengembangan perangkat lunak!**
Beberapa fungsi utama Git dalam pengembangan perangkat lunak :
1) Melacak setiap perubahan yang dibuat pada kode sumber selama pengembangan. Setiap perubahan dapat direkam dalam bentuk commit, yang berisi informasi tentang perubahan tersebut, seperti apa yang diubah, oleh siapa, dan kapan.
2) Git memfasilitasi kolaborasi antar anggota tim pengembang dengan mengizinkan beberapa orang untuk bekerja pada bagian yang sama dari sebuah proyek secara bersamaan. 
3) Git sering digunakan bersama dengan alat Continuous Integration/Continuous Deployment (CI/CD). Setiap kali ada perubahan kode yang dikirim ke repositori, pengujian otomatis dan proses build dapat dijalankan untuk memastikan kualitas dan konsistensi kode.
4) Git memungkinkan pengembang untuk membuat berbagai versi kode secara paralel menggunakan branching. Ini memudahkan pengelolaan fitur baru, perbaikan bug, dan eksperimen tanpa mengganggu kode utama (main branch). Setelah fitur atau perbaikan selesai, mereka dapat digabungkan kembali ke branch utama.

**Mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**
Menurut saya, Framework Django dijadikan permulaan pembelajaran dikarenakan Kemudahan penggunaan karena dokumentasiya lengkap dan berkualitas dan memiliki arsitektur yang terorganisir dengan baik (MVT - Model - View - Template) yang terstruktur dengan baik sehingga pemula dapat memahami bagaimana komponen aplikasi web berinteraksi satu sama lain. Django juga memiliki komunitas user dan developer yang aktif sehingga pemula dapat mudah menemukan jawaban atas pertanyaan mereka. Django juga memungkinkan pemula yang ingin menjadi developer untuk membuat aplikasi web fungsional dengan cepat dikarenakan kerangka kerjanya dilengkapi panel admin otomatis yang memungkinkan pengembang untuk mengelola data aplikasi tanpa menulis banyak kode. 

**Mengapa model pada Django disebut sebagai ORM?**
Model pada Django disebut sebagai ORM dikarenakan memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python dan metode, tanpa perlu menulis query SQL. Django ORM akan secara otomatis menerjemahkan operasi yang dilakukan pada objek Python menjadi perintah SQL yang setara. Django disebut ORM juga karena menyediakan interface berbasis python untuk melakukan operasi CRUD (Create, Read, Uodate, Delete) pada data dalam database. 
</ol>
</details>

<details>
<summary>Tugas 3</summary>
<p><strong>**Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**</strong></p>
<ol>
Kita memerlukan data delivery dalam pengimplementasian platform karena data sering kali perlu dipindahkan dari satu bagian sistem ke bagian lainnya, atau dari server ke client, agar aplikasi dapat berfungsi dengan baik. Data delivery juga memungkinkan berbagai sistem yang menggunakan format data berbeda, seperti XML dan JSON, untuk saling berkomunikasi. Ini membantu integrasi dengan aplikasi lain yang mungkin memiliki format data yang berbeda. Dengan data delivery, pengguna dapat melihat informasi yang diperbarui atau dinamis di aplikasi mereka. Contohnya, ketika pengguna mengisi formulir atau menambahkan data, sistem dapat memproses data tersebut dan menampilkannya kembali dengan cepat dalam format seperti HTML, XML, atau JSON.

**Menurutmu, mana yang lebih baik antara XML dan JSON?**
Perbandingan antara XML dan JSON:
- JSON lebih ringan dan lebih cepat: JSON memiliki struktur yang lebih sederhana dan tidak memerlukan tag pembuka dan penutup seperti XML, sehingga ukuran file JSON biasanya lebih kecil dan proses parsing lebih cepat.
- JSON lebih mudah dibaca oleh manusia dan mesin: JSON memiliki struktur yang lebih ringkas dan lebih mudah dibaca, terutama dalam format key-value yang mirip dengan objek di JavaScript, yang membuatnya lebih intuitif bagi banyak developer.
**Mengapa JSON lebih populer dibandingkan XML?**
- Efisiensi dan performa: Karena ukurannya yang lebih kecil dan parsing yang lebih cepat, JSON lebih disukai dalam aplikasi web modern yang membutuhkan komunikasi data yang cepat dan ringan.
- Kompatibilitas dengan JavaScript: JSON secara native mendukung JavaScript, sehingga lebih mudah diintegrasikan dalam aplikasi berbasis web yang banyak menggunakan JavaScript.
- Banyaknya dukungan oleh API: Sebagian besar API modern mendukung atau menggunakan JSON sebagai format utama untuk pertukaran data karena kemudahan integrasi dan efisiensinya.

**Jelaskan fungsi dari method is_valid() pada form Django**
Method is_valid() ini digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form Django valid atau tidak. Ketika is_valid() dipanggil, Django akan melakukan validasi terhadap semua field dalam form sesuai dengan aturan atau constraints yang telah didefinisikan dalam model atau form tersebut. Jika semua data valid, method ini akan mengembalikan nilai True. Jika terdapat kesalahan pada data yang diinput, method ini akan mengembalikan False dan menyediakan pesan error yang dapat ditampilkan kepada pengguna.
**Mengapa kita membutuhkan method tersebut?**
- Memastikan integritas data : Method ini penting untuk memastikan bahwa data yang diinput oleh pengguna sesuai dengan aturan yang telah ditentukan (misalnya format price yang benar, panjang minimal atau maksimal teks, angka yang valid, dll.).
- Mencegah kesalahan : Dengan adanya validasi melalui is_valid(), kita dapat mencegah penyimpanan data yang tidak sesuai, sehingga mengurangi risiko kesalahan sistem.

**Mengapa kita membutuhkan csrf_token saat membuat form di Django?**
Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah jenis serangan di mana penyerang dapat membuat pengguna yang terautentikasi secara tidak sengaja mengirimkan permintaan berbahaya ke server tanpa sepengetahuan mereka. Dengan menambahkan csrf_token, Django menghasilkan token unik yang dimasukkan ke dalam setiap form dan diperiksa oleh server saat menerima permintaan POST.
**Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?** 
Jika csrf_token tidak ditambahkan, aplikasi menjadi rentan terhadap serangan CSRF, di mana penyerang dapat memanfaatkan sesi aktif pengguna untuk mengirimkan permintaan yang tidak sah. Tanpa validasi token, server akan menerima dan memproses permintaan tersebut seolah-olah permintaan tersebut valid, yang dapat berakibat pada modifikasi data atau tindakan berbahaya lainnya.
**Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**
Penyerang dapat membuat halaman web yang secara diam-diam mengirimkan permintaan berbahaya (misalnya, menghapus akun atau mengubah data penting) ke aplikasi Django menggunakan sesi pengguna yang sudah terautentikasi, tanpa persetujuan atau sepengetahuan pengguna tersebut. Dengan menggunakan token CSRF, Django memastikan bahwa permintaan yang diterima berasal dari sumber yang sah (form dalam aplikasi) dan bukan dari sumber eksternal.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**
1) Membuat direktori templates pada root folder dan membuat berkas base.html untuk template dasar yang dapat digunakan sebagai kerangka umum untuk halaman web lainnya di dalam proyek. Lalu menambahkan variabel templates dengan "BASE_DIR / 'templates'". Lalu mengubah kode main.html dengan mengextends base.html agar base.html sebagai template utama
2) Menambahkan "import uuid" untuk mengubah primary key dari integer menjadi uuid, lalu melakukan migrasi.
3) Membuat berkas forms.py untuk membuat struktur form yang dapat menerima data Product Entry baru, setelah itu menambahkan import redirect pada berkas views.py dan membuat fungsi baru create_product_entry yang menerima parameter request untuk menghasilkan form yang dapat menambahkan data Product Entry secara otomatis ketika  data di-submit dari form. 
4) Menambahkan fungsi ProductEntry.objects.all() pada berkas views.py yang akan digunakan untuk mengambil seluruh objek ProductEntry yang tersimpan pada database, lalu menambahkan import fungsi create_product_entry pada urls.py.
5) Menambahkan path URL ke dalam variabel url patterns pada urls.py di main untuk mengakses fungsi create_product_entry. Setelah itu, membuat berkas html baru dengan nama create_product_entry.
6) Menambahkan kode "% block content %" untuk menampilkan data product dalam bentuk tabel serta tombol "Add New Skincare atau Product"
7) Menambahkan import HttpResponse dan Serializer pada berkas views.py dan membuat sebuah fungsi baru dengan nama show_xml serta membuat sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada ProductEntry. Lalu, menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter content_type="application/xml.
8) Menambahkan import fungsi show_xml pada urls.py dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor sebelumnya.
9) Membuat sebuah fungsi baru yang menerima parameter request dengan nama show_json dan menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON dan parameter content_type="application/json" serta menambahkan fungsi show_json pada urls.py. Lalu, menambahkan show_json pada path url.
10) Membuat dua fungsi baru, yaitu show_xml_by_id dan show_json_by_id. Lalu, membuat variabel di dalam fungsi buat nyimpen hasil query dari data dengan id tertentu yang ada pada ProductEntry. Setelah itu, menambahkan return function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value "application/xml" (untuk format XML) atau "application/json" (untuk format JSON).
11) Menambahkan import fungsi show_xml_by_id dan show_json_by_id dan menaambahkan path url tersebut untuk mengakses fungsi yang sudah diimpor.
12) Melihat data lewat Postman dengan method get dilengkapi dengan url xml dan json untuk mengetes apakah data terkirimkan dengan baik serta xml by id dan json by id untuk mengetes fungsi pengambilan data Product Entry berdasarkan ID.
13) Melakukan push ke pws secara otomatis menggunakan github actions, yaitu dengan membuat subdirektori .github dan di dalamnya diletakkan subdirektori bernama workflows. Lalu, membuat berkas deploy.yml. Selanjutnya, pada repositori di github di bagian actions pada settings mengisi nama dengan PWS_URL dan mengisi secret dengan format yang telah ditentukan. Setelah itu, menambahkan kode url pws pada settings.py dan terakhir melakukan git add, commit, dan push serta menunggu indikator kuning berubah menjadi indikator centang hijau.

**Hasil akses URL XML**
![alt text](image.png)

**Hasil akses URL JSON**
![alt text](image-1.png)

**Hasil akses URL XML by ID**
![alt text](image-2.png)

**Hasil akses URL JSON by ID**
![alt text](image-3.png)
</ol>
</details>

<details>
<summary>Tugas 4</summary>
<p><strong>**Apa perbedaan antara HttpResponseRedirect() dan redirect()**</strong></p>
<ol>
<ul>
<li> HttpResponseRedirect() adalah metode dari Django yang secara eksplisit digunakan untuk membuat objek respons yang mengarahkan pengguna ke URL tertentu. Ini secara eksplisit menggunakan URL sebagai argumen dan mengembalikan respons redirect HTTP ke browser pengguna. Dilakukan secara manual menentukan URL tujuan dalam bentuk string. </li>
<li> redirect() adalah metode yang lebih mudah digunakan karena secara otomatis menerima nama tampilan (view) atau URL yang ingin diarahkan. Ini adalah versi shortcut dari HttpResponseRedirect() yang disediakan oleh Django. Pengguna dapat menggunakan nama tampilan Django yang sudah didefinisikan atau objek URL, sehingga lebih fleksibel. Pada tugas 4 ini, URL telah didefinisikan di urls.py, redirect() secara otomatis akan mengkonversinya ke URL lengkap dan kemudian mengembalikan redirect HTTP. </li>
</ul>

**Jelaskan cara kerja penghubungan model Product dengan User!**

Pada tugas 4 ini, ketika ingin menghubungkan model Product dengan User, menggunakan relasi ForeignKey. Dalam model Product, saya menambahkan field user yang terhubung dengan model User. Ini memungkinkan setiap produk yang ditambahkan atau diubah akan terkait dengan user yang sedang login. Dengan menambahkan ForeignKey(User, on_delete=models.CASCADE), produk ini akan berhubungan dengan User, dan setiap kali produk disimpan, field user akan menyimpan referensi ke pengguna yang membuat produk tersebut dan jika user dihapus, semua produk yang terkait juga akan dihapus. 

**Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login?**
<ul>
<li> Authentication adalah proses memeriksa identitas user, memastikan bahwa user adalah orang yang diklaim melakukan login dengan username dan password. Saat pengguna login di Django, sistem memverifikasi kredensialnya dan memulai sesi user. </li>
<li> Authorization adalah proses untuk memberikan izin kepada user setelah mereka berhasil diotentikasi. Ini menentukan hak akses user terhadap fitur atau halaman tertentu di aplikasi.</li>
</ul>

**Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut**

Saat pengguna login di Django, proses authentication terjadi, dan setelah login berhasil, session dikelola untuk mengingat user yang telah login (authorization). Django mengimplementasikan session cookies untuk ini, di mana cookie menyimpan ID sesi pengguna yang login.

**Bagaimana Django mengingat pengguna yang telah login?**

Django menggunakan session cookies untuk mengingat user yang telah login. Setelah user berhasil login, Django menciptakan sesi yang terikat dengan user tersebut, lalu menyimpan session ID pada cookie di browser. Setiap kali pengguna mengirim request baru, session ID ini dikirimkan kembali ke server, sehingga server dapat mengenali user. Contoh penerapan pada tugas 4 adalah saat session ID dikirim setiap kali user melakukan request, dan server memverifikasi session untuk memastikan pengguna tersebut sudah login​.

**Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Cookies bisa digunakan untuk menyimpan informasi kecil di sisi klien, seperti preferensi user, data shopping cart, atau pengaturan tampilan. Selain untuk session tracking, cookies juga digunakan untuk mengingat status login, melacak user di situs yang berbeda (seperti pada iklan), atau menyimpan informasi yang bersifat sementara.
Tidak semua cookies aman digunakan, terutama jika tidak dienkripsi dengan benar. Cookies dapat disalahgunakan untuk serangan cross-site scripting (XSS) atau session hijacking jika tidak dikelola dengan baik. Oleh karena itu, penting untuk menggunakan cookie secure dan httpOnly agar hanya dapat diakses oleh server.

**Jelaskan bagaimana cara mengimplementasikan checklist di atas secara step-by-step**
1) Menambahkan import UserCreationForm dan messages pada file views.py dan menambahkan fungsi register untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.
2) Membuat berkas baru dengan nama register.html pada direktori main, lalu mengimpor fungsi register yang sudah dibuat pada urls.py, setelah itu menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor.
3) Menambahkan import authenticate, login, dan AuthenticationForm pada file views.py dan menambahkan fungsi login_user untuk mengautentikasi pengguna yang ingin login, lalu membuat berkas login.html serta mengimpor fungsi login_user dan menambahkan fungsi login_user ke path url.
4) Menambahkan import logout pada views.py dan menambahkan fungsi logout_user untuk melakukan mekanisme logout. Menambahkan "logout" button di bawah "add new product entry" button pada berkas main.html, lalu mengimpor fungsi logout_user pada urls.py dan menambahkan fungsinya pada path url.
5) Menambahkan import login_required pada views.py dan menambahkan potongan kode "@login_required(login_url='/login')" agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).
6) Melakukan logout terlebih dahulu, setelah itu menambahkan import HttpResponseRedirect, reverse, dan datetime pada views.py.
7) Pada fungsi login_user, menambahkan fungsionalitas dengan menambahkan cookie yang bernama last_login untuk melihat kapan terakhir kali pengguna melakukan login. Pada fungsi show_main menambahkan potongan kode "'last_login': request.COOKIES['last_login']" berfungsi menambahkan informasi cookie last_login pada response yang akan ditampilkan di halaman web. Setelah itu, menambahkan tombol logout untuk menampilkan data last login.
8) Mengimpor model user pada models.py dan mengubah value dari product_entries pada fungsi show_main menjadi "producr_entries = ProductEntry.objects.filter(user=request.user)" dan mengubah value dari name pada fungsi show_main menjadi "request.user.username"   
9) Menambahkan import os pada berkas settings.py dan mengganti variabel DEBUG dari berkas settings.py menjadi : 
PRODUCTION = os.getenv("PRODUCTION", False) dan DEBUG = not PRODUCTION
</ol>
</details>

<details>
<summary>Tugas 5</summary>
<p><strong>**Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**</strong></p>
<ol>
Ketika terdapat beberapa CSS selector yang diterapkan pada elemen HTML yang sama, urutan prioritas CSS ditentukan oleh specificity (ketepatan seleksi) dari setiap selector. Berikut adalah urutan prioritasnya dari yang tertinggi hingga terendah:
1) Inline Styles: Gaya yang langsung ditambahkan pada elemen menggunakan atribut style="" memiliki prioritas tertinggi.
2) ID Selector: Selector yang menggunakan format #id_name akan diterapkan setelah inline styles jika ada, karena ID bersifat unik dan memiliki nilai specificity yang tinggi.
3) Class Selector, Attribute Selector, dan Pseudo-class Selector: Selector yang menggunakan .class_name atau format [attribute=value] serta pseudo-class seperti :hover berada pada tingkat berikutnya dalam urutan prioritas.
4) Element Selector: Selector yang hanya memilih berdasarkan elemen HTML seperti div, p, h1, dll. memiliki prioritas terendah.
5) Browser Default Styles: Gaya bawaan browser akan diterapkan paling terakhir jika tidak ada style lain yang mendefinisikan elemen tersebut.
Jika terdapat beberapa selector dengan tingkat prioritas yang sama, maka CSS yang muncul paling akhir dalam file akan diterapkan. Hal ini disebut dengan cascading.


**Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**
Responsive design adalah konsep penting karena pengguna mengakses web dari berbagai perangkat dengan ukuran layar yang berbeda, seperti desktop, tablet, dan ponsel pintar. Oleh karena itu, desain web harus dapat menyesuaikan tampilannya agar konten dapat dibaca dan elemen dapat digunakan dengan nyaman di semua perangkat.
Contoh:
Aplikasi yang Sudah Menerapkan Responsive Design :
- Twitter: Menggunakan layout yang fleksibel dan mengubah tampilan berdasarkan lebar layar. Pada layar kecil, sidebar akan disembunyikan dan menu navigasi berubah menjadi ikon-ikon.
Aplikasi yang Belum Menerapkan Responsive Design :
- Craigslist: Dirancang untuk tampilan desktop dan ketika diakses pada layar kecil (seperti ponsel), tampilan menjadi terpotong dan font terlalu kecil.


**Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**
### Margin : Ruang kosong di luar border yang memisahkan elemen dari elemen lainnya di halaman web. Margin digunakan untuk memberi jarak antar elemen. Sintaks CSS:

```css
element {
    margin: 27px; /* Semua sisi (atas, kanan, bawah, kiri) */
    margin-top: 17px;  /* Margin atas */
    margin-bottom: 17px; /* Margin bawah */
    margin-right: 22px; /* Margin kanan */
    margin-left: 23px;  /* Margin kiri */
}
```

Border: Garis yang mengelilingi elemen di antara margin dan padding. Border digunakan untuk membingkai elemen dengan gaya tertentu. Sintaks CSS:

```css
element {
    border-style: groove; /* Gaya border menjadi groove */
    border-color: blue; /* Warna border biru */
    border: 4px solid black; /* Border hitam dengan ketebalan 4px */
    border-width: 6px; /* Lebar border 6px */
}
```

Padding: Ruang kosong di dalam elemen yang memisahkan konten dari border. Padding digunakan untuk memberi jarak antara isi elemen (teks atau gambar) dengan tepi elemen. Sintaks CSS:

```css
element {
    padding: 18px; /* Semua sisi (atas, kanan, bawah, kiri) */
    padding-top: 13px; /* Padding atas */
    padding-bottom: 13px; /* Padding bawah */
    padding-right: 16px; /* Padding kanan */
    padding-left: 16px; /* Padding kiri */
}
```

Contoh implementasi gabungan margin, border, dan padding : 
```css
.box {
    width: 220px;
    margin: 50px; /* Memberikan jarak di luar elemen */
    border: 10px solid red; /* Border merah 10px di sekitar elemen */
    padding: 40px;        /* Memberikan jarak di dalam elemen */
}
```

**Jelaskan konsep flex box dan grid layout beserta kegunaannya!**
### Flexbox: Flexbox (Flexible Box) adalah modul tata letak CSS yang dirancang untuk mengatur elemen dalam satu dimensi, baik secara horizontal (baris) maupun vertikal (kolom). Flexbox memudahkan pengaturan tata letak elemen seperti perataan (alignment), distribusi ruang, dan ukuran elemen di dalam container.

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

Flexbox cocok digunakan untuk membuat layout yang membutuhkan tata letak elemen dalam satu baris atau kolom, seperti navbar, tombol di dalam card, atau daftar produk.

Grid Layout: Grid Layout adalah modul CSS yang digunakan untuk mengatur elemen dalam dua dimensi (baris dan kolom). Dengan grid, kita dapat dengan mudah mendefinisikan area pada halaman, menentukan ukuran kolom dan baris, serta mengatur elemen-elemen agar mengisi tata letak secara responsif.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 10px;
}
```

Grid Layout lebih cocok untuk membuat tata letak kompleks yang melibatkan pengaturan posisi elemen di dalam baris dan kolom, seperti tata letak dashboard, galeri gambar, atau struktur halaman yang kompleks.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step**
1) Menambah tailwind ke aplikasi dan menambahkan tag <meta name="viewport"> agar halaman web  dpat menyesuaikan ukuran.
2) Pada views.py buat fungsi baru edit_product dan tambahkan import pada file dan membuat berkas HTML baru dengan nama edit_product.html, lalu import fungsi edit_product dan tambahkan path urlnya ke urlpatterns, setelah itu tambah button edit product.
3) Membuat fungsi baru dengan nama delete_product dan import fungsinya serta menambahkan path url ke dalam url patterns dan menambah button hapus di main.html.
4) Menambah navigation bar dengan membuat berkas navbar.html, kemudian menautkan navbar tersebut ke dalam main.html, create_product_entry.html, dan edit_product.html.
5) Menambah middleware WhiteNoise dan variabel STATIC_ROOT, STATICFILES_DIRS, dan STATIC_URL dikonfigurasikan.
6) Menghubungkan global.css dan script Tailwind ke base.html serta menambahkan custom styling ke global.css. Lalu styling halaman login, halaman register sesuai keinginan, serta halaman home. Setelah itu styling halaman create product entry dan styling untuk halaman edit product.
</details>


<details>
<summary>Tugas 6</summary>

**Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!**

JavaScript memiliki peran penting dalam pengembangan aplikasi web modern karena kemampuannya untuk memberikan interaktivitas yang dinamis pada halaman web. Beberapa manfaat utama penggunaan JavaScript adalah:
1. Meningkatkan Interaktivitas 
JavaScript memungkinkan halaman web untuk merespons tindakan pengguna secara real-time tanpa harus memuat ulang seluruh halaman, misalnya menampilkan notifikasi, validasi form, atau memperbarui konten halaman secara dinamis.
2. Manipulasi DOM
JavaScript memungkinkan manipulasi elemen HTML (Document Object Model) secara langsung, seperti mengubah CSS, menambah atau menghapus elemen, serta memodifikasi atribut HTML.
3. Kemampuan Asinkronus dengan AJAX
JavaScript dapat mengirim dan menerima data dari server tanpa harus me-reload halaman, memungkinkan pembuatan aplikasi single-page yang lebih responsif dan cepat.
4. Pemrosesan Client-Side
JavaScript dapat menangani logika bisnis sederhana di sisi pengguna, sehingga dapat mengurangi beban pada server dan mempercepat waktu respons.
5. Kompatibilitas Cross-Browser
JavaScript berjalan pada hampir semua peramban modern, sehingga kompatibilitasnya baik untuk berbagai platform web.

**Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?**

Await digunakan untuk menunggu hasil dari pemanggilan fetch() yang berbasis Promise. fetch() secara default bersifat asinkron, yang berarti akan mengembalikan Promise yang belum terisi dengan data (pending) saat pemanggilan pertama kali. Dengan await, kita bisa menunggu hingga permintaan (request) tersebut selesai dan mendapatkan respons dari server sebelum melanjutkan eksekusi baris kode berikutnya.
Jika wait tidak digunakan, kode akan mengeksekusi baris selanjutnya secara langsung tanpa menunggu hasil dari fetch(), sehingga variabel yang dimaksud untuk menyimpan hasil respons akan berisi undefined. Hal ini menyebabkan kemungkinan error ketika mencoba mengakses data respons yang belum tersedia (karena proses belum selesai).

**Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?**

Decorator csrf_exempt digunakan untuk menonaktifkan pemeriksaan Cross-Site Request Forgery (CSRF) pada view tertentu. Django secara default menerapkan pemeriksaan CSRF untuk semua permintaan POST, PUT, dan DELETE guna mencegah serangan CSRF. Namun, pada saat mengimplementasikan AJAX POST request yang tidak mengirimkan token CSRF (misalnya permintaan yang dikirim dari sumber eksternal atau dengan kode JavaScript yang tidak menyertakan token CSRF), permintaan tersebut akan ditolak oleh Django. Dengan menambahkan @csrf_exempt, kita memberitahu Django bahwa view tersebut tidak perlu melakukan pemeriksaan token CSRF pada permintaan tersebut.

**Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?**

Pembersihan data input pengguna di backend sangat penting meskipun kita telah melakukan validasi dan pembersihan di frontend, karena beberapa hal berikut :
1. Keamanan
   Validasi dan pembersihan di frontend mudah diabaikan oleh pengguna yang jahat. Mereka bisa memodifikasi data melalui alat seperti DevTools di browser, mengirimkan permintaan langsung menggunakan curl, atau menggunakan alat debugging lainnya. Oleh karena itu, backend harus tetap memverifikasi semua data yang diterima.
2. Integritas Data
   Backend bertanggung jawab untuk menjaga integritas dan keamanan seluruh sistem, termasuk database. Jika hanya mengandalkan pembersihan di frontend, maka data "kotor" masih bisa masuk ke server jika frontend dilewati atau dimanipulasi.
3. Trust Boundary
   Frontend dijalankan di sisi klien, yang berarti siapa pun bisa mengubah atau melewati kode di sana. Backend adalah satu-satunya tempat di mana kita bisa mempercayai bahwa kode tersebut tidak akan diubah oleh pengguna.
Dengan melakukan pembersihan di backend, kita memastikan bahwa semua data yang masuk ke dalam aplikasi telah melalui validasi yang benar dan aman. Pembersihan data di frontend hanya digunakan untuk memberikan pengalaman pengguna yang lebih baik (misalnya memberikan umpan balik langsung).


**Jelaskan bagaimana cara kamu mengimplementasikan checklist secara step-by-step**
1. Pertama-tama memberikan conditional view pada login_user untuk menempelkan pesan error kepada request yang mengirimkan permintaan login, seperti berikut :
```css 
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
else:
    messages.error(request, "Invalid username or password. Please try again.")
```
2. Membuat fungsi untuk menambahkan product dengan AJAX pada views.py dan menambahkan fungsi tersebut pada routing, seperti berikut :
```css
@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    product = request.POST.get("product")
    feelings = request.POST.get("feelings")
    product_intensity = request.POST.get("product_intensity")
    user = request.user

    new_product = productEntry(
        product=product, feelings=feelings,
        product_intensity=product_intensity,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201) 
```
3. Menampilkan Data Mood Entry dengan fetch() API (termasuk membuat fungsi baru getProductEntries dan refreshProductEntries) serta menghapus block conditional pada mood_entries untuk menampilkan card_mood ketika kosong atau tidak.
4. Mengimplementasikan tailwind pada website dan menambahkan fungsi javascript showModal dan hideModal, serta menambahkan tombol baru untuk melakukan penambahan data dengan AJAX.
5. Membuat fungsi addProductEntry dan menambahkan event listener pada form yang ada di modal untuk menjalankan fungsi tersebut.
6. Mencoba menambahkan data name baru dengan field name sebagai berikut : 
```css
<img src=x onerror="alert('XSS!');">
```
pastikan ketika melakukan penyimpanan mendapat alert dengan nilai XSS!

7. Menambahkan strip_tags untuk membersihkan data baru dengan menggunakan fungsi strip_tags pada setiap data yang mau diinput, serta menambahkan method clean yang merujuk pada setiap data.

8. Membersihkan data dengan DOMPurify dengan menambahkan potongan kode berikut pada block meta di berkas main.html : 
```css
<script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>
```

9. Terakhir pada fungsi refreshProductEntries tambahkan potongan kode berikut : 
```css
const mood = DOMPurify.sanitize(item.fields.mood);
const feelings = DOMPurify.sanitize(item.fields.feelings);
```

