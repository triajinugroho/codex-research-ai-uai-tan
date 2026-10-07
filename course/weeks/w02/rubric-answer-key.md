---
artifact_id: W02-RUBRIC
title: Eksplorasi Data untuk ML — RUBRIC
course_code: IF52510031
period: 2026–2027
week: 2
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
workbook_dependencies: Assignment / Quiz
scope_record: course/weeks/w02/scope.md
validation_records:
- course/production/reports/20261007-181601-P21-W02-D-validation.md
- course/production/reports/20261007-181603-P15-P16-W02-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
- course/production/reports/20261007-182459-P16-outcome-tags-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Eksplorasi Data untuk ML — RUBRIC

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

**DOSEN — kunci/solusi tidak masuk rute mahasiswa.**

## Skor lokal USULAN

Setiap butir maksimum 2: 2 keputusan/hasil dan alasan inti tepat; 1 bagian benar tetapi alasan/trace belum lengkap; 0 tidak menunjukkan indikator atau bertentangan dengan konteks. Total6 sama dengan soal. Ini skor latihan, bukan nilai resmi. Belum mengumpulkan/belum ditelaah bukan otomatis skor 0. RC01 mengukur LO01; RC02 mengukur LO02.

### W02-Q01 / W02-WK01

LO W02-LO01; RC01; kunci: 1 nilai hilang dari 5 baris, 1/5=0.2=20%; jangan membagi hanya 4 nilai teramati.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Tanpa missing berarti data sempurna. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

### W02-Q02 / W02-WK02

LO W02-LO01; RC01; kunci: Median=20 menit, mean=35 menit; satu pengulangan, baris 4 dibanding baris 2. row_id dikecualikan dengan alasan memeriksa isi pengukuran.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Outlier selalu salah. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

### W02-Q03 / W02-WK03

LO W02-LO02; RC02; kunci: Observasi=90 jauh dari tiga nilai lain; hipotesis=salah ukur atau durasi sah; sementara tandai/periksa, tidak otomatis hapus; cari log/prosedur/satuan/context.

Partial credit: hasil inti benar tetapi alasan/batas belum lengkap=1; hasil dan alasan sesuai=2; bertentangan inti/tanpa bukti=0. Alternatif sah harus menyebut asumsi yang mengubah keputusan; jangan menilai sekadar nama API. Kesalahan umum: Duplikat punya satu definisi universal. Tindak lanjut: ulangi satu input dan telusuri tahap yang hilang.

## Solusi praktik dan toleransi

[Solusi reference DOSEN](lab-solution.md) memuat kode yang diekstrak dan dijalankan. Actual output:

```json
{
  "shape": [
    5,
    3
  ],
  "missing": 1,
  "missing_pct": 20.0,
  "median": 20.0,
  "mean": 35.0,
  "duplicates_subset": 1
}
```

Angka floating dibandingkan dengan np.isclose/np.allclose default pada run; kategori/shape/count tepat. Hasil dataset/seed berbeda tidak dibandingkan dengan angka kasus ini tanpa provenance. Semua worksheet dan soal mempunyai kunci; stimulus tidak meminta informasi di luar data yang diberikan.

## Kalibrasi jawaban jangkar — SIMULASI

Jangkar A: keputusan sesuai kunci dengan alasan dan batas →2. Jangkar B: keputusan inti benar tanpa asal data/alasan →1. Jangkar C: bertentangan dengan stimulus atau klaim resmi rekaan →0 pada indikator terkait. Penelaahan desain mencoba soal dari stimulus dan mencocokkan arithmetic/reference; belum kalibrasi penilai nyata atau statistik kesulitan mahasiswa.

## Remediasi

LO01: kembali ke unit/tujuan/tipe input. LO02: telusuri satu parameter/kalimat dari bukti sampai klaim, bedakan informasi yang belum tersedia. Telaah revisi tiap LO; jangan menutupi gap dengan total skor latihan.
