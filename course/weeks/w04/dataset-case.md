---
artifact_id: W04-DATA
title: Pembagian Data dan Validasi — DATA
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
workbook_dependencies: RPS topic + case requirement
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

# Pembagian Data dan Validasi — DATA

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Konteks dan asal

Tiga skenario SIMULASI: A satu baris per unit independen, target kategori seimbang → holdout/stratified CV pada development; B enam catatan per group_id, deployment kelompok baru → GroupKFold; C 60 waktu berjarak sama, prediksi masa depan → TimeSeriesSplit(n_splits=3,test_size=10,gap=2). Kasus cacat D fit scaler pada seluruh data sebelum CV: perbaiki dengan Pipeline yang di-fit ulang di tiap training fold. Tidak dijanjikan skor selalu turun/naik; verifikasi asal parameter dan disjointness dahulu.

W04-EX01: seluruh data **SIMULASI**, dibuat dari literal/generator deterministik di kode; tidak diunduh, bukan data manusia nyata. W04 memakai seed42 dan tiga struktur kasus; W01–W03 literal tanpa RNG. Tidak ada file dataset fisik/notebook yang diklaim terbit. Dataset ini untuk inspeksi konsep, bukan generalisasi bisnis.

## Data dictionary

| Kolom | Tipe/satuan | Makna/batas |
| --- | --- | --- |
| x0–x5 | float | Enam fitur sintetis make_classification; x0 beberapa NaN |
| y | binary category | Label sintetis 0/1; bukan outcome mahasiswa |
| row_index | integer | 0–119, identitas baris kasus A |
| group_id | integer | 20 kelompok, masing-masing 6 catatan kasus B |
| time_index | integer | 0–59 waktu berjarak sama kasus C |

## Akses, ukuran dan kualitas

Input lengkap tercantum pada starter LAB serta worked example di atas. W01 empat kartu; W02 lima baris; W03 training 4/batch baru 2; W04 kasus A 120×6, kelompok 20×6 dan waktu 60. Null/missing/kategori baru sengaja dibuat sebagai kasus belajar. Jangan menyamakan missing dengan nol atau menganggap kategori baru mewakili populasi.

## Validasi dan risiko

W01 menilai framing, bukan akurasi. W02 hanya eksplorasi tabel dan tidak mengklaim sebab. W03 fit parameter pada empat training, transform dua batch baru. W04 test dipagari dari CV; kelompok/waktu mengikuti skenario. Semua hasil demo dapat menjadi exposed jika digunakan kembali; proyek harus memilih holdout baru dengan provenance. Bias/privasi pada contoh ini batas transfer ke data nyata, bukan statistik bias yang sudah diukur. Tidak ada klaim lisensi sumber eksternal; kode/generator dibuat untuk repo dari API lokal yang dirujuk.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): train_test_split, stratifiedkfold, groupkfold, timeseriessplit, pipeline, numpymean. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.

## ID contoh tetap

W04-EX01=A holdout/stratified CV; W04-EX02=B group_id; W04-EX03=C waktu/gap; W04-EX04=D prosedur cacat fit seluruh data versus fit training fold. Semua berada dalam recipe LAB yang sama; tidak menyatakan empat dataset fisik dibuat.
