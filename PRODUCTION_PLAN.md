# Rencana Produksi Bahan Ajar Dasar AI & ML 2026–2027

Tanggal rencana: 7 Oktober 2026. Versi perencanaan: 2. Status: rencana dan instruksi eksekusi; bahan ajar belum diproduksi.

## Paket rencana terperinci

Dokumen ini adalah peta utama. Detail operasional disimpan sebagai paket berikut agar sesi penalaran sedang/tinggi dapat membaca bagian yang relevan saja.

| Dokumen | Isi |
| --- | --- |
| [Baseline workbook](planning/WORKBOOK_BASELINE.md) | Ekstraksi 222 ID beserta path usulan, dependensi, status sumber, bobot produksi, DoD asli, dan catatan |
| [Pedoman eksekusi](planning/EXECUTION_PLAYBOOK.md) | Batch fondasi/mingguan/ujian, rekomendasi penalaran, konteks, status, validasi, dan paralelisme |
| [Spesifikasi artefak](planning/ARTIFACT_SPECS.md) | Struktur isi dan kriteria diterima untuk seluruh jenis artefak |
| [Blueprint mingguan](planning/WEEKLY_BLUEPRINTS.md) | Rancangan tujuan, konsep, kasus, praktik, miskonsepsi, asesmen, dan kesinambungan semua minggu |
| [Gate mutu](planning/QUALITY_GATES.md) | Pemeriksaan sumber, substansi, kode, asesmen, storyboard, paket, dan integrasi semester |
| [Pustaka prompt](planning/PROMPT_LIBRARY.md) | Kontrak bersama, prompt siap salin, input/output, batas edit, review, revisi, dan resume |
| [Template sesi](planning/SESSION_TEMPLATES.md) | Ticket, context pack, register sumber, keputusan, laporan run/review, dan handoff |
| [Review paket rencana](planning/PLAN_REVIEW.md) | Pemeriksaan inventaris dan konsistensi, temuan yang ditutup, serta keterbatasan yang masih berlaku |

**Urutan membaca untuk mulai eksekusi:** rencana ini → pedoman eksekusi → kontrak prompt → ticket target → spesifikasi/blueprint/gate terkait. Baseline dibaca per ID atau kelompok minggu, bukan wajib disalin seluruhnya ke setiap prompt.

**Fokus eksekusi saat ini:** menyiapkan seluruh bahan pekan 1–4 dalam Markdown, 56 artefak mingguan. Ikuti [roadmap W01–W04](planning/W01_W04_ROADMAP.md) untuk urutan prompt; inventaris semester 222 artefak tetap dipertahankan, sedangkan produksi isi pekan berikutnya ditunda.

## 1. Tujuan dan batas pekerjaan

Menghasilkan paket bahan ajar **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin**, kode **IF52510031**, untuk **IF24A dan IF24H**, dalam file Markdown di repositori ini. Paket mencakup tata kelola semester, buku per bab, modul mahasiswa, panduan dosen, naskah slide, praktik, asesmen, rubrik, panduan LMS, dan evaluasi pembelajaran.

Struktur dan cakupan awal mengikuti workbook unggahan, dengan prinsip **Govern → Know → Learn → Prove → Compound**. Pedoman visual dan pedagogi mengikuti master prompt sebagai referensi desain. Instruksi di dalam sumber tidak otomatis menjadi perintah untuk menjalankan layanan, menghasilkan gambar, atau memublikasikan materi.

Pada tahap ini keluaran utama adalah Markdown. Tidak termasuk produksi gambar, PPTX/PDF, sinkronisasi Google Drive, unggah ke LMS, pengumpulan data mahasiswa, atau penerbitan eksternal. Pekerjaan tersebut dapat dilakukan kemudian berdasarkan permintaan terpisah.

## 2. Sumber, fakta awal, dan kebutuhan tambahan

Sumber lokal:

- [Production Control Sheet](<references/MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx>): Dashboard, Semester_Master, Production_Backlog, Definitions, Sources.
- [Master Prompt Package](references/Master_Prompt_Package_Slide_Mata_Kuliah_Tri_Aji.md): alur pedagogi, storyboard, desain slide, aktivitas, dan pemeriksaan mutu.
- [Folder Google Drive](https://drive.google.com/drive/folders/1PSz_2tbCdjFh5TTdYwJ5ExzPIMpp8BvC?usp=drive_link): referensi eksternal; isinya belum dibaca.

Workbook mencatat **12 artefak semester** dan **210 item backlog**: 196 item untuk 14 minggu pembelajaran (14 artefak per minggu), ditambah 14 item ujian (7 UTS dan 7 UAS). Status sumber adalah 173 NOT STARTED, 31 DRAFT, dan 6 REVIEW untuk backlog mingguan/ujian. Status itu tidak membuktikan bahwa file terkait sudah tersedia di repo.

Kebutuhan sumber berikut diambil dari sheet Sources, tetapi isi dokumennya belum tersedia secara lokal:

| Sumber | Diperlukan untuk | Perlakuan sebelum tersedia |
| --- | --- | --- |
| Kurikulum OBE IF 2025 — Revisi 2026 | Identitas, CPL, CPMK, BK, prasyarat | Identitas dan kode outcome workbook dicatat sebagai data awal; kesesuaian resmi belum disahkan |
| RPS 2026–2027 | Cakupan, durasi, capaian, bobot nilai, bibliografi | Rancangan konten dapat dibuat; bobot, durasi, dan ketentuan resmi ditandai `PERLU KONFIRMASI SUMBER` |
| RTM IF24A/IF24H | Instruksi tugas, luaran, rubrik | Rancangan tugas diberi label usulan; belum dianggap RTM resmi |
| Materi minggu 1–3 dan storyboard minggu 4 | Audit dan penggunaan kembali materi | Catatan workbook tentang materi lama tidak diperlakukan sebagai isi materi tersebut |
| Tracker IF24A/IF24H | Bukti pelaksanaan, mastery, revisi | Hanya siapkan format kosong; jangan mengarang data mahasiswa |

Sumber yang belum tersedia tidak menghentikan penyusunan struktur, rancangan konten, dan contoh simulasi. Namun, finalisasi keselarasan kurikulum serta asesmen resmi menunggu pemeriksaan sumber tersebut. Materi teknis akan memakai sumber otoritatif yang benar-benar dibaca, misalnya dokumentasi scikit-learn dan buku rujukan yang dipilih; sitasi dicatat bersama bagian yang didukungnya.

## 3. Struktur repo yang akan dibuat

```text
README.md                         # Pintu masuk dan cara menggunakan paket
PRODUCTION_PLAN.md                # Rencana ini
planning/                         # Baseline, spesifikasi, blueprint, gate, prompt, dan handoff template
references/                       # Sumber unggahan asli, dipertahankan utuh
course/
  index.md                        # Navigasi seluruh semester
  governance/                     # SEM-01 sampai SEM-04
  semester/                       # SEM-05 sampai SEM-10
  standards/                      # SEM-11: standar konten, pedagogi, format, dan QA
  production/                     # SEM-12: dashboard dan backlog Markdown
    sources.md
    decisions.md
    semester-backlog.md
    weekly-backlog.md
    dashboard.md
    reports/                      # Ticket, laporan validasi/review, dan handoff saat produksi
  templates/                      # Format kerja yang digunakan ulang
  weeks/
    w01/ ... w07/
    w09/ ... w15/                  # 14 folder minggu pembelajaran
  exams/
    uts/                          # Minggu 8
    uas/                          # Minggu 16
```

File dapat ditambahkan untuk navigasi dan template di luar 222 artefak utama. Jumlah file bukan ukuran selesainya produksi. Folder dan judul memakai identitas stabil, misalnya `W04-BOOK` dan `SEM-02`, agar tetap dapat ditelusuri ke workbook.

## 4. Paket tingkat semester: 12 artefak

| ID | File yang direncanakan | Isi dan kriteria selesai |
| --- | --- | --- |
| SEM-01 | `course/governance/curriculum-audit.md` | Audit identitas, CPL/CPMK/BK, prasyarat; konflik dan sumber resolusinya tercatat |
| SEM-02 | `course/governance/rps.md` | RPS Markdown hasil pemeriksaan sumber, dengan peta mingguan, asesmen, dan bibliografi |
| SEM-03 | `course/governance/rtm.md` | RTM master: tugas, luaran, instruksi, dependensi, dan rubrik yang dapat dijalankan |
| SEM-04 | `course/governance/assessment-blueprint.md` | Pemetaan outcome–asesmen–bukti–level kognitif; bobot mengikuti RPS terverifikasi |
| SEM-05 | `course/semester/learning-architecture.md` | Alur semester, prasyarat antarminggu, WHY/WHAT/HOW, dan adaptasi IF24A/IF24H |
| SEM-06 | `course/semester/book-toc.md` | Daftar isi 14 bab dengan integrasi ujian dan proyek |
| SEM-07 | `course/semester/project-architecture.md` | Tahap proyek W12–W15, luaran, responsible AI, reproduksibilitas, dan rubrik |
| SEM-08 | `course/semester/lms-skeleton.md` | Struktur 16 minggu, penamaan, materi, aktivitas, dan alur pengumpulan untuk LMS |
| SEM-09 | `course/semester/mastery-tracker.md` | Definisi mastery, format pencatatan bukti, dan tindakan remediasi; tanpa data mahasiswa rekaan |
| SEM-10 | `course/semester/question-bank.md` | Bank soal bertag minggu, konsep, outcome, tingkat kesulitan, dan rujukan kunci |
| SEM-11 | `course/standards/teaching-package-os.md` | Standar produksi Markdown turunan master prompt; hierarki informasi dan pedagogi |
| SEM-12 | `course/production/dashboard.md` dan backlog terkait | Kendali status, dependensi, sumber, QA, dan tautan artefak; perubahan tidak menimpa workbook asli |

RPS dan RTM yang belum diverifikasi harus diberi judul/status rancangan, bukan dinyatakan resmi. Penyelesaian dokumen di repo tidak menggantikan pengesahan institusi.

## 5. Peta semester

Topik dan kode berikut disalin sebagai baseline dari workbook, bukan hasil audit terhadap kurikulum resmi.

| Minggu | Topik | Sub-CPMK baseline | Paket |
| --- | --- | --- | --- |
| 1 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | W01 |
| 2 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | W02 |
| 3 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | W03 |
| 4 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | W04 |
| 5 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | W05 |
| 6 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | W06 |
| 7 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | W07 |
| 8 | UTS | DAIML-Sub-CPMK102-1 | UTS |
| 9 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | W09 |
| 10 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | W10 |
| 11 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | W11 |
| 12 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | W12 |
| 13 | Responsible AI | DAIML-Sub-CPMK082-1 | W13 |
| 14 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | W14 |
| 15 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | W15 |
| 16 | UAS | DAIML-Sub-CPMK082-1 | UAS |

Minggu 15 memakai format klinik/presentasi proyek untuk bab, modul, dan lab; tidak dipaksakan menjadi kuliah algoritma baru. Cakupan UTS/UAS diperiksa terhadap RPS, bukan ditentukan hanya dari satu kode outcome pada baris workbook.

## 6. Paket setiap minggu pembelajaran: 14 artefak

Setiap folder minggu memiliki `index.md` untuk navigasi dan 14 artefak berikut. `Wnn` diganti dengan nomor minggu.

| ID | Nama file | Isi minimum |
| --- | --- | --- |
| Wnn-BOOK | `book-chapter.md` | Outcome, prasyarat, WHY, intuisi, definisi formal, konsep, mekanisme/formula, worked example, kesalahan umum, penerapan, rangkuman, dan sumber |
| Wnn-MOD | `student-module.md` | Jalur belajar mahasiswa, bacaan, aktivitas, latihan, tugas, refleksi, dan mastery checkpoint |
| Wnn-GUIDE | `lecturer-guide.md` | Agenda, alokasi waktu berstatus rancangan jika durasi belum diketahui, hook, demo, pertanyaan, debrief, dan adaptasi kedua kelas |
| Wnn-STORY | `storyboard.md` | Alur slide, peran pedagogi, satu pesan utama, arsitektur informasi, visual yang diusulkan, interaksi, dan takeaway |
| Wnn-SLIDE | `slides.md` | Naskah slide siap ditelaah: judul, teks, diagram/tabel, catatan penjelasan, sitasi, takeaway; belum berupa deck visual |
| Wnn-DATA | `dataset-case.md` | Konteks kasus, asal data/lisensi bila relevan, data dictionary, target, batas penggunaan, dan contoh simulasi berlabel |
| Wnn-LAB | `lab.md` | Lab berbentuk Markdown: prasyarat runtime, starter code, langkah, pengujian perilaku, hasil yang diharapkan, dan rujukan solusi |
| Wnn-WORK | `worksheet.md` | Prediksi, perhitungan, perbandingan, kritik, dan latihan yang meminta alasan, bukan hanya jawaban |
| Wnn-AIP | `ai-learning-prompts.md` | Prompt tutor/critic/checker; cara memeriksa output AI dan batas bantuan dalam tugas |
| Wnn-ASSESS | `assignment-quiz.md` | Instruksi tugas/kuis, luaran, cakupan, estimasi usaha, ketentuan bantuan AI, dan pemetaan outcome |
| Wnn-RUBRIC | `rubric-answer-key.md` | Kunci, penalaran, alternatif jawaban, kriteria, skor, dan contoh penilaian |
| Wnn-LMS | `lms-package.md` | Teks pengantar, urutan akses, petunjuk forum/kuis/upload, serta daftar file untuk unggah manual |
| Wnn-EVID | `evidence-spec.md` | Spesifikasi bukti mastery dan format pengumpulan; bukti aktual ditambahkan hanya jika tersedia |
| Wnn-QA | `post-class-qa.md` | Checklist pra-kelas dan format KEEP/FIX/ADD/REMOVE; hasil pascakelas menunggu bukti pelaksanaan |

Kode Python disimpan dalam fenced code blocks, sehingga materi tetap Markdown. Kode dieksekusi lewat berkas sementara di luar artefak terbit dan dicatat hasil verifikasinya. Starter dan solusi dipisahkan secara jelas dalam naskah; kunci/rubrik ditandai **dosen**. Paket mahasiswa tidak menyertakan kunci ujian/tugas secara otomatis. Jika kelak dibutuhkan notebook atau dataset fisik, itu menjadi keluaran tambahan yang disepakati, bukan diklaim tersedia dari file Markdown saja.

Target awal storyboard adalah sekitar 20 slide per pertemuan reguler, mengikuti master prompt. Jumlah final menyesuaikan isi dan durasi terverifikasi. W15 dapat memakai format presentasi/klinik proyek. Minimal satu worked example, satu pembahasan miskonsepsi, aktivitas mahasiswa, dan exit ticket masuk bila sesuai tujuan pertemuan.

## 7. Paket UTS dan UAS: masing-masing 7 artefak

| Sufiks ID workbook | File | Isi |
| --- | --- | --- |
| BLUEPRINT | `blueprint.md` | Cakupan, indikator, level kognitif, proporsi, dan pemetaan ke outcome |
| QUESTION | `question-set.md` | Soal dengan instruksi, data/contoh, dan alokasi skor yang konsisten |
| KEY | `answer-key-rubric.md` | Kunci dan rubrik dosen untuk penilaian konsisten |
| INSTR | `instructions.md` | Ketentuan akademik/teknis, bantuan AI, pengumpulan, dan waktu berdasarkan sumber resmi |
| LMS | `lms-package.md` | Panduan implementasi manual; tidak menyatakan LMS telah dikonfigurasi |
| EVID | `evidence-archive-spec.md` | Struktur arsip dan bukti pelaksanaan; belum berisi hasil ujian |
| QA | `post-exam-analysis.md` | Metode analisis soal/mastery dan format remediasi; diisi setelah hasil tersedia |

Soal latihan yang boleh dibagikan dan soal ujian yang masih rahasia dibedakan dalam indeks serta paket terbit. Menulis soal di repo tidak berarti ujian sudah dilaksanakan.

## 8. Urutan produksi

### Tahap A — Fondasi dan penelusuran sumber

1. Ekstrak seluruh 12 + 210 ID, dependensi, status sumber, prioritas, dan Definition of Done ke backlog Markdown; pertahankan workbook asli.
2. Buat register sumber, catatan keputusan, template artefak, dan indeks semester.
3. Susun audit kurikulum, rancangan peta semester, daftar isi buku, dan blueprint asesmen berdasarkan data yang tersedia.
4. Catat pertanyaan sumber secara spesifik: bobot resmi, durasi, prasyarat, bibliografi, aturan tugas, serta perbedaan IF24A/IF24H.

Keluaran: struktur kerja lengkap, semua ID terlacak, ketidakpastian terlihat. Tahap ini tidak menunggu seluruh sumber tersedia, tetapi keputusan yang bergantung pada sumber tetap berstatus rancangan.

### Tahap B — Paket minggu 4 sebagai contoh lengkap

Urutan: scope/outcome → bab → modul dan panduan dosen → dataset/kasus, lab, worksheet → asesmen dan rubrik → storyboard dan naskah slide → paket LMS → spesifikasi bukti → format QA.

Fokus substansi: train/validation/test, pemilihan strategi split, cross-validation, data leakage, preprocessing di dalam pipeline, dan evaluasi yang jujur. Gunakan contoh deterministik yang memperlihatkan perilaku benar dan kesalahan yang perlu dihindari. Kode dan hasil numerik diverifikasi; klaim performa tidak dibuat tanpa eksekusi.

Keluaran: 14 artefak W04 dengan isi, hubungan, dan pemeriksaan mutu yang nyata. Artefak yang memerlukan sumber resmi atau bukti pelaksanaan tetap ditandai menunggu; tidak dihitung selesai hanya karena file dibuat. Review W04 menetapkan pola untuk minggu berikutnya.

### Tahap C — Lengkapi minggu 1–3

Audit materi lama jika telah tersedia, lalu produksi W01, W02, dan W03 dengan standar W04. Pastikan istilah data, fitur, label, model, training, inference, dan evaluasi konsisten. Penjelasan preprocessing W03 harus menghindari leakage dan tersambung ke W04.

### Tahap D — Minggu 5–7 dan UTS

Produksi satu paket minggu sampai dapat direview sebelum pindah ke minggu berikutnya. UTS disusun dari outcome dan materi yang benar-benar tercakup pada W01–W07 serta ketentuan RPS. Bank soal semester diperbarui dari asesmen mingguan yang sudah diperiksa.

### Tahap E — Minggu 9–11

Bangun kesinambungan model selection → generalisasi/regularisasi → jaringan syaraf. Periksa konsistensi metrik, baseline, validasi, serta perbedaan optimisasi training dan evaluasi generalisasi. Pilih lab ringan berbasis CPU; ketergantungan GPU/API berbayar bukan syarat dasar sebelum ada kebutuhan yang jelas.

### Tahap F — Minggu 12–15 dan UAS

Produksi pengantar deep learning/GenAI, responsible AI, pipeline reproduksibel, dan presentasi proyek. Lengkapi arsitektur proyek, tahapan proposal sampai demo, bukti kontribusi, rubrik, dan alternatif aktivitas tanpa layanan berbayar. Susun UAS mengikuti RPS dan keterkaitannya dengan proyek, bukan asumsi bentuk ujian.

### Tahap G — Integrasi dan pemeriksaan semester

Periksa seluruh 222 artefak utama, navigasi, daftar sumber, outcome–materi–latihan–asesmen–rubrik, konsistensi terminologi, serta adaptasi IF24A/IF24H. Siapkan indeks paket mahasiswa dan dosen. Laporkan dokumen yang dapat dipakai, yang masih rancangan, serta yang menunggu bukti kelas/ujian.

Tidak ada tanggal selesai yang dijanjikan sebelum durasi kelas, sumber akademik, dan volume review diketahui. Pekerjaan dibagi per tahap dan per paket minggu agar setiap hasil dapat ditelaah.

## 9. Standar penulisan dan pemeriksaan mutu

Bahasa utama Indonesia; istilah teknis Inggris diperkenalkan bersama penjelasannya. Setiap artefak diawali metadata sederhana: ID, minggu, audiens, status produksi, status pemeriksaan sumber, sumber utama, dependensi, dan catatan validasi. Dokumen yang berisi kunci ditandai untuk dosen.

Setiap paket melewati pemeriksaan berikut:

1. **Sumber dan keselarasan:** fakta, istilah, outcome, kebijakan, dan bobot dapat ditelusuri; ketidakpastian diberi label.
2. **Akurasi:** definisi, formula, hitungan, tabel, dan kode diperiksa. Simulasi dibedakan dari data nyata. Sitasi tidak direka.
3. **Pedagogi:** WHY → intuisi → konsep → mekanisme → contoh → praktik → refleksi; pengetahuan awal dan miskonsepsi tercakup.
4. **Keterlaksanaan:** mahasiswa dapat memahami input, tugas, luaran, serta kriteria; dosen dapat menggunakan panduan dan rubrik.
5. **Koherensi:** bab, modul, lab, worksheet, soal, kunci, storyboard, dan slide memakai istilah serta contoh yang selaras.
6. **Validasi teknis:** tautan relatif dan ID diperiksa; contoh kode penting benar-benar dijalankan; hasil yang dicatat berasal dari run tersebut.
7. **Kelengkapan:** isi bukan sekadar heading/template. Artefak pascakelas dan pascaujian dibedakan dari materi siap ajar.

Diagram Mermaid atau tabel dipakai jika membantu penjelasan. Detail visual 16:9, palet navy/cyan, dan takeaway tetap menjadi spesifikasi dalam naskah slide; keberadaan Markdown tidak membuktikan deck visual sudah dirender.

## 10. Kendali status dan definisi selesai

Backlog Markdown menyimpan **status sumber** dan **status produksi repo** secara terpisah. Status sumber dibekukan sebagai baseline impor; status repo berubah mengikuti bukti pekerjaan. Setiap baris memuat ID, path, dependensi, prioritas, blocker, hasil QA, dan langkah berikutnya.

Gunakan lifecycle workbook: NOT STARTED → DRAFT → REVIEW → READY → PUBLISHED → DELIVERED. File dengan kerangka saja masih DRAFT atau NOT STARTED menurut kondisi isinya. REVIEW berarti isi tersedia untuk ditelaah, bukan persetujuan dosen. READY hanya dipakai jika Definition of Done terpenuhi dan pemeriksaan wajib selesai. PUBLISHED memerlukan bukti publikasi; DELIVERED memerlukan bukti penggunaan.

Sheet Definitions juga menetapkan **IMPROVE (0,85)** untuk materi yang sudah digunakan dan perlu perbaikan; ini cabang revisi setelah pelaksanaan, bukan urutan wajib menuju READY. Status sumber dan status repo menggunakan lifecycle tersebut, sedangkan **kesiapan Markdown** dan **pemenuhan DoD asli** dicatat terpisah. Naskah slide/lab/paket LMS dapat selesai sebagai Markdown sebelum deck/notebook/implementasi LMS selesai. Detail aturan ada di pedoman eksekusi dan spesifikasi artefak.

Pisahkan laporan kesiapan materi dari penyelesaian semester:

- Materi pra-kelas dapat selesai diproduksi dan diperiksa di repo.
- Pengesahan kurikulum/asesmen memerlukan verifikasi sumber dan keputusan pihak berwenang.
- Evidence dan analisis pascakelas/pascaujian dapat disiapkan sebagai spesifikasi, tetapi menunggu data aktual untuk selesai.
- Publikasi LMS, commit/push, serta pelaksanaan kelas tidak diasumsikan terjadi hanya karena Markdown tersimpan.

**Tindakan berikut saat produksi dimulai:** Tahap A, kemudian paket W04. Tidak perlu membuat seluruh materi sekaligus untuk memeriksa pola; setelah contoh W04 ditelaah, lanjutkan seluruh cakupan dengan status dan blocker yang tetap terlihat.

## 11. Keputusan desain yang sudah ditetapkan untuk rencana

| Area | Keputusan kerja | Alasan dan batas |
| --- | --- | --- |
| Format | Semua keluaran produksi utama berupa Markdown; sumber asli dipertahankan | Sesuai permintaan pengguna; format terbit lain belum dikerjakan |
| Baseline | Pertahankan 222 ID asli, tidak menambah jumlah karena helper/template | Mencegah progres semu dan duplikasi artefak |
| Bahasa | Indonesia dengan istilah teknis dijelaskan | Sesuai konteks kelas; kutipan/sitasi tetap akurat |
| Urutan produksi | W04 lebih dulu, lalu W01–03 dan gelombang berikutnya | Mengikuti prioritas workbook; urutan belajar mahasiswa tetap W01→W02→W03→W04 |
| Contoh | Simulasi mandiri atau dataset yang asalnya dapat diverifikasi | Jangan menggambarkan simulasi sebagai bukti empiris Indonesia/UAI |
| Runtime dasar | Rancangan praktik Python berbasis CPU dengan jalur tanpa API berbayar | Versi paket diperiksa saat produksi; bukan klaim dependensi sudah terpasang |
| Slide | Storyboard dan naskah terpisah; sekitar 20 slide sebagai awal, bukan kuota mutlak | Kepadatan, durasi, dan aktivitas lebih penting dari hitungan slide |
| Penalaran | Tinggi untuk keputusan/validasi konseptual; sedang untuk derivasi dari bahan yang stabil | Prompt dan ticket mengurangi beban penafsiran ulang |
| Publikasi | Hasil repo tidak otomatis dikirim ke LMS/Drive atau dipush | Tahap ini menyiapkan bahan dan rencana yang dapat diperiksa |

## 12. Keputusan yang masih terbuka dan default sementara

| ID kebutuhan | Informasi yang belum ada | Pekerjaan yang terdampak | Default sementara yang diperbolehkan |
| --- | --- | --- | --- |
| OPEN-01 | Versi kurikulum/RPS/RTM resmi dan isi lengkap | SEM-01–04, outcome, bobot, kebijakan | Gunakan topik/kode baseline; rumusan baru sebagai usulan; finalisasi resmi ditunda |
| OPEN-02 | Durasi pertemuan dan pola IF24A/IF24H | Agenda, workload, LMS, aktivitas | Sediakan adaptasi tatap muka/asinkron sebagai opsi, bukan menetapkan jadwal/format kelas |
| OPEN-03 | Materi W01–03 dan storyboard W04 yang disebut workbook | Audit penggunaan kembali | Produksi draft baru berlabel; cocokkan jika materi lama tersedia kemudian |
| OPEN-04 | Dataset dan kebutuhan lingkungan praktik yang diutamakan dosen | Kasus, lab, tugas/proyek | Kasus sintetis kecil berbasis CPU tanpa unduhan wajib; pilihan dicatat sebagai keputusan usulan |
| OPEN-05 | Bentuk/bobot UTS, UAS, dan proyek serta kebijakan AI | Paket ujian, RTM, rubrik | Buat rancangan alternatif yang konsisten; tidak memilih aturan resmi tanpa sumber |
| OPEN-06 | Hak akses repo dan skema berbagi materi dosen/mahasiswa | Kunci soal, solusi, paket distribusi | Label audiens dan indeks terpisah; label/folder tidak dianggap kontrol akses |
| OPEN-07 | Bukti pelaksanaan dan hasil belajar aktual | EVID, QA, mastery, analisis ujian | Format/spesifikasi disiapkan; field hasil nyata dibiarkan kosong dengan alasan |

Kebutuhan ini bukan daftar pertanyaan yang harus dijawab sebelum pekerjaan dimulai. Sumber/keputusan diminta saat benar-benar menghambat target. Pekerjaan independen tetap dilanjutkan; draft tidak berubah menjadi keputusan akademik resmi hanya karena belum ada jawaban.

## 13. Pemetaan belajar dan pengendalian perubahan

Setiap tujuan usulan memakai ID lokal, misalnya `W04-LO01`, yang tidak menggantikan `DAIML-Sub-CPMK102-1`. Hubungkan tujuan → bagian bab → contoh/latihan → item asesmen → kriteria rubrik → bukti belajar. Gunakan ID stabil untuk contoh, soal, slide, dan bukti sesuai spesifikasi.

Jika sumber atau konsep berubah, telusuri semua artefak turunan; beri status review STALE di catatan pemeriksaan sampai bagian terkait diperiksa kembali. Perubahan angka contoh harus diterapkan ke bab, worksheet, lab, kunci, storyboard, dan naskah yang menggunakan angka itu. Catat versi input pada review/handoff agar sesi berikut tidak memakai hasil yang sudah usang.

Rencana ini boleh dipertajam berdasarkan review pilot. Perubahan jumlah/cakupan artefak, rumusan outcome resmi, atau DoD dicatat sebagai keputusan eksplisit; baseline sumber tidak ditimpa untuk menyembunyikan perbedaan.

## 14. Hasil yang harus tersedia sebelum ekspansi besar

Pilot W04 menentukan apakah produksi dapat diperluas dengan prompt sedang/tinggi. Pemeriksa harus dapat memastikan:

1. Seluruh 14 artefak W04 dapat ditemukan, memiliki isi sesuai peran, dan saling tersambung.
2. Cakupan inti, contoh, latihan, soal, dan rubrik terpetakan; istilah dan angka konsisten.
3. Lab penting benar-benar diuji dengan laporan hasil, atau blocker teknisnya jelas dan tidak disebut lulus.
4. Prompt target dapat dipakai dari ticket/context pack tanpa bergantung pada memori percakapan lama.
5. Status Markdown, DoD asli, kebutuhan sumber, dan pekerjaan pascakelas dilaporkan terpisah.
6. Review pilot menghasilkan perbaikan template/prompt yang nyata sebelum digunakan pada minggu berikutnya.

Hasil pilot tidak mensyaratkan pelaksanaan kelas sudah terjadi. Yang diperiksa adalah pola produksi materi dan spesifikasi bukti, bukan mengarang hasil mahasiswa.

## 15. Cara melanjutkan nanti

Untuk eksekusi fondasi, gunakan contoh instruksi akhir di [template sesi](planning/SESSION_TEMPLATES.md). Setelah A01, ticket/handoff akan menunjuk batch dan prompt berikutnya. Untuk minggu, pilih scope dan bab dengan tinggi, lalu dokumen turunannya dengan sedang, serta praktik/asesmen/review dengan tinggi sesuai pedoman.

Tidak perlu mengeksekusi seluruh semester dalam satu permintaan. Setiap batch menyimpan hasil ke repo, pemeriksaan yang benar-benar dilakukan, kebutuhan yang belum terpenuhi, dan ticket lanjutan. Rencana ini selesai ketika dokumen instruksi dan cakupannya konsisten; produksi isi dimulai setelah perintah produksi berikutnya.
