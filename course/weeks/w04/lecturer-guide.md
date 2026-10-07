---
artifact_id: W04-GUIDE
title: Pembagian Data dan Validasi — GUIDE
course_code: IF52510031
period: 2026–2027
week: 4
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
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
workbook_dependencies: Student Module
scope_record: course/weeks/w04/scope.md
validation_records:
- course/production/reports/20261007-181500-P21-W04-B-validation.md
- course/production/reports/20261007-181504-P15-P16-W04-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182037-P16-dictionary-and-example-ids-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Pembagian Data dan Validasi — GUIDE

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

**DOSEN — jangan masuk manifest mahasiswa.**

## Persiapan dan agenda USULAN

Baca scope/BOOK/MOD, siapkan tabel kasus, runtime CPU/offline dan worksheet. Gunakan proporsi hook/diagnosis 15%, intuisi/konsep 25%, contoh/praktik 40%, kritik/refleksi 20%; total 100%, bukan durasi kelas resmi. Source S01–S03 belum tersedia; tugas digunakan sebagai rancangan formatif.

| Trigger | Aksi mahasiswa | Indikator teramati | Debrief |
| --- | --- | --- | --- |
| Hook: Skor hanya bermakna jika prosedur evaluasi meniru data yang akan dihadapi dan tidak dipakai untuk memilih jawaban. | Prediksi WK01 | Alasan merujuk input/tujuan | Bandingkan alasan dengan asumsi kasus |
| Pertanyaan asal informasi/parameter | Trace WK02 | Tiap parameter/keputusan punya asal | Bedakan data yang boleh digunakan dan yang belum diketahui |
| Klaim berlebihan pada WK03 | Kritik dengan bukti | Observasi dan hipotesis terpisah | Tanyakan pemeriksaan yang dapat membantah hipotesis |
| Exit ticket | Tuliskan batas klaim | LO01/02 mempunyai bukti | Rencanakan ulang butir yang belum memadai |

## Expected responses DOSEN

| Diagnosis/soal | Respons dan alternatif |
| --- | --- |
| Pilih strategi untuk A unit independen berlabel, B kelompok berulang dengan deployment kelompok baru, C prediksi masa depan. Jelaskan mengapa stratifikasi saja tidak cukup pada B. | A holdout/stratified CV development; B group split; C forward time split dengan gap beralasan. Stratifikasi menjaga label, bukan identitas kelompok; alternatif sah jika tujuan deployment berbeda dan dinyatakan. |
| Prosedur: fit scaler seluruh 120 → CV seluruh 120 → pilih model dengan skor test. Tandai pelanggaran dan perbaiki diagram. | Test belum dipagari, transformasi melihat validation/test, dan test dipakai memilih kandidat. Pisahkan test; CV development dengan transformasi di training fold; tetapkan kandidat sebelum evaluasi test. |
| Pada 120 baris test25%, berapa dev/test? Tiga fold CV memakai subset mana? Apakah mengganti seed memulihkan test yang dipakai tuning? | Dev90/test30; tiga fold hanya pada dev90; training per fold60/validation30 pada desain ini. Tidak: seed tidak menghapus informasi test yang sudah dipakai. |

## Demonstrasi, transisi dan contingency

Prediksi dahulu, lalu starter. Solusi reference di lab-solution untuk demo dosen; tidak salin ke paket mahasiswa. Jika import gagal, baca traceback, periksa versi; gunakan tabel/trace tanpa mengklaim kode dijalankan. Setelah contoh, minta mahasiswa menjelaskan batas sebelum pindah ke asesmen. Jika konsep dasar lemah, bridge unit/fitur/target/fit–transform dan ulangi satu kasus.

## Adaptasi terpisah

IF24A: fakta hanya kode kelas; USULAN diskusi berpasangan jika sesi langsung tersedia, amati alasan setiap peserta. IF24H: fakta hanya kode kelas; USULAN anotasi mandiri+checkpoint jika dibutuhkan. Keduanya output dan RC sama, mode/jadwal tidak ditebak. Pengayaan: ubah asumsi kasus, jangan menambah API berbayar atau materi di luar scope inti.

## Pascakelas

Gunakan QA/EVID untuk bukti aktual; belum ada hasil mahasiswa, waktu nyata atau statistik yang diisi. KEEP/FIX/ADD/REMOVE ditopang locator dan contoh bukti anonim setelah tersedia.
