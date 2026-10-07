---
artifact_id: W01-BOOK
title: Pengantar AI dan Machine Learning — BOOK
course_code: IF52510031
period: 2026–2027
week: 1
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
- W01-LO01
- W01-LO02
official_outcome_refs:
- DAIML-Sub-CPMK082-1
assessment_ids:
- W01-ASM01
example_ids:
- W01-EX01
evidence_requirement_ids:
- W01-EV01
source_ids:
- SRC-WORKBOOK
- SRC-TECH-001
- SRC-TECH-002
- SRC-TECH-003
dependencies: []
integration_refs: []
workbook_dependencies: Semester learning map + book TOC
scope_record: course/weeks/w01/scope.md
validation_records:
- course/production/reports/20261007-181554-P21-W01-A-validation.md
- course/production/reports/20261007-181557-P15-P16-W01-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pengantar AI dan Machine Learning — BOOK

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Orientasi dan tujuan

W01-LO01: Mengklasifikasikan kasus AI/ML, supervised/unsupervised, klasifikasi/regresi dengan alasan. W01-LO02: Merumuskan unit observasi, fitur tersedia saat prediksi, target dan manfaat keputusan. Sesudah membaca, hasilkan alasan keputusan dan trace/memo yang dapat diperiksa. Prasyarat: membaca tabel sederhana; bekal antarpekan ditulis pada scope. Semua tujuan lokal adalah USULAN.

## WHY

Salah merumuskan target membuat model yang rapi menjawab pertanyaan yang salah.

## Intuisi

Mental model: **Keputusan dahulu, model kemudian**. Analogi membantu memulai, tetapi bukan definisi formal atau bukti. Pada kasus kita, periksa input, keputusan, keluaran dan waktu informasi tersedia sebelum menyebut hasil benar.

## Definisi

| Istilah | Definisi dan batas |
| --- | --- |
| Unit observasi | Objek yang diwakili satu baris data; contoh satu email. |
| Fitur | Input yang tersedia ketika keputusan dibuat; contoh panjang email. |
| Target/label | Keluaran yang hendak diprediksi; contoh spam/tidak spam. |
| Supervised | Kasus dengan keluaran acuan y untuk fit; klasifikasi memakai kategori, regresi nilai numerik. |
| Unsupervised | Kasus pembentukan kelompok tanpa label kategori acuan pada contoh ini. |
| Fit dan predict | Fit membentuk keadaan estimator dari input; predict menggunakan estimator pada input berikutnya. |

## Konsep dan mekanisme

### Tahap 1

AI dipakai sebagai payung kerja pedagogi untuk sistem yang menjalankan tugas cerdas; ini kerangka operasional USULAN, bukan batas universal yang disahkan. ML pada contoh ini memakai estimator yang di-fit pada data. Aturan tertulis tanpa fit dibedakan dari model yang belajar; jangan menyimpulkan setiap otomatisasi adalah ML.

### Tahap 2

Pemilihan klasifikasi atau regresi bergantung makna target, bukan tipe penyimpanan. Kode angka 0/1 untuk spam tetap kategori; suhu 29.5 derajat adalah nilai dengan satuan. Clustering membentuk kelompok; nomor kelompok bukan label kebenaran yang sudah diberikan.

### Tahap 3

ClassifierMixin dan RegressorMixin pada sumber lokal mengharuskan y saat fit. KMeans mencontohkan pembentukan cluster. Paket ini belum mengajarkan algoritma KMeans; kartu segmentasi hanya menentukan jenis tugas.

### Tahap 4

Fitur yang baru diketahui setelah keputusan tidak boleh menjadi input ketika tugasnya prediksi sebelum keputusan. Ini pemeriksaan waktu pada kasus, bukan jaminan bahwa semua leakage terselesaikan.

## Worked example

Empat kartu SIMULASI: C1 deteksi spam dengan email berlabel → supervised klasifikasi; C2 prakiraan konsumsi esok kWh dengan sejarah konsumsi → supervised regresi; C3 segmentasi pelanggan tanpa label kelompok → unsupervised clustering; C4 thermostat mengikuti aturan suhu >= 28 → aturan eksplisit tanpa fit. Untuk C1, unit=email, fitur=panjang/subjek yang tersedia saat diterima, target=spam/tidak, manfaat=prioritas pemeriksaan. Keluhan pengguna yang terjadi kemudian tidak tersedia saat email diterima.

Langkah kerja: tulis input dan satuan → pilih tindakan dengan alasan → telusuri parameter/bagian data → hitung/inspeksi hasil → batasi klaim. Contoh ini SIMULASI dengan data yang diberikan, bukan statistik kelas/populasi. Kode verifikasi disimpan dalam solusi dosen dan dijalankan dari Markdown.

## Miskonsepsi dan koreksi

| Pernyataan | Koreksi |
| --- | --- |
| Angka berarti regresi | 0/1 spam adalah kode kategori; jelaskan makna target. |
| Skor tinggi berarti manfaat pasti | Manfaat keputusan memerlukan konteks dan biaya kesalahan, bukan skor saja. |
| Setiap otomatisasi belajar | Thermostat aturan tetap pada kartu tidak mengalami fit. |

## Penerapan dan keterbatasan

Contoh kecil dirancang untuk inspeksi, bukan model produksi. Ukuran/satuan/parameter dipilih untuk belajar; dataset riil memerlukan audit proses data, izin, representativitas dan tujuan. Bukti jawaban adalah alasan serta trace, bukan nama API atau skor saja. Hubungkan keluaran pekan ini dengan prasyarat pekan selanjutnya, tanpa menganggap source_status workbook berarti file telah siap.

## Latihan dan refleksi

1. Tunjukkan asumsi yang harus benar agar keputusan pada contoh tepat.
2. Ubah satu asumsi (waktu informasi/definisi unit/tipe fitur) dan jelaskan keputusan yang perlu ditinjau ulang.
3. Bedakan hasil yang benar-benar dihitung dari hipotesis. Kerjakan [worksheet](worksheet.md) sesudah tersedia.

## Rangkuman

Keputusan dahulu, model kemudian. LO01 diperiksa melalui pemilihan yang beralasan; LO02 melalui batas/trace dan interpretasi. Jangan menaikkan klaim melampaui data/prosedur yang diperiksa.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): classifiermixin, regressormixin, kmeans. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.

## Sambungan W01–W04

Framing W01 membantu menentukan unit/kolom pada W02; dataset contoh W02 adalah kasus durasi tersendiri, bukan email yang sama.

Lanjut: [modul W02](../w02/student-module.md).
