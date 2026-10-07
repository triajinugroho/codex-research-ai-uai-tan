---
artifact_id: W04-RUBRIC
title: Pembagian Data dan Validasi — RUBRIC
course_code: IF52510031
period: 2026–2027
week: 4
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
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
workbook_dependencies: Assignment / Quiz
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

# Pembagian Data dan Validasi — RUBRIC

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

**DOSEN — kunci/solusi tidak masuk rute mahasiswa.**

## Skor lokal USULAN

Setiap butir maksimum 2: 2 keputusan/hasil dan alasan inti tepat; 1 bagian benar tetapi alasan/trace belum lengkap; 0 tidak menunjukkan indikator atau bertentangan dengan konteks. Total6 sama dengan soal. Ini skor latihan, bukan nilai resmi. Belum mengumpulkan/belum ditelaah bukan otomatis skor 0. RC01 mengukur LO01; RC02 mengukur LO02.

### W04-Q01 / W04-WK01

LO W04-LO01; RC01; kunci: A holdout/stratified CV development; B group split; C forward time split dengan gap beralasan. Stratifikasi menjaga label, bukan identitas kelompok; alternatif sah jika tujuan deployment berbeda dan dinyatakan.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Stratifikasi mencegah kelompok bocor. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

### W04-Q02 / W04-WK02

LO W04-LO02; RC02; kunci: Test belum dipagari, transformasi melihat validation/test, dan test dipakai memilih kandidat. Pisahkan test; CV development dengan transformasi di training fold; tetapkan kandidat sebelum evaluasi test.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Seed tetap membuat split benar. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

### W04-Q03 / W04-WK03

LO W04-LO02; RC02; kunci: Dev90/test30; tiga fold hanya pada dev90; training per fold60/validation30 pada desain ini. Tidak: seed tidak menghapus informasi test yang sudah dipakai.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: CV mengizinkan tuning di test. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

## Solusi praktik dan toleransi

[Solusi reference DOSEN](lab-solution.md) memuat kode yang diekstrak dan dijalankan. Actual output:

```json
{
  "seed": 42,
  "n_dev": 90,
  "n_test": 30,
  "fold_scores": [
    0.5333333333333333,
    0.5333333333333333,
    0.5
  ],
  "mean_cv": 0.5222222222222223,
  "group_overlap": false,
  "last_time_fold": [
    47,
    50,
    59
  ],
  "holdout_demo_now_exposed": true
}
```

Angka floating dibandingkan dengan np.isclose/np.allclose default pada run; kategori/shape/count tepat. Hasil dataset/seed berbeda tidak dibandingkan dengan angka kasus ini tanpa provenance. Semua worksheet dan soal mempunyai kunci; stimulus tidak meminta informasi di luar data yang diberikan.

## Kalibrasi jawaban jangkar — SIMULASI

Jangkar A: keputusan sesuai kunci dengan alasan dan batas →2. Jangkar B: keputusan inti benar tanpa asal data/alasan →1. Jangkar C: bertentangan dengan stimulus atau klaim resmi rekaan →0 pada indikator terkait. Penelaahan desain mencoba soal dari stimulus dan mencocokkan arithmetic/reference; belum kalibrasi penilai nyata atau statistik kesulitan mahasiswa.

## Remediasi

LO01: kembali ke unit/tujuan/tipe input. LO02: telusuri satu parameter/kalimat dari bukti sampai klaim, bedakan informasi yang belum tersedia. Telaah revisi tiap LO; jangan menutupi gap dengan total skor latihan.
