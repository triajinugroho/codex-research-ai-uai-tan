---
artifact_id: W04-SLIDE
title: Pembagian Data dan Validasi — SLIDE
course_code: IF52510031
period: 2026–2027
week: 4
classes:
- IF24A
- IF24H
audience: mahasiswa
distribution: student_candidate
version: '0.4'
updated_at: '2026-10-07'
owner: Codex — penyusun; owner sumber dipertahankan di backlog
source_status: NOT STARTED
production:
  repo_status: REVIEW
markdown_readiness: VALIDATED
fulfillment: PARTIAL
source_verification: VERIFIED_FOR_SCOPE
official_alignment: PROVISIONAL
learning_ids:
- W04-LO01
- W04-LO02
official_outcome_refs:
- DAIML-Sub-CPMK102-1
assessment_ids:
- W04-ASM01
example_ids:
- W04-EX01
- W04-EX02
- W04-EX03
- W04-EX04
evidence_requirement_ids:
- W04-EV01
source_ids:
- SRC-WORKBOOK
- SRC-TECH-001
- SRC-TECH-002
- SRC-TECH-003
dependencies: []
integration_refs: []
workbook_dependencies: Storyboard
scope_record: course/weeks/w04/scope.md
validation_records:
- course/production/reports/20261007-181503-P21-W04-E2-validation.md
- course/production/reports/20261007-181504-P15-P16-W04-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182037-P16-dictionary-and-example-ids-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pembagian Data dan Validasi — SLIDE

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Naskah tampilan mahasiswa

20 slide sama dengan STORY; visual brief adalah spesifikasi teks, bukan gambar. Notes aman hanya mengarahkan urutan; kunci tidak ditampilkan.

### W04-SL01 — Alasan belajar

Skor hanya bermakna jika prosedur evaluasi meniru data yang akan dihadapi dan tidak dipakai untuk memilih jawaban.

Visual brief: **Skenario deployment**. Label/relasi: Unit baru/kelompok baru/masa depan → tujuan evaluasi berbeda. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Unit baru/kelompok baru/masa depan → tujuan evaluasi berbeda.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL02 — Tujuan keputusan

Memilih strategi split/CV sesuai tujuan prediksi, unit independen, kelompok dan waktu

Visual brief: **Matriks split**. Label/relasi: Tujuan | unit | group/time | strategi | alasan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Tujuan | unit | group/time | strategi | alasan.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL03 — Tujuan batas bukti

Mendeteksi leakage dan merancang batas fit serta penggunaan test

Visual brief: **Pagar fit/test**. Label/relasi: Training fit, development memilih, test evaluasi final. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Training fit, development memilih, test evaluasi final.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL04 — Prediksi sebelum kode

Pilih strategi untuk A unit independen berlabel, B kelompok berulang dengan deployment kelompok baru, C prediksi masa depan. Jelaskan mengapa stratifikasi saja tidak cukup pada B.

Visual brief: **Tiga kartu**. Label/relasi: A independent; B repeated group; C ordered time, tanpa kunci. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: A independent.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W04-SL05 — Mental model

Pagar data mengikuti tujuan generalisasi

Visual brief: **Diagram pagar**. Label/relasi: 120 → dev90 dan test30; CV hanya dalam dev. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: 120 → dev90 dan test30.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL06 — Istilah pertama

Subset yang digunakan pada fit model/transformasi.

Visual brief: **Training box**. Label/relasi: Parameter model/transformasi hanya belajar pada subset training. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Parameter model/transformasi hanya belajar pada subset training.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL07 — Istilah kedua

Data untuk memeriksa atau memilih kandidat; dapat dibagi beberapa fold.

Visual brief: **Development loop**. Label/relasi: Tiga fold pada dev90, masing-masing train60/validation30. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Tiga fold pada dev90, masing-masing train60/validation30.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL08 — Istilah ketiga

Data terpisah untuk evaluasi akhir prosedur setelah pilihan ditetapkan; jika digunakan memilih kandidat, tidak lagi independen untuk klaim itu.

Visual brief: **Test sealed box**. Label/relasi: Kandidat ditetapkan sebelum penggunaan test; demo menjadikannya exposed. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Kandidat ditetapkan sebelum penggunaan test.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL09 — Mekanisme awal

Pisahkan test sebelum pengembangan kandidat. Pada contoh 120 baris, test 25%=30 dan development=90. CV tiga fold berjalan hanya pada 90 development, bukan seluruh 120. Ukuran ini pilihan SIMULASI, bukan ketentuan kampus.

Visual brief: **Holdout proporsi**. Label/relasi: test0.25×120=30; sisanya90; label stratifikasi bukan group control. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: test0.25×120=30.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL10 — Trace keputusan

Prosedur: fit scaler seluruh 120 → CV seluruh 120 → pilih model dengan skor test. Tandai pelanggaran dan perbaiki diagram.

Visual brief: **Trace fold**. Label/relasi: dev local index → global index; cek disjointness dan asal parameter. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: dev local index → global index.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W04-SL11 — Worked example

Tiga skenario SIMULASI: A satu baris per unit independen, target kategori seimbang → holdout/stratified CV pada development; B enam catatan per group_id, deployment kelompok baru → GroupKFold; C 60 waktu berjarak sama, prediksi masa depan → TimeSeriesSplit(n_splits=3,test_size=10,gap=2). Kasus cacat D fit scaler pada seluruh data sebelum CV: perbaiki dengan Pipeline yang di-fit ulang di tiap training fold. Tidak dijanjikan skor selalu turun/naik; verifikasi asal parameter dan disjointness dahulu.

Visual brief: **Tiga panel worked example**. Label/relasi: A label stratification; B group boundary; C forward time gap2. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: A label stratification.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL12 — Mekanisme berikutnya

StratifiedKFold berusaha menjaga proporsi label pada fold; itu tidak mencegah pengguna sama ada di dua sisi. Untuk tujuan pengguna baru, GroupKFold menjaga kelompok tidak beririsan. Tujuan catatan baru pengguna lama dapat membutuhkan desain berbeda.

Visual brief: **Group strip**. Label/relasi: 20 group masing-masing6 baris; warna group tidak melintasi sisi fold. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: 20 group masing-masing6 baris.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL13 — Batas metode

TimeSeriesSplit melatih pada blok terdahulu dan mengevaluasi blok kemudian. gap mengeluarkan sejumlah sampel sebelum test; pilih gap dari horizon/ketergantungan, bukan menganggap default selalu benar. Data contoh berjarak sama dan sudah terurut.

Visual brief: **Time strip**. Label/relasi: Fold terakhir train sampai47, gap48–49, validation50–59. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Fold terakhir train sampai47, gap48–49, validation50–59.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL14 — Miskonsepsi

Label proporsi dan identitas kelompok masalah berbeda.

Visual brief: **Mitos–koreksi**. Label/relasi: Stratifikasi label tidak melarang group yang sama di dua sisi. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Stratifikasi label tidak melarang group yang sama di dua sisi.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL15 — Kritik klaim

Pada 120 baris test25%, berapa dev/test? Tiga fold CV memakai subset mana? Apakah mengganti seed memulihkan test yang dipakai tuning?

Visual brief: **Diagram prosedur cacat**. Label/relasi: fit semua → CV semua → tuning test; mahasiswa tandai batas. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: fit semua → CV semua → tuning test.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W04-SL16 — Periksa asumsi

Imputer/scaler harus di-fit di training fold. Rerata CV mean(s1,s2,s3) merangkum run pada kandidat; variasi fold tidak otomatis tiga observasi independen. Pipeline membantu batas fit, tetapi tidak mencegah label proxy/fitur masa depan.

Visual brief: **Pipeline per fold**. Label/relasi: Imputer/scaler/model di-fit pada training fold; statistik dicek. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Imputer/scaler/model di-fit pada training fold.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL17 — Koreksi kekeliruan

Seed tidak memperbaiki tujuan deployment atau urutan waktu.

Visual brief: **Kartu future feature**. Label/relasi: Feature proxy setelah prediksi tetap bocor meski ada Pipeline. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Feature proxy setelah prediksi tetap bocor meski ada Pipeline.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL18 — Rangkuman

Pagar data mengikuti tujuan generalisasi; keputusan dan alasan ditelusuri dari input.

Visual brief: **Ringkasan keputusan**. Label/relasi: Tujuan generalisasi menentukan pagar data; skor mengikuti prosedur. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Tujuan generalisasi menentukan pagar data.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL19 — Remediasi

Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.

Visual brief: **Tangga audit ulang**. Label/relasi: Satu skenario → tujuan/unit → split → fit → klaim. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Satu skenario → tujuan/unit → split → fit → klaim.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W04-SL20 — Exit ticket

Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.

Visual brief: **Exit card**. Label/relasi: Strategi | asumsi | invariant | batas test. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Strategi | asumsi | invariant | batas test.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.
