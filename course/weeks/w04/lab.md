---
artifact_id: W04-LAB
title: Pembagian Data dan Validasi — LAB
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
workbook_dependencies: Dataset / Case + Book Chapter
scope_record: course/weeks/w04/scope.md
validation_records:
- course/production/reports/20261007-181500-P21-W04-C1-validation.md
- course/production/reports/20261007-181504-P15-P16-W04-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182037-P16-dictionary-and-example-ids-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pembagian Data dan Validasi — LAB

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Tujuan, runtime dan input

W04-LO01/02; input [DATA](dataset-case.md). Jalur CPU/offline setelah paket terpasang. Runtime yang benar-benar tersedia: Python3.12, NumPy2.3.5, pandas2.2.3, scikit-learn1.8.0. Tidak memakai jaringan saat run; tidak membuat gambar. Target waktu/memori bukan batas kelas resmi dan diukur pada laporan.

## Starter runnable — LAB-STARTER

Salin utuh ke file sementara dan jalankan `python3 starter.py`. Starter hanya menyiapkan input/inspeksi, bukan solusi akhir. Expected: input terbaca dan tidak ada error; hasil konsep/perhitungan tetap Anda kerjakan.

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
X,y = make_classification(n_samples=120,n_features=6,n_informative=4,n_redundant=0,random_state=42)
X[::13,0] = np.nan
idx = np.arange(len(y))
dev,test = train_test_split(idx,test_size=.25,stratify=y,random_state=42)
print("Ukuran dev/test:",len(dev),len(test))
# Tuliskan invariant disjointness; kemudian ikuti langkah CV, group dan time pada lab.
```

## Langkah praktik

1. Tulis prediksi sebelum kode: Pilih strategi untuk A unit independen berlabel, B kelompok berulang dengan deployment kelompok baru, C prediksi masa depan. Jelaskan mengapa stratifikasi saja tidak cukup pada B.
2. Buat pemeriksaan untuk Prosedur: fit scaler seluruh 120 → CV seluruh 120 → pilih model dengan skor test. Tandai pelanggaran dan perbaiki diagram. Gunakan metode yang dijelaskan pada BOOK; catat input/kolom/subset/parameter.
3. Jelaskan keputusan dan batas yang diminta WK03. Jangan menganggap keluaran print sebagai alasan yang cukup.
4. Tambahkan assert yang dapat gagal jika keputusan salah: bentuk/missing/count untuk W02, asal parameter/kategori baru W03, disjoint indeks/kelompok/urutan waktu W04; W01 cek kategori dari arti target, bukan tipe penyimpanan.
5. Jalankan dari keadaan bersih; simpan versi paket, seed, output dan error. Kode inti reference dosen diuji terpisah, tidak ada solusi di naskah mahasiswa.

## Checkpoint dan output

Dev90/test30; tiga fold tanpa test; kelompok tidak overlap; waktu forward dengan gap2. Angka tepat dari SIMULASI dapat dibandingkan dengan worked example; runtime/hasil diperiksa pada laporan akhir pekan. Output pengumpulan: prediksi awal, kode yang dijalankan, actual output, alasan, batas dan refleksi perbaikan. Bukan notebook yang sudah diterbitkan.

## Troubleshooting/fallback

ImportError: cek paket/versi pada mesin Anda; lingkungan ini sudah menyediakan dependensi. Shape berubah: periksa kolom/input dan versi API. NaN tersisa: cek imputer/fit scope. Kategori baru: cek handle_unknown. Jika runtime tidak tersedia, kerjakan trace tabel dan tandai kode UNRUN; jangan mengarang output. Tidak ada proses/service yang perlu cleanup; file sementara boleh dihapus setelah hasil dicatat.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): train_test_split, stratifiedkfold, groupkfold, timeseriessplit, pipeline, numpymean. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.
