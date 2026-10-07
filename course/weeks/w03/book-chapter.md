---
artifact_id: W03-BOOK
title: Preprocessing dan Feature Engineering — BOOK
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
source_status: NOT STARTED
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
workbook_dependencies: Semester learning map + book TOC
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181603-P21-W03-A-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — BOOK

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Orientasi dan tujuan

W03-LO01: Memilih transformasi berdasarkan tipe fitur dan kebutuhan model. W03-LO02: Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru. Sesudah membaca, hasilkan alasan keputusan dan trace/memo yang dapat diperiksa. Prasyarat: membaca tabel sederhana; bekal antarpekan ditulis pada scope. Semua tujuan lokal adalah USULAN.

## WHY

Transformasi yang mengambil informasi evaluasi dapat merusak makna penilaian model.

## Intuisi

Mental model: **Belajar parameter sekali, terapkan pada data baru**. Analogi membantu memulai, tetapi bukan definisi formal atau bukti. Pada kasus kita, periksa input, keputusan, keluaran dan waktu informasi tersedia sebelum menyebut hasil benar.

## Definisi

| Istilah | Definisi dan batas |
| --- | --- |
| Fit | Mempelajari keadaan/parameter estimator pada data training yang diberikan. |
| Transform | Menerapkan keadaan yang telah dipelajari pada input. |
| Imputasi | Mengisi nilai hilang menggunakan strategi yang dinyatakan. |
| Scaling | Mengubah representasi skala; standard scaler mengurangi mean dan membagi simpangan baku yang dipelajari. |
| One-hot | Representasi kategori menjadi kolom indikator; kategori baru memerlukan aturan. |
| Pipeline | Rangkaian transformasi dan estimator; tidak menjamin fitur tersedia pada waktu prediksi. |

## Konsep dan mekanisme

### Tahap 1

Untuk nilai hilang numerik, imputer median mempelajari median training. Data baru tidak digunakan untuk menghitung ulang median pada prosedur ini.

### Tahap 2

StandardScaler menggunakan z=(x−mu)/s dengan mu mean training dan s simpangan baku populasi (ddof=0) training setelah imputasi pada contoh. z tidak bersatuan. Jika s=0, API menangani skala fitur konstan; periksa sumber/runtime, bukan bagi nol manual.

### Tahap 3

OneHotEncoder mempelajari kategori training. handle_unknown=ignore menghasilkan semua indikator nol untuk kategori yang belum dikenal; itu bukan jaminan kategori baru aman secara semantik.

### Tahap 4

ColumnTransformer memilih perlakuan per kolom. Pipeline menempatkan imputer/scaler di dalam setiap fit; fitur masa depan tetap harus dibuang melalui keputusan data, bukan diserahkan pada Pipeline.

## Worked example

Training SIMULASI volume [1,missing,3,5] dengan kanal [A,B,A,B]. Median training=3 sehingga volume menjadi [1,3,3,5]. Mean=3; simpangan baku ddof=0=sqrt(2). Untuk batch baru volume [missing,7] kanal [C,A], median tetap 3; z pertama=0 dan z kedua=4/sqrt(2). Kategori C diberi indikator A=0,B=0 oleh ignore, tidak membentuk kolom baru.

Langkah kerja: tulis input dan satuan → pilih tindakan dengan alasan → telusuri parameter/bagian data → hitung/inspeksi hasil → batasi klaim. Contoh ini SIMULASI dengan data yang diberikan, bukan statistik kelas/populasi. Kode verifikasi disimpan dalam solusi dosen dan dijalankan dari Markdown.

## Miskonsepsi dan koreksi

| Pernyataan | Koreksi |
| --- | --- |
| Transform juga belajar parameter baru | Transform mempertahankan keadaan dari fit pada prosedur ini. |
| Kode kategori 1/2 memiliki jarak numerik | Kode kategori tidak otomatis bermakna jarak; pilih representasi berdasarkan tujuan. |
| Pipeline menyelesaikan setiap leakage | Pipeline tidak mendeteksi fitur yang baru ada setelah prediksi. |

## Penerapan dan keterbatasan

Contoh kecil dirancang untuk inspeksi, bukan model produksi. Ukuran/satuan/parameter dipilih untuk belajar; dataset riil memerlukan audit proses data, izin, representativitas dan tujuan. Bukti jawaban adalah alasan serta trace, bukan nama API atau skor saja. Hubungkan keluaran pekan ini dengan prasyarat pekan selanjutnya, tanpa menganggap source_status workbook berarti file telah siap.

## Latihan dan refleksi

1. Tunjukkan asumsi yang harus benar agar keputusan pada contoh tepat.
2. Ubah satu asumsi (waktu informasi/definisi unit/tipe fitur) dan jelaskan keputusan yang perlu ditinjau ulang.
3. Bedakan hasil yang benar-benar dihitung dari hipotesis. Kerjakan [worksheet](worksheet.md) sesudah tersedia.

## Rangkuman

Belajar parameter sekali, terapkan pada data baru. LO01 diperiksa melalui pemilihan yang beralasan; LO02 melalui batas/trace dan interpretasi. Jangan menaikkan klaim melampaui data/prosedur yang diperiksa.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): simpleimputer, standardscaler, onehotencoder, columntransformer, pipeline. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.

## Sambungan W01–W04

Trace fit/transform W03 menjadi batas parameter pada fold W04; data training contoh W03 bukan test final W04.

Bekal: [modul W02](../w02/student-module.md).

Lanjut: [modul W04](../w04/student-module.md).
