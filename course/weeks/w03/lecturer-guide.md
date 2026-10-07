---
artifact_id: W03-GUIDE
title: Preprocessing dan Feature Engineering — GUIDE
course_code: IF52510031
period: 2026–2027
week: 3
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
workbook_dependencies: Student Module
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181604-P21-W03-B-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — GUIDE

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

**DOSEN — jangan masuk manifest mahasiswa.**

## Persiapan dan agenda USULAN

Baca scope/BOOK/MOD, siapkan tabel kasus, runtime CPU/offline dan worksheet. Gunakan proporsi hook/diagnosis 15%, intuisi/konsep 25%, contoh/praktik 40%, kritik/refleksi 20%; total 100%, bukan durasi kelas resmi. Source S01–S03 belum tersedia; tugas digunakan sebagai rancangan formatif.

| Trigger | Aksi mahasiswa | Indikator teramati | Debrief |
| --- | --- | --- | --- |
| Hook: Transformasi yang mengambil informasi evaluasi dapat merusak makna penilaian model. | Prediksi WK01 | Alasan merujuk input/tujuan | Bandingkan alasan dengan asumsi kasus |
| Pertanyaan asal informasi/parameter | Trace WK02 | Tiap parameter/keputusan punya asal | Bedakan data yang boleh digunakan dan yang belum diketahui |
| Klaim berlebihan pada WK03 | Kritik dengan bukti | Observasi dan hipotesis terpisah | Tanyakan pemeriksaan yang dapat membantah hipotesis |
| Exit ticket | Tuliskan batas klaim | LO01/02 mempunyai bukti | Rencanakan ulang butir yang belum memadai |

## Expected responses DOSEN

| Diagnosis/soal | Respons dan alternatif |
| --- | --- |
| Tentukan imputasi volume dan representasi channel; beri alasan dan penanganan kategori C. | Median training 3 untuk volume; one-hot kanal dengan ignore sebagai strategi kasus. C menjadi semua nol; alternatif encoder sah bila menjelaskan makna dan batas data. |
| Hitung median, mean dan s setelah imputasi; trace fit lalu transform pada batch baru. | Median=3; data [1,3,3,5]; mu=3; s=sqrt(2), ddof0; missing baru z0 dan 7 z4/sqrt2. Parameter tetap berasal training. |
| Seorang teman fit ulang imputer pada gabungan training+batch baru. Apakah itu transform yang sama? | Tidak; asal parameter berubah dan batch baru ikut belajar. Jika batch baru evaluasi, prosedur itu melanggar kontrak; fit training, transform batch baru. |

## Demonstrasi, transisi dan contingency

Prediksi dahulu, lalu starter. Solusi reference di lab-solution untuk demo dosen; tidak salin ke paket mahasiswa. Jika import gagal, baca traceback, periksa versi; gunakan tabel/trace tanpa mengklaim kode dijalankan. Setelah contoh, minta mahasiswa menjelaskan batas sebelum pindah ke asesmen. Jika konsep dasar lemah, bridge unit/fitur/target/fit–transform dan ulangi satu kasus.

## Adaptasi terpisah

IF24A: fakta hanya kode kelas; USULAN diskusi berpasangan jika sesi langsung tersedia, amati alasan setiap peserta. IF24H: fakta hanya kode kelas; USULAN anotasi mandiri+checkpoint jika dibutuhkan. Keduanya output dan RC sama, mode/jadwal tidak ditebak. Pengayaan: ubah asumsi kasus, jangan menambah API berbayar atau materi di luar scope inti.

## Pascakelas

Gunakan QA/EVID untuk bukti aktual; belum ada hasil mahasiswa, waktu nyata atau statistik yang diisi. KEEP/FIX/ADD/REMOVE ditopang locator dan contoh bukti anonim setelah tersedia.
