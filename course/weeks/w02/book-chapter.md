---
artifact_id: W02-BOOK
title: Eksplorasi Data untuk ML — BOOK
course_code: IF52510031
period: 2026–2027
week: 2
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
- W02-LO01
- W02-LO02
official_outcome_refs:
- DAIML-Sub-CPMK102-1
assessment_ids:
- W02-ASM01
example_ids:
- W02-EX01
evidence_requirement_ids:
- W02-EV01
source_ids:
- SRC-WORKBOOK
- SRC-TECH-001
- SRC-TECH-002
- SRC-TECH-003
dependencies: []
integration_refs: []
workbook_dependencies: Semester learning map + book TOC
scope_record: course/weeks/w02/scope.md
validation_records:
- course/production/reports/20261007-181559-P21-W02-A-validation.md
- course/production/reports/20261007-181603-P15-P16-W02-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Eksplorasi Data untuk ML — BOOK

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Orientasi dan tujuan

W02-LO01: Membuat profil tipe data, missingness, distribusi dan dugaan duplikasi. W02-LO02: Membedakan observasi dari hipotesis penyebab dan memilih pemeriksaan lanjutan. Sesudah membaca, hasilkan alasan keputusan dan trace/memo yang dapat diperiksa. Prasyarat: membaca tabel sederhana; bekal antarpekan ditulis pada scope. Semua tujuan lokal adalah USULAN.

## WHY

Transformasi tanpa profil dapat menghapus pola yang benar atau mempertahankan cacat data.

## Intuisi

Mental model: **Profil dahulu, kesimpulan dibatasi bukti**. Analogi membantu memulai, tetapi bukan definisi formal atau bukti. Pada kasus kita, periksa input, keputusan, keluaran dan waktu informasi tersedia sebelum menyebut hasil benar.

## Definisi

| Istilah | Definisi dan batas |
| --- | --- |
| Missingness | Ketiadaan nilai, dihitung per kolom dengan isna. |
| Distribusi | Ringkasan nilai yang terlihat pada data, bukan otomatis populasi. |
| Duplikasi | Baris identik menurut kolom yang dipilih; harus disebut definisinya. |
| Observasi | Pernyataan yang langsung ditopang tabel/hasil pemeriksaan. |
| Hipotesis | Dugaan penjelasan yang memerlukan pemeriksaan tambahan. |
| Satuan | Makna kuantitatif kolom, misalnya menit; angka tanpa satuan mudah disalahartikan. |

## Konsep dan mekanisme

### Tahap 1

isna menghasilkan mask nilai hilang; jumlah True memberi count. Proporsi hilang adalah count/n pada kolom dengan n baris. Missing bukan nol; nol dapat merupakan nilai yang sah.

### Tahap 2

duplicated menghitung pengulangan sesuai subset kolom; mempertahankan kemunculan pertama membuat jumlah duplikat lebih kecil daripada jumlah baris pada kelompok berulang. Nyatakan subset dan keep yang dipakai.

### Tahap 3

describe merangkum kolom numerik. Mean dan median merangkum data berbeda; pada contoh kecil bandingkan keduanya tanpa klaim distribusi populasi atau sebab.

### Tahap 4

Korelasi/pola bersama belum membuktikan sebab. Memo harus memisahkan observasi, dugaan, keputusan sementara dan data tambahan. Jangan menghapus outlier semata karena jarang; periksa satuan dan proses ukur.

## Worked example

Tabel SIMULASI lima baris: durasi menit [10,20,missing,20,90], kelas kanal [A,B,A,B,B]. Missing durasi=1/5=20%; median nilai teramati [10,20,20,90]=20; mean=35. Dengan subset durasi+kanal dan keep=first, baris keempat mengulang baris kedua sehingga count duplikat=1. Angka 90 adalah observasi jauh dari nilai lain; salah ukur hanya hipotesis sampai proses ukur diperiksa.

Langkah kerja: tulis input dan satuan → pilih tindakan dengan alasan → telusuri parameter/bagian data → hitung/inspeksi hasil → batasi klaim. Contoh ini SIMULASI dengan data yang diberikan, bukan statistik kelas/populasi. Kode verifikasi disimpan dalam solusi dosen dan dijalankan dari Markdown.

## Miskonsepsi dan koreksi

| Pernyataan | Koreksi |
| --- | --- |
| Tanpa missing berarti data sempurna | Satuan, duplikasi, bias cakupan dan waktu tetap perlu diperiksa. |
| Outlier selalu salah | Nilai 90 bisa sah; audit konteks sebelum menghapus. |
| Duplikat punya satu definisi universal | Subset dan unit observasi menentukan pemeriksaan. |

## Penerapan dan keterbatasan

Contoh kecil dirancang untuk inspeksi, bukan model produksi. Ukuran/satuan/parameter dipilih untuk belajar; dataset riil memerlukan audit proses data, izin, representativitas dan tujuan. Bukti jawaban adalah alasan serta trace, bukan nama API atau skor saja. Hubungkan keluaran pekan ini dengan prasyarat pekan selanjutnya, tanpa menganggap source_status workbook berarti file telah siap.

## Latihan dan refleksi

1. Tunjukkan asumsi yang harus benar agar keputusan pada contoh tepat.
2. Ubah satu asumsi (waktu informasi/definisi unit/tipe fitur) dan jelaskan keputusan yang perlu ditinjau ulang.
3. Bedakan hasil yang benar-benar dihitung dari hipotesis. Kerjakan [worksheet](worksheet.md) sesudah tersedia.

## Rangkuman

Profil dahulu, kesimpulan dibatasi bukti. LO01 diperiksa melalui pemilihan yang beralasan; LO02 melalui batas/trace dan interpretasi. Jangan menaikkan klaim melampaui data/prosedur yang diperiksa.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): dataframeisna, dataframeduplicated, dataframemedian, dataframedescribe. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.

## Sambungan W01–W04

Profil W02 mengajarkan alasan memilih transformasi pada W03; literal volume W03 berbeda dari durasi W02, sehingga angka tidak dipindahkan tanpa provenance.

Bekal: [modul W01](../w01/student-module.md).

Lanjut: [modul W03](../w03/student-module.md).
