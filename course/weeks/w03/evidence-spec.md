---
artifact_id: W03-EVID
title: Preprocessing dan Feature Engineering — EVID
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
workbook_dependencies: Assignment / Practice
scope_record: course/weeks/w03/scope.md
validation_records:
- course/production/reports/20261007-181608-P21-W03-F-validation.md
- course/production/reports/20261007-181609-P15-P16-W03-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Preprocessing dan Feature Engineering — EVID

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## W03-EV01 — spesifikasi, bukan rekaman

| LO | Bukti minimal | Kriteria USULAN | Verifikasi | Remediasi |
| --- | --- | --- | --- | --- |
| W03-LO01 | Tabel keputusan+alasan menunjuk input | Pilihan sesuai tujuan/unit/tipe dengan alasan | Cocokkan Q01/RC01 | Ulangi satu kasus dengan unit/target jelas |
| W03-LO02 | Trace/memo batas dan interpretasi | Asal informasi/parameter serta batas klaim jelas | Cocokkan Q02/Q03/RC02; kode bila dipakai punya log | Telusuri satu tahap yang tidak jelas |

## Nama, provenance dan skema kosong

Nama USULAN `W03-EV01-<pseudonym>-<version>.md`; gunakan pseudonym pada kanal yang diatur, jangan mengisi identitas nyata dalam repo. Record: evidence_id, learner_pseudonym, LO, source_artifact_version, input_hash/seed, runtime_versions, actual_output, interpretation, submitted_at, reviewer, reviewed_at, criterion_result, revision_of. Waktu/reviewer hanya diisi dari peristiwa nyata.

Bukti kode: simpan input/seed, kode, actual output, versi serta alasan; screenshot saja tidak mereproduksi run. Data hilang/belum ditelaah/perlu perbaikan/memadai dibedakan, lihat SEM-09. Tidak ada statistik mahasiswa atau batas kelulusan resmi. Penyimpanan/akses/retensi/izin adalah rencana yang harus ditetapkan, tidak dilakukan pada batch ini. Rekaman bukti aktual belum tersedia.

## Bukti spesifik per LO

| LO | Isi yang harus terlihat | Butir pendukung |
| --- | --- | --- |
| W03-LO01 | Memilih transformasi berdasarkan tipe fitur dan kebutuhan model | W03-Q01 |
| W03-LO02 | Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru | W03-Q02, W03-Q03 |
