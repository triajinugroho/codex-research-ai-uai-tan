---
artifact_id: W03-SLIDE
title: Preprocessing dan Feature Engineering — SLIDE
course_code: IF52510031
period: 2026–2027
week: 3
classes:
- IF24A
- IF24H
audience: mahasiswa
distribution: student_candidate
version: '0.3'
updated_at: '2026-10-07'
owner: Codex — penyusun; owner sumber dipertahankan di backlog
source_status: REVIEW
production:
  repo_status: REVIEW
markdown_readiness: VALIDATED
fulfillment: PARTIAL
source_verification: VERIFIED_FOR_SCOPE
official_alignment: PROVISIONAL
learning_ids:
- W03-LO01
- W03-LO02
official_outcome_refs:
- DAIML-Sub-CPMK102-1
assessment_ids:
- W03-ASM01
example_ids:
- W03-EX01
evidence_requirement_ids:
- W03-EV01
source_ids:
- SRC-WORKBOOK
- SRC-TECH-001
- SRC-TECH-002
- SRC-TECH-003
dependencies: []
integration_refs: []
workbook_dependencies: Storyboard
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181608-P21-W03-E2-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — SLIDE

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Naskah tampilan mahasiswa

20 slide sama dengan STORY; visual brief adalah spesifikasi teks, bukan gambar. Notes aman hanya mengarahkan urutan; kunci tidak ditampilkan.

### W03-SL01 — Alasan belajar

Transformasi yang mengambil informasi evaluasi dapat merusak makna penilaian model.

Visual brief: **Pagar parameter**. Label/relasi: Training sumber parameter; batch baru hanya penerapan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Training sumber parameter.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL02 — Tujuan keputusan

Memilih transformasi berdasarkan tipe fitur dan kebutuhan model

Visual brief: **Peta fitur**. Label/relasi: volume numerik dan channel kategori → perlakuan berbeda. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: volume numerik dan channel kategori → perlakuan berbeda.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL03 — Tujuan batas bukti

Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru

Visual brief: **Trace dua operasi**. Label/relasi: fit belajar keadaan → transform menerapkan keadaan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: fit belajar keadaan → transform menerapkan keadaan.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL04 — Prediksi sebelum kode

Tentukan imputasi volume dan representasi channel; beri alasan dan penanganan kategori C.

Visual brief: **Tabel training/batchbaru**. Label/relasi: Training1,missing,3,5; batchbaru missing,7 dan C,A. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Training1,missing,3,5.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W03-SL05 — Mental model

Belajar parameter sekali, terapkan pada data baru

Visual brief: **Dua kotak keadaan**. Label/relasi: Data training → parameter tersimpan → input baru. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Data training → parameter tersimpan → input baru.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL06 — Istilah pertama

Mempelajari keadaan/parameter estimator pada data training yang diberikan.

Visual brief: **Fit trace**. Label/relasi: Median diperoleh dari training yang disebut. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Median diperoleh dari training yang disebut.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL07 — Istilah kedua

Menerapkan keadaan yang telah dipelajari pada input.

Visual brief: **Transform trace**. Label/relasi: Parameter sama diterapkan pada batch baru tanpa fit ulang. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Parameter sama diterapkan pada batch baru tanpa fit ulang.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL08 — Istilah ketiga

Mengisi nilai hilang menggunakan strategi yang dinyatakan.

Visual brief: **Imputasi median**. Label/relasi: Training teramati1,3,5 → median3; hasil1,3,3,5. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Training teramati1,3,5 → median3.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL09 — Mekanisme awal

Untuk nilai hilang numerik, imputer median mempelajari median training. Data baru tidak digunakan untuk menghitung ulang median pada prosedur ini.

Visual brief: **Rumus bersatuan**. Label/relasi: z=(x−mu)/s; mu3, s sqrt2; z tidak bersatuan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: z=(x−mu)/s.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL10 — Trace keputusan

Hitung median, mean dan s setelah imputasi; trace fit lalu transform pada batch baru.

Visual brief: **Trace batch baru**. Label/relasi: Isi missing dulu, kemudian centering/scaling; mahasiswa hitung. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Isi missing dulu, kemudian centering/scaling.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W03-SL11 — Worked example

Training SIMULASI volume [1,missing,3,5] dengan kanal [A,B,A,B]. Median training=3 sehingga volume menjadi [1,3,3,5]. Mean=3; simpangan baku ddof=0=sqrt(2). Untuk batch baru volume [missing,7] kanal [C,A], median tetap 3; z pertama=0 dan z kedua=4/sqrt(2). Kategori C diberi indikator A=0,B=0 oleh ignore, tidak membentuk kolom baru.

Visual brief: **Tabel hasil**. Label/relasi: Training4×3; baru2×3; missingbaru z0; 7 z4/sqrt2. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Training4×3.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL12 — Mekanisme berikutnya

StandardScaler menggunakan z=(x−mu)/s dengan mu mean training dan s simpangan baku populasi (ddof=0) training setelah imputasi pada contoh. z tidak bersatuan. Jika s=0, API menangani skala fitur konstan; periksa sumber/runtime, bukan bagi nol manual.

Visual brief: **One-hot mapping**. Label/relasi: A→[1,0], B→[0,1], C→[0,0] dengan ignore. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: A→[1,0], B→[0,1], C→[0,0] dengan ignore.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL13 — Batas metode

OneHotEncoder mempelajari kategori training. handle_unknown=ignore menghasilkan semua indikator nol untuk kategori yang belum dikenal; itu bukan jaminan kategori baru aman secara semantik.

Visual brief: **Panel kategori baru**. Label/relasi: Semua nol bukan bukti C aman atau sama dengan kategori tertentu. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Semua nol bukan bukti C aman atau sama dengan kategori tertentu.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL14 — Miskonsepsi

Transform mempertahankan keadaan dari fit pada prosedur ini.

Visual brief: **Mitos–koreksi**. Label/relasi: Transform tidak mempelajari median batch baru. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Transform tidak mempelajari median batch baru.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL15 — Kritik klaim

Seorang teman fit ulang imputer pada gabungan training+batch baru. Apakah itu transform yang sama?

Visual brief: **Dua prosedur**. Label/relasi: fit training saja versus fit gabungan; mahasiswa telusuri asal median. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: fit training saja versus fit gabungan.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W03-SL16 — Periksa asumsi

ColumnTransformer memilih perlakuan per kolom. Pipeline menempatkan imputer/scaler di dalam setiap fit; fitur masa depan tetap harus dibuang melalui keputusan data, bukan diserahkan pada Pipeline.

Visual brief: **Kolom dalam pipeline**. Label/relasi: Num: imputer→scaler; category: encoder; gabungkan transform. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Num: imputer→scaler.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL17 — Koreksi kekeliruan

Kode kategori tidak otomatis bermakna jarak; pilih representasi berdasarkan tujuan.

Visual brief: **Kartu fitur masa depan**. Label/relasi: Pipeline bukan pemeriksa waktu fitur. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Pipeline bukan pemeriksa waktu fitur.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL18 — Rangkuman

Belajar parameter sekali, terapkan pada data baru; keputusan dan alasan ditelusuri dari input.

Visual brief: **Ringkasan batas**. Label/relasi: Asal parameter diketahui; penerapan pada input baru terlacak. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Asal parameter diketahui.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL19 — Remediasi

Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.

Visual brief: **Tangga trace ulang**. Label/relasi: Satu parameter → baris training → keputusan → batchbaru. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Satu parameter → baris training → keputusan → batchbaru.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W03-SL20 — Exit ticket

Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.

Visual brief: **Exit card**. Label/relasi: Parameter | asal input | penerapan | batas. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Parameter | asal input | penerapan | batas.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.
