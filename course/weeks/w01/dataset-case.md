---
artifact_id: W01-DATA
title: Pengantar AI dan Machine Learning — DATA
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
workbook_dependencies: RPS topic + case requirement
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

# Pengantar AI dan Machine Learning — DATA

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Konteks dan asal

Empat kartu SIMULASI: C1 deteksi spam dengan email berlabel → supervised klasifikasi; C2 prakiraan konsumsi esok kWh dengan sejarah konsumsi → supervised regresi; C3 segmentasi pelanggan tanpa label kelompok → unsupervised clustering; C4 thermostat mengikuti aturan suhu >= 28 → aturan eksplisit tanpa fit. Untuk C1, unit=email, fitur=panjang/subjek yang tersedia saat diterima, target=spam/tidak, manfaat=prioritas pemeriksaan. Keluhan pengguna yang terjadi kemudian tidak tersedia saat email diterima.

W01-EX01: seluruh data **SIMULASI**, dibuat dari literal/generator deterministik di kode; tidak diunduh, bukan data manusia nyata. W04 memakai seed42 dan tiga struktur kasus; W01–W03 literal tanpa RNG. Tidak ada file dataset fisik/notebook yang diklaim terbit. Dataset ini untuk inspeksi konsep, bukan generalisasi bisnis.

## Data dictionary

| Kolom | Tipe/satuan | Makna/batas |
| --- | --- | --- |
| id | string | C1–C4, ID kasus sintetis |
| input | string | Deskripsi fitur yang tersedia sebelum keputusan |
| target | string/null | Kategori/nilai acuan atau tidak ada pada C3/C4 |

## Akses, ukuran dan kualitas

Input lengkap tercantum pada starter LAB serta worked example di atas. W01 empat kartu; W02 lima baris; W03 training 4/batch baru 2; W04 kasus A 120×6, kelompok 20×6 dan waktu 60. Null/missing/kategori baru sengaja dibuat sebagai kasus belajar. Jangan menyamakan missing dengan nol atau menganggap kategori baru mewakili populasi.

## Validasi dan risiko

W01 menilai framing, bukan akurasi. W02 hanya eksplorasi tabel dan tidak mengklaim sebab. W03 fit parameter pada empat training, transform dua batch baru. W04 test dipagari dari CV; kelompok/waktu mengikuti skenario. Semua hasil demo dapat menjadi exposed jika digunakan kembali; proyek harus memilih holdout baru dengan provenance. Bias/privasi pada contoh ini batas transfer ke data nyata, bukan statistik bias yang sudah diukur. Tidak ada klaim lisensi sumber eksternal; kode/generator dibuat untuk repo dari API lokal yang dirujuk.

## Sumber dan batas

[Snapshot dokumentasi lokal](../../../references/technical-runtime-sources.md): classifiermixin, regressormixin, kmeans. SRC-TECH-001/002/003 adalah dokumentasi runtime yang dibaca; SRC-MASTER-PROMPT hanya desain. Perhitungan/hasil kode diperiksa pada laporan run, bukan klaim performa umum. Kode/topik baseline dari workbook Production_Backlog!C:D; rumusan outcome resmi belum tersedia.

Kamus data mengikuti starter: id/input/target. Solution DOSEN menambahkan method sebagai anotasi keputusan, bukan input model atau kolom yang wajib diketahui mahasiswa.
