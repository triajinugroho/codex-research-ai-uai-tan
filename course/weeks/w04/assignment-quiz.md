---
artifact_id: W04-ASSESS
title: Pembagian Data dan Validasi — ASSESS
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
source_status: DRAFT
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
workbook_dependencies: RTM + outcome
scope_record: course/weeks/w04/scope.md
validation_records:
- course/production/reports/20261007-181503-P21-W04-D-validation.md
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

# Pembagian Data dan Validasi — ASSESS

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Jenis dan instruksi

W04-ASM01 **USULAN latihan formatif**, bukan tugas/ujian resmi yang disahkan. Tiga butir Q01–Q03, skor lokal demonstrasi masing-masing 2, total 6; bukan bobot mata kuliah. Estimasi20–30 menit USULAN. Tenggat/kanal/penalti/AI/kolaborasi resmi PERLU KONFIRMASI SUMBER. Latihan mengulang konsep dengan alasan, bukan tes baru yang rahasia.

Stimulus lengkap: [DATA](dataset-case.md) dan worked example BOOK. Tulis jawaban bernomor, sumber/versi input, alasan serta revisi. Tidak memerlukan akses kunci dosen. Kriteria terbuka: Q01 pilihan beralasan; Q02 trace/perhitungan dan asal input; Q03 kritik batas klaim. Jawaban alternatif diterima jika asumsi dinyatakan dan sesuai konteks.

### W04-Q01

LO W04-LO01; maksimum 2 lokal USULAN.

Pilih strategi untuk A unit independen berlabel, B kelompok berulang dengan deployment kelompok baru, C prediksi masa depan. Jelaskan mengapa stratifikasi saja tidak cukup pada B.

Output: alasan dan langkah/bukti.

### W04-Q02

LO W04-LO02; maksimum 2 lokal USULAN.

Prosedur: fit scaler seluruh 120 → CV seluruh 120 → pilih model dengan skor test. Tandai pelanggaran dan perbaiki diagram.

Output: alasan dan langkah/bukti.

### W04-Q03

LO W04-LO02; maksimum 2 lokal USULAN.

Pada 120 baris test25%, berapa dev/test? Tiga fold CV memakai subset mana? Apakah mengganti seed memulihkan test yang dipakai tuning?

Output: alasan dan langkah/bukti.
