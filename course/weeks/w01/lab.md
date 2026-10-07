---
artifact_id: W01-LAB
title: Pengantar AI dan Machine Learning — LAB
course_code: IF52510031
period: 2026–2027
week: 1
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
workbook_dependencies: Dataset / Case + Book Chapter
scope_record: course/weeks/w01/scope.md
validation_records:
- course/production/reports/20261007-181554-P21-W01-C1-validation.md
- course/production/reports/20261007-181557-P15-P16-W01-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pengantar AI dan Machine Learning — LAB

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Tujuan, runtime dan input

W01-LO01/02; input [DATA](dataset-case.md). Jalur CPU/offline setelah paket terpasang. Runtime yang benar-benar tersedia: Python3.12, NumPy2.3.5, pandas2.2.3, scikit-learn1.8.0. Tidak memakai jaringan saat run; tidak membuat gambar. Target waktu/memori bukan batas kelas resmi dan diukur pada laporan.

## Starter runnable — LAB-STARTER

Salin utuh ke file sementara dan jalankan `python3 starter.py`. Starter hanya menyiapkan input/inspeksi, bukan solusi akhir. Expected: input terbaca dan tidak ada error; hasil konsep/perhitungan tetap Anda kerjakan.

```python
cards = [
 {"id":"C1","input":"email saat diterima","target":"spam/tidak"},
 {"id":"C2","input":"konsumsi historis","target":"kWh esok"},
 {"id":"C3","input":"profil belanja","target":None},
 {"id":"C4","input":"suhu saat ini, aturan tetap","target":None},
]
for card in cards:
    print(card)
# Tulis kategori, alasan dan problem statement pada worksheet; bukan TODO sintaks.
```

## Langkah praktik

1. Tulis prediksi sebelum kode: Klasifikasikan empat kartu C1–C4; beri alasan serta bedakan C3 dari C4.
2. Buat pemeriksaan untuk Rumuskan C1: unit, fitur, target dan manfaat. Apakah keluhan setelah email diterima boleh dipakai untuk prediksi saat penerimaan? Gunakan metode yang dijelaskan pada BOOK; catat input/kolom/subset/parameter.
3. Jelaskan keputusan dan batas yang diminta WK03. Jangan menganggap keluaran print sebagai alasan yang cukup.
4. Tambahkan assert yang dapat gagal jika keputusan salah: bentuk/missing/count untuk W02, asal parameter/kategori baru W03, disjoint indeks/kelompok/urutan waktu W04; W01 cek kategori dari arti target, bukan tipe penyimpanan.
5. Jalankan dari keadaan bersih; simpan versi paket, seed, output dan error. Kode inti reference dosen diuji terpisah, tidak ada solusi di naskah mahasiswa.

## Checkpoint dan output

Empat kartu dan jenis kasus; bukan hasil akurasi model. Angka tepat dari SIMULASI dapat dibandingkan dengan worked example; runtime/hasil diperiksa pada laporan akhir pekan. Output pengumpulan: prediksi awal, kode yang dijalankan, actual output, alasan, batas dan refleksi perbaikan. Bukan notebook yang sudah diterbitkan.

## Troubleshooting/fallback

ImportError: cek paket/versi pada mesin Anda; lingkungan ini sudah menyediakan dependensi. Shape berubah: periksa kolom/input dan versi API. NaN tersisa: cek imputer/fit scope. Kategori baru: cek handle_unknown. Jika runtime tidak tersedia, kerjakan trace tabel dan tandai kode UNRUN; jangan mengarang output. Tidak ada proses/service yang perlu cleanup; file sementara boleh dihapus setelah hasil dicatat.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): classifiermixin, regressormixin, kmeans. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.
