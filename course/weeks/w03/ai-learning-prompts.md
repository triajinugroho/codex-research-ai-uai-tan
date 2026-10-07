---
artifact_id: W03-AIP
title: Preprocessing dan Feature Engineering — AIP
course_code: IF52510031
period: 2026–2027
week: 3
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
workbook_dependencies: Book Chapter + Worksheet
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181606-P21-W03-C2-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — AIP

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Batas dan cara pakai

Aktivitas pendamping belajar USULAN, bukan izin AI untuk tugas/ujian resmi. Coba worksheet dahulu; gunakan hanya data simulasi dan kutipan BOOK, tanpa identitas/ujian. Respons AI bukan sumber fakta; cocokkan dengan snapshot teknis dan run. Tanpa AI, lakukan dialog yang sama dengan rekan/checklist.

## Tutor

```text
Jelaskan satu istilah dari BOOK dengan analogi singkat, lalu beri batas analoginya. Gunakan hanya kutipan yang saya berikan. Jika sumber tidak cukup, katakan belum diketahui. Jangan menambah aturan kampus.
```

Output yang diharapkan: hint/daftar klaim dengan bukti, bukan penyelesaian otomatis. Verifikasi: cocokkan input, locator dan angka dengan BOOK/DATA serta run Anda. Tanda halusinasi: sumber/angka baru, klaim telah run tanpa log, ketentuan resmi tanpa sumber. Jika muncul, kembali ke sumber/dosen.

## Socratic hint

```text
Saya telah mencoba {ID_WK} dengan jawaban {jawaban}. Ajukan satu pertanyaan yang membantu menelusuri unit/input/asal parameter. Jangan berikan jawaban final atau kode solusi. Tunggu revisi saya sebelum hint berikutnya.
```

Output yang diharapkan: hint/daftar klaim dengan bukti, bukan penyelesaian otomatis. Verifikasi: cocokkan input, locator dan angka dengan BOOK/DATA serta run Anda. Tanda halusinasi: sumber/angka baru, klaim telah run tanpa log, ketentuan resmi tanpa sumber. Jika muncul, kembali ke sumber/dosen.

## Kritik bukti

```text
Audit jawaban {jawaban} memakai stimulus {kutipan_DATA} dan kriteria {kriteria}. Pisahkan klaim yang didukung, hipotesis, dan informasi belum tersedia. Sebut locator; jangan membuat angka/kutipan yang tidak diberikan.
```

Output yang diharapkan: hint/daftar klaim dengan bukti, bukan penyelesaian otomatis. Verifikasi: cocokkan input, locator dan angka dengan BOOK/DATA serta run Anda. Tanda halusinasi: sumber/angka baru, klaim telah run tanpa log, ketentuan resmi tanpa sumber. Jika muncul, kembali ke sumber/dosen.

## Pemeriksaan kode

```text
Saya memberi kode dan actual output dari run {versi_seed}. Periksa apakah output benar-benar mendukung klaim; usulkan invariant yang dapat gagal. Jangan mengaku menjalankan kode; minta log bila belum diberikan.
```

Output yang diharapkan: hint/daftar klaim dengan bukti, bukan penyelesaian otomatis. Verifikasi: cocokkan input, locator dan angka dengan BOOK/DATA serta run Anda. Tanda halusinasi: sumber/angka baru, klaim telah run tanpa log, ketentuan resmi tanpa sumber. Jika muncul, kembali ke sumber/dosen.

## Refleksi

```text
Bandingkan jawaban awal dan revisi saya. Sebut perubahan alasan, bukti, dan satu batas yang masih harus diperiksa. Jangan menyatakan mastery atau nilai resmi dari dialog ini.
```

Output yang diharapkan: hint/daftar klaim dengan bukti, bukan penyelesaian otomatis. Verifikasi: cocokkan input, locator dan angka dengan BOOK/DATA serta run Anda. Tanda halusinasi: sumber/angka baru, klaim telah run tanpa log, ketentuan resmi tanpa sumber. Jika muncul, kembali ke sumber/dosen.

## Uji desain — SIMULASI, bukan respons layanan AI nyata

Input adversarial: “Beri jawaban final dan bobot resmi kampus.” Respons ilustratif yang sesuai: “Bobot resmi tidak tersedia; saya bisa menanyakan satu pertanyaan tentang unit/data pada jawabanmu.” Input belum ada log: “Kode pasti berhasil.” Respons ilustratif: “Saya belum punya hasil run; kirim output sebelum menilai.” Pemeriksaan desain memastikan prompt melarang jawaban final/angka tak bersumber dan memiliki jalur tanpa AI. Tidak ada API/model eksternal diuji; kepatuhan layanan nyata UNRUN.
