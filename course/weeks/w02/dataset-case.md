---
artifact_id: W02-DATA
title: Eksplorasi Data untuk ML — DATA
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
workbook_dependencies: RPS topic + case requirement
scope_record: course/weeks/w02/scope.md
validation_records:
- course/production/reports/20261007-181559-P21-W02-C1-validation.md
- course/production/reports/20261007-181603-P15-P16-W02-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Eksplorasi Data untuk ML — DATA

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Konteks dan asal

Tabel SIMULASI lima baris: durasi menit [10,20,missing,20,90], kelas kanal [A,B,A,B,B]. Missing durasi=1/5=20%; median nilai teramati [10,20,20,90]=20; mean=35. Dengan subset durasi+kanal dan keep=first, baris keempat mengulang baris kedua sehingga count duplikat=1. Angka 90 adalah observasi jauh dari nilai lain; salah ukur hanya hipotesis sampai proses ukur diperiksa.

W02-EX01: seluruh data **SIMULASI**, dibuat dari literal/generator deterministik di kode; tidak diunduh, bukan data manusia nyata. W04 memakai seed42 dan tiga struktur kasus; W01–W03 literal tanpa RNG. Tidak ada file dataset fisik/notebook yang diklaim terbit. Dataset ini untuk inspeksi konsep, bukan generalisasi bisnis.

## Data dictionary

| Kolom | Tipe/satuan | Makna/batas |
| --- | --- | --- |
| row_id | integer | 1–5, ID baris simulasi; bukan ID orang |
| duration_min | float | Durasi menit, satu nilai missing |
| channel | category | A/B, kategori kanal sintetis |

## Akses, ukuran dan kualitas

Input lengkap tercantum pada starter LAB serta worked example di atas. W01 empat kartu; W02 lima baris; W03 training 4/batch baru 2; W04 kasus A 120×6, kelompok 20×6 dan waktu 60. Null/missing/kategori baru sengaja dibuat sebagai kasus belajar. Jangan menyamakan missing dengan nol atau menganggap kategori baru mewakili populasi.

## Validasi dan risiko

W01 menilai framing, bukan akurasi. W02 hanya eksplorasi tabel dan tidak mengklaim sebab. W03 fit parameter pada empat training, transform dua batch baru. W04 test dipagari dari CV; kelompok/waktu mengikuti skenario. Semua hasil demo dapat menjadi exposed jika digunakan kembali; proyek harus memilih holdout baru dengan provenance. Bias/privasi pada contoh ini batas transfer ke data nyata, bukan statistik bias yang sudah diukur. Tidak ada klaim lisensi sumber eksternal; kode/generator dibuat untuk repo dari API lokal yang dirujuk.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): dataframeisna, dataframeduplicated, dataframemedian, dataframedescribe. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.
