# Blueprint konten mingguan — Dasar AI & ML 2026–2027

Status: **rancangan desain untuk produksi bertahap**, 7 Oktober 2026. Belum merupakan materi siap ajar, RPS/RTM resmi, hasil eksekusi lab, atau bukti pelaksanaan kelas.
Dokumen ini menerjemahkan [rencana produksi](../PRODUCTION_PLAN.md) menjadi brief konten W01–W07 dan W09–W15 serta brief UTS W08 dan UAS W16.
Gunakan bersama [spesifikasi artefak](ARTIFACT_SPECS.md), [gerbang mutu](QUALITY_GATES.md), [playbook eksekusi](EXECUTION_PLAYBOOK.md), dan [template sesi](SESSION_TEMPLATES.md).

## Batas sumber dan keputusan desain

- **Baseline sumber:** judul minggu dan kode Sub-CPMK pada tabel berikut disalin dari sheet `Production_Backlog`, [SRC-WORKBOOK](<../references/MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx>). Kode dipertahankan persis; makna lengkap capaian belum diperiksa.
- **Usulan desain:** seluruh tujuan terukur, prasyarat, isi rinci, contoh, aktivitas, asesmen, dan adaptasi di bawah adalah usulan produksi. Jangan mengutipnya sebagai rumusan resmi RPS/RTM.
- ID `Wnn-LO01/02` adalah tujuan belajar sementara, bukan kode CPMK/Sub-CPMK resmi. `Wnn-EX01`, `Wnn-ASM01`, dan `Wnn-EV01` menghubungkan contoh, asesmen, serta bukti; UTS/UAS menggunakan prefiks ujian.
- S01 kurikulum, S02 RPS, dan S03 RTM pada sheet `Sources` belum dibaca isinya. Verifikasi rumusan outcome, kedalaman, bibliografi, bobot, tugas, waktu, dan kebijakan pada dokumen tersebut sebelum pengesahan.
- S04/S05 tracker IF24A/IF24H belum menjadi bukti mode, jadwal, durasi, atau kebutuhan akses kelas. S05 diberi peran "Hybrid class delivery tracker" di workbook; label itu tidak menetapkan kewajiban pertemuan aktual.
- Angka `Weight` backlog adalah kendali produksi artefak; jangan menafsirkannya sebagai bobot nilai mahasiswa. Tidak ada bobot akademik atau tanggal pelaksanaan yang ditetapkan di brief ini.
- [SRC-MASTER-PROMPT](../references/Master_Prompt_Package_Slide_Mata_Kuliah_Tri_Aji.md) menjadi referensi alur pedagogi. Jumlah slide ditentukan kebutuhan pesan, interaksi, dan durasi terverifikasi; jangan membuat 20 slide identik untuk setiap topik.
- Rencana lab menyatakan **apa yang harus dijalankan dan diperiksa saat produksi**, bukan bahwa contoh telah dijalankan. Nilai metrik, keluaran numerik, dan klaim performa baru boleh ditulis setelah run tercatat.

## Peta baseline, bab, dan dependensi belajar

| Paket | Topik baseline persis dari workbook | Sub-CPMK baseline persis | Bab / fungsi |
| --- | --- | --- | --- |
| W01 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | Bab 01: bahasa bersama dan masalah |
| W02 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | Bab 02: memahami data |
| W03 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | Bab 03: transformasi data |
| W04 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | Bab 04: rancangan evaluasi |
| W05 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | Bab 05: model klasifikasi awal |
| W06 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | Bab 06: target numerik |
| W07 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | Bab 07: pola tanpa label |
| W08 / UTS | UTS | DAIML-Sub-CPMK102-1 | Paket ujian; bukan bab 08 |
| W09 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | Bab 08: memilih model |
| W10 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | Bab 09: mengendalikan kompleksitas |
| W11 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | Bab 10: jaringan sederhana |
| W12 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | Bab 11: batas dan peluang |
| W13 | Responsible AI | DAIML-Sub-CPMK082-1 | Bab 12: keputusan bertanggung jawab |
| W14 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | Bab 13: integrasi dan reproduksi |
| W15 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | Bab 14: klinik dan komunikasi bukti |
| W16 / UAS | UAS | DAIML-Sub-CPMK082-1 | Paket ujian; bukan bab 16 |

Bab 01–14 mengikuti **minggu pembelajaran**, sehingga nomor bab berbeda dari nomor minggu setelah UTS. W15 tetap bab panduan klinik/presentasi; UTS dan UAS mempunyai tujuh artefak ujian masing-masing.
Jumlah 14 artefak per minggu pada backlog tidak berarti 14 konsep, 14 tugas, atau 14 sesi; satu rantai contoh dapat dipakai konsisten pada beberapa artefak.

| Dependensi kurikuler usulan | Hubungan yang perlu dipertahankan |
| --- | --- |
| W01 → W02 → W03 → W04 | Masalah/target → profil data → transformasi → pembatasan fit dan evaluasi |
| W04 → W05/W06/W07 | Pilih unit evaluasi dan batas data sebelum menilai model atau cluster |
| W05 + W04 → W09 → W10 | Kandidat model → pencarian dengan validasi → diagnosis generalisasi |
| W03 + W04 + W10 → W11 → W12 | Skala data dan loss → jaringan kecil → pengantar DL/GenAI |
| W01–W12 → W13 → W14 → W15 | Klaim yang dibatasi bukti → analisis dampak → paket reproduksi → presentasi |
| W01–W07 → UTS; W09–W15 + fondasi → UAS | Hubungan untuk rancangan soal; cakupan resmi tetap menunggu S02/S03 |

**Urutan produksi berbeda dari urutan belajar:** pilot W04 boleh diproduksi pertama karena prioritas workbook dan rencana produksi, tetapi mahasiswa tetap memerlukan W01–W03. Sebelum W04, buat bridge rancangan W01–W03 yang dapat ditelaah: glosarium fitur/label/unit observasi, membaca tabel dan missingness, serta kontrak `fit`/`transform`. Bridge tidak membuat paket W01–W03 dianggap selesai; audit/pengembangan penuhnya menyusul pilot.
Setelah pilot ditelaah, produksi W01–W03 → W05–W07/UTS → W09–W11 → W12–W15/UAS, lalu integrasi. Jika sumber resmi mengubah cakupan, revisi peta sebelum memperbanyak paket.

## Kontrak bersama untuk semua brief

- Pisahkan alur inti dan pengayaan; targetkan WHY → intuisi → konsep → contoh → praktik → refleksi. Akhiri aktivitas inti dengan bukti pemahaman yang dapat diperiksa.
- Contoh tabular memakai data kecil terbuka/bawaan atau sintetis berlabel, seed jika relevan, dan data dictionary. Dataset yang sama dapat diteruskan jika cocok; regresi/clustering/GenAI boleh memakai kasus lain dengan alasan tertulis.
- Simpan rencana input, kode, versi lingkungan, pemeriksaan perilaku, dan hasil run pada artefak contoh/lab ketika diproduksi. Hindari klaim "metode A selalu lebih baik" dari satu contoh.
- **Siklus test lintas minggu:** contoh/data pengembangan dan protokol split boleh digunakan ulang untuk menghubungkan materi. Test yang hasilnya sudah dibuka pada W04/W05 tidak boleh dipakai sebagai bukti evaluasi final baru setelah tuning W09/W10. Labeli set itu sebagai test pedagogis yang telah terekspos; untuk klaim generalisasi baru gunakan kasus/holdout independen yang didefinisikan dengan provenance, atau pertahankan holdout proyek yang belum tersentuh sampai kandidat/prosedur dipilih. Seed baru pada data yang sama tidak otomatis memulihkan independensi. Demonstrasi pembelajaran tidak menyatakan evaluasi proyek final sudah selesai.
- **Adaptasi berlaku terpisah untuk IF24A dan IF24H:** setelah mode/durasi diketahui, pilih fasilitasi langsung, diskusi jarak jauh, atau aktivitas mandiri berbukti; pertahankan tujuan serta kriteria yang sama. Nama kelas tidak menentukan pilihannya.
- Untuk sesi singkat, prioritaskan contoh inti dan exit ticket; pindahkan pengayaan ke bacaan. Untuk akses komputasi terbatas, sediakan tabel/trace tercatat dan worksheet yang tetap meminta alasan; run mandiri disediakan jika perangkat memungkinkan.
- Asesmen berikut adalah proposal formatif/luaran RTM, bukan tugas bernilai yang sudah diberlakukan. Rubrik menilai alasan, kebenaran langkah, dan batas klaim; nilai resmi dan ketentuan AI menunggu S02/S03.
- Evidence di sini adalah **spesifikasi kosong**. Jangan membuat nama mahasiswa, skor, log kelas, atau hasil refleksi seolah sudah terjadi. Kunci dan solusi tetap pada paket dosen.

## W01 — Pengantar AI dan Machine Learning

Baseline: **DAIML-Sub-CPMK082-1**; Bab 01. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W01-LO01` mengklasifikasikan kasus AI/ML, supervised/unsupervised, klasifikasi/regresi dengan alasan; `W01-LO02` merumuskan satu masalah berisi unit observasi, fitur yang tersedia saat prediksi, target, dan manfaat keputusan.
- **Prasyarat:** membaca tabel sederhana, logika kondisi, rata-rata dasar; lakukan diagnosis awal tanpa menganggap semua mahasiswa sudah memakai Python.
- **Konsep inti:** AI/ML sebagai pendekatan, training dan inference, fitur/label, data versus model, masalah prediksi, baseline, keberhasilan teknis versus manfaat pemakai.
- **Batas/pengayaan:** sejarah singkat sebagai konteks; tidak wajib katalog algoritma, pembuktian matematika, atau debat definisi AGI. Pengayaan: contoh aturan eksplisit versus model yang belajar.
- **Miskonsepsi:** semua otomatisasi adalah ML; label/target boleh memakai informasi setelah keputusan terjadi; model dengan skor tinggi otomatis bermanfaat bagi pemakai.
- **Contoh/lab `W01-EX01`:** triase beberapa kartu kasus sintetis; petakan fitur/target dan saat tersedianya data; bandingkan aturan sederhana dengan alur model tanpa klaim akurasi.
- **Verifikasi saat produksi:** pastikan setiap kartu memiliki jawaban beralasan dan alternatif yang sah; periksa tidak ada fitur masa depan terselip; starter Python opsional hanya memuat/memeriksa tabel kecil.
- **Asesmen `W01-ASM01`:** problem framing singkat dan koreksi satu kasus salah. **Evidence `W01-EV01`:** tabel kasus, alasan klasifikasi, problem statement, dan exit ticket fitur versus target.
- **Adaptasi IF24A/IF24H:** pilih diskusi kartu berpasangan atau anotasi mandiri plus komentar rekan sesuai mode aktual; format jawaban dan kriteria sama untuk kedua kelas.
- **Koherensi:** problem statement menjadi jangkar data dictionary W02, keputusan preprocessing W03, dan risiko W13; istilah pada semua artefak harus konsisten.
- **Cek S01/S02/S03:** rumusan outcome 082-1, definisi/prasyarat mata kuliah, kedalaman pengantar, serta apakah problem framing masuk RTM.

## W02 — Eksplorasi Data untuk ML

Baseline: **DAIML-Sub-CPMK102-1**; Bab 02. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W02-LO01` membuat profil tipe data, missingness, distribusi, dan dugaan duplikasi; `W02-LO02` membedakan observasi data dari hipotesis penyebab serta memilih pemeriksaan lanjutan.
- **Prasyarat:** W01 fitur/target/unit observasi; frekuensi, rata-rata/median, membaca grafik; bridge sintaks pemuatan dan inspeksi tabel jika Python baru.
- **Konsep inti:** data dictionary, unit dan rentang, statistik deskriptif, distribusi, outlier, ketidakseimbangan kelas, korelasi, kualitas data dan batas representasi.
- **Batas/pengayaan:** tidak wajib inferensi statistik formal atau dashboard interaktif. Pengayaan: segmentasi profil berdasarkan subkelompok bila data dan etika memungkinkan.
- **Miskonsepsi:** korelasi membuktikan sebab; outlier selalu salah dan harus dihapus; tabel tanpa nilai kosong otomatis bermutu baik.
- **Contoh/lab `W02-EX01`:** profil dataset kecil sintetis dengan nilai hilang, kategori, unit, dan duplikasi yang ditanam secara transparan; gunakan tabel dan grafik yang menjawab pertanyaan eksplisit.
- **Verifikasi saat produksi:** periksa jumlah baris/kolom, tipe, nilai hilang yang ditanam, definisi duplikasi, dan keterbacaan grafik; jangan mengarang pola yang tidak tampak pada hasil run.
- **Asesmen `W02-ASM01`:** memo audit data yang memisahkan temuan, dugaan, keputusan sementara, dan data tambahan. **Evidence `W02-EV01`:** profil, satu visual beranotasi, serta daftar risiko.
- **Adaptasi IF24A/IF24H:** fasilitasi membaca grafik bersama atau bagikan tabel/plot hasil run untuk anotasi mandiri; sediakan format teks aksesibel dan pertanyaan yang sama.
- **Koherensi:** keputusan W03 harus merujuk temuan W02; eksplorasi untuk pemilihan model nanti dibatasi pada data pengembangan, bukan test tersegel W04.
- **Cek S02/S03:** dataset resmi, alat yang diwajibkan, kedalaman statistik, bentuk dan luaran audit data.

## W03 — Preprocessing dan Feature Engineering

Baseline: **DAIML-Sub-CPMK102-1**; Bab 03. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W03-LO01` memilih transformasi berdasarkan tipe fitur dan model; `W03-LO02` menjelaskan mengapa parameter transformasi dipelajari dari training dan dipakai kembali pada data baru.
- **Prasyarat:** W01 fitur dan inference; W02 missingness/tipe/skala; operasi aritmetika sederhana. Jelaskan kontrak estimator sebelum mengandalkan sintaks library.
- **Konsep inti:** imputasi, encoding, scaling, feature engineering berbasis domain, kategori baru, `fit` versus `transform`, `ColumnTransformer`, pengantar `Pipeline` dan kebocoran data.
- **Batas/pengayaan:** hindari katalog seluruh encoder dan seleksi fitur tingkat lanjut. Pengayaan: fitur turunan yang memiliki alasan domain dan tersedia sebelum prediksi.
- **Miskonsepsi:** semua fitur numerik harus diskalakan untuk semua algoritma; kode kategori berurutan selalu mewakili jarak bermakna; imputasi/scaling seluruh data sebelum split aman.
- **Contoh/lab `W03-EX01`:** tabel mixed-type dengan nilai hilang dan kategori yang baru muncul pada batch berikutnya; bangun transformasi kolom, lalu bedakan proses belajar parameter dan penerapannya.
- **Verifikasi saat produksi:** periksa bentuk hasil, nilai hilang yang tersisa, penanganan kategori baru, dan parameter imputasi/scaling cocok dengan training saja; uji transformasi batch baru.
- **Asesmen `W03-ASM01`:** pilih dan pertanggungjawabkan transformasi, lalu tandai langkah yang perlu `fit`. **Evidence `W03-EV01`:** peta fitur–transformasi serta trace fit/transform.
- **Adaptasi IF24A/IF24H:** gunakan trace transformasi per baris dalam sesi langsung atau worksheet dengan potongan kode dan cek mandiri; kedua kelas memperlihatkan alasan yang sama.
- **Koherensi:** W03 mengenalkan batas `fit`; W04 menentukan split dan menempatkan transformasi di tiap fold. Jangan mengajarkan urutan preprocessing penuh → split sebagai prosedur benar.
- **Cek S02/S03:** feature engineering yang diminta, library resmi, cakupan tugas, dan apakah pipeline sudah termasuk pada minggu ini atau diperdalam W04.

## W04 — Pembagian Data dan Validasi: pilot produksi

Baseline: **DAIML-Sub-CPMK102-1**; Bab 04. Semua rincian berikut adalah usulan desain; pilot menguji pola 14 artefak, bukan mengubah urutan belajar mahasiswa.

- **Tujuan:** `W04-LO01` memilih strategi split/CV yang cocok dengan tujuan prediksi, unit independen, kelompok, dan waktu; `W04-LO02` mendeteksi leakage serta merancang pipeline yang melakukan fit hanya pada subset training yang tepat.
- **Luaran terukur:** satu diagram aliran data, matriks tiga skenario split, trace indeks fold, dan memo evaluasi yang membedakan pengembangan model dari estimasi final. Pemetaan resmi ke 102-1 menunggu S01/S02.
- **Prasyarat kurikuler:** W01 masalah/fitur/label/inference; W02 unit observasi, distribusi kelas, duplikasi; W03 transformasi dan parameter yang dipelajari. Model baseline hanya alat ukur, tidak memerlukan W05 selesai.
- **Bootstrap produksi sebelum menulis pilot:** tulis glosarium prasyarat W01 ringkas, tabel audit prasyarat W02, dan trace fit/transform prasyarat W03 sebagai bagian bridge pada `course/weeks/w04/scope.md` atau `book-chapter.md`, berstatus rancangan. Ini tidak membuat file W01–W03 dalam ticket W04. Catat sumber/formula/code yang perlu diperiksa dan rujuk bagian bridge dari modul W04; paket minggu awal diproduksi pada gelombangnya sendiri.
- **Diagnosis masuk:** mahasiswa menunjukkan target, fitur tersedia saat prediksi, pasangan baris yang bergantung, serta parameter scaler yang dipelajari; bila belum mampu, gunakan bridge sebelum contoh split.
- **Konsep inti A:** training untuk belajar parameter, validation/CV untuk memilih kandidat, test untuk penilaian final; test tidak dipakai berulang untuk memilih fitur, model, atau threshold.
- **Konsep inti B:** random split hanya cocok jika asumsi pertukaran/independensi dan tujuan deployment mendukung; stratifikasi menjaga proporsi label, tetapi tidak menyelesaikan dependensi pasien/pengguna/kelompok.
- **Konsep inti C:** group split mencegah unit kelompok bocor ke dua sisi; evaluasi kelompok baru berbeda dari prediksi catatan baru bagi kelompok yang pernah dilihat.
- **Konsep inti D:** split waktu melatih pada masa lalu dan menguji masa depan; jendela/gap dipilih dari proses data, horizon target, dan fitur yang benar-benar tersedia, bukan dari kebiasaan default.
- **Konsep inti E:** CV menghasilkan beberapa evaluasi kandidat di data pengembangan; jelaskan rerata serta variasi fold tanpa mengklaim seluruh skor independen atau test tidak diperlukan.
- **Konsep inti F:** fit imputasi, scaling, encoding, dan seleksi fitur yang belajar dari data berada di dalam pipeline/fold; target leakage, proxy masa depan, duplikasi, dan preprocessing leakage perlu pemeriksaan tersendiri.
- **Formula yang harus diperiksa saat produksi:** ukuran subset dan indeks disjoint; rerata skor fold yang memang dijalankan; jangan memperkenalkan formula performa yang belum dibutuhkan untuk tujuan W04.
- **Batas/pengayaan:** inti mencakup holdout, stratified CV, group split, dan split waktu melalui kasus; pengayaan menjelaskan nested CV untuk estimasi prosedur tuning. Tidak wajib membuktikan statistik CV atau menjalankan semua splitter library.
- **Miskonsepsi 1–2:** seed yang tetap menjadikan split benar untuk semua konteks; stratifikasi mencegah leakage kelompok.
- **Miskonsepsi 3–4:** CV mengizinkan melihat test untuk memilih kandidat; pipeline otomatis mencegah fitur masa depan atau label proxy bocor.
- **Miskonsepsi 5–6:** skor training adalah ukuran generalisasi; scaler tanpa label boleh di-fit pada seluruh data sebelum CV.

### Rencana contoh dan pemeriksaan pilot

| ID usulan | Kasus dan tindakan | Pemeriksaan yang harus dijalankan saat produksi |
| --- | --- | --- |
| W04-EX01 | Data klasifikasi kecil; holdout terstratifikasi lalu CV pada subset pengembangan; baseline sederhana dan pipeline | Indeks train/test tidak beririsan; semua indeks fold berada di pengembangan; label/fitur sesuai data dictionary; seed dan versi dicatat |
| W04-EX02 | Catatan berulang dengan `group_id`; bandingkan random split dan group split berdasarkan tujuan generalisasi | Tidak ada kelompok yang beririsan pada split benar; contoh random dipakai untuk mendeteksi risiko, tanpa menjanjikan peningkatan/penurunan skor tertentu |
| W04-EX03 | Data berurutan waktu dengan waktu fitur dan target; rancang evaluasi prediksi masa depan | Urutan train sebelum validation/test; fitur tersedia pada waktu prediksi; gap/horizon dapat dijelaskan; indeks waktu tidak diacak |
| W04-EX04 | Imputasi/scaling salah sebelum CV versus pipeline di dalam CV pada data simulasi | Statistik transformasi dapat ditelusuri ke training fold; test tidak tersentuh oleh fit/tuning; besar perubahan metrik dilaporkan hanya jika benar-benar dijalankan |

- **Urutan lab:** prediksi risiko dari diagram → pilih splitter per kasus → inspeksi indeks → jalankan baseline → bandingkan prosedur → tulis batas klaim. Verifikasi invariant lebih dahulu daripada menginterpretasikan skor.
- **Rencana kode:** `train_test_split`, `StratifiedKFold`, `GroupShuffleSplit`/`GroupKFold`, `TimeSeriesSplit`, dan `Pipeline`; pilihan API dan parameter final diperiksa pada dokumentasi versi yang digunakan. Jangan menjanjikan satu parameter menyelesaikan semua kasus.
- **Kontrak test:** simpan indeks test setelah keputusan desain, lakukan pengembangan pada data lainnya; run final baru dilakukan setelah kandidat dipilih. Demo pedagogis yang sengaja membuka test diberi label pelanggaran, tidak diteruskan sebagai prosedur proyek.
- **Kontrak solusi:** kunci menjelaskan lebih dari satu strategi sah ketika tujuan deployment berbeda; rubrik menilai kecocokan tujuan–unit–split, batas fit, dan alasan, bukan nama splitter semata.
- **Asesmen `W04-ASM01`:** audit rancangan evaluasi yang mengandung leakage, perbaiki tiga skenario, dan pertanggungjawabkan batas test. **Evidence `W04-EV01`:** matriks skenario, diagram pipeline, trace indeks, hasil run saat tersedia, dan memo batas klaim.
- **Adaptasi IF24A/IF24H:** jika langsung, diskusi kasus dalam kelompok dan inspeksi kode berpasangan; jika mandiri, kartu kasus, trace fold, rekaman/demo tekstual serta umpan balik checkpoint. Keduanya mempertahankan bukti keputusan split dan fit.
- **Pilot antarartefak:** bab menjadi sumber definisi; modul/guide memilih alur; dataset/lab/worksheet memakai indeks kasus yang sama; asesmen/rubrik memeriksa LO; storyboard/slide mengikuti pesan inti; LMS/evidence/QA memuat tautan dan status sebenarnya.
- **Koherensi keluar:** protokol ini dipakai W05–W06, disesuaikan W07, dan diperluas untuk tuning W09 serta reproduksi W14. Kesalahan pilot harus diperbaiki sebelum disalin ke paket lain.
- **Cek S02/S03:** kedalaman group/time/nested CV, istilah outcome, bentuk tugas W04, durasi, sumber contoh dan ketentuan AI; materi minggu 1–3/storyboard W04 lama diaudit bila diperoleh.

## W05 — Klasifikasi I: KNN dan Decision Tree

Baseline: **DAIML-Sub-CPMK082-1**; Bab 05. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W05-LO01` menelusuri prediksi KNN/tree pada contoh kecil; `W05-LO02` membandingkan model dengan protokol evaluasi tetap dan menghubungkan kesalahan pada konteks keputusan.
- **Prasyarat:** W01 klasifikasi/label; W03 scaling/encoding; W04 split/CV dan pipeline; jarak sederhana, proporsi, dan membaca aturan jika–maka.
- **Konsep inti:** tetangga dan parameter k, jarak dan skala, pemisahan tree, kedalaman/leaf, baseline klasifikasi, confusion matrix, accuracy, precision/recall sesuai konteks.
- **Batas/pengayaan:** mekanisme split tree diilustrasikan secukupnya; pembuktian impurity, pruning rinci, dan ensemble ditempatkan sebagai pengayaan, bukan materi wajib diam-diam.
- **Miskonsepsi:** k lebih kecil selalu lebih baik; tree memerlukan scaling seperti KNN; accuracy tinggi menjamin kelas minoritas dikenali.
- **Contoh/lab `W05-EX01`:** klasifikasi tabular kecil; hitung satu prediksi KNN dan jalur tree, lalu jalankan kedua model dan dummy baseline pada split/pipeline yang sama.
- **Verifikasi saat produksi:** cocokkan hitungan tangan dengan aturan tie/library; pastikan scaling KNN fit di training; periksa confusion matrix dan pembilang/penyebut metrik dari prediksi aktual.
- **Asesmen `W05-ASM01`:** jelaskan satu salah klasifikasi dan alasan memilih model/parameter tanpa melihat test berulang. **Evidence `W05-EV01`:** trace prediksi, tabel evaluasi, serta keputusan dengan batas klaim.
- **Adaptasi IF24A/IF24H:** gunakan kartu tetangga/jalur tree secara langsung atau worksheet trace mandiri; praktik CPU tersedia, format penalaran tetap sama.
- **Koherensi:** pipeline W04 dipakai kembali; kandidat W05 menjadi pembanding W09 dan contoh kompleksitas W10, bukan pemenang yang ditetapkan sebelumnya.
- **Cek S02/S03:** metrik klasifikasi yang diwajibkan, kedalaman matematika tree, dan pemetaan tugas ke 082-1.

## W06 — Regresi Linear dan Metrik Evaluasi

Baseline: **DAIML-Sub-CPMK102-1**; Bab 06. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W06-LO01` menghitung prediksi/residual dari model linear kecil dan menjelaskan asumsi interpretasinya; `W06-LO02` memilih metrik regresi berdasarkan unit serta biaya kesalahan.
- **Prasyarat:** W01 target numerik, W02 distribusi/outlier, W03 transformasi, W04 evaluasi; aljabar linear sederhana dan rata-rata, bridge kuadrat/akar bila diperlukan.
- **Konsep inti:** garis/model linear, koefisien/intercept, loss kuadrat, residual, baseline rerata, MAE/MSE/RMSE/R², skala target, prediksi versus sebab-akibat.
- **Batas/pengayaan:** solusi normal equation dan inferensi koefisien tidak wajib tanpa RPS; pengayaan membaca residual plot dan keterbatasan extrapolation.
- **Miskonsepsi:** koefisien membuktikan sebab; R² adalah persentase prediksi yang benar; RMSE dan MAE dapat dibandingkan lintas target dengan unit berbeda tanpa penyesuaian.
- **Contoh/lab `W06-EX01`:** data numerik sintetis berlabel simulasi; hitung residual pada tabel kecil, bandingkan linear regression dan baseline pada protokol W04, lalu inspeksi residual.
- **Verifikasi saat produksi:** periksa formula/units, cocokkan metrik hitung tangan dan library, tangani definisi R² untuk target konstan, catat seed dan hasil aktual tanpa target skor yang dijanjikan.
- **Asesmen `W06-ASM01`:** memo pilihan metrik dan batas interpretasi koefisien. **Evidence `W06-EV01`:** tabel prediksi/residual, perhitungan terverifikasi, serta interpretasi berunit.
- **Adaptasi IF24A/IF24H:** hitungan residual dapat dibahas langsung atau melalui tabel mandiri dengan checkpoint; kedua kelas mendapat alternatif tanpa komputasi berat.
- **Koherensi:** bedakan metrik W05 dan W06; loss regresi menjadi pijakan W10/W11 tanpa menyamakan training loss dengan estimasi generalisasi.
- **Cek S02/S03:** daftar metrik resmi, kedalaman optimisasi/asumsi regresi, dan luaran tugas numerik.

## W07 — Clustering dan Metrik Clustering

Baseline: **DAIML-Sub-CPMK102-1**; Bab 07. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W07-LO01` menelusuri assignment/update K-Means pada contoh kecil; `W07-LO02` menilai hasil cluster dengan metrik dan interpretasi domain tanpa menyebutnya kebenaran kelas.
- **Prasyarat:** W01 unsupervised, W02 distribusi, W03 skala/jarak, W04 disiplin evaluasi; rata-rata, jarak, dan membaca koordinat sederhana.
- **Konsep inti:** kemiripan, centroid, K-Means, inisialisasi dan k, inertia, silhouette, metrik internal versus eksternal jika label pembanding tersedia, stabilitas dan kegunaan.
- **Batas/pengayaan:** K-Means adalah usulan algoritma inti sampai RPS diperiksa; DBSCAN/hierarchical sebagai pembanding opsional. Jangan menjanjikan setiap dataset mempunyai jumlah cluster objektif.
- **Miskonsepsi:** cluster adalah kelas yang benar; inertia terendah selalu menghasilkan k terbaik; nomor cluster mempunyai urutan/arti yang tetap antar-run.
- **Contoh/lab `W07-EX01`:** titik sintetis kecil; hitung satu iterasi, jalankan beberapa k/seed, bandingkan metrik dan visual, lalu usulkan label deskriptif secara hati-hati.
- **Verifikasi saat produksi:** cek centroid/hitungan, syarat jumlah cluster untuk silhouette, skala fitur, dan perbedaan label permutasi; jelaskan batas evaluasi unsupervised, jangan mengklaim CV klasifikasi cocok otomatis.
- **Asesmen `W07-ASM01`:** kritik rekomendasi segmentasi yang hanya memakai satu skor. **Evidence `W07-EV01`:** trace iterasi, tabel/plot, alasan k, dan satu keterbatasan domain.
- **Adaptasi IF24A/IF24H:** kelompokkan titik di kertas atau anotasi plot/trace mandiri; tujuan interpretasi sama, pengayaan algoritma menunggu waktu tersedia.
- **Koherensi:** menguatkan fitur/skala W03 dan batas klaim W04; UTS dapat memakai kasus membedakan klasifikasi, regresi, dan clustering bila cakupan resmi sesuai.
- **Cek S02/S03:** algoritma/metrik yang diwajibkan, penggunaan label pembanding, dan indikator capaian clustering.

## W08 / UTS — brief asesmen tengah semester

Baseline: **DAIML-Sub-CPMK102-1**; tujuh artefak ujian, tanpa bab baru. Rincian berikut adalah usulan desain, bukan kebijakan ujian.

- **Tujuan usulan:** `UTS-LO01` mengintegrasikan framing–data–transformasi–evaluasi pada kasus; `UTS-LO02` menjelaskan pilihan metode/metrik dan memperbaiki prosedur keliru. Jangan mengganti rumusan capaian resmi dengan ID ini.
- **Prasyarat:** materi W01–W07 yang benar-benar diajarkan; latihan dan remediation checkpoint sebelum ujian bila jadwal resmi memungkinkan.
- **Cakupan kandidat:** membaca data, fit/transform, leakage/split, trace model sederhana, metrik klasifikasi/regresi/clustering; daftar ini harus dicocokkan dengan blueprint/RPS asli.
- **Batas/pengayaan:** materi yang belum diajarkan tidak masuk soal wajib; jangan menganggap satu kode 102-1 pada baris ujian membatasi seluruh cakupan outcome.
- **Miskonsepsi yang didiagnosis:** preprocessing seluruh dataset sebelum evaluasi aman; satu skor yang tinggi cukup untuk memilih model; korelasi/cluster membuktikan sebab atau kelas benar.
- **Rencana contoh verifikasi `UTS-EX01`:** kasus latihan terpisah dari soal ujian, dengan tabel kecil dan prosedur salah; hitungan, data, kunci, serta alternatif jawaban dijalankan/diperiksa saat produksi.
- **Asesmen `UTS-ASM01`:** rancangan campuran interpretasi kasus, penelusuran langkah, dan alasan keputusan; proporsi, jumlah soal, skor, durasi, format dan alat mengikuti S02/S03, belum ditetapkan.
- **Evidence `UTS-EV01`:** spesifikasi arsip soal versi final, kunci dosen, jawaban aktual, keputusan penilaian, serta analisis butir/outcome setelah pelaksanaan; tidak diisi hasil rekaan.
- **Adaptasi IF24A/IF24H:** verifikasi akses, moda ujian, akomodasi, dan pengumpulan masing-masing; kesetaraan cakupan/kesulitan dibahas dalam blueprint, bukan mengasumsikan aturan kedua kelas identik.
- **Koherensi:** temuan aktual UTS dapat menentukan remediasi menuju W09; analisis pascaujian tetap template sampai jawaban tersedia.
- **Cek S02/S03 wajib:** cakupan, bobot, tanggal, durasi, kebijakan AI/open-book, integritas akademik, akomodasi, kanal pengumpulan dan kewenangan pengesahan. Tidak ada keputusan resmi dari brief ini.

## W09 — Klasifikasi II dan Model Selection

Baseline: **DAIML-Sub-CPMK082-1**; Bab 08. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W09-LO01` membandingkan kandidat memakai metric/CV yang konsisten; `W09-LO02` membedakan parameter model, hyperparameter, pencarian kandidat, dan penilaian test final.
- **Prasyarat:** W04 split/pipeline, W05 klasifikasi/metrik, hasil diagnosis UTS bila tersedia; tidak memerlukan semua pengayaan W07.
- **Konsep inti:** baseline, kandidat, hyperparameter, grid/random search berskala kecil, pipeline, skor validasi dan variasi, pilihan metrik, biaya komputasi serta test tersegel.
- **Pilihan classifier sementara:** logistic regression sebagai satu kandidat tambahan yang ringan di CPU, dibandingkan KNN/tree W05. SVM, Naive Bayes, atau ensemble dipilih hanya setelah cakupan asli RPS diperiksa; tidak otomatis semuanya wajib.
- **Batas/pengayaan:** nested CV dibahas sebagai cara mengestimasi prosedur seleksi bila relevan; pencarian besar dan optimisasi khusus bukan kebutuhan inti.
- **Miskonsepsi:** kandidat dengan train accuracy tertinggi pasti dipilih; hyperparameter boleh dipilih dari test; skor CV tertinggi membuktikan pemenang universal.
- **Contoh/lab `W09-EX01`:** reuse data klasifikasi dan protokol W04/W05; pilih pencarian kecil yang terdokumentasi, bandingkan skor/variasi, tetapkan kandidat lalu evaluasi final sesuai kontrak test.
- **Verifikasi saat produksi:** periksa identitas fold, preprocessing di dalam CV, daftar kandidat/parameter, metrik dan baseline; catat waktu/run aktual, jangan menjanjikan kandidat tambahan lebih baik.
- **Asesmen `W09-ASM01`:** memo seleksi model dengan alasan metrik, protokol, trade-off dan batas klaim. **Evidence `W09-EV01`:** konfigurasi pencarian, hasil run, keputusan, dan jejak penggunaan test.
- **Adaptasi IF24A/IF24H:** cari kandidat bersama atau distribusikan tabel run kecil yang telah diverifikasi untuk kritik mandiri; semua kelas menjelaskan keputusan, bukan berlomba komputasi.
- **Koherensi:** diagnosis score training versus validation diteruskan ke W10; model pilihan tetap dapat direvisi melalui protokol pengembangan yang tercatat.
- **Cek S02/S03:** classifier wajib, metode model selection, tingkat matematika logistic regression, serta luaran tugas dan batas compute.

## W10 — Generalisasi, Overfitting, dan Regularisasi

Baseline: **DAIML-Sub-CPMK082-1**; Bab 09. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W10-LO01` mendiagnosis underfit/overfit dari bukti training/validation dan keterbatasannya; `W10-LO02` mengusulkan kontrol kompleksitas serta menguji perubahan pada protokol yang sama.
- **Prasyarat:** W04 evaluasi, W05 tree/k, W06 loss/residual, W09 seleksi kandidat; pemahaman parameter/hyperparameter.
- **Konsep inti:** generalisasi, kapasitas model, underfit/overfit, train–validation gap, learning curve, pembatasan kedalaman, regularisasi L1/L2 secara intuitif, bias–variance sebagai kerangka diagnosis.
- **Batas/pengayaan:** derivasi statistik bias–variance tidak wajib; pengayaan regularisasi regresi atau early stopping sebagai jembatan W11, bukan janji penyelesaian semua overfit.
- **Miskonsepsi:** train score sempurna berarti model terbaik; regularisasi selalu meningkatkan semua metrik; seluruh gap training/validation pasti disebabkan overfitting, tanpa mempertimbangkan shift/leakage.
- **Contoh/lab `W10-EX01`:** variasikan kompleksitas tree pada data kecil, lalu satu contoh regularisasi model linear jika sesuai RPS; tampilkan train/validation curve dari run yang tercatat.
- **Verifikasi saat produksi:** gunakan fold/data yang sebanding, label sumbu dan arah metrik benar, penalty/parameter mengikuti library; pisahkan variasi sampling dari klaim efek yang tidak teramati.
- **Asesmen `W10-ASM01`:** diagnosis dua pola hasil dan usulan eksperimen lanjutan. **Evidence `W10-EV01`:** kurva/tabel, penjelasan pola, serta alasan kontrol kompleksitas.
- **Adaptasi IF24A/IF24H:** inspeksi kurva bersama atau anotasi mandiri dengan pertanyaan diagnosis; bagikan tabel ekuivalen bagi akses visual/komputasi terbatas.
- **Koherensi:** regularisasi dan pemisahan optimisasi/evaluasi menjadi bekal W11/W12; perubahan proyek nanti tetap mengikuti kontrak W04.
- **Cek S02/S03:** teknik regularisasi resmi, batas kedalaman matematis, dan jenis grafik/eksperimen yang diminta.

## W11 — Jaringan Syaraf Tiruan

Baseline: **DAIML-Sub-CPMK082-1**; Bab 10. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W11-LO01` menelusuri forward pass jaringan sangat kecil beserta bentuk input/output; `W11-LO02` membedakan optimisasi loss training dari evaluasi generalisasi jaringan.
- **Prasyarat:** W03 scaling, W04 split/pipeline, W06 loss, W10 kompleksitas; perkalian/penjumlahan matriks sederhana dengan bridge bentuk tensor, turunan sebagai intuisi jika diperlukan.
- **Konsep inti:** neuron, bobot/bias, activation, layer, forward pass, loss, gradient/backpropagation pada tingkat yang sesuai, learning rate, epoch/batch, regularisasi dan validation.
- **Batas/pengayaan:** pembuktian backpropagation lengkap dan training besar bukan inti tanpa RPS; pengayaan satu gradien scalar atau analisis arsitektur kecil.
- **Miskonsepsi:** neuron tiruan bekerja persis seperti otak manusia; lebih banyak layer selalu lebih baik; loss training menurun menjamin generalisasi membaik.
- **Contoh/lab `W11-EX01`:** hitung forward pass bernilai kecil, lalu MLP kecil dengan runtime dibatasi di CPU; bandingkan baseline dan inspeksi training/validation, bukan mengejar benchmark.
- **Verifikasi saat produksi:** cocokkan hitungan/bentuk tensor, scaling fit pada training, seed/versi, convergence warning dan hasil aktual; nyatakan reproducibility lintas platform dapat berbeda.
- **Asesmen `W11-ASM01`:** anotasi diagram jaringan dan kritik satu log training. **Evidence `W11-EV01`:** trace forward pass, konfigurasi run, hasil, serta batas interpretasi.
- **Adaptasi IF24A/IF24H:** forward pass dapat dipraktikkan di kertas atau worksheet digital; lab CPU dan trace hasil menjadi jalur setara ketika perangkat terbatas.
- **Koherensi:** istilah layer/loss/parameter digunakan konsisten di W12; jangan mengganti evaluasi W04 hanya karena model berupa jaringan.
- **Cek S02/S03:** kebutuhan backpropagation/math, framework wajib, durasi praktik dan akses perangkat. GPU bukan prasyarat dasar proposal ini.

## W12 — Pengantar Deep Learning dan Generative AI

Baseline: **DAIML-Sub-CPMK082-1**; Bab 11. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W12-LO01` membedakan model diskriminatif/generatif dan training/inference melalui kasus; `W12-LO02` menyusun proposal proyek terbatas dengan baseline, data, evaluasi, risiko, serta sumber daya.
- **Prasyarat:** W11 layer/loss, W04 evaluasi, W01 framing; pemahaman bahwa keluaran yang lancar tidak membuktikan ketepatan fakta.
- **Konsep inti:** deep learning sebagai representasi bertingkat, gambaran CNN/attention secukupnya, model generatif, token/context secara intuitif, prompting, hallucination, evaluasi dan batas pemakaian.
- **Batas/pengayaan:** training LLM, fine-tuning besar, produksi agen, dan layanan berbayar bukan syarat. Pengayaan demo lokal kecil hanya jika kompatibilitas/izin/lisensi terverifikasi.
- **Miskonsepsi:** semua jaringan syaraf adalah deep learning; teks yang yakin pasti faktual; prompt yang baik menggantikan verifikasi/evaluasi.
- **Contoh/lab `W12-EX01`:** bandingkan keluaran generatif sintetis berlabel terhadap bahan rujukan yang benar-benar dibaca; rancang kriteria verifikasi dan failure case. Demo model CPU kecil bersifat opsional, tidak memerlukan API key berbayar.
- **Verifikasi saat produksi:** bedakan keluaran simulasi dengan keluaran model aktual; periksa dukungan faktual, provenance, lisensi, input yang aman, serta resource jika demo lokal dipilih.
- **Asesmen `W12-ASM01`:** proposal proyek dan audit satu keluaran GenAI. **Evidence `W12-EV01`:** problem statement, data plan, baseline, evaluasi, batas compute, dan daftar klaim yang diperiksa.
- **Adaptasi IF24A/IF24H:** kritik keluaran/proposal dapat dilakukan dalam klinik langsung atau review asinkron berbukti; format proposal sama dan akses API/GPU tidak menentukan keberhasilan.
- **Koherensi:** milestone proposal → responsible AI W13 → pipeline W14 → demo W15 mengikuti catatan arsitektur proyek workbook; statusnya tetap usulan sampai RTM asli diperiksa.
- **Cek S02/S03:** cakupan DL/GenAI, kewajiban proyek, bentuk proposal, bantuan AI dan aturan data. Proyek ML tabular tetap alternatif jika tidak ada kewajiban model generatif.

## W13 — Responsible AI

Baseline: **DAIML-Sub-CPMK082-1**; Bab 12. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W13-LO01` mengidentifikasi pemangku kepentingan, risiko dan batas data pada kasus; `W13-LO02` menghubungkan mitigasi dengan bukti, trade-off serta risiko yang tersisa.
- **Prasyarat:** W01 tujuan keputusan, W02 representasi data, W04 batas evaluasi, W05/W06 metrik, proposal W12 bila proyek disahkan.
- **Konsep inti:** fairness sebagai pertanyaan kontekstual, kualitas/representasi data, privasi, consent/licensing, transparansi, keamanan, oversight manusia, keterbatasan model dan dokumentasi.
- **Batas/pengayaan:** tidak memberi nasihat hukum atau menganggap satu metrik fairness memadai; pengayaan perbandingan metrik subgroup bila data/sampel memungkinkan dan definisi diperiksa.
- **Miskonsepsi:** menghapus atribut sensitif otomatis menghilangkan bias; anonymization menjamin tidak ada risiko privasi; checklist etika lengkap membuktikan sistem aman.
- **Contoh/lab `W13-EX01`:** audit kasus sintetis dan proyek rancangan; identifikasi potensi kerugian, siapa terdampak, bukti yang dibutuhkan, tindakan mitigasi, dan keputusan penggunaan.
- **Verifikasi saat produksi:** periksa konsistensi tabel subgroup jika dipakai, denominators/sampel kecil, keterbatasan klaim, serta sumber prinsip/aturan yang benar-benar dibaca; gunakan data simulasi, tanpa mengumpulkan data mahasiswa.
- **Asesmen `W13-ASM01`:** risk register dan model/data card ringkas dengan satu trade-off. **Evidence `W13-EV01`:** risiko, pemilik tindakan usulan, mitigasi, batas penggunaan, dan gap bukti.
- **Adaptasi IF24A/IF24H:** debat stakeholder langsung atau memo/review rekan mandiri; kriteria menilai alasan dan bukti, bukan sikap yang sama pada setiap kasus.
- **Koherensi:** keputusan risiko mengubah scope/data/evaluasi proyek W14; final W15 harus mengomunikasikan risiko tersisa, bukan hanya menampilkan skor.
- **Cek S02/S03:** prinsip yang diwajibkan, sumber institusi, bentuk milestone proyek dan apakah data sensitif sama sekali boleh dipakai.

## W14 — Pipeline ML End-to-End dan Reproduksibilitas

Baseline: **DAIML-Sub-CPMK082-1**; Bab 13. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W14-LO01` menyusun alur data–transformasi–model–evaluasi–inference yang dapat dijalankan ulang; `W14-LO02` mengidentifikasi artefak/versi yang diperlukan agar orang lain dapat memeriksa klaim.
- **Prasyarat:** W03/W04 pipeline dan fit, W09/W10 evaluasi, proposal W12 dan risiko W13; operasi file/path serta cara menjalankan kode yang dipilih.
- **Konsep inti:** kontrak input/schema, split, pipeline training/inference, konfigurasi, seed, versi dependency/data, provenance, logging, manifest artefak, laporan evaluasi, reproduksibilitas dan batas nondeterminisme.
- **Batas/pengayaan:** CI/CD, cloud deployment, model registry enterprise, dan web service produksi tidak wajib; pengayaan contoh testing schema/inference tanpa memperluas ke MLOps penuh.
- **Miskonsepsi:** seed saja menjamin semua reproduksi lintas mesin; pipeline library mencakup seluruh provenance proyek; kode dapat dijalankan berarti klaim ilmiah sudah tervalidasi.
- **Contoh/lab `W14-EX01`:** integrasikan kasus CPU kecil ke satu jalur run dan inference pada batch baru; lakukan reproduksi dari proses bersih menggunakan data/konfigurasi yang dicatat.
- **Verifikasi saat produksi:** cek schema input, indeks split, tidak ada fit pada test/inference, versi dan sumber data, hasil run baru versus toleransi yang dijelaskan; catat kegagalan reproduksi bila ada.
- **Asesmen `W14-ASM01`:** paket reproduksi minimal dan peer audit README/run instructions. **Evidence `W14-EV01`:** manifest, konfigurasi, instruksi, log run, evaluasi serta model/data card usulan.
- **Adaptasi IF24A/IF24H:** reproduksi berpasangan atau reviewer mandiri dengan log/checklist; bila mahasiswa tidak bisa menjalankan kode, audit trace masih formatif dan tidak diklaim sebagai run yang berhasil.
- **Koherensi:** W04/W09 menyediakan protokol; W13 menyediakan batas penggunaan; W15 menyajikan bukti dari paket ini. Format repo/notebook mahasiswa menunggu RTM, berbeda dari keluaran bahan ajar Markdown.
- **Cek S02/S03:** luaran kode/repo/report, alat yang diperbolehkan, ketentuan submission, kontribusi individu dan kedalaman reproduksibilitas.

## W15 — Presentasi Proyek Akhir: klinik, demo, dan refleksi

Baseline: **DAIML-Sub-CPMK082-1**; Bab 14 berupa panduan klinik/presentasi, bukan teori algoritma baru. Semua rincian berikut adalah usulan desain.

- **Tujuan:** `W15-LO01` menyajikan masalah, metode, evaluasi, risiko dan batas klaim secara koheren; `W15-LO02` menanggapi pertanyaan dengan merujuk bukti dan mengusulkan revisi yang beralasan.
- **Prasyarat:** rangkaian proyek W12–W14 bila disahkan, artefak run/evaluasi yang tersedia, dan latihan menyampaikan alasan; proyek belum selesai diarahkan ke klinik perbaikan.
- **Konsep inti:** komunikasi klaim–bukti–batas, demonstrasi yang dapat dijelaskan, kontribusi, failure case, umpan balik, revisi dan refleksi pembelajaran.
- **Batas/pengayaan:** tidak menambah bab algoritma untuk memenuhi jumlah artefak; pengayaan diskusi lanjutan dan rencana pengembangan setelah masalah inti ditutup.
- **Miskonsepsi:** demo yang berjalan membuktikan model akurat/aman; slide menarik menggantikan evaluasi; menyembunyikan hasil buruk meningkatkan kredibilitas proyek.
- **Contoh/lab `W15-EX01`:** rehearsal/klinik dengan checklist klaim, demo menggunakan input tervalidasi dan failure case, lalu tanya-jawab berbasis artefak. Contoh dosen sintetis diberi label demonstrasi.
- **Verifikasi saat produksi:** periksa format demo fallback, tautan bukti, konsistensi klaim dengan run aktual, dan aksesibilitas; jangan membuat presentasi/log mahasiswa fiktif.
- **Asesmen `W15-ASM01`:** presentasi/klinik dan memo revisi; rubrik usulan mencakup framing, metode, validasi, reproducibility, responsible AI, komunikasi dan kontribusi. Bobot/aspek resmi menunggu RTM.
- **Evidence `W15-EV01`:** struktur paket final, rekaman/berkas bila diizinkan, pertanyaan/umpan balik, kontribusi dan revisi setelah tersedia; belum berupa arsip proyek aktual.
- **Adaptasi IF24A/IF24H:** verifikasi jumlah kelompok, moda, durasi dan akses; pilih live demo, rekaman plus tanya-jawab, atau presentasi dokumen dengan bukti setara sesuai ketentuan resmi.
- **Koherensi:** bab/modul/guide/lab menggunakan pola klinik; soal/refleksi menguji integrasi W01–W14. Hasil proyek tidak otomatis menggantikan UAS.
- **Cek S02/S03:** format final, kelompok/individu, jadwal, ketentuan bukti kontribusi, presentasi/demonstrasi, rubrik serta hubungan proyek dengan nilai UAS.

## W16 / UAS — brief asesmen akhir semester

Baseline: **DAIML-Sub-CPMK082-1**; tujuh artefak ujian, tanpa bab baru. Rincian berikut adalah usulan desain, bukan kebijakan ujian.

- **Tujuan usulan:** `UAS-LO01` mempertanggungjawabkan keputusan model/evaluasi pada kasus baru; `UAS-LO02` mengintegrasikan generalisasi, responsible AI serta reproduksibilitas untuk membatasi klaim.
- **Prasyarat:** materi yang benar-benar diajarkan dan capaian resmi; bukti proyek bila RTM menetapkan hubungan dengan UAS, tanpa menganggap semua proyek selesai/bernilai sama.
- **Cakupan kandidat:** model selection, generalisasi, jaringan/DL/GenAI pada tingkat yang diajarkan, risiko, pipeline dan kritik evaluasi; fondasi W01–W07 dipakai jika blueprint resmi mengizinkan.
- **Batas/pengayaan:** jangan otomatis membuat UAS presentasi proyek, ujian tulis, atau ujian kumulatif; cakupan/bentuk ditetapkan S02/S03. Pengayaan tidak diuji sebagai kewajiban.
- **Miskonsepsi yang didiagnosis:** memilih model dari test memberikan evaluasi final yang jujur; model kompleks/GenAI selalu lebih baik; reproduksibilitas dan ethical checklist menghilangkan semua risiko.
- **Rencana contoh verifikasi `UAS-EX01`:** latihan integratif terpisah dari soal rahasia; telaah skenario, tabel hasil yang benar-benar dihitung, dan kunci dengan alternatif keputusan yang sah saat produksi.
- **Asesmen `UAS-ASM01`:** blueprint menghubungkan soal/tugas ke outcome, indikator dan bukti; penetapan proporsi, jumlah soal, skor, waktu, alat dan bentuk dilakukan setelah sumber resmi dibaca.
- **Evidence `UAS-EV01`:** spesifikasi arsip versi soal, kunci dosen, submission aktual, keputusan rubric, analisis outcome dan remediasi; isi aktual menunggu pelaksanaan.
- **Adaptasi IF24A/IF24H:** verifikasi format/akses/akomodasi/kanal pengumpulan per kelas; setiap variasi soal atau tugas memerlukan kesetaraan indikator dan kesulitan yang ditelaah.
- **Koherensi:** bedakan nilai proyek, bukti mastery, dan hasil UAS sesuai aturan resmi; temuan akhir memberi masukan KEEP/FIX/ADD/REMOVE untuk produksi semester berikutnya.
- **Cek S02/S03 wajib:** bobot, cakupan, jadwal, durasi, hubungan UAS–proyek, bantuan AI, integritas akademik, pengumpulan dan pengesahan. Brief ini tidak menetapkan kebijakan tersebut.

## Pemeriksaan sebelum brief menjadi paket produksi

1. Tandai judul/kode baseline dan setiap usulan; setelah S01–S03 dibaca, catat perubahan beserta sumbernya. Jangan menghapus jejak konflik atau memindahkan bobot backlog menjadi nilai.
2. Petakan setiap LO sementara ke rumusan resmi, contoh, aktivitas, asesmen, rubrik, dan evidence; ubah/pecah LO jika cakupan tidak cocok. Pemetaan satu kode bukan bukti seluruh indikator tercakup.
3. Pilih contoh inti dan data berizin; jalankan pemeriksaan yang ditetapkan pada brief. Isi hasil numerik hanya dari eksekusi, pisahkan expected behavior dari measured result.
4. Tentukan kedalaman, agenda dan jumlah slide setelah durasi/mode IF24A/IF24H diketahui; pertahankan alur inti dan luaran, dokumentasikan pengayaan yang dipindah.
5. Selaraskan 14 artefak pembelajaran atau tujuh artefak ujian melalui ID contoh/asesmen/evidence; bedakan naskah siap review, siap Markdown, deck/notebook nyata, publikasi LMS dan bukti delivery.
6. Jalankan [gerbang mutu](QUALITY_GATES.md), perbarui backlog/status repo sesuai bukti, dan simpan masalah yang menunggu sumber resmi sebagai blocker spesifik, bukan klaim selesai.
