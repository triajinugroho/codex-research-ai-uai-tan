---
artifact_id: SEM-12
title: 'Dashboard produksi: fokus W01–W04'
course_code: IF52510031
period: 2026–2027
week: null
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
version: '0.3'
updated_at: '2026-10-08'
owner: Codex — pelaksana P02/P05; owner akademik tetap mengikuti sumber
source_status: READY
production:
  repo_status: DRAFT
markdown_readiness: DRAFT
fulfillment: PARTIAL
source_verification: PARTIAL
official_alignment: PROVISIONAL
learning_ids: []
official_outcome_refs: []
assessment_ids: []
example_ids: []
evidence_requirement_ids: []
source_ids:
- SRC-WORKBOOK
dependencies: []
integration_refs:
- SEM-01
workbook_dependencies: SEM-01
scope_record: course/production/reports/20261007-183058-P17-W01-W04-integrate-ticket.md
validation_records:
- course/production/reports/20261007-235905-P02-W01-W04-validation.md
- course/production/reports/20261008-004030-P05-W01-W04-validation.md
- course/production/reports/20261007-183058-P17-W01-W04-integrate-final-validation.md
blockers:
- S01–S03 belum terbaca; governance PROVISIONAL
- Bahan pekan dan fondasi P04/P20 belum diproduksi
class_adaptations: PROVISIONAL
delivery_evidence: []
---
# Dashboard Produksi — W01–W04

**56/56 artefak fokus VALIDATED untuk scope Markdown pedagogi/teknis/spec.** Official_alignment PROVISIONAL; DoD asli PARTIAL. Naskah slide bukan deck, lab bukan notebook terbit, LMS belum aktif, EVID/QA bukan bukti pelaksanaan. Tidak ada commit/push/publikasi.

## Keadaan aktual

| Ukuran | Aktual |
| --- | --- |
| Inventaris | 222 |
| Fokus | 56 |
| Fokus naskah VALIDATED | 56/56 |
| Target kanonik ada | 67/222 |
| Readiness seluruh inventaris | 59 VALIDATED (56 fokus+3 support); 8 DRAFT; 155 NOT_STARTED |
| Status produksi seluruh inventaris | 59 REVIEW; 8 DRAFT; 155 NOT STARTED |
| DoD asli | 67 PARTIAL; 155 NOT_FULFILLED; 0 FULFILLED |
| Akademik | 222 PROVISIONAL; S01–S03 belum dibaca |
| Publikasi/pelaksanaan | 0 |

## Navigasi

- [Mahasiswa](../index.md) · [Dosen](../instructor-index.md)
- [Backlog semester](semester-backlog.md) · [Backlog mingguan](weekly-backlog.md)
- [Sumber](sources.md) · [Keputusan](decisions.md)
- [Integrasi akhir](reports/20261007-183058-P17-W01-W04-integrate-validation.md)

## Scope dan gap tersisa

GAP-TECH inti W01–W04 ditutup dengan dokumentasi runtime, worked examples/perhitungan dan delapan eksekusi starter/reference beserta kontrol negatif/edge. Kepatuhan layanan AI nyata tidak diuji; contoh respons adalah simulasi berlabel. Render slide dan publikasi tidak dilakukan. GAP-S01/S02/S03 masih menahan finalisasi akademik; source_status dan bobot produksi asli di bawah tidak dipakai sebagai nilai mahasiswa. W05–W16/SEM-07 deferred; tidak dihitung siap. Finalisasi akademik memerlukan sumber asli, bukan menghentikan scope naskah yang telah diperiksa.

## 4. Snapshot source_status, terpisah dari status repo

| Status sumber | Semester_Master | Production_Backlog | Gabungan 222 |
| --- | --- | --- | --- |
| NOT STARTED | 4 | 173 | 177 |
| DRAFT | 2 | 31 | 33 |
| REVIEW | 4 | 6 | 10 |
| READY | 2 | 0 | 2 |
| PUBLISHED | 0 | 0 | 0 |
| DELIVERED | 0 | 0 | 0 |
| IMPROVE | 0 | 0 | 0 |

Angka KPI sumber berikut adalah nilai cache Dashboard asli; bukan hasil produksi repo:

| Dashboard row | KPI asli | Nilai cell asli |
| --- | --- | --- |
| 3 | Overall Progress | 0.05390625 |
| 4 | Semester System Progress | 0.3333333333 |
| 5 | Delivered | 0 |
| 6 | Ready / Published | 0 |
| 7 | In Review | 6 |
| 8 | Not Started | 173 |

Cache tidak dihitung ulang saat impor, dan tidak digunakan sebagai readiness. Overall Progress sumber `0.05390625` tidak berarti bahan repo telah siap 5,39%. Weight/score artefak bukan bobot nilai mahasiswa.

## 5. Definisi lifecycle dan prioritas asli

| Status sumber | Score asli | Makna asli |
| --- | --- | --- |
| NOT STARTED | 0.0 | Belum mulai. |
| DRAFT | 0.25 | Sudah ada draft awal. |
| REVIEW | 0.5 | Sedang/siap ditinjau untuk akurasi dan alignment. |
| READY | 0.75 | Secara substansi siap dipakai; final publishing belum selesai. |
| PUBLISHED | 0.9 | Sudah dipublikasikan/diunggah untuk mahasiswa. |
| DELIVERED | 1.0 | Sudah digunakan/dilaksanakan. |
| IMPROVE | 0.85 | Sudah digunakan namun perlu perbaikan pada iterasi berikut. |

| Priority asli | Makna asli |
| --- | --- |
| P0 — Now | Kerjakan sekarang / current bottleneck. |
| P1 — Next | Berikutnya setelah P0. |
| P2 — Planned | Perlu disiapkan dalam horizon dekat. |
| P3 — Later | Belum mendesak; jaga visibility. |

IMPROVE (0.85) adalah cabang revisi pascapenggunaan sesuai bukti, bukan tahap wajib. Status yang source READY/REVIEW tidak disalin menjadi status produksi.

## 6. Sumber yang disebut workbook — salinan inventaris, bukan audit P03

| Sources row | ID | Source asli | Role asli | URL asli | Notes asli |
| --- | --- | --- | --- | --- | --- |
| 2 | S01 | Kurikulum OBE IF 2025 — Revisi 2026 | Primary curriculum source of truth | https://docs.google.com/spreadsheets/d/14frRyWdgLshOJ-5hVcL2CCoxCtm0d5gc | Use for CPL/CPMK/BK/course identity. |
| 3 | S02 | RPS_RTM_Dasar_Kecerdasan_Artifisial_dan_Pembelajaran_Mesin_2026-2027 | Operational RPS/RTM — IF24A | https://docs.google.com/document/d/1jfaenJg9Oi6PEsMjASpqO1D90EcQyd5H/edit | Current weekly topic, assessment, and RTM basis. |
| 4 | S03 | RTM_Dasar_Kecerdasan_Artifisial_dan_Pembelajaran_Mesin_IF24A-IF24H_2026_Template_Resmi_UAI | RTM source — IF24A | https://docs.google.com/document/d/1ktAxiyG_ctP2Ql8Svx8RBbl370c8wPia/edit | Detailed task structure. |
| 5 | S04 | IF24A - Dasar AI & ML - Tracker Presensi, Tugas dan Nilai | Class delivery tracker | https://docs.google.com/spreadsheets/d/1N9HH-Pk2Dbg2NnV5w0mGIld2PDibdIz16H9GpBUDluI/edit | Operational class evidence. |
| 6 | S05 | IF24H - Dasar AI & ML - Tracker Presensi, Tugas dan Nilai | Hybrid class delivery tracker | https://docs.google.com/spreadsheets/d/1WBP9NIduXQ_xqiB_PorhJKzB1eryTcrKeG8fRO0L3RI/edit | Operational hybrid-class evidence. |
| 7 | S06 | Master Prompt Package Mata Kuliah v2 | Teaching Package Operating System | ∅ | Local master prompt created 7 Oct 2026; upload/link when finalized. |

Hanya workbook lokal dibaca untuk inventaris pada P02. S01–S05 di atas masih rujukan/link dari workbook, bukan dokumen yang dibaca isinya. S06 menyebut paket v2; file master prompt lokal belum diperiksa kesamaan versi pada P02. Nama/URL dicatat apa adanya; tidak ada token/credential yang diminta atau dicetak. Audit dan crosswalk P03 sudah tersedia di register; dua sumber lokal terbaca, dokumen eksternal belum terbaca. Metadata URL asli di tabel ini tetap immutable.

## 7. Cell kosong dan dependensi non-ID

| Sheet | Kolom asli | Cell kosong |
| --- | --- | --- |
| Semester_Master | H / Target Date | 12 |
| Semester_Master | I / Dependency | 1 |
| Semester_Master | K / File / URL | 10 |
| Production_Backlog | L / Target Date | 210 |
| Production_Backlog | N / File / URL | 210 |
| Production_Backlog | R / Notes | 173 |

Target date kosong bukan deadline baru. Catatan `TBD` dan owner sumber tidak diganti. Notes yang kosong bukan hasil QA lulus; URL target kosong bukan bukti artefak hilang akibat jaringan.

Dependensi artifact ID dapat dipetakan ke 222 ID. Label case requirement/outcome memerlukan scope/verifikasi; Delivered class/exam dan results/evidence adalah syarat peristiwa/data, bukan ID artefak yang sudah tersedia. Slash Assignment / Practice tidak dipaksakan sebagai dua prasyarat wajib. Rincian pemetaan ada pada backlog; semua nilai asli tetap dipertahankan.


## Keadaan otomatis terbaru

Bagian historis P05 di atas tetap snapshot tahap tersebut. Keadaan terkini berikut dihitung dari metadata file aktual.

| Ukuran | Aktual |
| --- | --- |
| Inventaris ID/path | 222 |
| Fokus aktif | 56 |
| Target kanonik ada | 67 |
| Fokus Markdown VALIDATED | 56/56 |
| Fokus file ada | 56/56 |
| DoD asli FULFILLED | 0 |
| Keselarasan akademik | PROVISIONAL: S01–S03 belum dibaca |
| Publikasi/pelaksanaan | Tidak ada |
| Tahap terakhir | 20261007-183058-P17-W01-W04-integrate |

## Laporan final yang menjadi rujukan

[Audit sembilan pemeriksaan PASS](reports/20261007-183058-P17-W01-W04-integrate-final-validation.md) · [Handoff akhir](reports/20261007-183058-P17-W01-W04-integrate-handoff.md).
