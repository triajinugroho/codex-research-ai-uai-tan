---
artifact_id: W03-ASSESS
title: Preprocessing dan Feature Engineering — ASSESS
course_code: IF52510031
period: 2026–2027
week: 3
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
workbook_dependencies: RTM + outcome
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181607-P21-W03-D-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
- course/production/reports/20261007-182459-P16-outcome-tags-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — ASSESS

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Jenis dan instruksi

W03-ASM01 **USULAN latihan formatif**, bukan tugas/ujian resmi yang disahkan. Tiga butir Q01–Q03, skor lokal demonstrasi masing-masing 2, total 6; bukan bobot mata kuliah. Estimasi20–30 menit USULAN. Tenggat/kanal/penalti/AI/kolaborasi resmi PERLU KONFIRMASI SUMBER. Latihan mengulang konsep dengan alasan, bukan tes baru yang rahasia.

Stimulus lengkap: [DATA](dataset-case.md) dan worked example BOOK. Tulis jawaban bernomor, sumber/versi input, alasan serta revisi. Tidak memerlukan akses kunci dosen. Kriteria terbuka: Q01 pilihan beralasan; Q02 trace/perhitungan dan asal input; Q03 kritik batas klaim. Jawaban alternatif diterima jika asumsi dinyatakan dan sesuai konteks.

### W03-Q01

LO W03-LO01; maksimum 2 lokal USULAN.

Tentukan imputasi volume dan representasi channel; beri alasan dan penanganan kategori C.

Output: alasan dan langkah/bukti.

### W03-Q02

LO W03-LO02; maksimum 2 lokal USULAN.

Hitung median, mean dan s setelah imputasi; trace fit lalu transform pada batch baru.

Output: alasan dan langkah/bukti.

### W03-Q03

LO W03-LO02; maksimum 2 lokal USULAN.

Seorang teman fit ulang imputer pada gabungan training+batch baru. Apakah itu transform yang sama?

Output: alasan dan langkah/bukti.
