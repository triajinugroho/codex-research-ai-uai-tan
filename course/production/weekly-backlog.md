# Backlog Produksi Mingguan dan Ujian

Document role: helper SEM-12, bukan ID baru. [Dashboard](dashboard.md) · [Backlog semester](semester-backlog.md).

Run: `20261007-235905-P02-W01-W04`. Snapshot aktual: 2026-10-07T23:59:05+07:00 (Asia/Jakarta); UTC 2026-10-07T16:59:05+00:00.

Sumber: [workbook asli](<../../references/MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx>), SHA-256 `e75b92af52d0f72974d6ff304ed8f82cdb66149f0a3a73f08a5dfbbd100dd9d8`.
Pemetaan path: [baseline perencanaan](../../planning/WORKBOOK_BASELINE.md), dicocokkan dengan [spesifikasi artefak](../../planning/ARTIFACT_SPECS.md).
Validasi impor: [laporan P02](reports/20261007-235905-P02-W01-W04-validation.md). Handoff: [langkah P03](reports/20261007-235905-P02-W01-W04-handoff.md).

Field sumber di bawah merupakan snapshot immutable; kolom kerja produksi pada tabel terpisah boleh berkembang dengan bukti baru. Tabel metadata adalah representasi tabular schema, bukan file artefak yang sudah dibuat. Path target yang belum ada ditampilkan sebagai code/planned, bukan tautan file aktif. Owner/target date kosong/TBD dipertahankan dari sumber; tidak menjadi penetapan owner/tanggal produksi.

Pembaruan kendali: `20261008-004030-P05-W01-W04` (2026-10-08T00:40:30+07:00); impor sumber tetap snapshot P02. [Audit P03](reports/20261008-003012-P03-W01-W04.md), [register sumber](sources.md), [keputusan](decisions.md), dan [validasi P05](reports/20261008-004030-P05-W01-W04-validation.md) menjadi bukti terbaru. P03/P05 telah dijalankan; sumber resmi masih belum terbaca. Tidak ada bahan pekan yang dibuat.

## 1. Cakupan dan fokus

- 210 item: 196 untuk 14 minggu belajar + 7 UTS + 7 UAS.
- Fokus aktif: 56 item W01–W04; sisa 154 item mingguan/ujian deferred, tanpa mengubah prioritas atau status sumber.
- Urutan produksi setelah fondasi: W04 pilot → W01 → W02 → W03 → rekonsiliasi W04. Urutan belajar tetap W01 → W02 → W03 → W04.
- Seluruh 210 target mingguan/ujian belum ada saat inspeksi P02; `production.repo_status: NOT STARTED`, `markdown_readiness: NOT_STARTED`, `fulfillment: NOT_FULFILLED`.
- Ketentuan RPS/RTM dan sumber teknis belum diaudit; verifikasi workbook ini hanya untuk inventaris.

## 2. Snapshot sumber Production_Backlog

Semua 18 kolom sumber disimpan: Week float cache dipertahankan, label/status/bobot/owner/dependensi/QA/notes tidak diubah. Status adalah `source_status`; Weight/Status Score/Weighted Score bukan bobot akademik. Cell kosong `∅` tetap kosong.

### W01 — Pengantar AI dan Machine Learning

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: ACTIVE_W01_W04.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | W01-BOOK | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 3 | W01-MOD | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 4 | W01-GUIDE | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 5 | W01-STORY | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | REVIEW | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0.5 | 2.5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| 6 | W01-SLIDE | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | REVIEW | P1 — Next | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0.5 | 5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| 7 | W01-DATA | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 8 | W01-LAB | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 9 | W01-WORK | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 10 | W01-AIP | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 11 | W01-ASSESS | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-01 already specified in RPS/RTM; production file still needs finalization. |
| 12 | W01-RUBRIC | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-01 already specified in RPS/RTM; production file still needs finalization. |
| 13 | W01-LMS | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 14 | W01-EVID | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 15 | W01-QA | 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W02 — Eksplorasi Data untuk ML

Sub-CPMK baseline: `DAIML-Sub-CPMK102-1`. Fokus: ACTIVE_W01_W04.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 16 | W02-BOOK | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 17 | W02-MOD | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Student Module | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 18 | W02-GUIDE | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 19 | W02-STORY | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Storyboard | 5.0 | REVIEW | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0.5 | 2.5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| 20 | W02-SLIDE | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Slides | 10.0 | REVIEW | P1 — Next | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0.5 | 5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| 21 | W02-DATA | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 22 | W02-LAB | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 23 | W02-WORK | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 24 | W02-AIP | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 25 | W02-ASSESS | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-02 already specified in RPS/RTM; production file still needs finalization. |
| 26 | W02-RUBRIC | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-02 already specified in RPS/RTM; production file still needs finalization. |
| 27 | W02-LMS | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 28 | W02-EVID | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 29 | W02-QA | 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W03 — Preprocessing dan Feature Engineering

Sub-CPMK baseline: `DAIML-Sub-CPMK102-1`. Fokus: ACTIVE_W01_W04.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 30 | W03-BOOK | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 31 | W03-MOD | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Student Module | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 32 | W03-GUIDE | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 33 | W03-STORY | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Storyboard | 5.0 | REVIEW | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0.5 | 2.5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| 34 | W03-SLIDE | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Slides | 10.0 | REVIEW | P1 — Next | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0.5 | 5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| 35 | W03-DATA | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 36 | W03-LAB | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 37 | W03-WORK | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 38 | W03-AIP | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 39 | W03-ASSESS | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-03 already specified in RPS/RTM; production file still needs finalization. |
| 40 | W03-RUBRIC | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-03 already specified in RPS/RTM; production file still needs finalization. |
| 41 | W03-LMS | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 42 | W03-EVID | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 43 | W03-QA | 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W04 — Pembagian Data dan Validasi

Sub-CPMK baseline: `DAIML-Sub-CPMK102-1`. Fokus: ACTIVE_W01_W04.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 44 | W04-BOOK | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P0 — Now | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 45 | W04-MOD | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Student Module | 8.0 | NOT STARTED | P0 — Now | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 46 | W04-GUIDE | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P0 — Now | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 47 | W04-STORY | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Storyboard | 5.0 | DRAFT | P0 — Now | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.25 | 20-slide storyboard drafted 7 Oct 2026: Validation Before Believing. |
| 48 | W04-SLIDE | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Slides | 10.0 | NOT STARTED | P0 — Now | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 49 | W04-DATA | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P0 — Now | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 50 | W04-LAB | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P0 — Now | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 51 | W04-WORK | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P0 — Now | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 52 | W04-AIP | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P0 — Now | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 53 | W04-ASSESS | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P0 — Now | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-04 scope and weighting defined; actual Moodle quiz/key still to produce. |
| 54 | W04-RUBRIC | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P0 — Now | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-04 scope and weighting defined; actual Moodle quiz/key still to produce. |
| 55 | W04-LMS | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P0 — Now | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 56 | W04-EVID | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P0 — Now | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 57 | W04-QA | 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P0 — Now | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W05 — Klasifikasi I: KNN dan Decision Tree

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 58 | W05-BOOK | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 59 | W05-MOD | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 60 | W05-GUIDE | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 61 | W05-STORY | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 62 | W05-SLIDE | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P1 — Next | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 63 | W05-DATA | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 64 | W05-LAB | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 65 | W05-WORK | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 66 | W05-AIP | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 67 | W05-ASSESS | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-05 already specified in RPS/RTM; production file still needs finalization. |
| 68 | W05-RUBRIC | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-05 already specified in RPS/RTM; production file still needs finalization. |
| 69 | W05-LMS | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 70 | W05-EVID | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 71 | W05-QA | 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W06 — Regresi Linear dan Metrik Evaluasi

Sub-CPMK baseline: `DAIML-Sub-CPMK102-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 72 | W06-BOOK | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P2 — Planned | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 73 | W06-MOD | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Student Module | 8.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 74 | W06-GUIDE | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P2 — Planned | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 75 | W06-STORY | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 76 | W06-SLIDE | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Slides | 10.0 | NOT STARTED | P2 — Planned | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 77 | W06-DATA | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P2 — Planned | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 78 | W06-LAB | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P2 — Planned | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 79 | W06-WORK | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 80 | W06-AIP | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 81 | W06-ASSESS | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P2 — Planned | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-06 already specified in RPS/RTM; production file still needs finalization. |
| 82 | W06-RUBRIC | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P2 — Planned | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-06 already specified in RPS/RTM; production file still needs finalization. |
| 83 | W06-LMS | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P2 — Planned | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 84 | W06-EVID | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P2 — Planned | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 85 | W06-QA | 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P2 — Planned | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W07 — Clustering dan Metrik Clustering

Sub-CPMK baseline: `DAIML-Sub-CPMK102-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 86 | W07-BOOK | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P2 — Planned | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 87 | W07-MOD | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Student Module | 8.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 88 | W07-GUIDE | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P2 — Planned | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 89 | W07-STORY | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 90 | W07-SLIDE | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Slides | 10.0 | NOT STARTED | P2 — Planned | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 91 | W07-DATA | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P2 — Planned | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 92 | W07-LAB | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P2 — Planned | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 93 | W07-WORK | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 94 | W07-AIP | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 95 | W07-ASSESS | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P2 — Planned | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-07 already specified in RPS/RTM; production file still needs finalization. |
| 96 | W07-RUBRIC | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P2 — Planned | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-07 already specified in RPS/RTM; production file still needs finalization. |
| 97 | W07-LMS | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P2 — Planned | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 98 | W07-EVID | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P2 — Planned | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 99 | W07-QA | 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P2 — Planned | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### UTS — UTS

Sub-CPMK baseline: `DAIML-Sub-CPMK102-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | UTS-BLUEPRINT | 8.0 | UTS | DAIML-Sub-CPMK102-1 | PROVE | Exam Blueprint | 20.0 | DRAFT | P2 — Planned | TBD | RPS + Assessment Blueprint | ∅ | Coverage, indikator, level kognitif, proporsi, dan traceability ke CPMK. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 5 | Coverage already defined in RPS; explicit blueprint still needs production. |
| 101 | UTS-QUESTION | 8.0 | UTS | DAIML-Sub-CPMK102-1 | PROVE | Question Set | 25.0 | NOT STARTED | P2 — Planned | TBD | Exam Blueprint | ∅ | Soal final lengkap, jelas, dan seimbang. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 102 | UTS-KEY | 8.0 | UTS | DAIML-Sub-CPMK102-1 | PROVE | Answer Key / Rubric | 20.0 | NOT STARTED | P2 — Planned | TBD | Question Set | ∅ | Kunci/rubrik lengkap dan dapat dipakai konsisten. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 103 | UTS-INSTR | 8.0 | UTS | DAIML-Sub-CPMK102-1 | LEARN | Exam Instruction | 10.0 | NOT STARTED | P2 — Planned | TBD | Exam Blueprint | ∅ | Instruksi teknis-akademik yang jelas untuk mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 104 | UTS-LMS | 8.0 | UTS | DAIML-Sub-CPMK102-1 | LEARN | LMS Exam Package | 10.0 | NOT STARTED | P2 — Planned | TBD | Question Set + Instruction | ∅ | Setup LMS, file, waktu, submission, dan komunikasi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 105 | UTS-EVID | 8.0 | UTS | DAIML-Sub-CPMK102-1 | PROVE | Exam Evidence Archive | 5.0 | NOT STARTED | P2 — Planned | TBD | Delivered exam | ∅ | Bukti pelaksanaan dan arsip asesmen tertata. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 106 | UTS-QA | 8.0 | UTS | DAIML-Sub-CPMK102-1 | COMPOUND | Post-Exam Analysis | 10.0 | NOT STARTED | P2 — Planned | TBD | Exam results + evidence | ∅ | Analisis item/hasil, gap mastery, dan tindakan perbaikan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W09 — Klasifikasi II dan Model Selection

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 107 | W09-BOOK | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 108 | W09-MOD | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 109 | W09-GUIDE | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 110 | W09-STORY | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 111 | W09-SLIDE | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 112 | W09-DATA | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 113 | W09-LAB | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 114 | W09-WORK | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 115 | W09-AIP | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 116 | W09-ASSESS | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-08 already specified in RPS/RTM; production file still needs finalization. |
| 117 | W09-RUBRIC | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-08 already specified in RPS/RTM; production file still needs finalization. |
| 118 | W09-LMS | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 119 | W09-EVID | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 120 | W09-QA | 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W10 — Generalisasi, Overfitting, dan Regularisasi

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121 | W10-BOOK | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 122 | W10-MOD | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 123 | W10-GUIDE | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 124 | W10-STORY | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 125 | W10-SLIDE | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 126 | W10-DATA | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 127 | W10-LAB | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 128 | W10-WORK | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 129 | W10-AIP | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 130 | W10-ASSESS | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-09 already specified in RPS/RTM; production file still needs finalization. |
| 131 | W10-RUBRIC | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-09 already specified in RPS/RTM; production file still needs finalization. |
| 132 | W10-LMS | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 133 | W10-EVID | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 134 | W10-QA | 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W11 — Jaringan Syaraf Tiruan

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 135 | W11-BOOK | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 136 | W11-MOD | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 137 | W11-GUIDE | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 138 | W11-STORY | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 139 | W11-SLIDE | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 140 | W11-DATA | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 141 | W11-LAB | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 142 | W11-WORK | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 143 | W11-AIP | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 144 | W11-ASSESS | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-10 already specified in RPS/RTM; production file still needs finalization. |
| 145 | W11-RUBRIC | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-10 already specified in RPS/RTM; production file still needs finalization. |
| 146 | W11-LMS | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 147 | W11-EVID | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 148 | W11-QA | 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W12 — Pengantar Deep Learning dan Generative AI

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 149 | W12-BOOK | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 150 | W12-MOD | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 151 | W12-GUIDE | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 152 | W12-STORY | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 153 | W12-SLIDE | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 154 | W12-DATA | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 155 | W12-LAB | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 156 | W12-WORK | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 157 | W12-AIP | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 158 | W12-ASSESS | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-11 already specified in RPS/RTM; production file still needs finalization. |
| 159 | W12-RUBRIC | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-11 already specified in RPS/RTM; production file still needs finalization. |
| 160 | W12-LMS | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 161 | W12-EVID | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 162 | W12-QA | 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W13 — Responsible AI

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 163 | W13-BOOK | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 164 | W13-MOD | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 165 | W13-GUIDE | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 166 | W13-STORY | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 167 | W13-SLIDE | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 168 | W13-DATA | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 169 | W13-LAB | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 170 | W13-WORK | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 171 | W13-AIP | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 172 | W13-ASSESS | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-12 already specified in RPS/RTM; production file still needs finalization. |
| 173 | W13-RUBRIC | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-12 already specified in RPS/RTM; production file still needs finalization. |
| 174 | W13-LMS | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 175 | W13-EVID | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 176 | W13-QA | 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W14 — Pipeline ML End-to-End dan Reproduksibilitas

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 177 | W14-BOOK | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 178 | W14-MOD | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 179 | W14-GUIDE | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 180 | W14-STORY | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 181 | W14-SLIDE | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 182 | W14-DATA | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 183 | W14-LAB | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 184 | W14-WORK | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 185 | W14-AIP | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 186 | W14-ASSESS | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-13 already specified in RPS/RTM; production file still needs finalization. |
| 187 | W14-RUBRIC | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-13 already specified in RPS/RTM; production file still needs finalization. |
| 188 | W14-LMS | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 189 | W14-EVID | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 190 | W14-QA | 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### W15 — Presentasi Proyek Akhir

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 191 | W15-BOOK | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | KNOW | Book Chapter | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 192 | W15-MOD | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Student Module | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 193 | W15-GUIDE | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Lecturer Guide | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 194 | W15-STORY | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Storyboard | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | Storyline slide lengkap dan audited sebelum visual final. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 195 | W15-SLIDE | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Slides | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | Deck final presentation-ready dan take-home friendly. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 196 | W15-DATA | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Dataset / Case | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 197 | W15-LAB | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Notebook / Lab | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | Starter + solution notebook dapat dijalankan/reproduksi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 198 | W15-WORK | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | Worksheet / Practice | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 199 | W15-AIP | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | AI Learning Prompts | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 200 | W15-ASSESS | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | PROVE | Assignment / Quiz | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | Instruksi asesmen executable dan aligned ke outcome. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 2 | T-14 already specified in RPS/RTM; production file still needs finalization. |
| 201 | W15-RUBRIC | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | PROVE | Rubric / Answer Key | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 1.75 | T-14 already specified in RPS/RTM; production file still needs finalization. |
| 202 | W15-LMS | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | LEARN | LMS Package | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 203 | W15-EVID | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | PROVE | Evidence / Student Artifact | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | Bukti mastery yang jelas: notebook/report/video/demo/dll. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 204 | W15-QA | 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Class QA | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

### UAS — UAS

Sub-CPMK baseline: `DAIML-Sub-CPMK082-1`. Fokus: DEFERRED.

| Source row | Item ID | Week | Topic | Sub-CPMK | Layer | Artifact | Weight | Status | Priority | Owner | Dependency | Target Date | Output / Definition of Done | File / URL | QA Gate | Status Score | Weighted Score | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 205 | UAS-BLUEPRINT | 16.0 | UAS | DAIML-Sub-CPMK082-1 | PROVE | Exam Blueprint | 20.0 | DRAFT | P3 — Later | TBD | RPS + Assessment Blueprint | ∅ | Coverage, indikator, level kognitif, proporsi, dan traceability ke CPMK. | ∅ | Accuracy + alignment + clarity + usability | 0.25 | 5 | Coverage already defined in RPS; explicit blueprint still needs production. |
| 206 | UAS-QUESTION | 16.0 | UAS | DAIML-Sub-CPMK082-1 | PROVE | Question Set | 25.0 | NOT STARTED | P3 — Later | TBD | Exam Blueprint | ∅ | Soal final lengkap, jelas, dan seimbang. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 207 | UAS-KEY | 16.0 | UAS | DAIML-Sub-CPMK082-1 | PROVE | Answer Key / Rubric | 20.0 | NOT STARTED | P3 — Later | TBD | Question Set | ∅ | Kunci/rubrik lengkap dan dapat dipakai konsisten. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 208 | UAS-INSTR | 16.0 | UAS | DAIML-Sub-CPMK082-1 | LEARN | Exam Instruction | 10.0 | NOT STARTED | P3 — Later | TBD | Exam Blueprint | ∅ | Instruksi teknis-akademik yang jelas untuk mahasiswa. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 209 | UAS-LMS | 16.0 | UAS | DAIML-Sub-CPMK082-1 | LEARN | LMS Exam Package | 10.0 | NOT STARTED | P3 — Later | TBD | Question Set + Instruction | ∅ | Setup LMS, file, waktu, submission, dan komunikasi. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 210 | UAS-EVID | 16.0 | UAS | DAIML-Sub-CPMK082-1 | PROVE | Exam Evidence Archive | 5.0 | NOT STARTED | P3 — Later | TBD | Delivered exam | ∅ | Bukti pelaksanaan dan arsip asesmen tertata. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |
| 211 | UAS-QA | 16.0 | UAS | DAIML-Sub-CPMK082-1 | COMPOUND | Post-Exam Analysis | 10.0 | NOT STARTED | P3 — Later | TBD | Exam results + evidence | ∅ | Analisis item/hasil, gap mastery, dan tindakan perbaikan. | ∅ | Accuracy + alignment + clarity + usability | 0 | 0 | ∅ |

## 3. Keadaan produksi repo: seluruh 210 item

| artifact_id | Planned path (repo-relative) | execution_focus | Target presence | production.repo_status | markdown_readiness | fulfillment | source_verification | official_alignment | blockers / next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W01-BOOK | `course/weeks/w01/book-chapter.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-MOD | `course/weeks/w01/student-module.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-GUIDE | `course/weeks/w01/lecturer-guide.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-STORY | `course/weeks/w01/storyboard.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-SLIDE | `course/weeks/w01/slides.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-DATA | `course/weeks/w01/dataset-case.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-LAB | `course/weeks/w01/lab.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-WORK | `course/weeks/w01/worksheet.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-AIP | `course/weeks/w01/ai-learning-prompts.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-ASSESS | `course/weeks/w01/assignment-quiz.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-RUBRIC | `course/weeks/w01/rubric-answer-key.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-LMS | `course/weeks/w01/lms-package.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-EVID | `course/weeks/w01/evidence-spec.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W01-QA | `course/weeks/w01/post-class-qa.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-BOOK | `course/weeks/w02/book-chapter.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-MOD | `course/weeks/w02/student-module.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-GUIDE | `course/weeks/w02/lecturer-guide.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-STORY | `course/weeks/w02/storyboard.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-SLIDE | `course/weeks/w02/slides.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-DATA | `course/weeks/w02/dataset-case.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-LAB | `course/weeks/w02/lab.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-WORK | `course/weeks/w02/worksheet.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-AIP | `course/weeks/w02/ai-learning-prompts.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-ASSESS | `course/weeks/w02/assignment-quiz.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-RUBRIC | `course/weeks/w02/rubric-answer-key.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-LMS | `course/weeks/w02/lms-package.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-EVID | `course/weeks/w02/evidence-spec.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W02-QA | `course/weeks/w02/post-class-qa.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-BOOK | `course/weeks/w03/book-chapter.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-MOD | `course/weeks/w03/student-module.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-GUIDE | `course/weeks/w03/lecturer-guide.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-STORY | `course/weeks/w03/storyboard.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-SLIDE | `course/weeks/w03/slides.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-DATA | `course/weeks/w03/dataset-case.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-LAB | `course/weeks/w03/lab.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-WORK | `course/weeks/w03/worksheet.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-AIP | `course/weeks/w03/ai-learning-prompts.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-ASSESS | `course/weeks/w03/assignment-quiz.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-RUBRIC | `course/weeks/w03/rubric-answer-key.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-LMS | `course/weeks/w03/lms-package.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-EVID | `course/weeks/w03/evidence-spec.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W03-QA | `course/weeks/w03/post-class-qa.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-BOOK | `course/weeks/w04/book-chapter.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-MOD | `course/weeks/w04/student-module.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-GUIDE | `course/weeks/w04/lecturer-guide.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-STORY | `course/weeks/w04/storyboard.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-SLIDE | `course/weeks/w04/slides.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-DATA | `course/weeks/w04/dataset-case.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-LAB | `course/weeks/w04/lab.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-WORK | `course/weeks/w04/worksheet.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-AIP | `course/weeks/w04/ai-learning-prompts.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-ASSESS | `course/weeks/w04/assignment-quiz.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-RUBRIC | `course/weeks/w04/rubric-answer-key.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-LMS | `course/weeks/w04/lms-package.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-EVID | `course/weeks/w04/evidence-spec.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W04-QA | `course/weeks/w04/post-class-qa.md` | ACTIVE_W01_W04 | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| W05-BOOK | `course/weeks/w05/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-MOD | `course/weeks/w05/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-GUIDE | `course/weeks/w05/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-STORY | `course/weeks/w05/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-SLIDE | `course/weeks/w05/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-DATA | `course/weeks/w05/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-LAB | `course/weeks/w05/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-WORK | `course/weeks/w05/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-AIP | `course/weeks/w05/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-ASSESS | `course/weeks/w05/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-RUBRIC | `course/weeks/w05/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-LMS | `course/weeks/w05/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W05-EVID | `course/weeks/w05/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W05-QA | `course/weeks/w05/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W06-BOOK | `course/weeks/w06/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-MOD | `course/weeks/w06/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-GUIDE | `course/weeks/w06/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-STORY | `course/weeks/w06/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-SLIDE | `course/weeks/w06/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-DATA | `course/weeks/w06/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-LAB | `course/weeks/w06/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-WORK | `course/weeks/w06/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-AIP | `course/weeks/w06/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-ASSESS | `course/weeks/w06/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-RUBRIC | `course/weeks/w06/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-LMS | `course/weeks/w06/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W06-EVID | `course/weeks/w06/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W06-QA | `course/weeks/w06/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W07-BOOK | `course/weeks/w07/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-MOD | `course/weeks/w07/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-GUIDE | `course/weeks/w07/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-STORY | `course/weeks/w07/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-SLIDE | `course/weeks/w07/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-DATA | `course/weeks/w07/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-LAB | `course/weeks/w07/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-WORK | `course/weeks/w07/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-AIP | `course/weeks/w07/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-ASSESS | `course/weeks/w07/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-RUBRIC | `course/weeks/w07/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-LMS | `course/weeks/w07/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W07-EVID | `course/weeks/w07/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W07-QA | `course/weeks/w07/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| UTS-BLUEPRINT | `course/exams/uts/blueprint.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UTS-QUESTION | `course/exams/uts/question-set.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UTS-KEY | `course/exams/uts/answer-key-rubric.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UTS-INSTR | `course/exams/uts/instructions.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UTS-LMS | `course/exams/uts/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UTS-EVID | `course/exams/uts/evidence-archive-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| UTS-QA | `course/exams/uts/post-exam-analysis.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W09-BOOK | `course/weeks/w09/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-MOD | `course/weeks/w09/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-GUIDE | `course/weeks/w09/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-STORY | `course/weeks/w09/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-SLIDE | `course/weeks/w09/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-DATA | `course/weeks/w09/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-LAB | `course/weeks/w09/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-WORK | `course/weeks/w09/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-AIP | `course/weeks/w09/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-ASSESS | `course/weeks/w09/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-RUBRIC | `course/weeks/w09/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-LMS | `course/weeks/w09/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W09-EVID | `course/weeks/w09/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W09-QA | `course/weeks/w09/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W10-BOOK | `course/weeks/w10/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-MOD | `course/weeks/w10/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-GUIDE | `course/weeks/w10/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-STORY | `course/weeks/w10/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-SLIDE | `course/weeks/w10/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-DATA | `course/weeks/w10/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-LAB | `course/weeks/w10/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-WORK | `course/weeks/w10/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-AIP | `course/weeks/w10/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-ASSESS | `course/weeks/w10/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-RUBRIC | `course/weeks/w10/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-LMS | `course/weeks/w10/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W10-EVID | `course/weeks/w10/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W10-QA | `course/weeks/w10/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W11-BOOK | `course/weeks/w11/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-MOD | `course/weeks/w11/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-GUIDE | `course/weeks/w11/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-STORY | `course/weeks/w11/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-SLIDE | `course/weeks/w11/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-DATA | `course/weeks/w11/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-LAB | `course/weeks/w11/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-WORK | `course/weeks/w11/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-AIP | `course/weeks/w11/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-ASSESS | `course/weeks/w11/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-RUBRIC | `course/weeks/w11/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-LMS | `course/weeks/w11/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W11-EVID | `course/weeks/w11/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W11-QA | `course/weeks/w11/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W12-BOOK | `course/weeks/w12/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-MOD | `course/weeks/w12/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-GUIDE | `course/weeks/w12/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-STORY | `course/weeks/w12/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-SLIDE | `course/weeks/w12/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-DATA | `course/weeks/w12/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-LAB | `course/weeks/w12/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-WORK | `course/weeks/w12/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-AIP | `course/weeks/w12/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-ASSESS | `course/weeks/w12/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-RUBRIC | `course/weeks/w12/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-LMS | `course/weeks/w12/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W12-EVID | `course/weeks/w12/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W12-QA | `course/weeks/w12/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W13-BOOK | `course/weeks/w13/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-MOD | `course/weeks/w13/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-GUIDE | `course/weeks/w13/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-STORY | `course/weeks/w13/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-SLIDE | `course/weeks/w13/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-DATA | `course/weeks/w13/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-LAB | `course/weeks/w13/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-WORK | `course/weeks/w13/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-AIP | `course/weeks/w13/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-ASSESS | `course/weeks/w13/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-RUBRIC | `course/weeks/w13/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-LMS | `course/weeks/w13/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W13-EVID | `course/weeks/w13/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W13-QA | `course/weeks/w13/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W14-BOOK | `course/weeks/w14/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-MOD | `course/weeks/w14/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-GUIDE | `course/weeks/w14/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-STORY | `course/weeks/w14/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-SLIDE | `course/weeks/w14/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-DATA | `course/weeks/w14/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-LAB | `course/weeks/w14/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-WORK | `course/weeks/w14/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-AIP | `course/weeks/w14/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-ASSESS | `course/weeks/w14/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-RUBRIC | `course/weeks/w14/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-LMS | `course/weeks/w14/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W14-EVID | `course/weeks/w14/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W14-QA | `course/weeks/w14/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W15-BOOK | `course/weeks/w15/book-chapter.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-MOD | `course/weeks/w15/student-module.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-GUIDE | `course/weeks/w15/lecturer-guide.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-STORY | `course/weeks/w15/storyboard.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-SLIDE | `course/weeks/w15/slides.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-DATA | `course/weeks/w15/dataset-case.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-LAB | `course/weeks/w15/lab.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-WORK | `course/weeks/w15/worksheet.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-AIP | `course/weeks/w15/ai-learning-prompts.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-ASSESS | `course/weeks/w15/assignment-quiz.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-RUBRIC | `course/weeks/w15/rubric-answer-key.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-LMS | `course/weeks/w15/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| W15-EVID | `course/weeks/w15/evidence-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| W15-QA | `course/weeks/w15/post-class-qa.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| UAS-BLUEPRINT | `course/exams/uas/blueprint.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UAS-QUESTION | `course/exams/uas/question-set.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UAS-KEY | `course/exams/uas/answer-key-rubric.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UAS-INSTR | `course/exams/uas/instructions.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UAS-LMS | `course/exams/uas/lms-package.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| UAS-EVID | `course/exams/uas/evidence-archive-spec.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |
| UAS-QA | `course/exams/uas/post-exam-analysis.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02; GAP-03 |

## 4. Pemetaan dependensi dan gap

Pemetaan di bawah adalah interpretasi implementasi, bukan penggantian teks sumber. Semua mapped ID termasuk inventaris 222 dan belum membuktikan input tersedia. Ketentuan outcome/case requirement serta peristiwa kelas/ujian dicatat sebagai kebutuhan non-ID.

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Assignment / Practice | Wnn-ASSESS, Wnn-WORK | Slash adalah alternatif/konteks Assignment atau Practice, bukan keputusan keduanya wajib. |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Assignment / Quiz | Wnn-ASSESS | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Book Chapter | Wnn-BOOK | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Book Chapter + Lecturer Guide | Wnn-BOOK, Wnn-GUIDE | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Book Chapter + Student Module | Wnn-BOOK, Wnn-MOD | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Book Chapter + Worksheet | Wnn-BOOK, Wnn-WORK | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Dataset / Case + Book Chapter | Wnn-DATA, Wnn-BOOK | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Delivered class + student evidence | Wnn-EVID | Peristiwa kelas terlaksana dan bukti kerja aktual; belum tersedia. |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Delivered exam | ∅ | Peristiwa ujian terlaksana; bukti aktual belum tersedia. |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Exam Blueprint | EXAM-BLUEPRINT | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Exam results + evidence | EXAM-EVID | Hasil ujian aktual; bukan artifact ID atau data yang sudah tersedia. |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Module + Slides + Assessment | Wnn-MOD, Wnn-SLIDE, Wnn-ASSESS | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Question Set | EXAM-QUESTION | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Question Set + Instruction | EXAM-QUESTION, EXAM-INSTR | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| RPS + Assessment Blueprint | SEM-02, SEM-04 | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| RPS topic + case requirement | SEM-02 | Case requirement: keputusan scope/kasus; diperinci pada P06, bukan ID sumber. |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| RTM + outcome | SEM-03 | Rumusan outcome resmi memerlukan sumber/verifikasi P03/P05. |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Semester learning map + book TOC | SEM-05, SEM-06 | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Storyboard | Wnn-STORY | ∅ |

| workbook_dependencies | Pola mapped refs | Gap / batas pemetaan |
| --- | --- | --- |
| Student Module | Wnn-MOD | ∅ |


### Gap saat ini

- GAP-01: 56 naskah fokus lengkap; W05–W16/SEM-07 deferred. Deliverable asli visual/LMS/pelaksanaan belum dibuktikan.
- GAP-02: audit sumber selesai; teknis inti fokus didukung dokumentasi lokal dan run. S01–S03 tetap belum dibaca, ketentuan resmi PROVISIONAL.
- GAP-03: belum ada bukti pelaksanaan/data mahasiswa. EVID/QA siap sebagai spesifikasi, bukan hasil kelas.

## Keadaan fokus setelah P17

56/56 naskah W01–W04 VALIDATED pada scope pedagogi/teknis/spec; sumber resmi PROVISIONAL. Bagian konteks P02/P05 di atas adalah snapshot historis, bukan klaim target masih hilang saat ini. Seluruh 222 ID/path dan field sumber dipertahankan. Minggu lain/proyek/ujian deferred.

[Laporan integrasi](reports/20261007-183058-P17-W01-W04-integrate-validation.md). Sasaran naskah selesai; finalisasi akademik menunggu kurikulum/RPS/RTM yang dapat dibaca. Tidak ada publikasi atau pelaksanaan kelas.
