---
artifact_id: W03-RUBRIC
title: Preprocessing dan Feature Engineering — RUBRIC
course_code: IF52510031
period: 2026–2027
week: 3
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
workbook_dependencies: Assignment / Quiz
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

# Preprocessing dan Feature Engineering — RUBRIC

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

**DOSEN — kunci/solusi tidak masuk rute mahasiswa.**

## Skor lokal USULAN

Setiap butir maksimum 2: 2 keputusan/hasil dan alasan inti tepat; 1 bagian benar tetapi alasan/trace belum lengkap; 0 tidak menunjukkan indikator atau bertentangan dengan konteks. Total6 sama dengan soal. Ini skor latihan, bukan nilai resmi. Belum mengumpulkan/belum ditelaah bukan otomatis skor 0. RC01 mengukur LO01; RC02 mengukur LO02.

### W03-Q01 / W03-WK01

LO W03-LO01; RC01; kunci: Median training 3 untuk volume; one-hot kanal dengan ignore sebagai strategi kasus. C menjadi semua nol; alternatif encoder sah bila menjelaskan makna dan batas data.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Transform juga belajar parameter baru. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

### W03-Q02 / W03-WK02

LO W03-LO02; RC02; kunci: Median=3; data [1,3,3,5]; mu=3; s=sqrt(2), ddof0; missing baru z0 dan 7 z4/sqrt2. Parameter tetap berasal training.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Kode kategori 1/2 memiliki jarak numerik. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

### W03-Q03 / W03-WK03

LO W03-LO02; RC02; kunci: Tidak; asal parameter berubah dan batch baru ikut belajar. Jika batch baru evaluasi, prosedur itu melanggar kontrak; fit training, transform batch baru.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Pipeline menyelesaikan setiap leakage. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

## Solusi praktik dan toleransi

[Solusi reference DOSEN](lab-solution.md) memuat kode yang diekstrak dan dijalankan. Actual output:

```json
{
  "median_training": 3.0,
  "mean_training": 3.0,
  "scale_training": 1.4142135623730951,
  "new_transformed": [
    [
      0.0,
      0.0,
      0.0
    ],
    [
      2.82842712474619,
      1.0,
      0.0
    ]
  ],
  "shape_training": [
    4,
    3
  ]
}
```

Angka floating dibandingkan dengan np.isclose/np.allclose default pada run; kategori/shape/count tepat. Hasil dataset/seed berbeda tidak dibandingkan dengan angka kasus ini tanpa provenance. Semua worksheet dan soal mempunyai kunci; stimulus tidak meminta informasi di luar data yang diberikan.

## Kalibrasi jawaban jangkar — SIMULASI

Jangkar A: keputusan sesuai kunci dengan alasan dan batas →2. Jangkar B: keputusan inti benar tanpa asal data/alasan →1. Jangkar C: bertentangan dengan stimulus atau klaim resmi rekaan →0 pada indikator terkait. Penelaahan desain mencoba soal dari stimulus dan mencocokkan arithmetic/reference; belum kalibrasi penilai nyata atau statistik kesulitan mahasiswa.

## Remediasi

LO01: kembali ke unit/tujuan/tipe input. LO02: telusuri satu parameter/kalimat dari bukti sampai klaim, bedakan informasi yang belum tersedia. Telaah revisi tiap LO; jangan menutupi gap dengan total skor latihan.
