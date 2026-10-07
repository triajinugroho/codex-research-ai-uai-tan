---
artifact_id: W02-GUIDE
title: Eksplorasi Data untuk ML — GUIDE
course_code: IF52510031
period: 2026–2027
week: 2
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
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
workbook_dependencies: Student Module
scope_record: course/weeks/w02/scope.md
validation_records:
- course/production/reports/20261007-181559-P21-W02-B-validation.md
- course/production/reports/20261007-181603-P15-P16-W02-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Eksplorasi Data untuk ML — GUIDE

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

**DOSEN — jangan masuk manifest mahasiswa.**

## Persiapan dan agenda USULAN

Baca scope/BOOK/MOD, siapkan tabel kasus, runtime CPU/offline dan worksheet. Gunakan proporsi hook/diagnosis 15%, intuisi/konsep 25%, contoh/praktik 40%, kritik/refleksi 20%; total 100%, bukan durasi kelas resmi. Source S01–S03 belum tersedia; tugas digunakan sebagai rancangan formatif.

| Trigger | Aksi mahasiswa | Indikator teramati | Debrief |
| --- | --- | --- | --- |
| Hook: Transformasi tanpa profil dapat menghapus pola yang benar atau mempertahankan cacat data. | Prediksi WK01 | Alasan merujuk input/tujuan | Bandingkan alasan dengan asumsi kasus |
| Pertanyaan asal informasi/parameter | Trace WK02 | Tiap parameter/keputusan punya asal | Bedakan data yang boleh digunakan dan yang belum diketahui |
| Klaim berlebihan pada WK03 | Kritik dengan bukti | Observasi dan hipotesis terpisah | Tanyakan pemeriksaan yang dapat membantah hipotesis |
| Exit ticket | Tuliskan batas klaim | LO01/02 mempunyai bukti | Rencanakan ulang butir yang belum memadai |

## Expected responses DOSEN

| Diagnosis/soal | Respons dan alternatif |
| --- | --- |
| Hitung missing count dan proporsi duration_min; jelaskan penyebutnya. | 1 nilai hilang dari 5 baris, 1/5=0.2=20%; jangan membagi hanya 4 nilai teramati. |
| Hitung median dan mean nilai teramati. Tentukan duplikat berdasarkan duration_min+channel, keep=first. | Median=20 menit, mean=35 menit; satu pengulangan, baris 4 dibanding baris 2. row_id dikecualikan dengan alasan memeriksa isi pengukuran. |
| Nilai 90 membuktikan kesalahan ukur? Tulis observasi, hipotesis, keputusan sementara dan pemeriksaan lanjutan. | Observasi=90 jauh dari tiga nilai lain; hipotesis=salah ukur atau durasi sah; sementara tandai/periksa, tidak otomatis hapus; cari log/prosedur/satuan/context. |

## Demonstrasi, transisi dan contingency

Prediksi dahulu, lalu starter. Solusi reference di lab-solution untuk demo dosen; tidak salin ke paket mahasiswa. Jika import gagal, baca traceback, periksa versi; gunakan tabel/trace tanpa mengklaim kode dijalankan. Setelah contoh, minta mahasiswa menjelaskan batas sebelum pindah ke asesmen. Jika konsep dasar lemah, bridge unit/fitur/target/fit–transform dan ulangi satu kasus.

## Adaptasi terpisah

IF24A: fakta hanya kode kelas; USULAN diskusi berpasangan jika sesi langsung tersedia, amati alasan setiap peserta. IF24H: fakta hanya kode kelas; USULAN anotasi mandiri+checkpoint jika dibutuhkan. Keduanya output dan RC sama, mode/jadwal tidak ditebak. Pengayaan: ubah asumsi kasus, jangan menambah API berbayar atau materi di luar scope inti.

## Pascakelas

Gunakan QA/EVID untuk bukti aktual; belum ada hasil mahasiswa, waktu nyata atau statistik yang diisi. KEEP/FIX/ADD/REMOVE ditopang locator dan contoh bukti anonim setelah tersedia.
