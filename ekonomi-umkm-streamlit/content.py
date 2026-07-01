# -*- coding: utf-8 -*-
"""
Materi pembelajaran Ekonomi UMKM.
Berisi 14 pertemuan: materi Baca lengkap, kuis, dan jenis simulasi.
Sumber: RPS Ekonomi UMKM, Prodi S1 Manajemen, FEB Universitas Muhammadiyah Metro.
Dosen: Ardiansyah Japlani, S.E., M.B.A.
"""

PROF = {
    "shiddiq": {"ic": "🕊️", "nm": "Shiddiq", "desc": "Jujur dalam data, promosi, dan laporan"},
    "amanah": {"ic": "🤝", "nm": "Amanah", "desc": "Dapat dipercaya mengelola uang dan janji usaha"},
    "fathonah": {"ic": "💡", "nm": "Fathonah", "desc": "Cerdas menganalisis dan mengambil keputusan"},
    "tabligh": {"ic": "📣", "nm": "Tabligh", "desc": "Mampu menyampaikan dan mempresentasikan"},
}

CPMK = {
    1: "Konsep, karakteristik, dan peran UMKM dalam perekonomian nasional",
    2: "Lingkungan bisnis, regulasi, dan ekosistem UMKM di Indonesia",
    3: "Manajemen usaha, keuangan, pemasaran, dan SDM UMKM",
    4: "Strategi pengembangan, inovasi, dan digitalisasi UMKM",
}

PERTEMUAN = [
    {
        "id": 1, "cpmk": 1, "prof": "fathonah",
        "judul": "Konsep, Definisi & Klasifikasi UMKM",
        "sub": "Sub-CPMK 1 · Mampu menjelaskan konsep, definisi, dan klasifikasi UMKM",
        "ayat": "QS Al-Jumuah: 10", "ayat_note": False,
        "ayat_text": "Apabila telah ditunaikan salat, bertebaranlah kamu di muka bumi dan carilah karunia Allah. Bekerja dan berwirausaha adalah bagian dari ibadah.",
        "baca": """
### Apa itu UMKM?

UMKM adalah singkatan dari Usaha Mikro, Kecil, dan Menengah. Inilah tulang punggung
ekonomi Indonesia: usaha yang dijalankan perorangan atau badan usaha kecil, mulai dari
warung kopi, penjahit, toko kelontong, sampai produsen makanan rumahan.

**Dasar hukum.** Definisi resmi UMKM diatur dalam **UU No. 20 Tahun 2008**, lalu
disempurnakan kriterianya dalam **PP No. 7 Tahun 2021**. Pemerintah menggolongkan UMKM
berdasarkan dua hal: modal usaha (di luar tanah dan bangunan) atau hasil penjualan
tahunan (omzet).

**Kriteria terbaru (PP No. 7 Tahun 2021), berdasarkan modal usaha:**
- Usaha Mikro: modal sampai dengan Rp1 miliar
- Usaha Kecil: modal lebih dari Rp1 miliar sampai Rp5 miliar
- Usaha Menengah: modal lebih dari Rp5 miliar sampai Rp10 miliar

**Berdasarkan hasil penjualan tahunan (omzet):**
- Usaha Mikro: sampai Rp2 miliar
- Usaha Kecil: lebih dari Rp2 miliar sampai Rp15 miliar
- Usaha Menengah: lebih dari Rp15 miliar sampai Rp50 miliar

**Beda UMKM dengan perusahaan besar.** UMKM biasanya lebih lincah dan dekat dengan
pelanggan, tetapi modalnya terbatas dan manajemennya sering masih sederhana. Perusahaan
besar punya modal kuat dan sistem rapi, tetapi lebih lambat beradaptasi.

**Tipologi UMKM di Indonesia** sangat beragam: dari usaha bertahan hidup (survival),
usaha mikro keluarga, sampai usaha yang berorientasi pertumbuhan. Jumlah UMKM nasional
terus tumbuh dan mencakup lebih dari 90 persen unit usaha di Indonesia.

> Nilai profetik (Fathonah): seorang wirausaha yang cerdas paham betul di kelas mana
> usahanya berada, agar bisa memilih strategi dan bantuan yang tepat.
""",
        "kuis": [
            {"q": "UMKM di Indonesia pertama kali diatur secara khusus dalam undang-undang nomor berapa?",
             "o": ["UU No. 20 Tahun 2008", "UU No. 11 Tahun 2020", "UU No. 40 Tahun 2007"], "a": 0},
            {"q": "Dua dasar penggolongan UMKM menurut peraturan adalah...",
             "o": ["Warna dan logo", "Modal usaha atau omzet tahunan", "Jumlah karyawan dan media sosial"], "a": 1},
            {"q": "Peraturan yang memperbarui kriteria UMKM adalah...",
             "o": ["PP No. 7 Tahun 2021", "Perpres No. 2 Tahun 2015", "Permendag No. 50"], "a": 0},
            {"q": "Keunggulan khas UMKM dibanding perusahaan besar adalah...",
             "o": ["Modal sangat besar", "Lincah dan dekat dengan pelanggan", "Sistem yang sangat birokratis"], "a": 1},
        ],
        "sim": "klasifikasi",
    },
    {
        "id": 2, "cpmk": 1, "prof": "tabligh",
        "judul": "Peran & Kontribusi UMKM",
        "sub": "Sub-CPMK 2 · Mampu menjelaskan peran dan kontribusi UMKM terhadap perekonomian nasional",
        "ayat": "QS As-Shaf: 4", "ayat_note": False,
        "ayat_text": "Allah menyukai orang yang berjuang di jalan-Nya dalam barisan yang teratur dan kokoh. UMKM yang terorganisir menjadi kekuatan ekonomi bangsa.",
        "baca": """
### Kenapa UMKM begitu penting?

UMKM bukan sekadar usaha kecil. Secara nasional, UMKM adalah penyumbang terbesar bagi
perekonomian Indonesia.

**Kontribusi terhadap PDB.** UMKM menyumbang sekitar 60 persen dari Produk Domestik
Bruto (PDB) Indonesia. Artinya, lebih dari separuh roda ekonomi negara digerakkan oleh
usaha-usaha kecil dan menengah.

**Penyerapan tenaga kerja.** UMKM menyerap sekitar 97 persen dari total tenaga kerja
nasional. Inilah alasan UMKM disebut sebagai bantalan sosial: ketika krisis melanda,
UMKM yang paling banyak menampung lapangan kerja.

**Peran dalam ekspor non-migas.** Walau kontribusinya masih bisa ditingkatkan, UMKM
mulai menembus pasar ekspor lewat produk kerajinan, makanan olahan, fesyen, dan kopi.

**Penggerak ekonomi kerakyatan.** UMKM menyebarkan kegiatan ekonomi sampai ke desa dan
pelosok, sehingga pertumbuhan tidak hanya menumpuk di kota besar.

**Perbandingan Asia Tenggara.** Di hampir seluruh negara ASEAN, UMKM juga mendominasi
jumlah unit usaha. Yang membedakan tingkat kemajuan adalah seberapa baik UMKM didukung
teknologi, pembiayaan, dan akses pasar.

> Nilai profetik (Tabligh): memahami peran UMKM membuat kita mampu menyampaikan dan
> meyakinkan orang lain bahwa membangun UMKM berarti membangun bangsa.
""",
        "kuis": [
            {"q": "UMKM menyumbang sekitar berapa persen terhadap PDB Indonesia?",
             "o": ["Sekitar 10 persen", "Sekitar 60 persen", "Sekitar 95 persen"], "a": 1},
            {"q": "UMKM disebut bantalan sosial terutama karena...",
             "o": ["Menyerap sangat banyak tenaga kerja", "Membayar pajak paling besar", "Memiliki gedung megah"], "a": 0},
            {"q": "Salah satu produk UMKM yang menembus pasar ekspor adalah...",
             "o": ["Reaktor nuklir", "Kopi dan kerajinan", "Pesawat terbang"], "a": 1},
        ],
        "sim": "freeform",
    },
    {
        "id": 3, "cpmk": 1, "prof": "fathonah",
        "judul": "Karakteristik & Permasalahan UMKM",
        "sub": "Sub-CPMK 3 · Mampu menerapkan pemahaman tentang karakteristik dan permasalahan UMKM",
        "ayat": "QS Al-Kahfi: 22", "ayat_note": False,
        "ayat_text": "Janganlah berdebat tentang hal yang tidak kamu kuasai. Dalam bisnis, keputusan harus berdasar data, bukan kira-kira.",
        "baca": """
### Mengenali wajah asli UMKM

**Keunggulan UMKM:** fleksibel, cepat mengambil keputusan, dekat dengan pelanggan,
modal awal relatif kecil, dan mampu mengisi ceruk pasar yang diabaikan usaha besar.

**Kelemahan UMKM:** modal terbatas, manajemen sering bercampur dengan urusan keluarga,
catatan keuangan belum rapi, dan teknologi masih sederhana.

**Lima masalah klasik UMKM:**
1. Akses modal dan pembiayaan yang terbatas, karena banyak UMKM belum bankable.
2. Hambatan SDM dan teknologi, misalnya belum melek digital.
3. Isu legalitas dan formalitas, banyak UMKM belum punya NIB atau izin usaha.
4. Pemasaran yang masih sempit, mengandalkan pelanggan sekitar saja.
5. Pencatatan keuangan yang lemah, sehingga sulit menilai untung atau rugi.

**Studi kasus lokal.** Banyak UMKM kuliner ramai pembeli tetapi tetap sulit berkembang
karena pemiliknya tidak memisahkan uang usaha dan uang pribadi, lalu kehabisan modal
untuk membeli bahan baku keesokan harinya.

> Nilai profetik (Fathonah): wirausaha cerdas tidak menebak masalahnya, melainkan
> memetakan akar persoalan agar solusinya tepat sasaran.
""",
        "kuis": [
            {"q": "Hambatan paling klasik yang dihadapi UMKM adalah...",
             "o": ["Terlalu banyak modal", "Akses pembiayaan terbatas", "Kelebihan tenaga ahli"], "a": 1},
            {"q": "Istilah 'belum bankable' berarti UMKM...",
             "o": ["Sudah punya banyak rekening", "Belum memenuhi syarat untuk dapat kredit bank", "Menolak menabung"], "a": 1},
            {"q": "Salah satu isu legalitas UMKM adalah...",
             "o": ["Belum memiliki NIB atau izin usaha", "Punya terlalu banyak izin", "Logo terlalu bagus"], "a": 0},
        ],
        "sim": "freeform",
    },
    {
        "id": 4, "cpmk": 2, "prof": "amanah",
        "judul": "Regulasi, Kebijakan & Ekosistem UMKM",
        "sub": "Sub-CPMK 4 · Mampu menjelaskan regulasi, kebijakan pemerintah, dan ekosistem pendukung UMKM",
        "ayat": "QS Al-Fatir: 1", "ayat_note": False,
        "ayat_text": "Segala puji bagi Allah yang menciptakan dengan keteraturan. Mematuhi regulasi usaha adalah bentuk keteraturan dan amanah.",
        "baca": """
### Aturan main dan siapa saja pendukung UMKM

**Payung hukum.** Selain UU No. 20 Tahun 2008, ada UU Cipta Kerja yang mempermudah
perizinan UMKM lewat sistem **OSS (Online Single Submission)** dan penerbitan **NIB
(Nomor Induk Berusaha)** secara online dan gratis.

**Program pembiayaan dan bantuan:**
- **KUR (Kredit Usaha Rakyat):** kredit dengan bunga subsidi pemerintah.
- **BPUM:** bantuan modal langsung untuk usaha mikro pada masa pemulihan.
- Berbagai program pelatihan dan pendampingan dari Kemenkop UKM.

**Pemain ekosistem:**
- **OJK** mengawasi lembaga jasa keuangan, termasuk pembiayaan UMKM.
- **Bank Indonesia** menjaga stabilitas dan mendorong UMKM lewat klaster.
- **Kemenkop UKM** membina koperasi dan UMKM.
- **Inkubator dan akselerator bisnis** membantu UMKM tumbuh lebih cepat.

> Nilai profetik (Amanah): mengurus izin dan mengikuti aturan bukan beban, melainkan
> wujud amanah agar usaha berjalan jujur, aman, dan dipercaya.
""",
        "kuis": [
            {"q": "Sistem perizinan usaha online di Indonesia disebut...",
             "o": ["OSS", "ATM", "GPS"], "a": 0},
            {"q": "Lembaga yang mengawasi sektor jasa keuangan termasuk pembiayaan UMKM adalah...",
             "o": ["OJK", "BMKG", "KPU"], "a": 0},
            {"q": "NIB adalah singkatan dari...",
             "o": ["Nomor Induk Berusaha", "Nilai Investasi Bisnis", "Nota Izin Bangunan"], "a": 0},
        ],
        "sim": "freeform",
    },
    {
        "id": 5, "cpmk": 2, "prof": "fathonah",
        "judul": "Model Bisnis & Kewirausahaan",
        "sub": "Sub-CPMK 5 · Mampu menjelaskan model bisnis dan kewirausahaan dalam UMKM",
        "ayat": "QS Al-An'am: 160", "ayat_note": False,
        "ayat_text": "Kebaikan akan dibalas berlipat ganda. Memberi nilai lebih kepada pelanggan adalah inti model bisnis yang sehat.",
        "baca": """
### Merancang model bisnis yang masuk akal

**Business Model Canvas (BMC)** adalah peta satu halaman untuk merancang bisnis. Ada
9 blok, tetapi 4 yang paling inti untuk UMKM pemula:
1. **Customer Segments:** siapa pelangganmu.
2. **Value Proposition:** nilai atau keunggulan yang kamu tawarkan.
3. **Revenue Streams:** dari mana uang masuk.
4. **Cost Structure:** biaya terbesarmu.

**Value proposition** adalah jawaban atas pertanyaan: kenapa orang harus beli darimu,
bukan dari pesaing? Bisa karena lebih murah, lebih cepat, lebih enak, atau lebih dekat.

**Lean startup dan MVP.** Daripada langsung modal besar, uji dulu ide dengan **MVP
(Minimum Viable Product)**, yaitu versi paling sederhana dari produk untuk melihat
apakah pasar suka. Contoh: jual 20 porsi dulu sebelum buka kedai permanen.

**Wirausaha mandiri vs UMKM formal.** Wirausaha mandiri sering belum berbadan hukum,
sedangkan UMKM formal sudah punya legalitas sehingga lebih mudah mengakses pembiayaan
dan pasar yang lebih besar.

> Nilai profetik (Fathonah): merancang model bisnis adalah berpikir cerdas sebelum
> bertindak, agar usaha tidak sekadar ikut-ikutan tren.
""",
        "kuis": [
            {"q": "Alat satu halaman untuk merancang model bisnis disebut...",
             "o": ["Business Model Canvas", "Kartu nama", "Struk belanja"], "a": 0},
            {"q": "MVP (Minimum Viable Product) berguna untuk...",
             "o": ["Menguji ide dengan modal kecil dulu", "Langsung membuka 10 cabang", "Menghindari pelanggan"], "a": 0},
            {"q": "Value proposition menjawab pertanyaan...",
             "o": ["Kenapa orang harus membeli darimu", "Berapa nomor teleponmu", "Apa warna kemasanmu"], "a": 0},
        ],
        "sim": "bmc",
    },
    {
        "id": 6, "cpmk": 3, "prof": "amanah",
        "judul": "Manajemen Keuangan Sederhana",
        "sub": "Sub-CPMK 6 · Mampu menjelaskan manajemen keuangan sederhana untuk UMKM",
        "ayat": "QS An-Nisa: 11", "ayat_note": False,
        "ayat_text": "Ayat tentang pembagian warisan yang teliti mengajarkan ketelitian mencatat hak dan kewajiban, termasuk dalam keuangan usaha.",
        "baca": """
### Uang usaha harus tercatat dan terpisah

**Pencatatan sederhana.** UMKM tidak perlu akuntansi rumit. Cukup catat tiga hal
secara disiplin: uang masuk, uang keluar, dan sisa kas. Bisa pakai buku tulis, Excel,
atau aplikasi seperti BukuKas dan Wave.

**Laporan laba rugi mini.** Rumus dasarnya:
Laba = Total Pendapatan − Total Biaya. Kalau hasilnya positif berarti untung, kalau
negatif berarti rugi.

**Manajemen kas harian.** Banyak UMKM tutup bukan karena rugi di atas kertas, tetapi
karena kehabisan kas untuk belanja bahan esok hari. Maka arus kas harus dijaga.

**Pemisahan keuangan pribadi dan usaha.** Ini aturan emas UMKM. Jika tercampur, pemilik
tidak akan pernah tahu usahanya benar-benar untung atau hanya terasa untung. Solusinya:
buat rekening usaha terpisah dan tetapkan gaji untuk diri sendiri.

> Nilai profetik (Amanah): mencatat keuangan apa adanya dan tidak mencampur uang usaha
> dengan uang pribadi adalah bentuk amanah dalam mengelola rezeki.
""",
        "kuis": [
            {"q": "Aturan emas keuangan UMKM adalah...",
             "o": ["Mencampur uang usaha dan pribadi", "Memisahkan uang usaha dan pribadi", "Tidak mencatat apa pun"], "a": 1},
            {"q": "Rumus laba yang benar adalah...",
             "o": ["Pendapatan − Biaya", "Pendapatan + Biaya", "Biaya − Modal"], "a": 0},
            {"q": "Banyak UMKM tutup karena...",
             "o": ["Kehabisan kas harian", "Terlalu banyak pelanggan", "Kelebihan tabungan"], "a": 0},
        ],
        "sim": "labarugi",
    },
    {
        "id": 7, "cpmk": 3, "prof": "amanah",
        "judul": "Perencanaan Keuangan & Akses Pembiayaan",
        "sub": "Sub-CPMK 7 · Mampu menerapkan perencanaan keuangan dan akses pembiayaan UMKM",
        "ayat": "QS Ali Imran: 59", "ayat_note": False,
        "ayat_text": "Ketelitian terhadap ketetapan mengajarkan kita jujur pada angka. Catat keuangan apa adanya dan pisahkan uang usaha dari pribadi.",
        "baca": """
### Merencanakan modal dan menilai kelayakan usaha

**Sumber pembiayaan UMKM:** modal sendiri, KUR, koperasi, P2P lending, crowdfunding,
dan modal ventura. Masing-masing punya syarat, biaya, dan risiko berbeda.

**KUR (Kredit Usaha Rakyat).** Kredit dengan bunga subsidi pemerintah untuk usaha
produktif dan layak. Plafon KUR Mikro mencapai puluhan juta rupiah. Catatan penting:
plafon dan suku bunga berubah tiap tahun, jadi selalu cek angka terbaru di sumber resmi
(kur.ekon.go.id).

**Syarat umum KUR:** usaha produktif dan layak, sudah berjalan beberapa bulan,
melengkapi identitas dan legalitas usaha (misalnya NIB).

**Analisis kelayakan dengan BEP (Break Even Point).** BEP adalah titik di mana
pendapatan sama dengan biaya, belum untung dan belum rugi. Rumusnya:
- Margin kontribusi per unit = Harga jual − Biaya variabel per unit
- BEP (unit) = Biaya tetap ÷ Margin kontribusi per unit
- BEP (rupiah) = BEP unit × Harga jual

Kalau penjualan sudah di atas BEP, usaha mulai untung dan lebih layak diberi pinjaman.

> Nilai profetik (Amanah): saat mengajukan pinjaman, tunjukkan catatan yang jujur.
> Amanah keuangan membangun kepercayaan pemberi modal.
""",
        "kuis": [
            {"q": "Rumus BEP dalam unit adalah...",
             "o": ["Biaya tetap ÷ margin kontribusi per unit", "Harga jual × jumlah unit", "Modal awal + utang"], "a": 0},
            {"q": "Harga jual Rp15.000 dan biaya variabel Rp6.000. Margin kontribusinya...",
             "o": ["Rp21.000", "Rp9.000", "Rp6.000"], "a": 1},
            {"q": "KUR ditujukan untuk...",
             "o": ["Usaha produktif dan layak", "Liburan keluarga", "Membeli barang mewah"], "a": 0},
            {"q": "Biaya tetap Rp4.500.000 dan margin kontribusi Rp9.000. BEP unitnya...",
             "o": ["300 unit", "500 unit", "900 unit"], "a": 1},
        ],
        "sim": "bep",
    },
    {
        "id": 8, "cpmk": 3, "prof": "shiddiq",
        "judul": "Strategi Pemasaran Konvensional",
        "sub": "Sub-CPMK 8 · Mampu menjelaskan strategi pemasaran konvensional dan digital untuk UMKM",
        "ayat": "Usulan: QS Al-Muthaffifin: 1-3", "ayat_note": True,
        "ayat_text": "Celakalah bagi orang yang curang dalam takaran. Pemasaran yang jujur, tidak melebih-lebihkan, adalah wujud Shiddiq.",
        "baca": """
### Dasar pemasaran yang membumi

**Marketing mix 4P** adalah kerangka klasik pemasaran:
1. **Product:** kualitas, kemasan, dan keunikan produk.
2. **Price:** strategi penetapan harga yang menutup biaya dan tetap bersaing.
3. **Place:** lokasi dan jalur distribusi agar produk mudah dijangkau.
4. **Promotion:** cara mengenalkan produk ke calon pelanggan.

**Penetapan harga.** Cara paling sederhana adalah cost-plus: hitung biaya per unit lalu
tambahkan margin keuntungan. Harga tidak boleh di bawah biaya, dan harus
mempertimbangkan harga pesaing serta daya beli pelanggan.

**Distribusi lokal.** UMKM bisa menjual langsung, lewat reseller, atau menitip di toko
dan warung sekitar.

**Promosi dari mulut ke mulut dan komunitas** sangat ampuh dan murah bagi UMKM.
Pelanggan yang puas adalah iklan berjalan.

**Branding sederhana:** nama yang mudah diingat, logo konsisten, dan kemasan rapi sudah
cukup membuat UMKM terlihat profesional.

> Nilai profetik (Shiddiq): promosi boleh menarik, tetapi tidak boleh menipu. Sebutkan
> keunggulan produk apa adanya.
""",
        "kuis": [
            {"q": "Empat unsur marketing mix klasik (4P) adalah...",
             "o": ["Product, Price, Place, Promotion", "Plan, Pray, Push, Profit", "People, Power, Phone, Photo"], "a": 0},
            {"q": "Strategi penetapan harga paling sederhana adalah...",
             "o": ["Cost-plus (biaya + margin)", "Asal murah", "Mengikuti suasana hati"], "a": 0},
            {"q": "Promosi yang murah dan ampuh bagi UMKM adalah...",
             "o": ["Iklan TV nasional", "Dari mulut ke mulut", "Baliho di luar negeri"], "a": 1},
        ],
        "sim": "harga",
    },
    {
        "id": 9, "cpmk": 3, "prof": "shiddiq",
        "judul": "Pemasaran Digital & E-Commerce",
        "sub": "Sub-CPMK 9 · Mampu menerapkan strategi pemasaran digital dan e-commerce untuk UMKM",
        "ayat": "Usulan: QS Al-Ahzab: 70", "ayat_note": True,
        "ayat_text": "Bertakwalah dan ucapkanlah perkataan yang benar. Konten dan iklan digital harus jujur, sesuai produk yang dijual.",
        "baca": """
### Menjual lewat layar

**Media sosial.** Instagram dan TikTok adalah etalase gratis bagi UMKM. Kuncinya konten
yang konsisten, visual menarik, dan cerita di balik produk.

**Marketplace.** Tokopedia, Shopee, dan sejenisnya memperluas jangkauan dari lokal jadi
nasional. Penting menjaga rating, kecepatan respons, dan kualitas foto produk.

**Google Business Profile** membantu UMKM lokal muncul di pencarian dan peta, sehingga
pelanggan sekitar mudah menemukan lokasi dan jam buka.

**Konten dan storytelling.** Orang membeli cerita, bukan sekadar barang. Ceritakan asal
bahan, proses pembuatan, atau kisah pemilik untuk membangun kedekatan.

**Analisis performa iklan.** Saat beriklan, ukur hasilnya. Dua metrik penting:
- **ROAS (Return on Ad Spend)** = pendapatan dari iklan ÷ biaya iklan.
- **CPA (Cost per Acquisition)** = biaya iklan ÷ jumlah pembeli baru.

Iklan disebut sehat jika menghasilkan lebih banyak daripada yang dikeluarkan.

> Nilai profetik (Shiddiq): foto dan klaim produk di dunia digital harus sesuai
> kenyataan. Jangan edit berlebihan hingga menipu pembeli.
""",
        "kuis": [
            {"q": "ROAS mengukur...",
             "o": ["Pendapatan dibanding biaya iklan", "Jumlah follower palsu", "Lama waktu tidur"], "a": 0},
            {"q": "Storytelling produk bertujuan untuk...",
             "o": ["Membohongi pembeli", "Membangun kedekatan dan kepercayaan", "Menaikkan harga diam-diam"], "a": 1},
            {"q": "Google Business Profile membantu UMKM agar...",
             "o": ["Muncul di pencarian dan peta lokal", "Menghapus pesaing", "Menghindari pajak"], "a": 0},
        ],
        "sim": "iklan",
    },
    {
        "id": 10, "cpmk": 3, "prof": "amanah",
        "judul": "Manajemen Produksi & Operasi",
        "sub": "Sub-CPMK 10 · Mampu menjelaskan manajemen produksi dan operasi dalam UMKM",
        "ayat": "Usulan: QS Al-Baqarah: 168", "ayat_note": True,
        "ayat_text": "Makan dan produksilah yang halal lagi baik. Menjaga kualitas dan kehalalan produk adalah amanah kepada konsumen.",
        "baca": """
### Memproduksi dengan rapi dan efisien

**Alur produksi.** Setiap UMKM punya alur dari bahan baku, proses, sampai produk jadi.
Memetakan alur ini membantu menemukan langkah yang boros waktu atau biaya.

**Manajemen persediaan sederhana.** Jangan terlalu banyak stok hingga bahan rusak, dan
jangan terlalu sedikit hingga kehabisan saat ada pesanan. Catat stok masuk dan keluar.

**Standar kualitas.** Produk yang kualitasnya konsisten membuat pelanggan kembali.
Tetapkan standar sederhana, misalnya takaran dan rasa yang sama setiap kali.

**Efisiensi biaya produksi** lewat **HPP (Harga Pokok Produksi)**. HPP adalah total
biaya untuk menghasilkan satu unit produk. Mengetahui HPP membuat penetapan harga jadi
tepat dan tidak rugi.

**Sertifikasi penting bagi UMKM:**
- **PIRT** untuk pangan olahan rumahan.
- **Sertifikat Halal** untuk meyakinkan konsumen muslim.
- **SNI** untuk standar mutu produk tertentu.

> Nilai profetik (Amanah): menjaga kualitas dan kehalalan adalah amanah kepada
> konsumen yang mempercayakan kesehatannya pada produk kita.
""",
        "kuis": [
            {"q": "Sertifikat untuk pangan olahan rumahan UMKM adalah...",
             "o": ["PIRT", "SIM", "NPWP"], "a": 0},
            {"q": "HPP adalah singkatan dari...",
             "o": ["Harga Pokok Produksi", "Harga Pasar Pesaing", "Hasil Penjualan Pribadi"], "a": 0},
            {"q": "Manajemen persediaan yang baik berarti...",
             "o": ["Stok pas, tidak berlebih dan tidak kurang", "Selalu stok sebanyak mungkin", "Tidak pernah mencatat stok"], "a": 0},
        ],
        "sim": "hpp",
    },
    {
        "id": 11, "cpmk": 3, "prof": "tabligh",
        "judul": "Manajemen SDM & Kapasitas Pelaku",
        "sub": "Sub-CPMK 11 · Mampu menerapkan manajemen SDM dan pengembangan kapasitas pelaku UMKM",
        "ayat": "Usulan: QS An-Nahl: 125", "ayat_note": True,
        "ayat_text": "Serulah ke jalan yang baik dengan hikmah dan nasihat yang baik. Membimbing dan memotivasi tim adalah bentuk Tabligh.",
        "baca": """
### Mengelola orang dalam usaha kecil

**Rekrutmen sederhana.** UMKM tidak butuh proses rumit, tetapi tetap perlu jelas mencari
orang dengan sikap baik dan mau belajar, bukan hanya yang murah.

**Pelatihan dan pengembangan.** Karyawan yang terampil membuat usaha lebih produktif.
Manfaatkan pelatihan gratis dari pemerintah dan komunitas.

**Budaya kerja dan motivasi.** Pada tim kecil, hubungan personal sangat berpengaruh.
Pemimpin yang adil, komunikatif, dan menghargai akan menumbuhkan loyalitas.

**Kompensasi dan insentif.** Selain gaji, insentif sederhana seperti bonus penjualan
bisa memotivasi tim. Yang penting adil dan transparan.

**Pengembangan kapasitas pelaku UMKM** lewat pelatihan kewirausahaan, pendampingan, dan
sertifikasi membuat pemilik usaha naik kelas bersama usahanya.

> Nilai profetik (Tabligh): pemimpin UMKM adalah penyampai nilai. Cara membimbing tim
> dengan baik akan tercermin pada cara tim melayani pelanggan.
""",
        "kuis": [
            {"q": "Cara meningkatkan kapasitas SDM UMKM antara lain...",
             "o": ["Membiarkan tanpa arahan", "Pelatihan dan pengembangan", "Memotong semua gaji"], "a": 1},
            {"q": "Pada tim kecil, faktor yang sangat berpengaruh adalah...",
             "o": ["Hubungan personal dan budaya kerja", "Jumlah lantai kantor", "Warna seragam"], "a": 0},
            {"q": "Insentif yang baik bersifat...",
             "o": ["Adil dan transparan", "Rahasia dan pilih kasih", "Tidak pernah diberikan"], "a": 0},
        ],
        "sim": "freeform",
    },
    {
        "id": 12, "cpmk": 4, "prof": "fathonah",
        "judul": "Inovasi Produk & Pengembangan",
        "sub": "Sub-CPMK 12 · Mampu menjelaskan inovasi produk dan strategi pengembangan UMKM",
        "ayat": "Usulan: QS Ar-Ra'd: 11", "ayat_note": True,
        "ayat_text": "Allah tidak mengubah keadaan suatu kaum hingga mereka mengubah diri mereka sendiri. Inovasi adalah ikhtiar mengubah keadaan usaha.",
        "baca": """
### Agar usaha tidak jalan di tempat

**Inovasi produk dan diversifikasi.** Inovasi tidak harus besar. Menambah varian rasa,
memperbaiki kemasan, atau membuat ukuran baru sudah termasuk inovasi yang menjaga minat
pelanggan.

**Design thinking.** Cara berpikir yang berpusat pada pelanggan: pahami kebutuhan
mereka, buat ide, bikin purwarupa, uji, lalu perbaiki. Cocok untuk mengembangkan produk
yang benar-benar dibutuhkan pasar.

**Scaling up.** Setelah model bisnis terbukti, usaha bisa diperbesar lewat tambahan
kapasitas, cabang, atau kemitraan. Yang penting sistem sudah rapi sebelum diperbesar.

**Kemitraan dan supply chain.** Bekerja sama dengan pemasok, distributor, atau UMKM lain
membuat usaha lebih kuat dan efisien.

**UMKM naik kelas.** Tujuannya bertumbuh dari mikro ke kecil, lalu ke menengah, dengan
manajemen, legalitas, dan pasar yang makin matang.

> Nilai profetik (Fathonah): inovasi lahir dari kecerdasan membaca kebutuhan zaman
> tanpa meninggalkan nilai dan kualitas.
""",
        "kuis": [
            {"q": "UMKM naik kelas berarti...",
             "o": ["Tutup usaha", "Bertumbuh dari mikro ke kecil ke menengah", "Pindah ke kota lain"], "a": 1},
            {"q": "Design thinking berpusat pada...",
             "o": ["Kebutuhan pelanggan", "Keinginan pemilik semata", "Harga pesaing"], "a": 0},
            {"q": "Contoh inovasi sederhana adalah...",
             "o": ["Menambah varian rasa dan memperbaiki kemasan", "Menaikkan harga tanpa alasan", "Mengurangi kualitas"], "a": 0},
        ],
        "sim": "freeform",
    },
    {
        "id": 13, "cpmk": 4, "prof": "tabligh",
        "judul": "Digitalisasi & UMKM Go Global",
        "sub": "Sub-CPMK 13 · Mampu menjelaskan digitalisasi, transformasi bisnis, dan UMKM go global",
        "ayat": "Usulan: QS Saba': 28", "ayat_note": True,
        "ayat_text": "Kami mengutusmu untuk seluruh umat manusia. UMKM go global adalah menyampaikan karya bangsa ke dunia.",
        "baca": """
### Dari warung ke pasar dunia

**Transformasi digital UMKM.** Digitalisasi bukan sekadar punya media sosial, tetapi
mengubah cara kerja: pencatatan digital, pembayaran QRIS, dan penjualan online.

**Teknologi pendukung:**
- **POS (Point of Sale)** untuk mencatat penjualan otomatis.
- **ERP mini** untuk mengelola stok, penjualan, dan keuangan dalam satu sistem.
- **Cloud** agar data aman dan bisa diakses dari mana saja.

**Peluang ekspor.** Produk Indonesia seperti kopi, rempah, kerajinan, dan fesyen
diminati pasar global. Tantangannya adalah standar mutu, kemasan, dan konsistensi
pasokan.

**Platform go global:** Export.id, marketplace internasional seperti Alibaba, dan
pameran dagang membantu UMKM menjangkau pembeli luar negeri.

**Studi kasus.** Banyak UMKM kopi dan kerajinan Indonesia kini rutin ekspor setelah
memperbaiki kemasan, sertifikasi, dan kemampuan berbahasa Inggris dalam negosiasi.

> Nilai profetik (Tabligh): membawa produk ke pasar global berarti menyampaikan karya
> dan nama baik bangsa kepada dunia.
""",
        "kuis": [
            {"q": "Salah satu platform untuk membantu UMKM ekspor adalah...",
             "o": ["Export.id", "Game online", "Aplikasi cuaca"], "a": 0},
            {"q": "POS (Point of Sale) berfungsi untuk...",
             "o": ["Mencatat penjualan otomatis", "Memesan tiket pesawat", "Mengedit foto"], "a": 0},
            {"q": "Tantangan utama UMKM go global adalah...",
             "o": ["Standar mutu, kemasan, dan konsistensi pasokan", "Terlalu banyak pembeli", "Tidak ada produk"], "a": 0},
        ],
        "sim": "freeform",
    },
    {
        "id": 14, "cpmk": 4, "prof": "tabligh",
        "judul": "Proposal Pengembangan UMKM Berbasis Riset",
        "sub": "Sub-CPMK 14 · Mampu merancang dan mempresentasikan proposal pengembangan UMKM berbasis riset",
        "ayat": "Usulan: QS Thaha: 25-28", "ayat_note": True,
        "ayat_text": "Doa Nabi Musa memohon kelapangan dada dan kefasihan lisan. Pitch yang baik butuh persiapan dan komunikasi yang jelas.",
        "baca": """
### Menutup semester dengan karya nyata

**Sistematika proposal pengembangan UMKM** umumnya berisi: profil UMKM, identifikasi
masalah, analisis kondisi, usulan strategi, rencana pelaksanaan, dan proyeksi hasil.

**Analisis SWOT.** Alat untuk memetakan kondisi usaha:
- **Strength (kekuatan):** keunggulan internal.
- **Weakness (kelemahan):** kekurangan internal.
- **Opportunity (peluang):** faktor luar yang menguntungkan.
- **Threat (ancaman):** faktor luar yang membahayakan.

**Rekomendasi berbasis data.** Usulan strategi harus berdasar temuan lapangan dan angka,
bukan asumsi. Inilah inti proyek akhir mata kuliah ini.

**Teknik presentasi proposal.** Susun alur yang jelas, gunakan visual sederhana, dan
latih penyampaian. Pesan inti harus tersampaikan dalam waktu singkat.

**Simulasi pitch.** Bayangkan menyampaikan proposal ke investor atau pembina dalam 60
detik. Sampaikan masalah, solusi, dan kebutuhan dana secara meyakinkan.

> Nilai profetik (Tabligh): proposal dan pitch yang baik adalah seni menyampaikan
> gagasan dengan jujur, jelas, dan meyakinkan.
""",
        "kuis": [
            {"q": "SWOT terdiri dari...",
             "o": ["Strength, Weakness, Opportunity, Threat", "Sale, Win, Open, Top", "Stok, Warna, Order, Toko"], "a": 0},
            {"q": "Rekomendasi dalam proposal sebaiknya berdasar...",
             "o": ["Data dan temuan lapangan", "Perasaan semata", "Tebakan"], "a": 0},
            {"q": "Inti dari pitch 60 detik adalah menyampaikan...",
             "o": ["Masalah, solusi, dan kebutuhan dana", "Riwayat hidup lengkap", "Daftar semua teman"], "a": 0},
        ],
        "sim": "swot",
    },
]


def get_pertemuan(pid):
    for p in PERTEMUAN:
        if p["id"] == pid:
            return p
    return None
