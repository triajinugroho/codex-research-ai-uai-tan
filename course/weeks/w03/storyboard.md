---
artifact_id: W03-STORY
title: Preprocessing dan Feature Engineering — STORY
course_code: IF52510031
period: 2026–2027
week: 3
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
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
workbook_dependencies: Book Chapter + Lecturer Guide
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181607-P21-W03-E1-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — STORY

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Journey 20 slide

Target desain, bukan render/deck. Empat student-action SL04/10/15/20; aksi terkait worksheet dan exit ticket. Semua waktu1–3 menit USULAN, bukan jumlah durasi kelas resmi.

### W03-SL01

- Nomor: 1; role: explanation.
- Headline: Alasan belajar — Belajar parameter sekali, terapkan pada data baru.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Transformasi yang mengambil informasi evaluasi dapat merusak makna penilaian model.
- Primary visual: Pagar parameter; label/relasi: Training sumber parameter; batch baru hanya penerapan. Uraian teks tetap tersedia.
- Information architecture: Pagar parameter sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Training sumber parameter.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL02

- Nomor: 2; role: explanation.
- Headline: Tujuan keputusan — Memilih transformasi berdasarkan tipe fitur dan kebutuhan model.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Memilih transformasi berdasarkan tipe fitur dan kebutuhan model
- Primary visual: Peta fitur; label/relasi: volume numerik dan channel kategori → perlakuan berbeda. Uraian teks tetap tersedia.
- Information architecture: Peta fitur sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: volume numerik dan channel kategori → perlakuan berbeda.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL03

- Nomor: 3; role: explanation.
- Headline: Tujuan batas bukti — Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru
- Primary visual: Trace dua operasi; label/relasi: fit belajar keadaan → transform menerapkan keadaan. Uraian teks tetap tersedia.
- Information architecture: Trace dua operasi sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: fit belajar keadaan → transform menerapkan keadaan.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL04

- Nomor: 4; role: student-action.
- Headline: Prediksi sebelum kode — Tentukan imputasi volume dan representasi channel; beri alasan dan penanganan kategori C.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Tentukan imputasi volume dan representasi channel; beri alasan dan penanganan kategori C.
- Primary visual: Tabel training/batchbaru; label/relasi: Training1,missing,3,5; batchbaru missing,7 dan C,A. Uraian teks tetap tersedia.
- Information architecture: Tabel training/batchbaru sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: jawab WK01 pada stimulus DATA; output alasan/trace tertulis; debrief menunjuk kunci Q01 pada GUIDE/RUBRIC DOSEN.
- Bottom takeaway: Training1,missing,3,5.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL05

- Nomor: 5; role: explanation.
- Headline: Mental model — Belajar parameter sekali, terapkan pada data baru.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Belajar parameter sekali, terapkan pada data baru
- Primary visual: Dua kotak keadaan; label/relasi: Data training → parameter tersimpan → input baru. Uraian teks tetap tersedia.
- Information architecture: Dua kotak keadaan sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Data training → parameter tersimpan → input baru.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL06

- Nomor: 6; role: explanation.
- Headline: Istilah pertama — Mempelajari keadaan/parameter estimator pada data training yang diberikan.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Mempelajari keadaan/parameter estimator pada data training yang diberikan.
- Primary visual: Fit trace; label/relasi: Median diperoleh dari training yang disebut. Uraian teks tetap tersedia.
- Information architecture: Fit trace sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Median diperoleh dari training yang disebut.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL07

- Nomor: 7; role: explanation.
- Headline: Istilah kedua — Menerapkan keadaan yang telah dipelajari pada input.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Menerapkan keadaan yang telah dipelajari pada input.
- Primary visual: Transform trace; label/relasi: Parameter sama diterapkan pada batch baru tanpa fit ulang. Uraian teks tetap tersedia.
- Information architecture: Transform trace sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Parameter sama diterapkan pada batch baru tanpa fit ulang.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL08

- Nomor: 8; role: explanation.
- Headline: Istilah ketiga — Mengisi nilai hilang menggunakan strategi yang dinyatakan.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Mengisi nilai hilang menggunakan strategi yang dinyatakan.
- Primary visual: Imputasi median; label/relasi: Training teramati1,3,5 → median3; hasil1,3,3,5. Uraian teks tetap tersedia.
- Information architecture: Imputasi median sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Training teramati1,3,5 → median3.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL09

- Nomor: 9; role: explanation.
- Headline: Mekanisme awal — Untuk nilai hilang numerik, imputer median mempelajari median training.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Untuk nilai hilang numerik, imputer median mempelajari median training. Data baru tidak digunakan untuk menghitung ulang median pada prosedur ini.
- Primary visual: Rumus bersatuan; label/relasi: z=(x−mu)/s; mu3, s sqrt2; z tidak bersatuan. Uraian teks tetap tersedia.
- Information architecture: Rumus bersatuan sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: z=(x−mu)/s.
- LO: W03-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL10

- Nomor: 10; role: student-action.
- Headline: Trace keputusan — Hitung median, mean dan s setelah imputasi; trace fit lalu transform pada batch baru.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Hitung median, mean dan s setelah imputasi; trace fit lalu transform pada batch baru.
- Primary visual: Trace batch baru; label/relasi: Isi missing dulu, kemudian centering/scaling; mahasiswa hitung. Uraian teks tetap tersedia.
- Information architecture: Trace batch baru sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: jawab WK02 pada stimulus DATA; output alasan/trace tertulis; debrief menunjuk kunci Q02 pada GUIDE/RUBRIC DOSEN.
- Bottom takeaway: Isi missing dulu, kemudian centering/scaling.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL11

- Nomor: 11; role: worked-example.
- Headline: Worked example — Training SIMULASI volume [1,missing,3,5] dengan kanal [A,B,A,B].
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Training SIMULASI volume [1,missing,3,5] dengan kanal [A,B,A,B]. Median training=3 sehingga volume menjadi [1,3,3,5]. Mean=3; simpangan baku ddof=0=sqrt(2). Untuk batch baru volume [missing,7] kanal [C,A], median tetap 3; z pertama=0 dan z kedua=4/sqrt(2). Kategori C diberi indikator A=0,B=0 oleh ignore, tidak membentuk kolom baru.
- Primary visual: Tabel hasil; label/relasi: Training4×3; baru2×3; missingbaru z0; 7 z4/sqrt2. Uraian teks tetap tersedia.
- Information architecture: Tabel hasil sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Training4×3.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL12

- Nomor: 12; role: explanation.
- Headline: Mekanisme berikutnya — StandardScaler menggunakan z=(x−mu)/s dengan mu mean training dan s simpangan baku populasi (ddof=0) training setelah imputasi pada contoh.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: StandardScaler menggunakan z=(x−mu)/s dengan mu mean training dan s simpangan baku populasi (ddof=0) training setelah imputasi pada contoh. z tidak bersatuan. Jika s=0, API menangani skala fitur konstan; periksa sumber/runtime, bukan bagi nol manual.
- Primary visual: One-hot mapping; label/relasi: A→[1,0], B→[0,1], C→[0,0] dengan ignore. Uraian teks tetap tersedia.
- Information architecture: One-hot mapping sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: A→[1,0], B→[0,1], C→[0,0] dengan ignore.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL13

- Nomor: 13; role: explanation.
- Headline: Batas metode — OneHotEncoder mempelajari kategori training.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: OneHotEncoder mempelajari kategori training. handle_unknown=ignore menghasilkan semua indikator nol untuk kategori yang belum dikenal; itu bukan jaminan kategori baru aman secara semantik.
- Primary visual: Panel kategori baru; label/relasi: Semua nol bukan bukti C aman atau sama dengan kategori tertentu. Uraian teks tetap tersedia.
- Information architecture: Panel kategori baru sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Semua nol bukan bukti C aman atau sama dengan kategori tertentu.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL14

- Nomor: 14; role: explanation.
- Headline: Miskonsepsi — Transform mempertahankan keadaan dari fit pada prosedur ini.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Transform mempertahankan keadaan dari fit pada prosedur ini.
- Primary visual: Mitos–koreksi; label/relasi: Transform tidak mempelajari median batch baru. Uraian teks tetap tersedia.
- Information architecture: Mitos–koreksi sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Transform tidak mempelajari median batch baru.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL15

- Nomor: 15; role: student-action.
- Headline: Kritik klaim — Seorang teman fit ulang imputer pada gabungan training+batch baru.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Seorang teman fit ulang imputer pada gabungan training+batch baru. Apakah itu transform yang sama?
- Primary visual: Dua prosedur; label/relasi: fit training saja versus fit gabungan; mahasiswa telusuri asal median. Uraian teks tetap tersedia.
- Information architecture: Dua prosedur sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: jawab WK03 pada stimulus DATA; output alasan/trace tertulis; debrief menunjuk kunci Q03 pada GUIDE/RUBRIC DOSEN.
- Bottom takeaway: fit training saja versus fit gabungan.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL16

- Nomor: 16; role: explanation.
- Headline: Periksa asumsi — ColumnTransformer memilih perlakuan per kolom.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: ColumnTransformer memilih perlakuan per kolom. Pipeline menempatkan imputer/scaler di dalam setiap fit; fitur masa depan tetap harus dibuang melalui keputusan data, bukan diserahkan pada Pipeline.
- Primary visual: Kolom dalam pipeline; label/relasi: Num: imputer→scaler; category: encoder; gabungkan transform. Uraian teks tetap tersedia.
- Information architecture: Kolom dalam pipeline sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Num: imputer→scaler.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL17

- Nomor: 17; role: explanation.
- Headline: Koreksi kekeliruan — Kode kategori tidak otomatis bermakna jarak; pilih representasi berdasarkan tujuan.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Kode kategori tidak otomatis bermakna jarak; pilih representasi berdasarkan tujuan.
- Primary visual: Kartu fitur masa depan; label/relasi: Pipeline bukan pemeriksa waktu fitur. Uraian teks tetap tersedia.
- Information architecture: Kartu fitur masa depan sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Pipeline bukan pemeriksa waktu fitur.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL18

- Nomor: 18; role: explanation.
- Headline: Rangkuman — Belajar parameter sekali, terapkan pada data baru.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Belajar parameter sekali, terapkan pada data baru; keputusan dan alasan ditelusuri dari input.
- Primary visual: Ringkasan batas; label/relasi: Asal parameter diketahui; penerapan pada input baru terlacak. Uraian teks tetap tersedia.
- Information architecture: Ringkasan batas sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Asal parameter diketahui.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL19

- Nomor: 19; role: explanation.
- Headline: Remediasi — Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.
- Primary visual: Tangga trace ulang; label/relasi: Satu parameter → baris training → keputusan → batchbaru. Uraian teks tetap tersedia.
- Information architecture: Tangga trace ulang sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Satu parameter → baris training → keputusan → batchbaru.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W03-SL20

- Nomor: 20; role: student-action.
- Headline: Exit ticket — Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.
- Subtitle: Preprocessing dan Feature Engineering; satu langkah yang dapat dijelaskan.
- Pesan utama: Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.
- Primary visual: Exit card; label/relasi: Parameter | asal input | penerapan | batas. Uraian teks tetap tersedia.
- Information architecture: Exit card sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W03-EX01, SIMULASI.
- Student action: exit ticket: satu keputusan, bukti dan batas; debrief periksa kedua LO, bukan skor saja.
- Bottom takeaway: Parameter | asal input | penerapan | batas.
- LO: W03-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.
