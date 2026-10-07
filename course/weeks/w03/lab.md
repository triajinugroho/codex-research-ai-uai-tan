---
artifact_id: W03-LAB
title: Preprocessing dan Feature Engineering — LAB
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
workbook_dependencies: Dataset / Case + Book Chapter
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181604-P21-W03-C1-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — LAB

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Tujuan, runtime dan input

W03-LO01/02; input [DATA](dataset-case.md). Jalur CPU/offline setelah paket terpasang. Runtime yang benar-benar tersedia: Python3.12, NumPy2.3.5, pandas2.2.3, scikit-learn1.8.0. Tidak memakai jaringan saat run; tidak membuat gambar. Target waktu/memori bukan batas kelas resmi dan diukur pada laporan.

## Starter runnable — LAB-STARTER

Salin utuh ke file sementara dan jalankan `python3 starter.py`. Starter hanya menyiapkan input/inspeksi, bukan solusi akhir. Expected: input terbaca dan tidak ada error; hasil konsep/perhitungan tetap Anda kerjakan.

```python
import numpy as np
import pandas as pd
train = pd.DataFrame({"volume":[1.,np.nan,3.,5.],"channel":["A","B","A","B"]})
new = pd.DataFrame({"volume":[np.nan,7.],"channel":["C","A"]})
print(train.to_string(index=False)); print(new.to_string(index=False))
# Prediksi median training dan perilaku C dahulu; ikuti langkah lab untuk membangun transformasi.
```

## Langkah praktik

1. Tulis prediksi sebelum kode: Tentukan imputasi volume dan representasi channel; beri alasan dan penanganan kategori C.
2. Buat pemeriksaan untuk Hitung median, mean dan s setelah imputasi; trace fit lalu transform pada batch baru. Gunakan metode yang dijelaskan pada BOOK; catat input/kolom/subset/parameter.
3. Jelaskan keputusan dan batas yang diminta WK03. Jangan menganggap keluaran print sebagai alasan yang cukup.
4. Tambahkan assert yang dapat gagal jika keputusan salah: bentuk/missing/count untuk W02, asal parameter/kategori baru W03, disjoint indeks/kelompok/urutan waktu W04; W01 cek kategori dari arti target, bukan tipe penyimpanan.
5. Jalankan dari keadaan bersih; simpan versi paket, seed, output dan error. Kode inti reference dosen diuji terpisah, tidak ada solusi di naskah mahasiswa.

## Checkpoint dan output

Median 3; mean 3; skala sqrt(2); batch baru 2×3 tanpa missing. Angka tepat dari SIMULASI dapat dibandingkan dengan worked example; runtime/hasil diperiksa pada laporan akhir pekan. Output pengumpulan: prediksi awal, kode yang dijalankan, actual output, alasan, batas dan refleksi perbaikan. Bukan notebook yang sudah diterbitkan.

## Troubleshooting/fallback

ImportError: cek paket/versi pada mesin Anda; lingkungan ini sudah menyediakan dependensi. Shape berubah: periksa kolom/input dan versi API. NaN tersisa: cek imputer/fit scope. Kategori baru: cek handle_unknown. Jika runtime tidak tersedia, kerjakan trace tabel dan tandai kode UNRUN; jangan mengarang output. Tidak ada proses/service yang perlu cleanup; file sementara boleh dihapus setelah hasil dicatat.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): simpleimputer, standardscaler, onehotencoder, columntransformer, pipeline. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.
