---
artifact_id: W04-WORK
title: Pembagian Data dan Validasi — WORK
course_code: IF52510031
period: 2026–2027
week: 4
classes:
- IF24A
- IF24H
audience: mahasiswa
distribution: student_candidate
version: '0.5'
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
workbook_dependencies: Book Chapter + Student Module
scope_record: course/weeks/w04/scope.md
validation_records:
- course/production/reports/20261007-181503-P21-W04-C2-validation.md
- course/production/reports/20261007-181504-P15-P16-W04-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182037-P16-dictionary-and-example-ids-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
- course/production/reports/20261007-182459-P16-outcome-tags-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pembagian Data dan Validasi — WORK

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Instruksi dan stimulus

Gunakan tabel/kasus lengkap pada [DATA](dataset-case.md). Semua contoh SIMULASI. Ini latihan berhint, bukan ketentuan nilai resmi; estimasi10–20 menit USULAN. Tulis prediksi sebelum kode, lalu revisi dengan bukti.

### W04-WK01

LO: W04-LO01. Stimulus: DATA dan worked example BOOK; input lengkap tercantum di sana.

Pilih strategi untuk A unit independen berlabel, B kelompok berulang dengan deployment kelompok baru, C prediksi masa depan. Jelaskan mengapa stratifikasi saja tidak cukup pada B.

Output: alasan + tabel/trace/interpretasi; ruang jawaban: tulis pada dokumen kerja Anda. Hint1: tunjukkan unit dan waktu informasi. Hint2: pisahkan data yang tersedia dari asumsi, telusuri satu langkah dahulu. Jangan membuka solusi reference saat prediksi.

### W04-WK02

LO: W04-LO02. Stimulus: DATA dan worked example BOOK; input lengkap tercantum di sana.

Prosedur: fit scaler seluruh 120 → CV seluruh 120 → pilih model dengan skor test. Tandai pelanggaran dan perbaiki diagram.

Output: alasan + tabel/trace/interpretasi; ruang jawaban: tulis pada dokumen kerja Anda. Hint1: tunjukkan unit dan waktu informasi. Hint2: pisahkan data yang tersedia dari asumsi, telusuri satu langkah dahulu. Jangan membuka solusi reference saat prediksi.

### W04-WK03

LO: W04-LO02. Stimulus: DATA dan worked example BOOK; input lengkap tercantum di sana.

Pada 120 baris test25%, berapa dev/test? Tiga fold CV memakai subset mana? Apakah mengganti seed memulihkan test yang dipakai tuning?

Output: alasan + tabel/trace/interpretasi; ruang jawaban: tulis pada dokumen kerja Anda. Hint1: tunjukkan unit dan waktu informasi. Hint2: pisahkan data yang tersedia dari asumsi, telusuri satu langkah dahulu. Jangan membuka solusi reference saat prediksi.

## Refleksi

Tulis satu jawaban yang berubah setelah pemeriksaan dan bukti yang mengubahnya. Periksa LO01 melalui alasan keputusan, LO02 melalui trace/batas. Kriteria transparan ada pada ASSESS; kunci hanya pada paket dosen.
