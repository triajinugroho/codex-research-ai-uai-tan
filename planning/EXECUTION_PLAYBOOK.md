# Pedoman Eksekusi Bertahap

Dokumen ini mengatur cara menjalankan [rencana utama](../PRODUCTION_PLAN.md) dengan penalaran sedang atau tinggi. Ini pedoman untuk produksi berikutnya; permintaan saat ini hanya merinci rencana.

## 1. Paket instruksi yang dipakai setiap sesi

| Dokumen | Fungsi | Dibaca kapan |
| --- | --- | --- |
| [PRODUCTION_PLAN](../PRODUCTION_PLAN.md) | Tujuan, cakupan, batas pekerjaan, urutan semester | Awal proyek dan saat cakupan berubah |
| [WORKBOOK_BASELINE](WORKBOOK_BASELINE.md) | 222 ID, path, status/dependensi/DoD sumber yang sebenarnya | Hanya bagian target dan definisi terkait pada tiap batch |
| [ARTIFACT_SPECS](ARTIFACT_SPECS.md) | Kontrak isi dan metadata setiap jenis artefak | Bagian metadata dan jenis target |
| [WEEKLY_BLUEPRINTS](WEEKLY_BLUEPRINTS.md) | Brief desain tiap minggu dan ujian | Minggu target serta minggu prasyarat/transisi |
| [QUALITY_GATES](QUALITY_GATES.md) | Bukti yang diperlukan untuk melewati review | Gate yang berlaku pada batch |
| [PROMPT_LIBRARY](PROMPT_LIBRARY.md) | Instruksi siap salin | Kontrak bersama + prompt target |
| [SESSION_TEMPLATES](SESSION_TEMPLATES.md) | Ticket, context pack, laporan, dan handoff | Awal, review, dan akhir batch |

File workbook dan master prompt unggahan dipertahankan sebagai sumber asli. Dokumen perencanaan ini merupakan turunan kerja; jika sumber berubah, lakukan analisis dampak terlebih dahulu.

## 2. Kebijakan penalaran dan ukuran pekerjaan

Pengaturan penalaran dipilih di antarmuka/model yang dipakai, bukan diubah oleh kalimat dalam prompt. Tabel berikut adalah rekomendasi penggunaan; tidak menjamin opsi yang sama tersedia pada semua model.

| Penalaran | Cocok untuk | Prasyarat | Eskalasi ke tinggi jika |
| --- | --- | --- | --- |
| Sedang | Impor baseline, metadata, indeks, modul turunan, panduan dosen, naskah slide dari storyboard, LMS, format bukti/QA, handoff | Scope, sumber, contoh, istilah, dan acceptance criteria cukup jelas | Harus menentukan outcome, memperbaiki formula, menafsir konflik sumber, atau mengubah rancangan asesmen |
| Tinggi | Audit kurikulum, arsitektur belajar, bab konseptual, desain/validasi lab, soal/rubrik, storyboard, review antardokumen | Input dan target dibatasi; sumber yang belum ada ditandai | Keputusan tidak dapat dibuat dari informasi tersedia; catat kebutuhan sumber/keputusan, bukan menaikkan penalaran tanpa henti |
| Ultra | Perombakan arsitektur besar atau konflik mendasar yang melibatkan banyak komponen | Dipakai selektif; tetap perlu bukti sumber | Tidak menyelesaikan sumber yang tidak tersedia atau pengesahan institusi |

Batch adalah unit hasil, bukan batas satu percakapan. Mulai dengan satu bab, dua dokumen turunan, satu lab/kasus, atau satu paket soal-rubrik. Untuk batch yang memuat empat dokumen praktik, pecah menjadi DATA+LAB dan WORK+AIP bila konteks/hasil terlalu besar. Untuk naskah slide, gunakan bagian 5–10 slide bila diperlukan, dengan indeks slide tetap utuh.

Jangan menurunkan standar review ketika menggunakan sedang. Sedang mengerjakan transformasi yang jelas; tinggi memeriksa keputusan konseptual yang dapat salah.

## 3. Model status: empat hal yang tidak boleh dicampur

| Dimensi | Nilai kerja | Makna |
| --- | --- | --- |
| `source_status` | Lifecycle workbook, termasuk IMPROVE | Snapshot laporan sumber; bukan hasil pekerjaan saat ini |
| `production.repo_status` | NOT STARTED, DRAFT, REVIEW, READY, PUBLISHED, DELIVERED, IMPROVE | Status artefak terhadap DoD asli; READY membutuhkan bukti cakupan tersebut |
| `markdown_readiness` | NOT_STARTED, DRAFT, IN_REVIEW, VALIDATED | Kesiapan isi Markdown sesuai spesifikasi adaptasinya |
| `fulfillment` | NOT_FULFILLED, PARTIAL, FULFILLED | Apakah output asli workbook benar-benar terpenuhi |

`markdown_readiness: VALIDATED` berarti isi Markdown memenuhi pemeriksaan yang berlaku, bukan status resmi institusi. `source_verification` dan `blockers` tetap dicatat menurut spesifikasi artefak. Status format bukti yang telah divalidasi tidak menyatakan bukti mahasiswa tersedia.

Contoh kebijakan:

| Artefak | Saat Markdown lolos review | Yang masih diperlukan untuk DoD asli |
| --- | --- | --- |
| BOOK/MOD/GUIDE/WORK/AIP/ASSESS/RUBRIC | Dapat memenuhi DoD konten jika sumber/kebijakan dan verifikasi yang diwajibkan lengkap | Pengesahan resmi jika relevan; format lain hanya jika diwajibkan sumber |
| STORY | Storyboard Markdown dapat memenuhi DoD storyline | Render bukan syarat storyboard; isi dan audit alur tetap wajib |
| SLIDE | Naskah VALIDATED; `fulfillment: PARTIAL` | Deck yang dirender dan review keterbacaan presentasi |
| DATA | Kasus/simulasi mandiri dalam Markdown dapat memenuhi kebutuhan kasus | Jika perlu dataset eksternal: data, asal/lisensi, akses, dan penggunaan terverifikasi |
| LAB | Panduan dan kode diuji, `fulfillment: PARTIAL` untuk notebook asli | Notebook starter/solusi jika DoD workbook tetap dipakai |
| LMS | Paket instruksi VALIDATED, `fulfillment: PARTIAL` | Implementasi dan pemeriksaan LMS aktual |
| EVID/QA | Spesifikasi siap; `fulfillment: PARTIAL` | Bukti kelas/ujian, analisis, dan tindak lanjut aktual |

Penilaian pemenuhan dilakukan per item, bukan hanya per jenis. Jika pengguna kelak menetapkan Markdown sebagai pengganti deliverable asli, catat keputusan perubahan DoD dan tanggalnya; jangan mengubah baseline workbook diam-diam.

Dashboard produksi melaporkan jumlah Markdown VALIDATED, jumlah DoD asli FULFILLED, blocker sumber, dan item yang menunggu pelaksanaan secara terpisah. Rumus skor workbook boleh direproduksi sebagai metrik sumber, tetapi tidak menggantikan metrik kesiapan Markdown. Bobot produksi tidak menjadi bobot nilai mahasiswa.

## 4. Fondasi: batch A01–A06

| Batch | Penalaran | Target dan keluaran | Dependensi | Syarat selesai batch |
| --- | --- | --- | --- | --- |
| A01 — Inventaris | Sedang | Impor baseline ke `course/production/semester-backlog.md` dan `weekly-backlog.md`; buat `dashboard.md` dan tautan kendali produksi | WORKBOOK_BASELINE | 12+210 ID unik dan path benar; status sumber terpisah dari repo; SEM-12 sebatas kendali Markdown |
| A02 — Sumber dan keputusan | Sedang; tinggi untuk konflik | `sources.md`, `decisions.md`, `reports/source-audit-initial.md` | A01 + file/tautan yang benar-benar tersedia | S01–S06 tercatat; sumber lokal hash/versi; belum dibaca ditandai; daftar kebutuhan sumber spesifik |
| A03 — Tata kelola | Tinggi | SEM-01–04: audit, RPS, RTM, blueprint asesmen | A02 + sumber yang tersedia | Rancangan substantif tersedia; kekosongan resmi dilabeli; belum ada angka akademik yang direka |
| A04 — Alur dan standar | Tinggi | SEM-05, SEM-06, SEM-11: arsitektur belajar, TOC, teaching OS | A03 sebagai rancangan atau terverifikasi | 14 bab+ujian/proyek dipetakan; W04 dapat dimulai dengan jembatan prasyarat W01–03 |
| A05 — Template dan contoh metadata | Sedang | `course/templates/` untuk artefak, scope, review, indeks; satu metadata contoh | Spesifikasi + A04 | Template dapat dipakai prompt; heading/kriteria tidak dianggap konten produksi |
| A06 — Sistem semester pendukung | Tinggi untuk proyek/asesmen, sedang untuk struktur | SEM-07–10: proyek, LMS skeleton, mastery tracker, question bank | A03/A04 | Struktur 16 minggu; stage gate W12–15; bank awal tanpa soal semu; tracker tidak berisi data mahasiswa rekaan |

A03 dan A06 boleh dikerjakan dalam beberapa ticket agar hasil tetap dapat ditelaah. Jika RPS/RTM belum tersedia, selesaikan bagian rancangan yang aman dan catat bagian yang belum terverifikasi. W04 boleh mulai setelah scope sementara, standar, dan template cukup jelas; tidak wajib menunggu pengesahan seluruh semester.

Inventaris baseline dalam `planning/` telah disiapkan saat merinci rencana. A01 tetap diperlukan untuk membuat kendali produksi berjalan; jangan menganggap semua batch fondasi telah selesai karena file rencana ada. Navigasi umum `course/index.md` dan README diperbarui melalui prompt integrasi P17 setelah file terkait tersedia; jangan menambahnya ke write set P02 diam-diam.

Pemetaan prompt fondasi: **A01=P02; A02=P03; A03=P05; A04/A05=P04; A06=P20**. P00 adalah orientasi opsional. P05 tidak menunggu P04; arsitektur berikutnya memanfaatkan tata kelola awal yang dapat masih provisional. Rujukan balik dari RPS/RTM ke blueprint/arsitektur/proyek adalah pemeriksaan integrasi akhir, bukan prasyarat yang membuat draft saling menunggu.

## 5. Pola eksekusi setiap minggu: A–F dan review

`Wnn` adalah minggu target. Prompt spesifik tersedia di pustaka prompt; pilih berdasarkan nama tugas dan ID yang tercantum di manifest, bukan menebak instruksi dari tahap sebelumnya.

| Batch | Penalaran | Read set utama | Write set | Kriteria hasil |
| --- | --- | --- | --- | --- |
| Wnn-A — Scope dan bab | Tinggi | Brief minggu, sumber terkait, peta semester/TOC, catatan prasyarat | `scope.md`, BOOK | Outcome usulan dan official terpisah; batas cakupan; bab menyeluruh dengan contoh/sumber; angka yang belum diuji dilabeli |
| Wnn-B — Modul dan panduan | Sedang | Scope+BOOK yang sudah diperiksa | MOD, GUIDE | Alur mahasiswa/dosen dapat dijalankan; waktu sebagai usulan jika durasi resmi belum ada; tidak menduplikasi bab sebagai modul |
| Wnn-C1 — Kasus dan lab | Tinggi | Scope+BOOK, kebutuhan praktik, dependensi runtime | DATA, LAB + laporan validasi | Kasus konsisten, kode penting dijalankan; ada expected behavior, keterbatasan, dan bukti run |
| Wnn-C2 — Latihan dan prompt AI | Sedang; tinggi bila reasoning baru | BOOK+MOD+DATA/LAB | WORK, AIP | Latihan meminta alasan; petunjuk tidak membocorkan jawaban; prompt AI diuji dengan simulasi respons yang dilabeli |
| Wnn-D — Asesmen dan rubrik | Tinggi | Scope+BOOK+praktik+blueprint+RTM bila tersedia | ASSESS, RUBRIC | Semua item dan solusi berpasangan, skor konsisten, outcome tercakup, tidak mengarang bobot mata kuliah |
| Wnn-E1 — Storyboard | Tinggi | Scope+BOOK+GUIDE+praktik/asesmen | STORY | Alur/mental model, contoh, interaksi, takeaway, cakupan, dan jumlah slide sesuai tujuan |
| Wnn-E2 — Naskah slide | Sedang | STORY versi yang telah lolos review konten | SLIDE | Seluruh slide terpetakan, teks/diagram/sitasi sesuai storyboard; belum mengklaim hasil visual |
| Wnn-F — Paket dan format bukti | Sedang | Semua artefak minggu + standar LMS/mastery | LMS, EVID, QA, `index.md` | Indeks mahasiswa/dosen; spesifikasi bukti/QA lengkap; publikasi dan hasil kelas belum diasumsikan |
| Wnn-R — Review paket | Tinggi | Seluruh paket + gate + kebutuhan sumber | Laporan review; revisi hanya write set ticket | Temuan ditutup atau diberi blocker; sumber/hasil run benar; status dan handoff diperbarui |

Batch E2 dapat mulai setelah audit internal storyboard Markdown; permintaan approval visual dalam master prompt tidak memblokir penulisan naskah Markdown. Pembuatan gambar/deck adalah fase terpisah yang belum diminta. Perubahan headline/urutan yang mengubah makna mengharuskan review storyboard terkait.

Dalam batch C1, run yang menghasilkan perbandingan performa bertujuan menguji perilaku, bukan memaksa skor model tertentu. Seed tetap tidak menjamin semua versi pustaka menghasilkan angka identik; gunakan toleransi dan penjelasan yang sesuai. Jangan memodifikasi contoh supaya selalu membuktikan klaim yang tidak didukung data.

## 6. Urutan semester dan titik integrasi

| Gelombang | Paket | Tujuan integrasi | Kebutuhan sebelum pindah |
| --- | --- | --- | --- |
| 0 | A01–A06 bertahap | Fondasi, sumber, definisi, template | Scope sementara dan backlog berfungsi; blocker resmi tercatat |
| 1 | W04-A sampai W04-R | Contoh lengkap standar produksi | Review pola, validasi praktik, hasil/kelemahan pola tercatat |
| 2 | W01, W02, W03 | Lengkapi prasyarat mahasiswa | Audit sambungan data/preprocessing/validasi; W04 disesuaikan bila asumsi berubah |
| 3 | W05, W06, W07 | Klasifikasi, regresi, clustering | Metrik dan strategi validasi konsisten; bank soal diperbarui |
| 4 | UTS | Paket evaluasi W01–W07 sebagai usulan awal | Cakupan final sesuai RPS; kunci dan soal diverifikasi; kebijakan waktu/AI jelas |
| 5 | W09, W10, W11 | Selection, generalisasi, jaringan syaraf | Split/metric/test-set discipline tetap berlaku pada model baru |
| 6 | W12, W13, W14, W15 | Deep learning/GenAI, responsible AI, pipeline, proyek | SEM-07 diperiksa; tahapan proposal/demo berasal dari sumber atau label usulan |
| 7 | UAS | Evaluasi akhir dan hubungan proyek | Bentuk/cakupan ditetapkan dari RPS; tidak menebak final exam vs proyek |
| 8 | Audit semester | Konsistensi 222 ID, sumber, istilah, outcome, link | Laporan kesiapan Markdown vs pemenuhan DoD asli; daftar tertunda jujur |

Urutan produksi berbeda dari urutan belajar mahasiswa. W04 memakai jembatan prasyarat sementara tanpa menyebut W01–W03 telah diproduksi. Catat dependensi belajar W01→W02→W03→W04 terpisah dari jadwal pengerjaan. Perbedaan ini mencegah siklus semu: W04 dirancang lebih dulu, lalu diselaraskan setelah bab awal tersedia.

## 7. Paket ujian: X-A sampai X-D

`X` adalah UTS/UAS. Pecah pengerjaan jika jumlah soal melebihi konteks yang dapat diperiksa.

1. **X-A, tinggi:** blueprint dan instruksi. Tetapkan cakupan outcome dan bentuk berdasarkan sumber; usulan skor per item dapat dibuat, bobot nilai semester tidak direka.
2. **X-B, tinggi:** soal dan kunci/rubrik. Kembangkan satu kelompok soal bertag; lakukan perhitungan independen dan pencocokan semua item.
3. **X-C, sedang:** panduan LMS, spesifikasi arsip, format analisis. Bedakan teks mahasiswa dan materi dosen; belum menyatakan ujian berlangsung.
4. **X-D, tinggi:** review keseluruhan, waktu pengerjaan usulan diuji secara wajar, kejelasan, coverage, skor, kunci, dan checklist implementasi.

File kunci dalam repo yang sama dapat dibaca oleh semua yang memiliki akses repo. Label dosen dan indeks terpisah membantu packaging, bukan kontrol akses. Sebelum membagikan repo/arsip kepada mahasiswa, periksa seluruh isi yang ikut dibagikan, termasuk contoh solusi. Membuat kontrol akses atau memublikasikan paket memerlukan langkah aktual di layanan terkait.

## 8. Read set, write set, dan konteks yang cukup

Setiap ticket menggunakan path relatif terhadap root repo. Daftarkan file yang boleh diedit dengan jelas. Shared files (`sources.md`, backlog, dashboard, decision log) hanya diperbarui oleh pelaksana integrasi agar tidak bentrok.

Context pack berisi:

- Ticket: target ID, keluaran, status awal, scope edit, gate, blocker, penalaran.
- Bagian relevan spesifikasi/gate, bukan semua dokumen semester.
- Baris sumber: ID sheet, cell/row, versi/hash, kutipan atau ringkasan faktual yang dapat dicek.
- Scope minggu, daftar istilah, contoh/kasus yang sudah dipilih, hasil run yang terkait.
- Review terbuka dan catatan perubahan upstream.
- Definition of Done Markdown dan DoD asli, serta rencana membuktikan masing-masing.

Ringkasan memudahkan orientasi tetapi tidak menggantikan membaca bagian sumber yang memengaruhi keputusan. Jangan menyalin kunci ujian ke context pack yang akan diberikan kepada mahasiswa. Jika context pack masih memuat placeholder untuk input wajib, isi dari file nyata atau catat blocker; jangan diam-diam mengarang.

Hindari membaca 210 baris backlog penuh setiap kali menulis satu dokumen. Gunakan pencarian ID target dan bagian definisinya. Namun, audit final harus memeriksa seluruh inventaris, bukan sampel.

## 9. Validasi konten dan kode

Pada produksi berikutnya, gunakan runtime yang tersedia dahulu. Python diketahui tersedia pada setup awal, tetapi versi dan dependensi harus diperiksa kembali saat run. Jangan menganggap numpy/pandas/scikit-learn telah dipasang dari keberadaan Python.

Untuk lab:

1. Tetapkan operasi dan hasil perilaku yang perlu diuji, input, seed jika relevan, serta dependensi.
2. Simpan kode runner sementara di `/tmp` atau direktori kerja di luar artefak terbit; pertahankan isi kode utama di `lab.md`.
3. Gunakan venv terisolasi jika dependensi diperlukan. Catat versi yang benar-benar dipakai dalam laporan. Jangan mengarang lockfile atau angka output.
4. Jalankan jalur contoh dan pemeriksaan yang sesuai: ukuran split, tidak ada overlap, preprocessing training-only, hasil metrik/perhitungan, reproduksibilitas sesuai toleransi.
5. Catat tanggal, command, input/version, exit status, hasil ringkas, perbandingan ekspektasi, serta keterbatasan di `course/production/reports/`.
6. Jika langkah gagal, diagnosis setup vs kesalahan contoh. Perbaiki contoh milik produksi sesuai ticket; sumber asli dipertahankan. Run ulang hanya bagian yang terdampak.

Code fence `TODO` atau starter yang sengaja belum lengkap bukan program selesai. Bedakan run starter yang memang belum diisi dari run solusi referensi. Jangan mencatat starter belum lengkap sebagai bug runtime atau solusi tanpa uji sebagai lulus.

Rumus diperiksa dengan substitusi contoh kecil dan interpretasi satuan/arti. Grafik/tabel hanya memakai output terverifikasi atau angka simulasi yang jelas. Klaim real-world, kebijakan, bibliografi, dan lisensi memerlukan sumber yang mendukung klaim itu secara spesifik.

## 10. Review dan penanganan kegagalan

Review dilakukan menurut gate ID dalam QUALITY_GATES; catat finding ID, lokasi, masalah, dampak, koreksi, dan bukti closure. Pelaksana boleh memperbaiki hal yang jelas dalam ticket. Reviewer independen dianjurkan untuk scope konseptual, lab, soal/rubrik, dan integrasi semester.

| Situasi | Tindakan |
| --- | --- |
| Tautan sumber saja, belum bisa dibaca | Label UNAVAILABLE/LINK_ONLY sesuai metadata; lanjutkan draft; jangan mengutip isinya |
| RPS dan workbook berbeda | Catat konflik dan sumber masing-masing; gunakan versi resmi terverifikasi untuk keputusan resmi; belum ada keputusan berarti provisional |
| Kode tidak berjalan | Diagnosis, perbaikan, run ulang; teknis UNRUN/FAIL tidak dilabeli PASS |
| Reviewer menemukan penalaran/metrik salah | Revisi sumber konten internal dan semua turunan terdampak; lakukan pemeriksaan terarah |
| Reviewer meminta perubahan di luar batch | Buat ticket lanjutan dan tandai dependensi STALE; jangan merombak seluruh semester tanpa alasan |
| Hanya data pelaksanaan yang belum ada | Selesaikan spesifikasi; tandai menunggu kelas/ujian; tidak menghalangi materi pra-kelas yang independen |
| Pengguna memperbarui sumber | Bandingkan versi, buat daftar dampak, revisi urutan batch jika perlu |
| Konteks percakapan hampir habis | Simpan handoff dan ticket berikutnya; jangan mengurangi kualitas dengan menyebut semua target selesai |

Pertanyaan ke pengguna hanya diperlukan untuk keputusan yang tidak dapat disimpulkan dan menghalangi pekerjaan berguna. Review draft rutin tidak menjadi alasan meminta izin berulang. Pengesahan akademik tetap keputusan dosen/institusi, sedangkan pemeriksaan konsistensi internal dapat berjalan autonom.

## 11. Paralelisme yang aman

Paralelkan hanya pekerjaan yang inputnya cukup stabil: MOD dan GUIDE dari bab yang sama, WORK dan AIP dari praktik yang telah diperiksa, atau reviewer terpisah dari penulis. Jangan menulis solusi saat soal/cakupan masih berubah tanpa koordinasi.

Setiap agen mendapat read set, write set unik, versi input, jenis output, dan gate. Hanya integrator memperbarui shared state/backlog/dashboard. Jika upstream berubah di tengah pekerjaan, hasil turunan diberi STALE sampai diperiksa; file selesai tidak otomatis tervalidasi.

Tidak perlu Git worktree untuk task cloud yang sudah terisolasi. Gunakan checkout ini dan pertahankan perubahan yang sudah ada. Jangan commit, push, mengunggah, atau memublikasikan sebagai efek samping prompt produksi yang hanya meminta penulisan file.

## 12. Handoff dan definisi selesai sesi

Setiap sesi berakhir dengan laporan handoff tersimpan di `course/production/reports/<ticket-id>-handoff.md`:

1. Target dan file yang berubah, termasuk work in progress.
2. ID, status sebelum/sesudah, dan bukti perubahannya.
3. Sumber yang dibaca, yang belum tersedia, dan keputusan provisional.
4. Pemeriksaan yang PASS/FAIL/UNRUN/NOT_APPLICABLE; exact input/version untuk run yang perlu direproduksi.
5. Temuan terbuka dan blocker sumber/pelaksanaan.
6. Ticket berikutnya, penalaran rekomendasi, read/write set, prompt ID, dan acceptance criteria.

Jika tidak ada perubahan konten setelah review lulus, jangan mengulang run panjang hanya demi menambah bukti. Jika input/angka/kode/sumber berubah, pemeriksaan terkait menjadi STALE dan harus dijalankan lagi.

**Selesai sesi** berarti keluaran ticket dan laporan statusnya akurat. **Selesai produksi Markdown** berarti cakupan Markdown yang disepakati memenuhi gate, dengan keterbatasan sumber/delivery dinyatakan. **Selesai seluruh DoD workbook** baru dapat diklaim setelah deck/notebook/LMS dan bukti kelas/ujian yang diwajibkan benar-benar tersedia.
