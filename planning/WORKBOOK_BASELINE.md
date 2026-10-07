# Baseline Workbook dan Pemetaan 222 Artefak

Dokumen perencanaan ini diekstrak dari workbook asli pada 7 Oktober 2026. Ini **snapshot sumber**, bukan backlog produksi berjalan. Tidak ada status READY dari sumber yang disalin sebagai status hasil repo.

**SHA-256 workbook:** `e75b92af52d0f72974d6ff304ed8f82cdb66149f0a3a73f08a5dfbbd100dd9d8`

Sumber: [workbook asli](<../references/MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx>). Navigasi: [rencana utama](../PRODUCTION_PLAN.md), [pedoman eksekusi](EXECUTION_PLAYBOOK.md), [spesifikasi artefak](ARTIFACT_SPECS.md).

## Cara membaca baseline

- Semua ID, status, prioritas, bobot, dependensi, catatan, tanggal target, dan URL di bawah berasal dari sheet sumber. Kolom path adalah **pemetaan usulan repo**, bukan bukti file sudah ada.
- `∅` berarti cell kosong; tidak diganti dengan nilai buatan. Nilai angka ditampilkan sebagaimana nilai cell/cache workbook, tanpa pembulatan baru.
- Definisi per jenis artefak dan QA gate diletakkan pada tabel terpisah untuk mengurangi pengulangan; setiap baris item mengacu pada jenisnya.
- Bobot produksi dan skor status bukan bobot penilaian mahasiswa. Jangan mengubah angka 10/20/25 di tabel menjadi persentase nilai mata kuliah.
- Tanggal target kosong dan owner TBD dipertahankan. Nama Tri Aji pada sumber bukan penetapan bahwa agen telah memperoleh persetujuan dosen.
- Nilai Score/Weighted Score adalah baseline workbook, bukan hasil validasi run produksi. Progres sumber tidak boleh disebut progres materi Markdown.
- Tahap A akan membentuk backlog kerja baru di `course/production/` dengan status sumber terpisah, `repo_status`, `markdown_readiness`, `fulfillment`, dan blocker.

## Ringkasan cakupan

| Kelompok | Jumlah | Rincian |
| --- | ---: | --- |
| Semester_Master | 12 | SEM-01–SEM-12 |
| Minggu pembelajaran | 196 | 14 minggu × 14 artefak |
| Ujian | 14 | UTS 7 + UAS 7 |
| Total | 222 | Seluruh ID unik |

Backlog sumber: 173 NOT STARTED, 31 DRAFT, 6 REVIEW. Semester_Master sumber: 4 NOT STARTED, 2 DRAFT, 4 REVIEW, 2 READY. Belum ada dokumen hasil produksi `course/` yang dinyatakan selesai oleh baseline ini.

## Definisi lifecycle dari sheet Definitions

| Status sumber | Score | Makna asli |
| --- | --- | --- |
| NOT STARTED | 0.0 | Belum mulai. |
| DRAFT | 0.25 | Sudah ada draft awal. |
| REVIEW | 0.5 | Sedang/siap ditinjau untuk akurasi dan alignment. |
| READY | 0.75 | Secara substansi siap dipakai; final publishing belum selesai. |
| PUBLISHED | 0.9 | Sudah dipublikasikan/diunggah untuk mahasiswa. |
| DELIVERED | 1.0 | Sudah digunakan/dilaksanakan. |
| IMPROVE | 0.85 | Sudah digunakan namun perlu perbaikan pada iterasi berikut. |

`IMPROVE` adalah jalur revisi setelah penggunaan, bukan tahap wajib sebelum READY. PUBLISHED/DELIVERED memerlukan bukti peristiwa yang sebenarnya. Lihat model status terpisah di pedoman eksekusi.

## Register sumber dari sheet Sources

| ID sumber | Nama asli | Peran asli | URL asli | Catatan asli |
| --- | --- | --- | --- | --- |
| S01 | Kurikulum OBE IF 2025 — Revisi 2026 | Primary curriculum source of truth | https://docs.google.com/spreadsheets/d/14frRyWdgLshOJ-5hVcL2CCoxCtm0d5gc | Use for CPL/CPMK/BK/course identity. |
| S02 | RPS_RTM_Dasar_Kecerdasan_Artifisial_dan_Pembelajaran_Mesin_2026-2027 | Operational RPS/RTM — IF24A | https://docs.google.com/document/d/1jfaenJg9Oi6PEsMjASpqO1D90EcQyd5H/edit | Current weekly topic, assessment, and RTM basis. |
| S03 | RTM_Dasar_Kecerdasan_Artifisial_dan_Pembelajaran_Mesin_IF24A-IF24H_2026_Template_Resmi_UAI | RTM source — IF24A | https://docs.google.com/document/d/1ktAxiyG_ctP2Ql8Svx8RBbl370c8wPia/edit | Detailed task structure. |
| S04 | IF24A - Dasar AI & ML - Tracker Presensi, Tugas dan Nilai | Class delivery tracker | https://docs.google.com/spreadsheets/d/1N9HH-Pk2Dbg2NnV5w0mGIld2PDibdIz16H9GpBUDluI/edit | Operational class evidence. |
| S05 | IF24H - Dasar AI & ML - Tracker Presensi, Tugas dan Nilai | Hybrid class delivery tracker | https://docs.google.com/spreadsheets/d/1WBP9NIduXQ_xqiB_PorhJKzB1eryTcrKeG8fRO0L3RI/edit | Operational hybrid-class evidence. |
| S06 | Master Prompt Package Mata Kuliah v2 | Teaching Package Operating System | ∅ | Local master prompt created 7 Oct 2026; upload/link when finalized. |

S01–S05 belum dibaca isinya pada tahap perencanaan ini. S06 menyebut paket v2, sementara file lokal berjudul Master Prompt Package Slide; catat hubungan ke `SRC-MASTER-PROMPT` tanpa menganggap identitas versi sudah pasti. `SRC-WORKBOOK` merujuk workbook lokal ini. Kegagalan akses domain Drive sebelumnya bukan bukti izin setiap dokumen sumber.

## Artefak tingkat semester

Semua kolom selain path dan row berasal dari Semester_Master. Score adalah cache kolom M.

| ID | Row | Path usulan | Layer | Artefak | DoD asli | Status sumber | Prioritas | Owner | Target Date | Dependensi asli | Output / Acceptance Criteria | File / URL | Notes | Score |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEM-01 | 2 | `course/governance/curriculum-audit.md` | GOVERN | Curriculum / Source-of-Truth Audit | Curriculum identity, CPL/CPMK/BK and prerequisite alignment locked. | REVIEW | P0 — Now | Tri Aji | ∅ | ∅ | Kurikulum workbook reviewed and conflicts recorded. | ∅ | Review against latest workbook. | 0.5 |
| SEM-02 | 3 | `course/governance/rps.md` | GOVERN | RPS Final | RPS identities, outcomes, weekly map, assessment, bibliography consistent. | REVIEW | P0 — Now | Tri Aji | ∅ | SEM-01 | RPS signed/ready as authoritative semester contract. | https://docs.google.com/document/d/1jfaenJg9Oi6PEsMjASpqO1D90EcQyd5H/edit | Current RPS exists; final QA needed. | 0.5 |
| SEM-03 | 4 | `course/governance/rtm.md` | GOVERN | RTM Master | All weekly assignments/assessments mapped to RPS and operational. | REVIEW | P0 — Now | Tri Aji | ∅ | SEM-02 | RTM instructions + outputs + rubrics are executable. | https://docs.google.com/document/d/1ktAxiyG_ctP2Ql8Svx8RBbl370c8wPia/edit | Current RTM exists; QA and production links needed. | 0.5 |
| SEM-04 | 5 | `course/governance/assessment-blueprint.md` | GOVERN | Assessment Blueprint | Assessment coverage, weights, cognitive level, evidence and traceability mapped. | DRAFT | P1 — Next | Tri Aji | ∅ | SEM-02, SEM-03 | One semester assessment blueprint approved. | ∅ | RPS already gives weights; convert into explicit blueprint. | 0.25 |
| SEM-05 | 6 | `course/semester/learning-architecture.md` | LEARN | Semester Learning Architecture | End-to-end learning spine, dependencies, WHY/WHAT/HOW progression. | REVIEW | P0 — Now | Tri Aji | ∅ | SEM-02 | All weeks form one coherent learning journey. | ∅ | Topic spine exists in RPS; pedagogical audit needed. | 0.5 |
| SEM-06 | 7 | `course/semester/book-toc.md` | KNOW | Book Table of Contents | 14 learning chapters + exam/project integration mapped to weekly outcomes. | NOT STARTED | P1 — Next | Tri Aji | ∅ | SEM-05 | TOC locked before chapter-by-chapter production. | ∅ | Use rolling book development. | 0 |
| SEM-07 | 8 | `course/semester/project-architecture.md` | PROVE | Project Architecture | W12–15 project stages, evidence, repo/report/demo, responsible AI and reproducibility. | DRAFT | P2 — Planned | Tri Aji | ∅ | SEM-03 | Project brief, stage gates, rubric and submission flow locked. | ∅ | RPS defines proposal → responsible AI → pipeline → final demo. | 0.25 |
| SEM-08 | 9 | `course/semester/lms-skeleton.md` | LEARN | LMS Course Skeleton | Weekly sections, naming, content pattern, submission pattern and links standardized. | NOT STARTED | P1 — Next | TBD | ∅ | SEM-05 | All 16 weeks have standard LMS shells. | ∅ | Can be implemented progressively. | 0 |
| SEM-09 | 10 | `course/semester/mastery-tracker.md` | PROVE | Mastery Tracker | Outcome-level mastery beyond attendance/grades, with remediation flags. | NOT STARTED | P2 — Planned | TBD | ∅ | SEM-04 | Students can be tracked by mastery dimension and evidence. | ∅ | Separate from existing attendance/grade trackers. | 0 |
| SEM-10 | 11 | `course/semester/question-bank.md` | PROVE | Question Bank | Tagged question bank by week, concept, level, difficulty and answer/rubric. | NOT STARTED | P2 — Planned | TBD | ∅ | SEM-04 | Reusable bank ready for quizzes, UTS, UAS and practice. | ∅ | Build continuously from weekly packages. | 0 |
| SEM-11 | 12 | `course/standards/teaching-package-os.md` | COMPOUND | Teaching Package Visual & Prompt OS | Standard for content, storyboard, slides, visuals, learning action and QA. | READY | P0 — Now | Tri Aji | ∅ | SEM-05 | Master prompt package version-controlled and reusable. | ∅ | Master Prompt Package Mata Kuliah v2 prepared. | 0.75 |
| SEM-12 | 13 | `course/production/dashboard.md` | COMPOUND | Production Control Sheet | Single command center for semester and weekly package production. | READY | P0 — Now | Tri Aji | ∅ | SEM-01 | Dashboard, backlog, status lifecycle, sources and QA controls operational. | ∅ | This workbook. | 0.75 |

## Peta topik dan outcome dari Production_Backlog

| Week cell | Topik asli | Sub-CPMK asli | Folder usulan | Jumlah item |
| --- | --- | --- | --- | ---: |
| 1.0 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | `course/weeks/w01` | 14 |
| 2.0 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | `course/weeks/w02` | 14 |
| 3.0 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | `course/weeks/w03` | 14 |
| 4.0 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | `course/weeks/w04` | 14 |
| 5.0 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | `course/weeks/w05` | 14 |
| 6.0 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | `course/weeks/w06` | 14 |
| 7.0 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | `course/weeks/w07` | 14 |
| 8.0 | UTS | DAIML-Sub-CPMK102-1 | `course/exams/uts` | 7 |
| 9.0 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | `course/weeks/w09` | 14 |
| 10.0 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | `course/weeks/w10` | 14 |
| 11.0 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | `course/weeks/w11` | 14 |
| 12.0 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | `course/weeks/w12` | 14 |
| 13.0 | Responsible AI | DAIML-Sub-CPMK082-1 | `course/weeks/w13` | 14 |
| 14.0 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | `course/weeks/w14` | 14 |
| 15.0 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | `course/weeks/w15` | 14 |
| 16.0 | UAS | DAIML-Sub-CPMK082-1 | `course/exams/uas` | 7 |

Kode Sub-CPMK di sini adalah baseline label sumber; jangan memperluas menjadi rumusan CPL/CPMK resmi tanpa S01/S02. Tujuan belajar rancangan menggunakan ID `Wnn-LOxx` terpisah.

## Definisi jenis artefak backlog

Layer, Artifact, DoD, QA Gate diturunkan dari setiap jenis baris Production_Backlog. Jika aturan Markdown berbeda dari output workbook, simpan kedua definisi; jangan menimpa definisi asli.

| Jenis ID | Layer | Artifact asli | Definition of Done asli | QA Gate asli |
| --- | --- | --- | --- | --- |
| Wnn-BOOK | KNOW | Book Chapter | Bab kanonik: konsep, intuisi, istilah, contoh, common mistakes, rangkuman. | Accuracy + alignment + clarity + usability |
| Wnn-MOD | LEARN | Student Module | Tujuan, prerequisite, alur belajar, aktivitas, practice, tugas, refleksi. | Accuracy + alignment + clarity + usability |
| Wnn-GUIDE | LEARN | Lecturer Guide | Timing, hook, analogi, pertanyaan Socratic, demo, transisi, debrief. | Accuracy + alignment + clarity + usability |
| Wnn-STORY | LEARN | Storyboard | Storyline slide lengkap dan audited sebelum visual final. | Accuracy + alignment + clarity + usability |
| Wnn-SLIDE | LEARN | Slides | Deck final presentation-ready dan take-home friendly. | Accuracy + alignment + clarity + usability |
| Wnn-DATA | LEARN | Dataset / Case | Dataset/kasus valid, data dictionary/source, dan konteks penggunaan. | Accuracy + alignment + clarity + usability |
| Wnn-LAB | LEARN | Notebook / Lab | Starter + solution notebook dapat dijalankan/reproduksi. | Accuracy + alignment + clarity + usability |
| Wnn-WORK | LEARN | Worksheet / Practice | Latihan aktif yang menghasilkan reasoning/output mahasiswa. | Accuracy + alignment + clarity + usability |
| Wnn-AIP | LEARN | AI Learning Prompts | Prompt tutor/critic/checker yang membantu tanpa menggantikan berpikir. | Accuracy + alignment + clarity + usability |
| Wnn-ASSESS | PROVE | Assignment / Quiz | Instruksi asesmen executable dan aligned ke outcome. | Accuracy + alignment + clarity + usability |
| Wnn-RUBRIC | PROVE | Rubric / Answer Key | Rubrik/kunci jelas, konsisten, dan dapat dipakai menilai. | Accuracy + alignment + clarity + usability |
| Wnn-LMS | LEARN | LMS Package | Materi, instruksi, link/file, forum/quiz/upload tertata di LMS. | Accuracy + alignment + clarity + usability |
| Wnn-EVID | PROVE | Evidence / Student Artifact | Bukti mastery yang jelas: notebook/report/video/demo/dll. | Accuracy + alignment + clarity + usability |
| Wnn-QA | COMPOUND | Post-Class QA | KEEP/FIX/ADD/REMOVE + bukti kesulitan mahasiswa + revisi. | Accuracy + alignment + clarity + usability |
| EXAM-BLUEPRINT | PROVE | Exam Blueprint | Coverage, indikator, level kognitif, proporsi, dan traceability ke CPMK. | Accuracy + alignment + clarity + usability |
| EXAM-QUESTION | PROVE | Question Set | Soal final lengkap, jelas, dan seimbang. | Accuracy + alignment + clarity + usability |
| EXAM-KEY | PROVE | Answer Key / Rubric | Kunci/rubrik lengkap dan dapat dipakai konsisten. | Accuracy + alignment + clarity + usability |
| EXAM-INSTR | LEARN | Exam Instruction | Instruksi teknis-akademik yang jelas untuk mahasiswa. | Accuracy + alignment + clarity + usability |
| EXAM-LMS | LEARN | LMS Exam Package | Setup LMS, file, waktu, submission, dan komunikasi. | Accuracy + alignment + clarity + usability |
| EXAM-EVID | PROVE | Exam Evidence Archive | Bukti pelaksanaan dan arsip asesmen tertata. | Accuracy + alignment + clarity + usability |
| EXAM-QA | COMPOUND | Post-Exam Analysis | Analisis item/hasil, gap mastery, dan tindakan perbaikan. | Accuracy + alignment + clarity + usability |

## Seluruh 210 item mingguan dan ujian

Row menunjuk baris asli Production_Backlog. Topik/outcome mengikuti tabel minggu, DoD dan QA mengikuti jenis ID. Kolom G/H/I/J/K/L/N/P/Q/R sumber dicatat per item di bawah.

| ID | Row | Path usulan | Production Weight | Status sumber | Prioritas | Owner | Dependensi asli | Target Date | File / URL | Status Score | Weighted Score | Notes |
| --- | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W01-BOOK | 2 | `course/weeks/w01/book-chapter.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W01-MOD | 3 | `course/weeks/w01/student-module.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W01-GUIDE | 4 | `course/weeks/w01/lecturer-guide.md` | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W01-STORY | 5 | `course/weeks/w01/storyboard.md` | 5.0 | REVIEW | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0.5 | 2.5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| W01-SLIDE | 6 | `course/weeks/w01/slides.md` | 10.0 | REVIEW | P1 — Next | TBD | Storyboard | ∅ | ∅ | 0.5 | 5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| W01-DATA | 7 | `course/weeks/w01/dataset-case.md` | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W01-LAB | 8 | `course/weeks/w01/lab.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W01-WORK | 9 | `course/weeks/w01/worksheet.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W01-AIP | 10 | `course/weeks/w01/ai-learning-prompts.md` | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W01-ASSESS | 11 | `course/weeks/w01/assignment-quiz.md` | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-01 already specified in RPS/RTM; production file still needs finalization. |
| W01-RUBRIC | 12 | `course/weeks/w01/rubric-answer-key.md` | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-01 already specified in RPS/RTM; production file still needs finalization. |
| W01-LMS | 13 | `course/weeks/w01/lms-package.md` | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W01-EVID | 14 | `course/weeks/w01/evidence-spec.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W01-QA | 15 | `course/weeks/w01/post-class-qa.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W02-BOOK | 16 | `course/weeks/w02/book-chapter.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W02-MOD | 17 | `course/weeks/w02/student-module.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W02-GUIDE | 18 | `course/weeks/w02/lecturer-guide.md` | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W02-STORY | 19 | `course/weeks/w02/storyboard.md` | 5.0 | REVIEW | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0.5 | 2.5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| W02-SLIDE | 20 | `course/weeks/w02/slides.md` | 10.0 | REVIEW | P1 — Next | TBD | Storyboard | ∅ | ∅ | 0.5 | 5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| W02-DATA | 21 | `course/weeks/w02/dataset-case.md` | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W02-LAB | 22 | `course/weeks/w02/lab.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W02-WORK | 23 | `course/weeks/w02/worksheet.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W02-AIP | 24 | `course/weeks/w02/ai-learning-prompts.md` | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W02-ASSESS | 25 | `course/weeks/w02/assignment-quiz.md` | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-02 already specified in RPS/RTM; production file still needs finalization. |
| W02-RUBRIC | 26 | `course/weeks/w02/rubric-answer-key.md` | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-02 already specified in RPS/RTM; production file still needs finalization. |
| W02-LMS | 27 | `course/weeks/w02/lms-package.md` | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W02-EVID | 28 | `course/weeks/w02/evidence-spec.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W02-QA | 29 | `course/weeks/w02/post-class-qa.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W03-BOOK | 30 | `course/weeks/w03/book-chapter.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W03-MOD | 31 | `course/weeks/w03/student-module.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W03-GUIDE | 32 | `course/weeks/w03/lecturer-guide.md` | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W03-STORY | 33 | `course/weeks/w03/storyboard.md` | 5.0 | REVIEW | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0.5 | 2.5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| W03-SLIDE | 34 | `course/weeks/w03/slides.md` | 10.0 | REVIEW | P1 — Next | TBD | Storyboard | ∅ | ∅ | 0.5 | 5 | Existing Week 1–3 material exists; needs audit against current Teaching Package OS. |
| W03-DATA | 35 | `course/weeks/w03/dataset-case.md` | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W03-LAB | 36 | `course/weeks/w03/lab.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W03-WORK | 37 | `course/weeks/w03/worksheet.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W03-AIP | 38 | `course/weeks/w03/ai-learning-prompts.md` | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W03-ASSESS | 39 | `course/weeks/w03/assignment-quiz.md` | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-03 already specified in RPS/RTM; production file still needs finalization. |
| W03-RUBRIC | 40 | `course/weeks/w03/rubric-answer-key.md` | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-03 already specified in RPS/RTM; production file still needs finalization. |
| W03-LMS | 41 | `course/weeks/w03/lms-package.md` | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W03-EVID | 42 | `course/weeks/w03/evidence-spec.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W03-QA | 43 | `course/weeks/w03/post-class-qa.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W04-BOOK | 44 | `course/weeks/w04/book-chapter.md` | 10.0 | NOT STARTED | P0 — Now | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W04-MOD | 45 | `course/weeks/w04/student-module.md` | 8.0 | NOT STARTED | P0 — Now | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W04-GUIDE | 46 | `course/weeks/w04/lecturer-guide.md` | 6.0 | NOT STARTED | P0 — Now | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W04-STORY | 47 | `course/weeks/w04/storyboard.md` | 5.0 | DRAFT | P0 — Now | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0.25 | 1.25 | 20-slide storyboard drafted 7 Oct 2026: Validation Before Believing. |
| W04-SLIDE | 48 | `course/weeks/w04/slides.md` | 10.0 | NOT STARTED | P0 — Now | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W04-DATA | 49 | `course/weeks/w04/dataset-case.md` | 6.0 | NOT STARTED | P0 — Now | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W04-LAB | 50 | `course/weeks/w04/lab.md` | 10.0 | NOT STARTED | P0 — Now | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W04-WORK | 51 | `course/weeks/w04/worksheet.md` | 7.0 | NOT STARTED | P0 — Now | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W04-AIP | 52 | `course/weeks/w04/ai-learning-prompts.md` | 3.0 | NOT STARTED | P0 — Now | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W04-ASSESS | 53 | `course/weeks/w04/assignment-quiz.md` | 8.0 | DRAFT | P0 — Now | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-04 scope and weighting defined; actual Moodle quiz/key still to produce. |
| W04-RUBRIC | 54 | `course/weeks/w04/rubric-answer-key.md` | 7.0 | DRAFT | P0 — Now | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-04 scope and weighting defined; actual Moodle quiz/key still to produce. |
| W04-LMS | 55 | `course/weeks/w04/lms-package.md` | 5.0 | NOT STARTED | P0 — Now | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W04-EVID | 56 | `course/weeks/w04/evidence-spec.md` | 8.0 | NOT STARTED | P0 — Now | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W04-QA | 57 | `course/weeks/w04/post-class-qa.md` | 7.0 | NOT STARTED | P0 — Now | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W05-BOOK | 58 | `course/weeks/w05/book-chapter.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W05-MOD | 59 | `course/weeks/w05/student-module.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W05-GUIDE | 60 | `course/weeks/w05/lecturer-guide.md` | 6.0 | NOT STARTED | P1 — Next | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W05-STORY | 61 | `course/weeks/w05/storyboard.md` | 5.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W05-SLIDE | 62 | `course/weeks/w05/slides.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W05-DATA | 63 | `course/weeks/w05/dataset-case.md` | 6.0 | NOT STARTED | P1 — Next | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W05-LAB | 64 | `course/weeks/w05/lab.md` | 10.0 | NOT STARTED | P1 — Next | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W05-WORK | 65 | `course/weeks/w05/worksheet.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W05-AIP | 66 | `course/weeks/w05/ai-learning-prompts.md` | 3.0 | NOT STARTED | P1 — Next | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W05-ASSESS | 67 | `course/weeks/w05/assignment-quiz.md` | 8.0 | DRAFT | P1 — Next | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-05 already specified in RPS/RTM; production file still needs finalization. |
| W05-RUBRIC | 68 | `course/weeks/w05/rubric-answer-key.md` | 7.0 | DRAFT | P1 — Next | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-05 already specified in RPS/RTM; production file still needs finalization. |
| W05-LMS | 69 | `course/weeks/w05/lms-package.md` | 5.0 | NOT STARTED | P1 — Next | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W05-EVID | 70 | `course/weeks/w05/evidence-spec.md` | 8.0 | NOT STARTED | P1 — Next | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W05-QA | 71 | `course/weeks/w05/post-class-qa.md` | 7.0 | NOT STARTED | P1 — Next | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W06-BOOK | 72 | `course/weeks/w06/book-chapter.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W06-MOD | 73 | `course/weeks/w06/student-module.md` | 8.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W06-GUIDE | 74 | `course/weeks/w06/lecturer-guide.md` | 6.0 | NOT STARTED | P2 — Planned | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W06-STORY | 75 | `course/weeks/w06/storyboard.md` | 5.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W06-SLIDE | 76 | `course/weeks/w06/slides.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W06-DATA | 77 | `course/weeks/w06/dataset-case.md` | 6.0 | NOT STARTED | P2 — Planned | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W06-LAB | 78 | `course/weeks/w06/lab.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W06-WORK | 79 | `course/weeks/w06/worksheet.md` | 7.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W06-AIP | 80 | `course/weeks/w06/ai-learning-prompts.md` | 3.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W06-ASSESS | 81 | `course/weeks/w06/assignment-quiz.md` | 8.0 | DRAFT | P2 — Planned | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-06 already specified in RPS/RTM; production file still needs finalization. |
| W06-RUBRIC | 82 | `course/weeks/w06/rubric-answer-key.md` | 7.0 | DRAFT | P2 — Planned | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-06 already specified in RPS/RTM; production file still needs finalization. |
| W06-LMS | 83 | `course/weeks/w06/lms-package.md` | 5.0 | NOT STARTED | P2 — Planned | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W06-EVID | 84 | `course/weeks/w06/evidence-spec.md` | 8.0 | NOT STARTED | P2 — Planned | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W06-QA | 85 | `course/weeks/w06/post-class-qa.md` | 7.0 | NOT STARTED | P2 — Planned | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W07-BOOK | 86 | `course/weeks/w07/book-chapter.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W07-MOD | 87 | `course/weeks/w07/student-module.md` | 8.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W07-GUIDE | 88 | `course/weeks/w07/lecturer-guide.md` | 6.0 | NOT STARTED | P2 — Planned | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W07-STORY | 89 | `course/weeks/w07/storyboard.md` | 5.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W07-SLIDE | 90 | `course/weeks/w07/slides.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W07-DATA | 91 | `course/weeks/w07/dataset-case.md` | 6.0 | NOT STARTED | P2 — Planned | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W07-LAB | 92 | `course/weeks/w07/lab.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W07-WORK | 93 | `course/weeks/w07/worksheet.md` | 7.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W07-AIP | 94 | `course/weeks/w07/ai-learning-prompts.md` | 3.0 | NOT STARTED | P2 — Planned | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W07-ASSESS | 95 | `course/weeks/w07/assignment-quiz.md` | 8.0 | DRAFT | P2 — Planned | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-07 already specified in RPS/RTM; production file still needs finalization. |
| W07-RUBRIC | 96 | `course/weeks/w07/rubric-answer-key.md` | 7.0 | DRAFT | P2 — Planned | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-07 already specified in RPS/RTM; production file still needs finalization. |
| W07-LMS | 97 | `course/weeks/w07/lms-package.md` | 5.0 | NOT STARTED | P2 — Planned | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W07-EVID | 98 | `course/weeks/w07/evidence-spec.md` | 8.0 | NOT STARTED | P2 — Planned | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W07-QA | 99 | `course/weeks/w07/post-class-qa.md` | 7.0 | NOT STARTED | P2 — Planned | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| UTS-BLUEPRINT | 100 | `course/exams/uts/blueprint.md` | 20.0 | DRAFT | P2 — Planned | TBD | RPS + Assessment Blueprint | ∅ | ∅ | 0.25 | 5 | Coverage already defined in RPS; explicit blueprint still needs production. |
| UTS-QUESTION | 101 | `course/exams/uts/question-set.md` | 25.0 | NOT STARTED | P2 — Planned | TBD | Exam Blueprint | ∅ | ∅ | 0 | 0 | ∅ |
| UTS-KEY | 102 | `course/exams/uts/answer-key-rubric.md` | 20.0 | NOT STARTED | P2 — Planned | TBD | Question Set | ∅ | ∅ | 0 | 0 | ∅ |
| UTS-INSTR | 103 | `course/exams/uts/instructions.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Exam Blueprint | ∅ | ∅ | 0 | 0 | ∅ |
| UTS-LMS | 104 | `course/exams/uts/lms-package.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Question Set + Instruction | ∅ | ∅ | 0 | 0 | ∅ |
| UTS-EVID | 105 | `course/exams/uts/evidence-archive-spec.md` | 5.0 | NOT STARTED | P2 — Planned | TBD | Delivered exam | ∅ | ∅ | 0 | 0 | ∅ |
| UTS-QA | 106 | `course/exams/uts/post-exam-analysis.md` | 10.0 | NOT STARTED | P2 — Planned | TBD | Exam results + evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W09-BOOK | 107 | `course/weeks/w09/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W09-MOD | 108 | `course/weeks/w09/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W09-GUIDE | 109 | `course/weeks/w09/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W09-STORY | 110 | `course/weeks/w09/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W09-SLIDE | 111 | `course/weeks/w09/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W09-DATA | 112 | `course/weeks/w09/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W09-LAB | 113 | `course/weeks/w09/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W09-WORK | 114 | `course/weeks/w09/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W09-AIP | 115 | `course/weeks/w09/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W09-ASSESS | 116 | `course/weeks/w09/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-08 already specified in RPS/RTM; production file still needs finalization. |
| W09-RUBRIC | 117 | `course/weeks/w09/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-08 already specified in RPS/RTM; production file still needs finalization. |
| W09-LMS | 118 | `course/weeks/w09/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W09-EVID | 119 | `course/weeks/w09/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W09-QA | 120 | `course/weeks/w09/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W10-BOOK | 121 | `course/weeks/w10/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W10-MOD | 122 | `course/weeks/w10/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W10-GUIDE | 123 | `course/weeks/w10/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W10-STORY | 124 | `course/weeks/w10/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W10-SLIDE | 125 | `course/weeks/w10/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W10-DATA | 126 | `course/weeks/w10/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W10-LAB | 127 | `course/weeks/w10/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W10-WORK | 128 | `course/weeks/w10/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W10-AIP | 129 | `course/weeks/w10/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W10-ASSESS | 130 | `course/weeks/w10/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-09 already specified in RPS/RTM; production file still needs finalization. |
| W10-RUBRIC | 131 | `course/weeks/w10/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-09 already specified in RPS/RTM; production file still needs finalization. |
| W10-LMS | 132 | `course/weeks/w10/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W10-EVID | 133 | `course/weeks/w10/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W10-QA | 134 | `course/weeks/w10/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W11-BOOK | 135 | `course/weeks/w11/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W11-MOD | 136 | `course/weeks/w11/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W11-GUIDE | 137 | `course/weeks/w11/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W11-STORY | 138 | `course/weeks/w11/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W11-SLIDE | 139 | `course/weeks/w11/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W11-DATA | 140 | `course/weeks/w11/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W11-LAB | 141 | `course/weeks/w11/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W11-WORK | 142 | `course/weeks/w11/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W11-AIP | 143 | `course/weeks/w11/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W11-ASSESS | 144 | `course/weeks/w11/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-10 already specified in RPS/RTM; production file still needs finalization. |
| W11-RUBRIC | 145 | `course/weeks/w11/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-10 already specified in RPS/RTM; production file still needs finalization. |
| W11-LMS | 146 | `course/weeks/w11/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W11-EVID | 147 | `course/weeks/w11/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W11-QA | 148 | `course/weeks/w11/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W12-BOOK | 149 | `course/weeks/w12/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W12-MOD | 150 | `course/weeks/w12/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W12-GUIDE | 151 | `course/weeks/w12/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W12-STORY | 152 | `course/weeks/w12/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W12-SLIDE | 153 | `course/weeks/w12/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W12-DATA | 154 | `course/weeks/w12/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W12-LAB | 155 | `course/weeks/w12/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W12-WORK | 156 | `course/weeks/w12/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W12-AIP | 157 | `course/weeks/w12/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W12-ASSESS | 158 | `course/weeks/w12/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-11 already specified in RPS/RTM; production file still needs finalization. |
| W12-RUBRIC | 159 | `course/weeks/w12/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-11 already specified in RPS/RTM; production file still needs finalization. |
| W12-LMS | 160 | `course/weeks/w12/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W12-EVID | 161 | `course/weeks/w12/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W12-QA | 162 | `course/weeks/w12/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W13-BOOK | 163 | `course/weeks/w13/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W13-MOD | 164 | `course/weeks/w13/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W13-GUIDE | 165 | `course/weeks/w13/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W13-STORY | 166 | `course/weeks/w13/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W13-SLIDE | 167 | `course/weeks/w13/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W13-DATA | 168 | `course/weeks/w13/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W13-LAB | 169 | `course/weeks/w13/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W13-WORK | 170 | `course/weeks/w13/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W13-AIP | 171 | `course/weeks/w13/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W13-ASSESS | 172 | `course/weeks/w13/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-12 already specified in RPS/RTM; production file still needs finalization. |
| W13-RUBRIC | 173 | `course/weeks/w13/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-12 already specified in RPS/RTM; production file still needs finalization. |
| W13-LMS | 174 | `course/weeks/w13/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W13-EVID | 175 | `course/weeks/w13/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W13-QA | 176 | `course/weeks/w13/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W14-BOOK | 177 | `course/weeks/w14/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W14-MOD | 178 | `course/weeks/w14/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W14-GUIDE | 179 | `course/weeks/w14/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W14-STORY | 180 | `course/weeks/w14/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W14-SLIDE | 181 | `course/weeks/w14/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W14-DATA | 182 | `course/weeks/w14/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W14-LAB | 183 | `course/weeks/w14/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W14-WORK | 184 | `course/weeks/w14/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W14-AIP | 185 | `course/weeks/w14/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W14-ASSESS | 186 | `course/weeks/w14/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-13 already specified in RPS/RTM; production file still needs finalization. |
| W14-RUBRIC | 187 | `course/weeks/w14/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-13 already specified in RPS/RTM; production file still needs finalization. |
| W14-LMS | 188 | `course/weeks/w14/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W14-EVID | 189 | `course/weeks/w14/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W14-QA | 190 | `course/weeks/w14/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| W15-BOOK | 191 | `course/weeks/w15/book-chapter.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Semester learning map + book TOC | ∅ | ∅ | 0 | 0 | ∅ |
| W15-MOD | 192 | `course/weeks/w15/student-module.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W15-GUIDE | 193 | `course/weeks/w15/lecturer-guide.md` | 6.0 | NOT STARTED | P3 — Later | TBD | Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W15-STORY | 194 | `course/weeks/w15/storyboard.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Lecturer Guide | ∅ | ∅ | 0 | 0 | ∅ |
| W15-SLIDE | 195 | `course/weeks/w15/slides.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Storyboard | ∅ | ∅ | 0 | 0 | ∅ |
| W15-DATA | 196 | `course/weeks/w15/dataset-case.md` | 6.0 | NOT STARTED | P3 — Later | TBD | RPS topic + case requirement | ∅ | ∅ | 0 | 0 | ∅ |
| W15-LAB | 197 | `course/weeks/w15/lab.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Dataset / Case + Book Chapter | ∅ | ∅ | 0 | 0 | ∅ |
| W15-WORK | 198 | `course/weeks/w15/worksheet.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Student Module | ∅ | ∅ | 0 | 0 | ∅ |
| W15-AIP | 199 | `course/weeks/w15/ai-learning-prompts.md` | 3.0 | NOT STARTED | P3 — Later | TBD | Book Chapter + Worksheet | ∅ | ∅ | 0 | 0 | ∅ |
| W15-ASSESS | 200 | `course/weeks/w15/assignment-quiz.md` | 8.0 | DRAFT | P3 — Later | TBD | RTM + outcome | ∅ | ∅ | 0.25 | 2 | T-14 already specified in RPS/RTM; production file still needs finalization. |
| W15-RUBRIC | 201 | `course/weeks/w15/rubric-answer-key.md` | 7.0 | DRAFT | P3 — Later | TBD | Assignment / Quiz | ∅ | ∅ | 0.25 | 1.75 | T-14 already specified in RPS/RTM; production file still needs finalization. |
| W15-LMS | 202 | `course/weeks/w15/lms-package.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Module + Slides + Assessment | ∅ | ∅ | 0 | 0 | ∅ |
| W15-EVID | 203 | `course/weeks/w15/evidence-spec.md` | 8.0 | NOT STARTED | P3 — Later | TBD | Assignment / Practice | ∅ | ∅ | 0 | 0 | ∅ |
| W15-QA | 204 | `course/weeks/w15/post-class-qa.md` | 7.0 | NOT STARTED | P3 — Later | TBD | Delivered class + student evidence | ∅ | ∅ | 0 | 0 | ∅ |
| UAS-BLUEPRINT | 205 | `course/exams/uas/blueprint.md` | 20.0 | DRAFT | P3 — Later | TBD | RPS + Assessment Blueprint | ∅ | ∅ | 0.25 | 5 | Coverage already defined in RPS; explicit blueprint still needs production. |
| UAS-QUESTION | 206 | `course/exams/uas/question-set.md` | 25.0 | NOT STARTED | P3 — Later | TBD | Exam Blueprint | ∅ | ∅ | 0 | 0 | ∅ |
| UAS-KEY | 207 | `course/exams/uas/answer-key-rubric.md` | 20.0 | NOT STARTED | P3 — Later | TBD | Question Set | ∅ | ∅ | 0 | 0 | ∅ |
| UAS-INSTR | 208 | `course/exams/uas/instructions.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Exam Blueprint | ∅ | ∅ | 0 | 0 | ∅ |
| UAS-LMS | 209 | `course/exams/uas/lms-package.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Question Set + Instruction | ∅ | ∅ | 0 | 0 | ∅ |
| UAS-EVID | 210 | `course/exams/uas/evidence-archive-spec.md` | 5.0 | NOT STARTED | P3 — Later | TBD | Delivered exam | ∅ | ∅ | 0 | 0 | ∅ |
| UAS-QA | 211 | `course/exams/uas/post-exam-analysis.md` | 10.0 | NOT STARTED | P3 — Later | TBD | Exam results + evidence | ∅ | ∅ | 0 | 0 | ∅ |

## Pemeriksaan ekstraksi

- 12 baris Semester_Master dan 210 baris Production_Backlog telah terbaca; 222 ID unik.
- 14 jenis artefak mingguan × 14 minggu dan 7 jenis ujian × 2 ujian telah dipetakan ke path; tidak ada ID dibuang atau path utama ganda.
- DoD/QA yang dideduplikasi diperiksa identik untuk semua baris jenis yang sama.
- Status backlog dihitung ulang dari cell, bukan menggunakan angka dashboard sebagai satu-satunya bukti.
- SHA-256 digunakan untuk mendeteksi perubahan sumber; jika workbook baru masuk, buat revisi baseline dan laporan perubahan, jangan menghapus baseline lama tanpa catatan.

Baseline ini menyelesaikan inventaris perencanaan. Produksi isi bahan ajar, pemeriksaan kurikulum resmi, run lab, dan bukti pelaksanaan masih pekerjaan berikutnya.
