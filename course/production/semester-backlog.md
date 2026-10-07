# Backlog Produksi Tingkat Semester

Document role: helper SEM-12, bukan ID baru. [Dashboard](dashboard.md) · [Backlog mingguan/ujian](weekly-backlog.md).

Run: `20261007-235905-P02-W01-W04`. Snapshot aktual: 2026-10-07T23:59:05+07:00 (Asia/Jakarta); UTC 2026-10-07T16:59:05+00:00.

Sumber: [workbook asli](<../../references/MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx>), SHA-256 `e75b92af52d0f72974d6ff304ed8f82cdb66149f0a3a73f08a5dfbbd100dd9d8`.
Pemetaan path: [baseline perencanaan](../../planning/WORKBOOK_BASELINE.md), dicocokkan dengan [spesifikasi artefak](../../planning/ARTIFACT_SPECS.md).
Validasi impor: [laporan P02](reports/20261007-235905-P02-W01-W04-validation.md). Handoff: [langkah P03](reports/20261007-235905-P02-W01-W04-handoff.md).

Field sumber di bawah merupakan snapshot immutable; kolom kerja produksi pada tabel terpisah boleh berkembang dengan bukti baru. Tabel metadata adalah representasi tabular schema, bukan file artefak yang sudah dibuat. Path target yang belum ada ditampilkan sebagai code/planned, bukan tautan file aktif. Owner/target date kosong/TBD dipertahankan dari sumber; tidak menjadi penetapan owner/tanggal produksi.

Pembaruan kendali: `20261008-004030-P05-W01-W04` (2026-10-08T00:40:30+07:00); impor sumber tetap snapshot P02. [Audit P03](reports/20261008-003012-P03-W01-W04.md), [register sumber](sources.md), [keputusan](decisions.md), dan [validasi P05](reports/20261008-004030-P05-W01-W04-validation.md) menjadi bukti terbaru. P03/P05 telah dijalankan; sumber resmi masih belum terbaca. Tidak ada bahan pekan yang dibuat.

## 1. Snapshot sumber Semester_Master: 12 item

Kolom Status adalah `source_status`, Priority adalah `source_priority`. Score adalah cache workbook, bukan hasil review repo. SEM-11/SEM-12 yang READY pada sumber tidak membuat target repo READY.

| Source row | ID | Layer | Artifact | Definition of Done | Status | Priority | Owner | Target Date | Dependency | Output / Acceptance Criteria | File / URL | Notes | Status Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | SEM-01 | GOVERN | Curriculum / Source-of-Truth Audit | Curriculum identity, CPL/CPMK/BK and prerequisite alignment locked. | REVIEW | P0 — Now | Tri Aji | ∅ | ∅ | Kurikulum workbook reviewed and conflicts recorded. | ∅ | Review against latest workbook. | 0.5 |
| 3 | SEM-02 | GOVERN | RPS Final | RPS identities, outcomes, weekly map, assessment, bibliography consistent. | REVIEW | P0 — Now | Tri Aji | ∅ | SEM-01 | RPS signed/ready as authoritative semester contract. | https://docs.google.com/document/d/1jfaenJg9Oi6PEsMjASpqO1D90EcQyd5H/edit | Current RPS exists; final QA needed. | 0.5 |
| 4 | SEM-03 | GOVERN | RTM Master | All weekly assignments/assessments mapped to RPS and operational. | REVIEW | P0 — Now | Tri Aji | ∅ | SEM-02 | RTM instructions + outputs + rubrics are executable. | https://docs.google.com/document/d/1ktAxiyG_ctP2Ql8Svx8RBbl370c8wPia/edit | Current RTM exists; QA and production links needed. | 0.5 |
| 5 | SEM-04 | GOVERN | Assessment Blueprint | Assessment coverage, weights, cognitive level, evidence and traceability mapped. | DRAFT | P1 — Next | Tri Aji | ∅ | SEM-02, SEM-03 | One semester assessment blueprint approved. | ∅ | RPS already gives weights; convert into explicit blueprint. | 0.25 |
| 6 | SEM-05 | LEARN | Semester Learning Architecture | End-to-end learning spine, dependencies, WHY/WHAT/HOW progression. | REVIEW | P0 — Now | Tri Aji | ∅ | SEM-02 | All weeks form one coherent learning journey. | ∅ | Topic spine exists in RPS; pedagogical audit needed. | 0.5 |
| 7 | SEM-06 | KNOW | Book Table of Contents | 14 learning chapters + exam/project integration mapped to weekly outcomes. | NOT STARTED | P1 — Next | Tri Aji | ∅ | SEM-05 | TOC locked before chapter-by-chapter production. | ∅ | Use rolling book development. | 0 |
| 8 | SEM-07 | PROVE | Project Architecture | W12–15 project stages, evidence, repo/report/demo, responsible AI and reproducibility. | DRAFT | P2 — Planned | Tri Aji | ∅ | SEM-03 | Project brief, stage gates, rubric and submission flow locked. | ∅ | RPS defines proposal → responsible AI → pipeline → final demo. | 0.25 |
| 9 | SEM-08 | LEARN | LMS Course Skeleton | Weekly sections, naming, content pattern, submission pattern and links standardized. | NOT STARTED | P1 — Next | TBD | ∅ | SEM-05 | All 16 weeks have standard LMS shells. | ∅ | Can be implemented progressively. | 0 |
| 10 | SEM-09 | PROVE | Mastery Tracker | Outcome-level mastery beyond attendance/grades, with remediation flags. | NOT STARTED | P2 — Planned | TBD | ∅ | SEM-04 | Students can be tracked by mastery dimension and evidence. | ∅ | Separate from existing attendance/grade trackers. | 0 |
| 11 | SEM-10 | PROVE | Question Bank | Tagged question bank by week, concept, level, difficulty and answer/rubric. | NOT STARTED | P2 — Planned | TBD | ∅ | SEM-04 | Reusable bank ready for quizzes, UTS, UAS and practice. | ∅ | Build continuously from weekly packages. | 0 |
| 12 | SEM-11 | COMPOUND | Teaching Package Visual & Prompt OS | Standard for content, storyboard, slides, visuals, learning action and QA. | READY | P0 — Now | Tri Aji | ∅ | SEM-05 | Master prompt package version-controlled and reusable. | ∅ | Master Prompt Package Mata Kuliah v2 prepared. | 0.75 |
| 13 | SEM-12 | COMPOUND | Production Control Sheet | Single command center for semester and weekly package production. | READY | P0 — Now | Tri Aji | ∅ | SEM-01 | Dashboard, backlog, status lifecycle, sources and QA controls operational. | ∅ | This workbook. | 0.75 |

## 2. Keadaan produksi repo: 12 item

| artifact_id | Planned path (repo-relative) | execution_focus | Target presence | production.repo_status | markdown_readiness | fulfillment | source_verification | official_alignment | blockers / next action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEM-01 | `course/governance/curriculum-audit.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-02 | `course/governance/rps.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-03 | `course/governance/rtm.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-04 | `course/governance/assessment-blueprint.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-05 | `course/semester/learning-architecture.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-06 | `course/semester/book-toc.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-07 | `course/semester/project-architecture.md` | DEFERRED | PLANNED | NOT STARTED | NOT_STARTED | NOT_FULFILLED | NOT_CHECKED | PROVISIONAL | GAP-01; GAP-02 |
| SEM-08 | `course/semester/lms-skeleton.md` | SUPPORT | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-09 | `course/semester/mastery-tracker.md` | SUPPORT | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-10 | `course/semester/question-bank.md` | SUPPORT | PRESENT | REVIEW | VALIDATED | PARTIAL | VERIFIED_FOR_SCOPE | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-11 | `course/standards/teaching-package-os.md` | SUPPORT | PRESENT | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |
| SEM-12 | `course/production/dashboard.md` | SUPPORT | PRESENT_CONTROL | DRAFT | DRAFT | PARTIAL | PARTIAL | PROVISIONAL | S01–S03 PROVISIONAL; sumber substansi/run diperiksa untuk scope naskah; bukti pelaksanaan belum tersedia |

SEM-12 tetap DRAFT/PARTIAL: P02 mengimpor inventaris, P03 mengaudit sumber, dan P05 merekonsiliasi kendali. Penutupan seluruh DoD kendali produksi dan pengesahan akademik belum terpenuhi.
Pada P02 hanya kendali diproduksi; pada P05 SEM-01–04 hadir sebagai DRAFT/PARTIAL. `SUPPORT` berarti fondasi yang relevan bagi W01–W04; tidak termasuk denominator 56.

## 3. Pemetaan dependensi sumber

| artifact_id | workbook_dependencies (asli) | Mapped artifact refs | Gap/keterangan |
| --- | --- | --- | --- |
| SEM-01 | ∅ | ∅ | Tidak ditentukan oleh sumber; jangan menambahkan prasyarat resmi. |
| SEM-02 | SEM-01 | SEM-01 | ∅ |
| SEM-03 | SEM-02 | SEM-02 | ∅ |
| SEM-04 | SEM-02, SEM-03 | SEM-02, SEM-03 | ∅ |
| SEM-05 | SEM-02 | SEM-02 | ∅ |
| SEM-06 | SEM-05 | SEM-05 | ∅ |
| SEM-07 | SEM-03 | SEM-03 | ∅ |
| SEM-08 | SEM-05 | SEM-05 | ∅ |
| SEM-09 | SEM-04 | SEM-04 | ∅ |
| SEM-10 | SEM-04 | SEM-04 | ∅ |
| SEM-11 | SEM-05 | SEM-05 | ∅ |
| SEM-12 | SEM-01 | SEM-01 | ∅ |

ID dipetakan untuk navigasi perencanaan; input draft awal dan referensi integrasi akhir tetap mengikuti playbook. Jangan menambahkan backrefs yang menciptakan siklus prasyarat.

### Gap saat ini

- GAP-01: 56 naskah fokus lengkap; W05–W16/SEM-07 deferred. Deliverable asli visual/LMS/pelaksanaan belum dibuktikan.
- GAP-02: audit sumber selesai; teknis inti fokus didukung dokumentasi lokal dan run. S01–S03 tetap belum dibaca, ketentuan resmi PROVISIONAL.
- GAP-03: belum ada bukti pelaksanaan/data mahasiswa. EVID/QA siap sebagai spesifikasi, bukan hasil kelas.

## Keadaan fokus setelah P17

56/56 naskah W01–W04 VALIDATED pada scope pedagogi/teknis/spec; sumber resmi PROVISIONAL. Bagian konteks P02/P05 di atas adalah snapshot historis, bukan klaim target masih hilang saat ini. Seluruh 222 ID/path dan field sumber dipertahankan. Minggu lain/proyek/ujian deferred.

[Laporan integrasi](reports/20261007-183058-P17-W01-W04-integrate-validation.md). Sasaran naskah selesai; finalisasi akademik menunggu kurikulum/RPS/RTM yang dapat dibaca. Tidak ada publikasi atau pelaksanaan kelas.
