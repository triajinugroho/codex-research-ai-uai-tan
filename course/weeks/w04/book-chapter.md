---
artifact_id: W04-BOOK
title: Pembagian Data dan Validasi — BOOK
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
workbook_dependencies: Semester learning map + book TOC
scope_record: course/weeks/w04/scope.md
validation_records:
- course/production/reports/20261007-181458-P21-W04-A-validation.md
- course/production/reports/20261007-181504-P15-P16-W04-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182037-P16-dictionary-and-example-ids-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pembagian Data dan Validasi — BOOK

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Orientasi dan tujuan

W04-LO01: Memilih strategi split/CV sesuai tujuan prediksi, unit independen, kelompok dan waktu. W04-LO02: Mendeteksi leakage dan merancang batas fit serta penggunaan test. Sesudah membaca, hasilkan alasan keputusan dan trace/memo yang dapat diperiksa. Prasyarat: membaca tabel sederhana; bekal antarpekan ditulis pada scope. Semua tujuan lokal adalah USULAN.

## WHY

Skor hanya bermakna jika prosedur evaluasi meniru data yang akan dihadapi dan tidak dipakai untuk memilih jawaban.

## Intuisi

Mental model: **Pagar data mengikuti tujuan generalisasi**. Analogi membantu memulai, tetapi bukan definisi formal atau bukti. Pada kasus kita, periksa input, keputusan, keluaran dan waktu informasi tersedia sebelum menyebut hasil benar.

## Definisi

| Istilah | Definisi dan batas |
| --- | --- |
| Training | Subset yang digunakan pada fit model/transformasi. |
| Development/validation | Data untuk memeriksa atau memilih kandidat; dapat dibagi beberapa fold. |
| Test | Data terpisah untuk evaluasi akhir prosedur setelah pilihan ditetapkan; jika digunakan memilih kandidat, tidak lagi independen untuk klaim itu. |
| Fold | Satu pembagian training/validation di dalam data pengembangan. |
| Group | Unit yang mengaitkan beberapa baris, misalnya pengguna sintetis. |
| Leakage | Informasi di luar batas tersedia/diizinkan masuk ke pengembangan atau prediksi. |

## Konsep dan mekanisme

### Tahap 1

Pisahkan test sebelum pengembangan kandidat. Pada contoh 120 baris, test 25%=30 dan development=90. CV tiga fold berjalan hanya pada 90 development, bukan seluruh 120. Ukuran ini pilihan SIMULASI, bukan ketentuan kampus.

### Tahap 2

StratifiedKFold berusaha menjaga proporsi label pada fold; itu tidak mencegah pengguna sama ada di dua sisi. Untuk tujuan pengguna baru, GroupKFold menjaga kelompok tidak beririsan. Tujuan catatan baru pengguna lama dapat membutuhkan desain berbeda.

### Tahap 3

TimeSeriesSplit melatih pada blok terdahulu dan mengevaluasi blok kemudian. gap mengeluarkan sejumlah sampel sebelum test; pilih gap dari horizon/ketergantungan, bukan menganggap default selalu benar. Data contoh berjarak sama dan sudah terurut.

### Tahap 4

Imputer/scaler harus di-fit di training fold. Rerata CV mean(s1,s2,s3) merangkum run pada kandidat; variasi fold tidak otomatis tiga observasi independen. Pipeline membantu batas fit, tetapi tidak mencegah label proxy/fitur masa depan.

### Tahap 5

Seed membuat run dapat diulang pada runtime tertentu; seed tidak membuktikan kesesuaian split. Test yang pernah dibuka pada demo disebut exposed ketika dipakai lagi; mengganti seed pada data yang sama tidak memulihkan independensi.

## Worked example

Tiga skenario SIMULASI: A satu baris per unit independen, target kategori seimbang → holdout/stratified CV pada development; B enam catatan per group_id, deployment kelompok baru → GroupKFold; C 60 waktu berjarak sama, prediksi masa depan → TimeSeriesSplit(n_splits=3,test_size=10,gap=2). Kasus cacat D fit scaler pada seluruh data sebelum CV: perbaiki dengan Pipeline yang di-fit ulang di tiap training fold. Tidak dijanjikan skor selalu turun/naik; verifikasi asal parameter dan disjointness dahulu.

Langkah kerja: tulis input dan satuan → pilih tindakan dengan alasan → telusuri parameter/bagian data → hitung/inspeksi hasil → batasi klaim. Contoh ini SIMULASI dengan data yang diberikan, bukan statistik kelas/populasi. Kode verifikasi disimpan dalam solusi dosen dan dijalankan dari Markdown.

## Miskonsepsi dan koreksi

| Pernyataan | Koreksi |
| --- | --- |
| Stratifikasi mencegah kelompok bocor | Label proporsi dan identitas kelompok masalah berbeda. |
| Seed tetap membuat split benar | Seed tidak memperbaiki tujuan deployment atau urutan waktu. |
| CV mengizinkan tuning di test | CV hanya memakai development; test yang disentuh memilih model tidak final independen. |
| Pipeline melarang fitur masa depan | Pemilihan fitur berdasarkan waktu tetap audit manusia. |

## Penerapan dan keterbatasan

Contoh kecil dirancang untuk inspeksi, bukan model produksi. Ukuran/satuan/parameter dipilih untuk belajar; dataset riil memerlukan audit proses data, izin, representativitas dan tujuan. Bukti jawaban adalah alasan serta trace, bukan nama API atau skor saja. Hubungkan keluaran pekan ini dengan prasyarat pekan selanjutnya, tanpa menganggap source_status workbook berarti file telah siap.

## Latihan dan refleksi

1. Tunjukkan asumsi yang harus benar agar keputusan pada contoh tepat.
2. Ubah satu asumsi (waktu informasi/definisi unit/tipe fitur) dan jelaskan keputusan yang perlu ditinjau ulang.
3. Bedakan hasil yang benar-benar dihitung dari hipotesis. Kerjakan [worksheet](worksheet.md) sesudah tersedia.

## Rangkuman

Pagar data mengikuti tujuan generalisasi. LO01 diperiksa melalui pemilihan yang beralasan; LO02 melalui batas/trace dan interpretasi. Jangan menaikkan klaim melampaui data/prosedur yang diperiksa.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): train_test_split, stratifiedkfold, groupkfold, timeseriessplit, pipeline, numpymean. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.

## Sambungan W01–W04

W01 menyediakan unit/fitur/target; W02 menyediakan audit struktur; W03 menyediakan trace parameter. Ketiganya sekarang mempunyai naskah nyata, tetapi tidak ada klaim mahasiswa sudah mengikuti kelas.

Bekal: [modul W03](../w03/student-module.md).
