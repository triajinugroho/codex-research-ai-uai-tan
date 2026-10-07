# Spesifikasi Artefak Produksi Bahan Ajar

Dokumen kerja berbahasa Indonesia untuk **Dasar Kecerdasan Artifisial dan Pembelajaran Mesin**, kode baseline **IF52510031**, kelas **IF24A dan IF24H**, tahun akademik **2026–2027**. Status dokumen ini: **spesifikasi rencana**, bukan bahan ajar atau bukti pelaksanaan. Identitas akademik masih mengikuti baseline workbook sampai sumber resmi diperiksa.

Gunakan bersama [rencana produksi](../PRODUCTION_PLAN.md), [baseline workbook](WORKBOOK_BASELINE.md), [playbook eksekusi](EXECUTION_PLAYBOOK.md), [peta mingguan](WEEKLY_BLUEPRINTS.md), [pustaka prompt](PROMPT_LIBRARY.md), dan [quality gates](QUALITY_GATES.md). Sumber desain yang dibaca adalah [Master Prompt Package](../references/Master_Prompt_Package_Slide_Mata_Kuliah_Tri_Aji.md); file sumber unggahan dipertahankan utuh.

## 1. Satuan produksi dan batas pemenuhan

Ada **222 artefak utama**: **12 semester + (14 minggu pembelajaran × 14 artefak) + (2 ujian × 7 artefak)**. Minggu pembelajaran adalah **W01–W07 dan W09–W15**; **UTS=W08**, **UAS=W16**. Satu SEM-12 dapat terdiri atas beberapa file kendali, tetapi tetap satu artefak workbook. Indeks, template, scope mingguan, register sumber, dan laporan QA adalah file pendukung; jumlah file tidak menjadi pengganti hitungan artefak.

Spesifikasi di bawah mendefinisikan **adaptasi keluaran Markdown**. Definition of Done asli workbook tetap dicatat di baseline. Contoh perbedaan yang wajib terlihat:

| Artefak | Yang dapat selesai pada produksi Markdown | Yang memerlukan keluaran/bukti tambahan |
| --- | --- | --- |
| SLIDE | Naskah slide, diagram/tabel teks, speaker notes, sitasi | Deck/render visual sesuai DoD asli bila diminta kemudian |
| LAB | Panduan, starter/solusi di fenced code blocks, hasil run terverifikasi | Notebook/dataset fisik sesuai DoD asli bila menjadi keluaran lanjutan |
| LMS | Naskah, urutan, konfigurasi usulan, manifest unggah manual | Publikasi/konfigurasi LMS yang benar-benar dilakukan |
| EVID | Definisi bukti, skema arsip, contoh sintetis berlabel bila dibutuhkan | Bukti kerja/kelas/ujian aktual dan izin penggunaan yang relevan |
| QA pascakelas/pascaujian | Instrumen, metode analisis, format temuan/tindak lanjut | Analisis berdasarkan pelaksanaan dan hasil aktual |
| RPS/RTM/blueprint resmi | Rancangan dengan provenance dan daftar keputusan terbuka | Sumber resmi terverifikasi dan pengesahan yang benar-benar tersedia |

Pisahkan `source_status`, `production.repo_status`, `markdown_readiness`, `fulfillment`, dan `delivery_evidence`. **`production.repo_status: READY` menilai DoD asli**, sedangkan **`markdown_readiness: VALIDATED` menilai adaptasi naskah**. Naskah tervalidasi tidak boleh dilaporkan sebagai deck sudah jadi, LMS terpublikasi, atau semester telah selesai. PUBLISHED/DELIVERED membutuhkan bukti tindakan terkait. IMPROVE dipakai ketika revisi berdasarkan penggunaan nyata telah dimulai; bukan langkah wajib untuk semua artefak yang belum digunakan.

Setiap artefak mempunyai fungsi berbeda; menyalin bab yang sama ke modul, panduan, slide, dan lab tidak memenuhi spesifikasi hanya karena jumlah file sudah sesuai.

## 2. Kontrak metadata bersama

Setiap artefak utama memuat metadata di awal. YAML berikut adalah **template**, bukan klaim adanya file atau validasi W04. Placeholder harus diganti sebelum REVIEW; placeholder yang bergantung pada sumber resmi tetap terlihat dan tercatat sebagai blocker.

```yaml
---
artifact_id: W04-BOOK
title: "[Judul sesuai scope yang disepakati]"
course_code: IF52510031
period: "2026–2027"
week: 4                  # null untuk artefak semester; 8/16 untuk ujian
classes: [IF24A, IF24H]
audience: mahasiswa      # mahasiswa | dosen | keduanya
distribution: student_candidate  # student_candidate | instructor_only | mixed_split_required
version: "0.1"
updated_at: "[YYYY-MM-DD aktual]"
owner: "[penanggung jawab produksi]"
source_status: "[nilai impor; jangan ditulis ulang dari status repo]"
production:
  repo_status: DRAFT      # lifecycle asli; READY hanya bila DoD asli terbukti
markdown_readiness: DRAFT # NOT_STARTED | DRAFT | IN_REVIEW | VALIDATED
fulfillment: NOT_FULFILLED # NOT_FULFILLED | PARTIAL | FULFILLED
source_verification: NOT_CHECKED # NOT_CHECKED | PARTIAL | VERIFIED_FOR_SCOPE | CONFLICT
official_alignment: PROVISIONAL # PROVISIONAL | VERIFIED_AGAINST_SOURCE
learning_ids: [W04-LO01]
official_outcome_refs: [DAIML-Sub-CPMK102-1] # baseline, bukan verifikasi keselarasan
assessment_ids: [W04-ASM01]
example_ids: [W04-EX01]
evidence_requirement_ids: [W04-EV01]
source_ids: [SRC-WORKBOOK, SRC-MASTER-PROMPT]
dependencies: [SEM-05, SEM-06] # rancangan fondasi tersedia; scope_record adalah input awal
integration_refs: [W03-BOOK, W04-LAB, W04-ASSESS] # backrefs; tidak memblokir draft pilot W04
workbook_dependencies: "[nilai impor asli, termasuk bila berupa label, bukan ID]"
scope_record: "course/weeks/w04/scope.md" # file pendukung yang direncanakan
validation_records: []   # isi hanya dengan laporan pemeriksaan yang benar-benar dilakukan
blockers: ["[ketidakpastian yang memengaruhi pemakaian]" ]
class_adaptations: PROVISIONAL
delivery_evidence: []    # kosong sampai ada publikasi/penggunaan nyata
---
```

`source_ids` memuat sumber yang benar-benar dipakai artefak; contoh dua ID di atas tidak menyatakan bahwa keduanya mendukung isi teknis bab. Sumber desain mendukung desain, bukan klaim akurasi algoritma. `blockers: []` berarti tidak ada blocker yang diketahui setelah pemeriksaan, bukan belum melakukan pemeriksaan. `fulfillment: FULFILLED` memerlukan pemetaan dan bukti lengkap; jangan memakai alasan “tidak berlaku” untuk menyembunyikan keluaran asli yang belum dibuat. NOT_FULFILLED berarti pemenuhan belum terbukti; catatan validasi menerangkan apakah sudah diperiksa atau belum.

`source_status` menyimpan status workbook asli dan immutable. `production.repo_status` mengikuti **NOT STARTED, DRAFT, REVIEW, READY, PUBLISHED, DELIVERED, IMPROVE**. Enum readiness Markdown menggunakan underscore seperti pada template; blocker disimpan terpisah dan bukan status readiness tambahan. Review naskah memakai IN_REVIEW, bukan status REVIEW sumber.

`source_verification: VERIFIED_FOR_SCOPE` berarti klaim yang diperlukan dalam scope naskah telah didukung, bukan semua sumber resmi semester telah tersedia. Bab teknis dapat VALIDATED ketika substansinya terverifikasi, sementara `official_alignment: PROVISIONAL` dan `fulfillment: PARTIAL` tetap jujur terhadap keselarasan resmi/keluaran asli. Jika sumber yang hilang mendukung klaim inti yang masih digunakan, naskah tetap DRAFT/IN_REVIEW sampai klaim diperiksa, dihapus, atau scope direvisi secara sah.

Metadata dapat berupa tabel jika parser YAML tidak dipakai, tetapi nama, arti, dan nilai status harus konsisten. Field durasi, bobot nilai, bentuk ujian, prasyarat formal, mode kelas, dan aturan penggunaan AI hanya diberi nilai final dari sumber resmi yang dibaca. Usulan dapat disimpan dengan label **USULAN / PERLU KONFIRMASI SUMBER**.

### 2.1 ID stabil dan provenance

| Objek | Pola ID | Aturan |
| --- | --- | --- |
| Artefak semester/minggu/ujian | `SEM-01`, `W04-BOOK`, `UTS-BLUEPRINT` | Pertahankan ID workbook; nama file dapat berubah melalui catatan migrasi |
| Tujuan belajar lokal | `W04-LO01` | Target teramati untuk produksi; tidak mengganti kode CPL/CPMK/Sub-CPMK resmi |
| Contoh / kegiatan | `W04-EX01` / `W04-ACT01` | Gunakan ulang pada bab, lab, worksheet, dan slide; perubahan data dicatat |
| Asesmen / soal | `W04-ASM01` / `W04-Q01`; `UTS-Q01` | Satu ID untuk satu butir; jangan membuat ID baru hanya karena pindah file |
| Kriteria rubrik | `W04-RC01`; `UTS-RC01` | Tautkan ke asesmen, bukti yang diamati, dan bobotnya |
| Spesifikasi bukti | `W04-EV01`; `UTS-EV01` | Menunjuk jenis bukti; berbeda dari ID rekaman bukti aktual |
| Slide | `W04-SL01` | Tetap stabil saat urutan berubah; nomor tampil disimpan terpisah |
| Sumber workbook | `S01`–`S06` | Pertahankan ID dan label asli; isi belum tersedia tidak berarti telah dibaca |
| Sumber lokal / teknis baru | `SRC-WORKBOOK`, `SRC-MASTER-PROMPT`, `SRC-TECH-001` | ID teknis baru hanya dibuat ketika sumber nyata didaftarkan; contoh pola bukan bibliografi |
| Temuan / run | `QA-W04-001`, `RUN-W04-001` | Hanya diterbitkan untuk pemeriksaan/run yang terjadi; log bantu di `course/production/reports/` |

Register sumber menyimpan crosswalk **S06 ↔ SRC-MASTER-PROMPT** dengan catatan bahwa label workbook dan nama berkas unggahan mungkin berbeda; jangan mengklaim versi atau isi identik tanpa pemeriksaan. Satu sumber mencatat judul asli, penulis/organisasi bila tersedia, lokasi file/URL, tanggal akses aktual, bagian/halaman/anchor pendukung, status baca/verifikasi, batas pemakaian, dan artefak pengguna.

Gunakan status **per sumber**: `VERIFIED_LOCAL` (file lokal dibaca dan bagian relevan diperiksa), `VERIFIED_EXTERNAL` (sumber eksternal benar-benar diakses/dibaca), `LINK_ONLY` (hanya tautan/label tersedia), `UNAVAILABLE` (sumber yang diperlukan belum dapat diperiksa), dan `CONFLICT` (perbedaan yang belum terselesaikan). Lokasi lokal/eksternal tidak menyatakan otoritas akademik; verifikasi isi, kecukupan bagi klaim, dan pengesahan institusi tetap berbeda. Status per sumber ini tidak mengganti `source_status` lifecycle baseline.

Klaim teknis, kebijakan, angka, dan formula mempunyai locator sumber pada bagian yang relevan. Jika halaman tidak tersedia, gunakan heading/section yang benar-benar ada. Contoh sintetis diberi label, generator/seed dicatat, dan tidak diberi provenance seolah data riil. Jangan mengarang DOI, tahun, kutipan, lisensi, atau hasil benchmark.

### 2.2 Matriks penelusuran minimal

Isi matriks berikut dengan baris untuk **setiap LO dan asesmen**, bukan hanya satu contoh. Sel kosong harus memiliki alasan dan tindak lanjut.

| LO lokal | Outcome resmi + status | Bagian materi | Aktivitas/contoh | Asesmen/soal | Rubrik | Bukti | Sumber substansi |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `[Wnn-LOxx]` | `[kode baseline; belum diverifikasi]` | `[artefak + heading]` | `[ACT/EX]` | `[ASM/Q]` | `[RC]` | `[EV]` | `[SRC + locator]` |

LO memakai verba teramati seperti menjelaskan, memilih dengan alasan, menghitung, membandingkan, menguji, atau mengkritik. Kata “memahami” perlu diturunkan menjadi perilaku yang dapat diperiksa. Level kognitif adalah label rancangan sampai kerangka dan cakupan resmi diverifikasi. Semua asesmen harus mengukur LO yang diajarkan; semua LO inti harus mempunyai cara memeriksa mastery atau alasan eksplisit mengapa belum dinilai.

## 3. Spesifikasi 12 artefak semester

Setiap subbagian memakai ID baseline. “Lulus Markdown” berarti isi naskah memenuhi spesifikasi berikut dan gate yang berlaku; tidak berarti otomatis resmi/published/delivered.

**Prasyarat awal** adalah input minimum untuk mulai draft, bukan kewajiban semua input sudah final. **Integrasi akhir** adalah referensi silang yang direkonsiliasi ketika tersedia. Jangan mengubah referensi integrasi menjadi blocker produksi yang menciptakan siklus RPS↔blueprint, modul↔lab, panduan↔storyboard, tracker↔evidence, atau standar↔pilot W04. Dependensi asli workbook tetap disimpan tersendiri; jika labelnya ambigu, catat pemetaan usulan tanpa mengubah baseline.

Prasyarat belajar juga berbeda dari file prasyarat produksi. Pilot W04 dapat menjelaskan kembali konsep data/fitur/label dan preprocessing secara singkat dari sumber yang telah diperiksa tanpa menunggu W01–W03 diproduksi. Scope menandai bridge tersebut dan kebutuhan integrasi W03; jangan mengklaim mahasiswa sudah mempelajari materi atau bab lama sudah tersedia.

### SEM-01 — Audit kurikulum

**Path:** `course/governance/curriculum-audit.md`. **Audiens:** dosen. **Input:** workbook, kurikulum/RPS resmi bila tersedia, register sumber.

- Isi: identitas mata kuliah, kode dan nama outcome, BK, prasyarat, posisi semester, crosswalk antarversi, serta tabel fakta baseline versus hasil verifikasi.
- Catat setiap konflik sebagai objek: fakta yang berbeda, dua locator sumber, dampak ke artefak, keputusan sementara, kebutuhan resolusi, dan penanggung jawab yang benar-benar ditetapkan atau “belum ditetapkan”.
- Lulus Markdown: seluruh kolom identitas/outcome baseline terpetakan; setiap nilai mempunyai sumber/status; tidak ada konflik yang dihapus diam-diam. Bagian belum tersedia diberi daftar kebutuhan yang spesifik.
- Pengesahan audit resmi tertahan jika sumber primer belum dibaca atau konflik memengaruhi outcome/prasyarat. Rancangan crosswalk tetap dapat dibuat.

### SEM-02 — RPS Markdown

**Path:** `course/governance/rps.md`. **Audiens:** keduanya. **Prasyarat awal:** SEM-01/baseline yang tersedia. **Integrasi akhir:** SEM-04, SEM-05, serta sumber resmi setelah tersedia.

- Isi: identitas, deskripsi, CPL/CPMK/Sub-CPMK, prasyarat, rancangan belajar, tabel 16 minggu, metode/aktivitas, asesmen, bibliografi, dan aturan yang benar-benar bersumber.
- Semua baris W01–W16 mempunyai topik, outcome, aktivitas, luaran/bukti, dan rujukan; W08/W16 dinyatakan ujian. Bobot/durasi yang belum terverifikasi ditulis sebagai nilai belum tersedia, bukan nol.
- Lulus Markdown: 16 baris lengkap; total bobot konsisten jika bobot resmi tersedia; cakupan cocok dengan audit dan blueprint; semua bagian usulan diberi label. Bibliografi hanya berisi sumber nyata.
- Judul “Rancangan RPS” dipertahankan sampai sumber resmi diperiksa. Tidak mengarang tanda tangan, tanggal pengesahan, SK, atau aturan institusi.

### SEM-03 — RTM master

**Path:** `course/governance/rtm.md`. **Audiens:** dosen, dengan bagian instruksi mahasiswa yang dapat dipisahkan. **Prasyarat awal:** rancangan SEM-02. **Integrasi akhir:** SEM-04, SEM-07; instruksi tugas direkonsiliasi setelah blueprint/proyek tersedia.

- Isi: katalog tugas bernomor stabil, tujuan, prasyarat, konteks, input, langkah, luaran, format pengumpulan, sumber daya, estimasi usaha sebagai usulan, rubrik, bantuan AI, dan remediasi.
- Bedakan tugas latihan, tugas dinilai, dan proyek; ketentuan kolaborasi/AI resmi belum tersedia ditandai. Setiap tugas menunjuk minggu, LO, asesmen, dan rubrik.
- Lulus Markdown: 100% tugas memiliki instruksi dan luaran yang dapat diperiksa; tidak ada skor/bobot yang bertentangan antarfile; panduan mahasiswa tidak memuat kunci yang belum layak dibagikan.
- Kesetaraan terhadap RTM resmi belum dapat dinyatakan dari rancangan ini saja.

### SEM-04 — Blueprint asesmen semester

**Path:** `course/governance/assessment-blueprint.md`. **Audiens:** dosen. **Prasyarat awal:** rancangan SEM-02/SEM-03 dan outcome baseline. **Integrasi akhir:** hasil audit SEM-01 dan paket asesmen yang diproduksi kemudian.

- Isi: matriks outcome–indikator–level kognitif–asesmen–bukti–kriteria; cakupan kuis/tugas/UTS/UAS/proyek; pola umpan balik dan remediasi.
- Pisahkan proporsi yang bersumber dari rancangan proporsi. Catat coverage gap, asesmen berulang tanpa alasan, dan keterampilan yang diuji sebelum diajarkan.
- Lulus Markdown: semua outcome inti baseline mempunyai rencana bukti; setiap asesmen menunjuk materi yang diajarkan; total skor/bobot dapat dihitung ulang jika nilainya sudah tersedia.
- Finalisasi nilai, bobot, cakupan resmi UTS/UAS tertahan oleh kebijakan/RPS yang belum terverifikasi. Rancangan butir dan matriks dapat dilanjutkan.

### SEM-05 — Arsitektur pembelajaran

**Path:** `course/semester/learning-architecture.md`. **Audiens:** dosen. **Prasyarat awal:** rancangan SEM-02, baseline semester, peta mingguan perencanaan. **Integrasi akhir:** audit SEM-01 dan scope mingguan ketika masing-masing diproduksi; tidak menunggu seluruh 14 scope untuk mulai.

- Isi: alur Govern → Know → Learn → Prove → Compound; peta prasyarat; tujuan dan titik transisi 14 minggu belajar + 2 ujian; WHY/WHAT/HOW; istilah bersama.
- Jelaskan sambungan EDA → preprocessing → validasi → pemodelan → generalisasi → proyek serta pencegahan leakage sejak W03/W04.
- Ada matriks adaptasi IF24A/IF24H yang menyimpan fakta diketahui, kebutuhan belum diketahui, versi inti, pilihan dukungan/pengayaan, dan risiko beban kerja.
- Lulus Markdown: tidak ada minggu hilang atau W08/W16 diperlakukan sebagai paket 14 artefak; setiap prasyarat memiliki tempat pengajaran; adaptasi tidak mengasumsikan mode/durasi kelas yang tidak bersumber.

### SEM-06 — Daftar isi buku semester

**Path:** `course/semester/book-toc.md`. **Audiens:** keduanya. **Prasyarat awal:** rancangan SEM-05 dan topik baseline. **Integrasi akhir:** scope/bab mingguan ketika tersedia.

- Isi: 14 bab untuk minggu pembelajaran, judul/ID, synopsis, LO, konsep dan prasyarat, contoh/lab, latihan, sumber inti, serta penghubung ke bab berikutnya.
- UTS/UAS ditautkan sebagai checkpoint tersendiri; W15 adalah sintesis/presentasi/klinik proyek, bukan bab algoritma baru yang dibuat demi simetri.
- Lulus Markdown: 14 bab terdaftar tepat sekali; hubungan bab–modul–lab–asesmen jelas; tidak ada klaim bab sudah ditulis bila baru synopsis.
- Daftar isi siap review tidak menandakan buku semester lengkap.

### SEM-07 — Arsitektur proyek

**Path:** `course/semester/project-architecture.md`. **Audiens:** keduanya, solusi/contoh penilaian dipisahkan. **Prasyarat awal:** rancangan SEM-03/04/05 yang tersedia. **Integrasi akhir:** scope W12–W15 dan ketentuan resmi proyek/UAS.

- Isi: masalah yang boleh dipilih, batas data, baseline, tahapan W12–W15, deliverable per milestone, responsible AI, keterulangan, kontribusi anggota, presentasi/demo, dan rubrik.
- Jelaskan data/target, split/validasi, metrik, keterbatasan, mitigasi bias, dokumentasi keputusan, serta bahan yang harus diserahkan untuk mereproduksi hasil.
- Sediakan jalur CPU/offline dan mekanisme demonstrasi bila layanan eksternal tidak tersedia; waktu, jumlah anggota, bobot, dan hubungan proyek–UAS tetap usulan jika sumber belum tersedia.
- Lulus Markdown: tiap milestone punya input/output/kriteria; tidak mewajibkan GPU, API berbayar, atau data pribadi tanpa kebutuhan yang telah ditetapkan; rubrik mencakup kualitas proses dan penalaran, bukan skor model saja.

### SEM-08 — Kerangka LMS semester

**Path:** `course/semester/lms-skeleton.md`. **Audiens:** dosen. **Prasyarat awal:** rancangan SEM-02 dan slot 16 minggu. **Integrasi akhir:** paket LMS mingguan/ujian ketika masing-masing tersedia; skeleton dibuat lebih dahulu.

- Isi: struktur 16 minggu, konvensi nama, urutan konten, prasyarat akses, aktivitas/forum, kuis/tugas, format pengumpulan, pengumuman, dan manifest mahasiswa/dosen.
- Konfigurasi waktu, attempt, visibility, scoring, gradebook, dan batas bantuan AI ditulis sebagai usulan atau fakta bersumber; jangan mengklaim fitur platform tertentu tersedia tanpa pemeriksaan.
- Lulus Markdown: semua minggu punya slot yang tepat; tiap unggahan yang direncanakan punya ID/path/audiens; tidak ada kunci/rubrik rahasia di manifest mahasiswa.
- Belum mengunggah apa pun. DoD asli “LMS siap/terpublikasi” memerlukan bukti pelaksanaan tambahan.

### SEM-09 — Tracker mastery

**Path:** `course/semester/mastery-tracker.md`. **Audiens:** dosen. **Prasyarat awal:** rancangan SEM-04 untuk membuat skema kosong. **Integrasi akhir:** EVID mingguan/ujian dan hasil aktual kemudian; EVID memakai skema awal tracker tanpa menunggu tracker berisi data.

- Isi: definisi mastery per LO, kriteria bukti, skema kolom, cara pencatatan, status data hilang, diagnosis kesulitan, remediasi dan pemeriksaan ulang.
- Ambang mastery yang belum bersumber ditandai usulan; jangan menurunkan skor workbook menjadi batas kelulusan mahasiswa. Bedakan belum mengumpulkan, belum dinilai, tidak memenuhi, dan memenuhi.
- Lulus Markdown: semua LO mempunyai bukti/kriteria/tindak lanjut; format kosong dapat dipakai; contoh opsional menggunakan ID sintetis dan label eksplisit.
- Rekaman mahasiswa nyata, statistik kelas, dan keberhasilan remediasi menunggu bukti. Jangan mengisi daftar mahasiswa, nilai, atau mastery rekaan.

### SEM-10 — Bank soal semester

**Path:** `course/semester/question-bank.md`. **Audiens:** dosen; bagian latihan yang boleh dibagikan terpisah. **Prasyarat awal:** SEM-04 untuk struktur/tag bank. **Integrasi akhir:** ASSESS/RUBRIC mingguan dan butir ujian ketika tersedia; kelengkapan bank tidak menjadi prasyarat membuat soal pertama.

- Isi setiap butir: ID, minggu/topik, LO/outcome, jenis soal, level kognitif rancangan, kesulitan rancangan, stimulus/data, pertanyaan, jawaban/rubrik, skor, sumber, dan status penggunaan.
- Tag `practice/shareable`, `assessment/instructor_only`, atau status setara; catat versi dan riwayat penggunaan yang memang terjadi. Kesulitan empiris baru diisi setelah data tersedia.
- Lulus Markdown: 100% butir punya kunci yang cocok dan traceability; soal yang identik tidak dihitung berkali-kali karena disalin; cakupan bank ditunjukkan lewat matriks, bukan jumlah tanpa kebutuhan.
- Kuota butir ditetapkan dari blueprint/scope; jangan mengklaim bank lengkap ketika target belum disepakati atau cakupan masih berlubang.

### SEM-11 — Standar paket ajar

**Path:** `course/standards/teaching-package-os.md`. **Audiens:** dosen/penulis. **Prasyarat awal:** dokumen perencanaan ini dan master prompt untuk standar versi awal. **Integrasi akhir:** temuan pilot W04 menyempurnakan standar; W04 tidak harus selesai sebelum standar awal dibuat.

- Isi: metadata/ID, istilah, struktur bab/modul/lab/asesmen, sumber, format Markdown, pedagogi, storyboard, naskah slide, code fence, aksesibilitas, QA, dan packaging.
- Adaptasi DNA visual: spesifikasi 16:9, palet navy/cyan, headline dengan pesan, visual bermakna, takeaway, dan variasi komposisi; semuanya naskah sampai rendering dilakukan.
- Lulus Markdown: setiap tipe artefak mempunyai template dan checklist; semua template sesuai kontrak metadata; jelas bagian wajib, opsional, dan pengecualian beralasan untuk W15/ujian.
- Approval storyboard pada alur gambar master prompt berlaku untuk produksi visual lanjutan. Penulisan/revisi draft Markdown berjalan dalam scope yang telah diotorisasi.

### SEM-12 — Kendali produksi

**Path utama:** `course/production/dashboard.md`. **File pendukung:** `semester-backlog.md`, `weekly-backlog.md`, `sources.md`, `decisions.md`, dan `reports/` sesuai kebutuhan. **Audiens:** dosen/penulis.

- Isi: 222 ID unik, path rencana, tipe, minggu, prioritas asli, dependensi asli dan tambahan yang dibedakan, DoD asli, adaptasi Markdown, status baseline, status repo, readiness, blocker, QA, next action.
- Tampilkan jumlah per kategori/status tanpa mencampur Markdown VALIDATED dengan pemenuhan DoD asli. Baseline sumber tetap immutable; pembaruan produksi dicatat sebagai kolom/rekaman baru.
- Lulus Markdown: 12 + 196 + 14 tepat; tidak ada ID ganda/hilang; perhitungan dashboard dapat direkonsiliasi dengan backlog; tautan file yang belum dibuat ditandai planned.
- Status/snapshot workbook tidak membuktikan adanya file, review, publikasi, atau penggunaan. IMPROVE dan score dashboard workbook tidak boleh ditafsirkan sebagai persentase kesiapan materi tanpa penjelasan rumus/konteks.

## 4. Spesifikasi 14 artefak per minggu pembelajaran

Terapkan untuk **W01–W07, W09–W15**. `Wnn` mengikuti nomor minggu, bukan urutan ke-1 hingga ke-14. Semua artefak memakai scope/LO yang sama. W15 menyesuaikan bentuk presentasi/klinik proyek dengan alasan tercatat; jangan menghapus coverage inti atau mengisi materi baru yang tidak dibutuhkan.

### Wnn-BOOK — Bab buku

**Path:** `course/weeks/wnn/book-chapter.md`. **Audiens:** mahasiswa. **Input:** scope, LO, sumber teknis yang dibaca, bab prasyarat.

- Bagian wajib: orientasi/LO, prasyarat, WHY, intuisi, definisi, konsep, mekanisme/algoritma/formula yang relevan, worked example, miskonsepsi, penerapan, keterbatasan, latihan/refleksi, rangkuman, sumber.
- Definisikan setiap simbol, satuan, istilah baru, input/output, asumsi, dan batas metode. Pisahkan analogi awal dari makna teknis yang presisi.
- Lulus Markdown: seluruh LO tercakup dan ditautkan ke bagian; minimal satu worked example dengan langkah dan interpretasi, satu miskonsepsi beserta koreksi, dan latihan yang memeriksa penalaran. Materi W15 memakai sintesis/kritik proyek sebagai contoh.
- Hasil numerik/kode berasal dari pemeriksaan aktual; klaim di luar sumber diberi label pengayaan dan sumber yang sesuai.

### Wnn-MOD — Modul mahasiswa

**Path:** `course/weeks/wnn/student-module.md`. **Audiens:** mahasiswa. **Prasyarat awal:** BOOK/scope untuk jalur belajar draft. **Integrasi akhir:** LAB, WORK, ASSESS ketika tersedia; slot/rujukan planned diberi tanda lalu dilengkapi.

- Isi: peta belajar sebelum–saat–setelah pertemuan, bacaan spesifik, aktivitas, instruksi lab/worksheet, luaran, self-check, remediasi, refleksi, exit ticket/mastery checkpoint.
- Beri urutan dan estimasi usaha usulan, input yang harus disiapkan, cara mengetahui hasil benar, dan dukungan bila runtime/internet terbatas.
- Lulus Markdown: setiap aktivitas punya instruksi, output, dan cara cek; tautan tidak menyertakan kunci dosen; materi yang harus dibaca tidak hanya “lihat buku” tanpa bagian.
- Modul berfungsi mandiri tanpa menyalin seluruh bab. Jadwal final mengikuti durasi/mode resmi setelah diketahui.

### Wnn-GUIDE — Panduan dosen

**Path:** `course/weeks/wnn/lecturer-guide.md`. **Audiens:** dosen. **Prasyarat awal:** scope, BOOK, draft MOD. **Integrasi akhir:** LAB, RUBRIC, STORY; panduan awal memberi konteks bagi storyboard, lalu keduanya diselaraskan tanpa saling menunggu versi final.

- Isi: LO/prasyarat, persiapan, hook, agenda, demonstrasi, pertanyaan diagnostik, expected responses, miskonsepsi, titik cek, debrief, remediasi/pengayaan, dan contingency.
- Alokasi waktu berupa proporsi atau skenario berlabel usulan sebelum durasi diketahui; setelah resmi, jumlah menit konsisten dengan total pertemuan.
- Cantumkan adaptasi IF24A/IF24H sebagai dua catatan terpisah dengan fakta versus asumsi; siapkan jalur CPU/offline dan fallback demo.
- Lulus Markdown: setiap aktivitas memiliki trigger–aksi–indikator–debrief; dosen tahu apa yang diamati dan kapan beralih; kunci/solusi ditandai instructor-only.

### Wnn-STORY — Storyboard

**Path:** `course/weeks/wnn/storyboard.md`. **Audiens:** dosen/penulis. **Prasyarat awal:** BOOK/scope dan contoh inti; gunakan GUIDE awal sebagai konteks. **Integrasi akhir:** LAB, WORK, ASSESS, GUIDE final; storyboard produksi mengikuti konten yang telah diperiksa pada urutan playbook.

- Untuk setiap slide: ID/nomor, role, conclusion-driven headline, subtitle, satu pesan utama, primary visual, information architecture, supporting elements, contoh, student action, bottom takeaway. Tambahkan LO, source/locator, speaker cue, dan estimasi waktu usulan bila relevan.
- Rancang WHY → intuisi → konsep → mekanisme → contoh → praktik → aplikasi → kritik → mastery; struktur mengikuti kebutuhan materi, tidak harus satu slide per tahap.
- Gunakan intuisi sebelum formalisasi sebagai aturan naskah konsisten dengan pedagogi utama/master prompt Zero-to-Hero. Field subtitle/takeaway tetap diperiksa pada storyboard; keberadaan field tidak memaksa layout render yang sama pada setiap slide.
- Target awal sekitar 20 slide untuk pertemuan reguler. Target desain: 2–4 slide student-action, minimal satu miskonsepsi/kritik, satu worked example, dan mastery map/exit ticket. Penyimpangan jumlah/format dijelaskan pada scope; W15 dapat memakai pola klinik.
- Lulus Markdown: semua slide memiliki satu pesan dominan; contoh/angka cocok dengan bab/lab; aksi mahasiswa memiliki instruksi/output/debrief. Tidak menyatakan kualitas proyeksi/render sudah lolos dari teks saja.

### Wnn-SLIDE — Naskah slide Markdown

**Path:** `course/weeks/wnn/slides.md`. **Audiens:** mahasiswa untuk naskah tampilan, dosen untuk notes/kunci yang dipisahkan. **Dependensi:** STORY, sumber/contoh terkunci secara substansi.

- Pisahkan slide dengan heading/ID atau separator konsisten; setiap slide berisi judul, teks tampil ringkas, diagram/tabel/visual brief, takeaway, sitasi, dan speaker notes terpisah.
- Tabel/angka/formula yang penting ditulis sebagai teks yang dapat diperiksa; Mermaid atau ASCII dapat dipakai. Visual brief menjelaskan objek, hubungan, label, dan data, bukan instruksi estetika saja.
- Lulus Markdown: ID/jumlah/urutan cocok dengan storyboard; tidak ada data atau formula baru yang belum diverifikasi; semua aset eksternal yang diusulkan punya status sumber/lisensi atau ditandai belum tersedia.
- Notes dengan jawaban/diskusi dosen tidak masuk paket mahasiswa otomatis. Deck 16:9, render, keterbacaan proyektor, dan aset gambar memerlukan pemeriksaan tambahan bila kelak diproduksi.

### Wnn-DATA — Dataset dan studi kasus

**Path:** `course/weeks/wnn/dataset-case.md`. **Audiens:** mahasiswa; detail sensitif dosen dipisahkan. **Dependensi:** scope, sumber data.

- Isi: konteks masalah, asal data/status sintetis, akses, lisensi/batas penggunaan yang diketahui, data dictionary, satuan/tipe, target atau alasan tidak memakai target, ukuran, kualitas, risiko bias/privasi, dan penggunaan dalam EX/ACT/LAB.
- Rencana split/validasi menjaga kelompok/waktu bila relevan; preprocessing tidak memakai informasi data evaluasi. Contoh kecil dapat disertakan sebagai tabel/generator deterministik.
- Lulus Markdown: semua kolom yang dipakai lab didefinisikan; data dapat diperoleh/dibangun lewat prosedur yang jelas; label sintetis eksplisit; hak penggunaan tidak diasumsikan.
- Jalur offline tidak membutuhkan download saat kelas. Ketersediaan dataset fisik tidak boleh diklaim bila hanya spesifikasi/generator yang ditulis.

### Wnn-LAB — Praktik Markdown

**Path:** `course/weeks/wnn/lab.md`. **Audiens:** mahasiswa untuk starter; dosen untuk solusi yang terpisah. **Dependensi:** DATA, BOOK, scope/LO.

- Isi: tujuan/prasyarat, runtime dan versi yang diuji, kebutuhan CPU/memori sebagai target/rencana, input, starter code, langkah, checkpoint, output, interpretasi, troubleshooting, cleanup jika relevan, dan rujukan solusi dosen.
- Kode memakai fenced blocks berlabel bahasa. Blok diberi ID/urutan dan status runnable versus pseudocode; jangan mencampurkan komentar placeholder yang membuat starter gagal tanpa penjelasan.
- Solusi referensi dijalankan dari awal pada data/seed yang disebut. Verifikasi perilaku, bentuk output, toleransi numerik, dan edge case yang mendukung LO; log mencatat environment, command, actual result, dan batas pemeriksaan.
- Lulus Markdown: mahasiswa mengetahui langkah/output; run aktual sesuai klaim; split/pipeline/leakage benar; jalur dasar CPU/offline tersedia. Skenario tanpa coding dapat dipakai W15 dengan alasan dan luaran setara, bukan lab kosong.
- Jangan mengklaim notebook tersedia. Solusi di file/repo yang sama harus dipisahkan saat distribusi; label “dosen” tidak menjadi kontrol akses.

### Wnn-WORK — Worksheet

**Path:** `course/weeks/wnn/worksheet.md`. **Audiens:** mahasiswa. **Prasyarat awal:** BOOK, DATA/contoh. **Integrasi akhir:** LAB bila relevan dan RUBRIC yang disusun berpasangan; tidak menunggu rubrik final untuk menulis butir awal.

- Isi: prediksi sebelum demo, penelusuran mekanisme, perhitungan/perbandingan, interpretasi, kritik hasil, refleksi, ruang jawaban, dan petunjuk bertingkat bila diperlukan.
- Tiap butir memiliki ID, LO, stimulus lengkap, instruksi, output yang diminta, estimasi usaha usulan, dan referensi rubrik/kunci dosen tanpa membocorkan jawabannya.
- Lulus Markdown: minimal satu butir meminta alasan/interpretasi, bukan hasil akhir saja; input cukup untuk mengerjakan; soal tidak menuntut konsep yang belum diajarkan tanpa label pengayaan.
- W15 dapat berupa peer-review/pemeriksaan reproduksibilitas proyek dengan bukti yang diminta secara jelas.

### Wnn-AIP — Prompt belajar dengan AI

**Path:** `course/weeks/wnn/ai-learning-prompts.md`. **Audiens:** mahasiswa. **Dependensi:** LO, BOOK, WORK, kebijakan AI bila tersedia.

- Isi: prompt tutor, Socratic hint, kritik penalaran, pemeriksaan kode/hasil, refleksi; variabel input dan konteks sumber; instruksi agar mahasiswa mencoba terlebih dahulu.
- Setiap prompt menyatakan output yang diminta, batas bantuan, cara verifikasi, tanda halusinasi, dan kapan harus kembali ke sumber/dosen. Sediakan aktivitas setara tanpa akses AI.
- Lulus Markdown: minimal satu prompt memberi hint bertahap tanpa menyerahkan jawaban final dan satu prompt mengaudit jawaban dengan bukti; tidak meminta memasukkan data pribadi atau materi ujian rahasia.
- Contoh respons AI yang belum benar-benar diuji disebut ilustrasi, bukan validasi. Kebijakan bantuan AI untuk tugas/ujian tidak ditetapkan hanya dari prompt ini.

### Wnn-ASSESS — Tugas dan kuis

**Path:** `course/weeks/wnn/assignment-quiz.md`. **Audiens:** mahasiswa. **Prasyarat awal:** scope/LO, BOOK dan rancangan SEM-04. **Integrasi akhir:** MOD/LAB/WORK dan RUBRIC yang disusun berpasangan; kunci/rubrik awal dipakai mengecek kelayakan butir sebelum final.

- Isi: tujuan, cakupan, ID soal/tugas, stimulus/input, instruksi, luaran/format, estimasi usaha, skor bila tersedia, bantuan/kolaborasi/AI, pengumpulan, dan kriteria penilaian.
- Bedakan latihan formatif versus penilaian; ketentuan resmi belum tersedia diberi label usulan. Instruksi tidak bergantung pada kunci dosen untuk dapat dipahami.
- Lulus Markdown: 100% butir bertaut ke LO dan RUBRIC; angka/skor/input konsisten; tidak ada ambiguitas jawaban yang tidak ditangani rubrik; cakupan materi telah diajarkan atau pengayaan dinyatakan.
- Jam pengumpulan, durasi, bobot, penalti, dan aturan akademik jangan direka. Tanpa kebijakan final, draft soal tetap dapat diproduksi tetapi belum disahkan untuk asesmen resmi.

### Wnn-RUBRIC — Rubrik dan kunci

**Path:** `course/weeks/wnn/rubric-answer-key.md`. **Audiens:** dosen. **Prasyarat awal:** butir draft ASSESS/WORK dan solusi/contoh LAB yang relevan. **Integrasi akhir:** naskah soal final; rubrik dan soal diperbaiki berpasangan tanpa siklus blocker.

- Isi per butir: jawaban/solusi, langkah penalaran, alternatif benar, kesalahan umum, kriteria teramati, tingkat kualitas, skor/partial credit, dan rujukan sumber/run.
- Rubrik menyatakan bukti yang diamati; istilah seperti “baik” harus diuraikan. Hasil berbeda karena seed/versi/toleransi ditangani eksplisit jika relevan.
- Lulus Markdown: seluruh butir mempunyai kunci/rubrik; total skor cocok dengan soal; penilai dapat menilai contoh jawaban jangkar secara konsisten; solusi kode benar-benar diperiksa.
- Pisahkan rubrik transparan yang boleh dibagikan dari kunci/solusi instructor-only pada manifest. Penyimpanan di repositori tidak menjamin kerahasiaan akses.

### Wnn-LMS — Paket LMS mingguan

**Path:** `course/weeks/wnn/lms-package.md`. **Audiens:** dosen; naskah pengantar mahasiswa di dalamnya dipisahkan. **Prasyarat awal:** MOD/scope dan pola SEM-08 untuk kerangka paket. **Integrasi akhir:** SLIDE, LAB, WORK, ASSESS, manifest sumber sebelum naskah paket dinyatakan VALIDATED.

- Isi: teks pengantar, tujuan, urutan akses, aktivitas/forum, kuis/tugas, instruksi submit, konfigurasi usulan, manifest path/audiens/status, dan checklist unggah manual.
- Sediakan urutan belajar tanpa koneksi terus-menerus; tanggal/jam/link LMS dibiarkan belum tersedia sampai diketahui.
- Lulus Markdown: semua aset mahasiswa yang diperlukan terdaftar; tidak ada file/heading/kunci dosen masuk rute mahasiswa; konfigurasi skor cocok dengan asesmen.
- Status paket Markdown tidak berarti LMS sudah dibuat atau terpublikasi. Bukti publikasi harus berasal dari tindakan dan pemeriksaan LMS yang nyata.

### Wnn-EVID — Spesifikasi bukti belajar

**Path:** `course/weeks/wnn/evidence-spec.md`. **Audiens:** dosen; instruksi pengumpulan aman untuk mahasiswa dipisahkan. **Prasyarat awal:** LO, draft ASSESS/RUBRIC, skema awal SEM-09. **Integrasi akhir:** tracker/rubrik final dan bukti aktual kemudian; spec tidak menunggu tracker berisi data.

- Isi: bukti per LO/ASM/EV, bentuk dan minimal content, penamaan, sumber waktu/versi, cara verifikasi, kriteria mastery, data hilang, rencana penyimpanan/akses, dan tindak lanjut.
- Untuk coding, tentukan input/seed/environment, hasil, interpretasi, dan bukti proses yang diperlukan; screenshot saja tidak selalu cukup untuk reproduksibilitas.
- Lulus Markdown sebagai spesifikasi: semua LO yang dinilai mempunyai jenis bukti/kriteria; skema kosong dapat digunakan; tidak ada nama/nilai/hasil kelas rekaan.
- Bukti aktual mempunyai rekaman terpisah yang menyebut pelaksanaan, asal, dan reviewer. Spesifikasi lengkap tetap dilaporkan “bukti aktual belum tersedia” sampai pengumpulan terjadi.

### Wnn-QA — QA dan tindak lanjut pascakelas

**Path:** `course/weeks/wnn/post-class-qa.md`. **Audiens:** dosen. **Prasyarat awal:** scope dan checklist gate untuk instrumen kosong. **Integrasi akhir:** paket minggu/EVID/GUIDE/SEM-09 ketika tersedia, kemudian hasil pelaksanaan; instrumen tidak menunggu kelas berlangsung.

- Isi pra-kelas: kesiapan sumber, scope, kode, tautan, kegiatan, asesmen, kunci, dan distribusi. Isi pascakelas: bukti pelaksanaan, pola kesulitan, coverage, waktu aktual, KEEP/FIX/ADD/REMOVE, dan rencana revisi.
- Setiap temuan memiliki ID, bukti/locator, dampak, severity, tindakan, owner/status; opini dosen dan bukti belajar mahasiswa dibedakan.
- Lulus Markdown sebagai instrumen: checklist konkret, format analisis dan remediasi lengkap; bagian pascakelas jelas “belum diisi—menunggu pelaksanaan”.
- Analisis pascakelas lulus setelah ada bukti aktual yang cukup, temuan ditautkan, dan tindakan dapat ditelusuri. Kehadiran file kosong/templated tidak menjadi bukti penggunaan.

## 5. Spesifikasi 7 artefak per ujian

Gunakan **UTS pada W08** dan **UAS pada W16**; kedua paket berisi suffix yang sama. Rancangan cakupan UTS mengacu W01–W07 dan materi yang benar-benar diajarkan; cakupan/bentuk UAS serta hubungan proyek mengikuti RPS yang diverifikasi, bukan asumsi bahwa semua semester wajib diuji ulang atau proyek otomatis menggantikan ujian.

### UTS/UAS-BLUEPRINT — Blueprint ujian

**Path:** `course/exams/uts/blueprint.md` / `course/exams/uas/blueprint.md`. **Audiens:** dosen. **Prasyarat awal:** rancangan SEM-04 dan scope cakupan untuk blueprint usulan. **Integrasi akhir:** materi yang benar-benar diajarkan dan kebijakan resmi sebelum blueprint final.

- Isi: cakupan dan pengecualian, LO/outcome, indikator, jenis butir, level kognitif rancangan, jumlah/skor/proposi, kebutuhan data/alat, dan peta butir.
- Lulus Markdown: setiap butir direncanakan pada indikator; semua target cakupan terwakili atau gap dinyatakan; total skor cocok dengan QUESTION/KEY.
- Finalisasi resmi tertahan bila cakupan, bentuk, durasi, bobot, atau aturan belum diverifikasi. Usulan blueprint tetap dapat ditelaah.

### UTS/UAS-QUESTION — Naskah soal

**Path:** `course/exams/uts/question-set.md` / `course/exams/uas/question-set.md`. **Audiens:** dosen sebelum ujian; distribusi mahasiswa hanya pada waktu yang ditetapkan kemudian.

- Isi: identitas versi, instruksi umum, ID butir, stimulus/data, pertanyaan, format jawaban, skor, dan bahan pendukung yang cukup untuk menjawab.
- Lulus Markdown: semua butir cocok dengan blueprint/kunci; data dapat dibaca dan dihitung; formula/angka akurat; estimasi beban ditelaah dengan durasi aktual bila sudah tersedia.
- Soal latihan terpisah dari soal ujian yang masih rahasia. Tidak menyimpan jawaban dalam notes, komentar, heading tersembunyi, atau tautan paket mahasiswa.

### UTS/UAS-KEY — Kunci dan rubrik ujian

**Path:** `course/exams/uts/answer-key-rubric.md` / `course/exams/uas/answer-key-rubric.md`. **Audiens:** dosen.

- Isi: solusi lengkap per ID butir, penalaran, alternatif benar, langkah/scoring, partial credit, toleransi, kesalahan umum, dan contoh jangkar penilaian bila perlu.
- Lulus Markdown: 100% butir memiliki rubrik; total skor konsisten; hasil hitung/kode diverifikasi; reviewer independen dapat menyelesaikan soal tanpa membaca kunci terlebih dahulu.
- Manifest instructor-only ditetapkan sebelum distribusi. Label/path/file presence di repo tidak memberi kontrol akses terhadap mahasiswa maupun riwayat Git.

### UTS/UAS-INSTR — Instruksi pelaksanaan

**Path:** `course/exams/uts/instructions.md` / `course/exams/uas/instructions.md`. **Audiens:** mahasiswa setelah ketentuan siap dibagikan.

- Isi: format ujian, waktu, bahan/alat yang diperbolehkan, bantuan AI/kolaborasi, pengumpulan, penamaan, kendala teknis, aksesibilitas, dan kontak/eskalasi yang benar-benar ditetapkan.
- Lulus Markdown: ketentuan saling konsisten dengan QUESTION/LMS/RPS; setiap aturan resmi punya sumber; belum tersedia diberi label dan blocker yang jelas.
- Jangan menciptakan kebijakan akademik, penalti, prosedur banding, atau kewajiban surveilans. Draft instruksi tetap dapat disiapkan tanpa menyebutnya final.

### UTS/UAS-LMS — Paket LMS ujian

**Path:** `course/exams/uts/lms-package.md` / `course/exams/uas/lms-package.md`. **Audiens:** dosen.

- Isi: naskah pengantar, urutan distribusi, manifest soal/instruksi versus kunci, pengaturan usulan, alur submit, contingency, dan checklist pemeriksaan sebelum dibuka.
- Lulus Markdown: file soal/instruksi dan jalur pengumpulan terpetakan; kunci tidak masuk manifest mahasiswa; waktu/attempt/scoring yang belum resmi tetap tertahan.
- Publikasi, uji akses mahasiswa, dan pengumpulan belum diklaim terjadi. DoD asli memerlukan bukti LMS jika menjadi tahap lanjutan yang diminta.

### UTS/UAS-EVID — Spesifikasi arsip bukti

**Path:** `course/exams/uts/evidence-archive-spec.md` / `course/exams/uas/evidence-archive-spec.md`. **Audiens:** dosen.

- Isi: versi naskah/rubrik, bukti distribusi/pelaksanaan/pengumpulan yang dibutuhkan, skema hasil, penamaan, keterkaitan mahasiswa–butir–LO, penyimpanan/akses, dan penanganan bukti hilang.
- Lulus Markdown sebagai spesifikasi: seluruh proses yang akan dianalisis memiliki data/bukti yang ditetapkan; format kosong jelas; tidak ada hasil/identitas/rekap rekaan.
- Kebijakan retensi/akses mengikuti sumber institusi bila tersedia; sebelum itu dicatat sebagai keputusan terbuka. Jangan mengarang durasi retensi resmi.

### UTS/UAS-QA — Analisis pascaujian

**Path:** `course/exams/uts/post-exam-analysis.md` / `course/exams/uas/post-exam-analysis.md`. **Audiens:** dosen.

- Isi instrumen: kualitas butir/rubrik, pola jawaban, coverage/mastery, data hilang, revisi, remediasi, dan catatan keterbatasan analisis.
- Jika statistik butir direncanakan, definisikan input, rumus/metode, kondisi kelayakan, dan interpretasi; sampel kecil atau format esai tidak dipaksakan ke metrik yang tidak sesuai.
- Lulus Markdown sebagai instrumen: tabel kosong dan metode dapat dipakai, hubungan ke EV/LO/Q/RC jelas, analisis aktual ditandai belum tersedia.
- Selesai analisis memerlukan data hasil yang benar-benar diperoleh, perhitungan terverifikasi, keterbatasan dilaporkan, dan tindak lanjut; bukan angka simulasi yang diberi judul hasil ujian.

## 6. Adaptasi IF24A/IF24H dan keterlaksanaan

Kedua kelas memakai konsep inti, LO, standar bukti, dan kriteria asesmen yang sama kecuali sumber resmi menetapkan perbedaan. Jangan menginferensikan IF24A reguler/tatap muka atau IF24H malam/hybrid dari kode kelas.

| Dimensi | IF24A | IF24H | Keputusan produksi sementara |
| --- | --- | --- | --- |
| Mode, durasi, jadwal | Belum terverifikasi | Belum terverifikasi | Gunakan agenda berbasis proporsi dan opsi sinkron/asinkron berlabel usulan |
| Pengetahuan awal | Menunggu diagnosis | Menunggu diagnosis | Pre-check yang sama; scaffolding/pengayaan menurut hasil nyata |
| Perangkat/koneksi | Belum terverifikasi | Belum terverifikasi | Jalur CPU/offline inti; opsi demo atau tracing manual yang mencapai LO sama |
| Kebutuhan aksesibilitas | Belum tersedia | Belum tersedia | Teks alternatif visual, instruksi jelas, tabel/diagram yang dapat dibaca |
| Kebijakan penilaian | Menunggu sumber | Menunggu sumber | Jangan menetapkan bobot/durasi/penalti berbeda dari asumsi |

Setelah data tersedia, catat perubahan kelas beserta sumber, dampak, dan versi; hindari mengubah LO/kriteria diam-diam demi menyesuaikan alat. Materi alternatif offline harus setara pada penalaran dan bukti yang diperiksa, bukan sekadar menghilangkan praktik.

## 7. Kontrak teknis Markdown, CPU, dan offline

- Semua artefak utama tetap `.md`; kode menggunakan code fence berlabel bahasa; blok solusi diberi batas distribusi. Notebook, PPTX/PDF, gambar, layanan berbayar, atau dataset fisik merupakan keluaran tambahan, tidak diasumsikan tersedia.
- Diagram punya judul, legenda bila perlu, dan uraian teks. Mermaid yang belum dirender disebut spesifikasi diagram; bentuk Mermaid valid tidak membuktikan tampilannya terbaca di proyektor.
- Dataset kecil dari library atau generator sintetis deterministik menjadi opsi dasar; jangan memerlukan download/API di tengah kelas. Simpan seed, ukuran, target, dan batas kasus.
- Runtime dasar memakai CPU. Bila paket tambahan diperlukan, tulis versi, langkah instalasi opsional, kebutuhan jaringan pada setup, dan fallback. Target runtime/memori ditetapkan per lab dan diukur sebelum dinyatakan terpenuhi.
- DL/GenAI dapat memakai demonstrasi konseptual, data/output simulasi berlabel, atau model ringan CPU. Jelaskan keterbatasan representasi; hasil simulasi tidak disebut hasil training/inference aktual.
- Pengujian kode dilakukan di berkas sementara, bukan dengan menambahkan artefak teknis yang tidak diminta. Catat command, versi, seed, actual output, toleransi, pass/fail, dan bagian kode yang belum diuji. “Dapat dijalankan” tanpa run tidak cukup untuk kode inti.
- Hindari versi paket/batas waktu/memori palsu. Jika environment yang tersedia belum mampu run, tandai `technical_unverified` pada catatan dan blocker untuk klaim hasil teknis terkait.

## 8. Pemisahan paket mahasiswa dan dosen

Manifest memetakan **artefak + bagian/heading + audiens + versi + status**. File `GUIDE`, `RUBRIC`, bank soal rahasia, kunci ujian, laporan QA dengan hasil individual, serta solusi lab tidak dimasukkan otomatis ke paket mahasiswa. Rubrik kriteria yang boleh dibagikan dibedakan dari kunci/solusi lengkap.

Pemisahan nama folder, metadata `instructor_only`, collapsible section, atau komentar Markdown **bukan kontrol akses**. Jika repositori dapat diakses mahasiswa, isi dan riwayat file dapat terbaca. Sebelum berbagi, periksa batas akses/manifest dan buat salinan distribusi yang memang tidak memuat bagian dosen; jangan mengklaim kerahasiaan hanya karena kunci tersimpan di file berbeda. Perubahan akses atau publikasi eksternal dilakukan dalam tahap yang memang diotorisasi.

Paket mahasiswa harus tetap lengkap: instruksi, input, starter, kriteria transparan, cara submit, dan dukungan. Paket dosen menambahkan jawaban, expected responses, diagnosis kesalahan, catatan demonstrasi, dan langkah penilaian. Laporan produksi membedakan kesiapan kedua paket.

## 9. Catatan penerimaan per artefak

Gunakan format singkat berikut setelah review dilakukan; template ini belum menjadi bukti review.

```text
Artefak/versi: [ID; versi]
Mode pemeriksaan: [spec-only / content / run / package / actual-delivery]
Scope/LO yang diperiksa: [...]
Gate berlaku + keputusan: [PASS / FAIL / PROVISIONAL / UNRUN / NOT_APPLICABLE beralasan]
Check/run result aktual: [PASS / FAIL / UNRUN / NOT_APPLICABLE beralasan]
Bukti/locator/log: [...]
Temuan terbuka: [ID; severity; dampak; tindakan]
Readiness Markdown: [...]
Pemenuhan DoD asli: [NOT_FULFILLED / PARTIAL / FULFILLED + alasan]
Bukti aktual kelas/ujian/publikasi: [tersedia + locator / belum tersedia]
Reviewer/tanggal aktual: [...]
Langkah berikut: [...]
```

Pemakaian spesifikasi ini pada produksi berikutnya dimulai dari scope dan matriks penelusuran, lalu isi artefak, pemeriksaan berisiko tinggi, dan packaging. Gunakan [quality gates](QUALITY_GATES.md) untuk keputusan kesiapan dan [prompt library](PROMPT_LIBRARY.md) agar permintaan pada reasoning medium/high memiliki input dan definisi selesai yang cukup.
