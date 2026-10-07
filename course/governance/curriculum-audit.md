---
artifact_id: SEM-01
title: Audit Kurikulum — RANCANGAN
course_code: IF52510031
period: 2026–2027
week: null
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
version: '0.2'
updated_at: '2026-10-08'
owner: Tri Aji
source_status: REVIEW
production:
  repo_status: DRAFT
markdown_readiness: DRAFT
fulfillment: PARTIAL
source_verification: PARTIAL
official_alignment: PROVISIONAL
learning_ids:
- W01-LO01
- W01-LO02
- W02-LO01
- W02-LO02
- W03-LO01
- W03-LO02
- W04-LO01
- W04-LO02
official_outcome_refs:
- DAIML-Sub-CPMK082-1
- DAIML-Sub-CPMK102-1
assessment_ids:
- W01-ASM01
- W02-ASM01
- W03-ASM01
- W04-ASM01
example_ids: []
evidence_requirement_ids:
- W01-EV01
- W02-EV01
- W03-EV01
- W04-EV01
source_ids:
- SRC-WORKBOOK
- SRC-MASTER-PROMPT
- SRC-TECH-001
- SRC-TECH-002
- SRC-TECH-003
dependencies: []
integration_refs:
- SEM-02
- SEM-04
- SEM-05
workbook_dependencies: ''
scope_record: course/production/reports/20261008-004030-P05-W01-W04-ticket.md
validation_records:
- course/production/reports/20261008-004030-P05-W01-W04-validation.md
- course/production/reports/20261007-182808-P16-governance-delta-validation.md
blockers:
- 'GAP-S01: kurikulum resmi belum dibaca'
- 'GAP-S02: RPS dan kebijakan resmi belum dibaca'
- 'GAP-S03: RTM resmi belum dibaca'
class_adaptations: PROVISIONAL
delivery_evidence: []
---
# Audit Kurikulum — RANCANGAN

Run P05: `20261008-004030-P05-W01-W04`; versi rancangan 0.1. **RANCANGAN / PERLU KONFIRMASI SUMBER**. Dokumen ini membantu produksi bahan W01–W04; belum menjadi kontrak akademik atau dokumen yang disahkan. `official_outcome_refs` pada metadata adalah kode baseline, bukan outcome resmi yang telah diperiksa. Semua tujuan, aktivitas, tugas, indikator dan rubrik lokal di bawah adalah **USULAN**.

[Audit](curriculum-audit.md) · [RPS](rps.md) · [RTM](rtm.md) · [Blueprint](assessment-blueprint.md) · [Register sumber](../production/sources.md) · [Kendali](../production/dashboard.md)

Provenance: SRC-WORKBOOK untuk identitas/topik/kode/inventaris; SRC-MASTER-PROMPT untuk desain pedagogi saja. S01–S03 belum dibaca menurut audit P03. Tidak ada akses ulang eksternal pada P05; status akses mengacu pada hasil P03, bukan klaim pemeriksaan jaringan baru. Dua file lokal tetap mempunyai hash yang sama. Isi ML, dataset, kode dan hitungan belum diuji pada batch governance ini.

## Identitas dan fakta yang tersedia

| Bidang | Nilai/batas | Sumber/locator | Status |
| --- | --- | --- | --- |
| Nama mata kuliah | Dasar Kecerdasan Artifisial dan Pembelajaran Mesin | Dashboard!B3 | BASELINE; S01/S02 belum dibaca |
| Kode | IF52510031 | Dashboard!B4 | BASELINE; bukan verifikasi kurikulum |
| Cakupan kelas | IF24A + IF24H | Dashboard!B5 | BASELINE; kesetaraan ketentuan kelas perlu pemeriksaan |
| Tahun | 2026–2027 | Nama workbook dan label S02/S03 | BASELINE; kalender semester belum diketahui |
| Konteks program/institusi | Informatika, Universitas Al-Azhar Indonesia | SRC-MASTER-PROMPT §1.A, baris 37–41 | Konteks desain tertulis; identitas akademik menunggu S01 |
| Owner sumber SEM-01–04 | Tri Aji | Semester_Master!G2:G5 | Owner produksi sumber; bukan pengesah yang ditetapkan |
| SKS, semester penempatan, prasyarat formal | PERLU KONFIRMASI SUMBER | S01/S02 belum dibaca | Tidak ditetapkan dari topik/kelas |
| CPL, CPMK dan BK resmi | PERLU KONFIRMASI SUMBER | S01 belum dibaca | Kode Sub-CPMK bukan rumusan induk lengkap |
| Durasi/moda/jadwal, bobot, aturan AI/kolaborasi | PERLU KONFIRMASI SUMBER | S02/S03 belum dibaca | Tidak diwarisi dari label tracker atau skor produksi |
| Versi resmi, pengesahan dan bibliografi | PERLU KONFIRMASI SUMBER | S01–S03 belum dibaca | Tidak ada tanda tangan/tanggal pengesahan rekaan |

CPL adalah capaian lulusan program; CPMK adalah capaian mata kuliah; Sub-CPMK adalah capaian yang dirinci; BK adalah bahan kajian. Istilah dipakai sebagai kategori audit, tanpa menambahkan rumusan resmi. Angka 082/102 dalam kode tidak ditafsirkan sebagai CPL, level, semester atau jam. Tidak ada crosswalk kurikulum antarversi yang dapat disahkan dari nama sumber saja.

## Peta topik dan outcome baseline

| Minggu | Topik baseline persis | Kode baseline persis | Locator workbook | Status akademik |
| --- | --- | --- | --- | --- |
| W01 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | Production_Backlog!C2:D2 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W02 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | Production_Backlog!C16:D16 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W03 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | Production_Backlog!C30:D30 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W04 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | Production_Backlog!C44:D44 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W05 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | Production_Backlog!C58:D58 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W06 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | Production_Backlog!C72:D72 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W07 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | Production_Backlog!C86:D86 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W08 | UTS | DAIML-Sub-CPMK102-1 | Production_Backlog!C100:D100 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W09 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | Production_Backlog!C107:D107 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W10 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | Production_Backlog!C121:D121 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W11 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | Production_Backlog!C135:D135 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W12 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | Production_Backlog!C149:D149 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W13 | Responsible AI | DAIML-Sub-CPMK082-1 | Production_Backlog!C163:D163 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W14 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | Production_Backlog!C177:D177 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W15 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | Production_Backlog!C191:D191 | BASELINE; rumusan/mapping resmi belum diperiksa |
| W16 | UAS | DAIML-Sub-CPMK082-1 | Production_Backlog!C205:D205 | BASELINE; rumusan/mapping resmi belum diperiksa |

Hanya dua kode unik teramati: DAIML-Sub-CPMK082-1 dan DAIML-Sub-CPMK102-1. Satu kode muncul pada beberapa minggu; pengulangan bukan bukti typo dan tidak diubah. W08/W16 adalah slot UTS/UAS; jumlah 16 baris tidak berarti 16 bab belajar. Workbook menyimpan 14 minggu belajar dan 2 ujian.

## Tujuan operasional fokus — USULAN

| LO lokal | Perilaku yang akan diperiksa | Rujukan kode baseline | Hubungan resmi |
| --- | --- | --- | --- |
| W01-LO01 | mengklasifikasikan kasus AI/ML, supervised/unsupervised, klasifikasi/regresi dengan alasan | DAIML-Sub-CPMK082-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W01-LO02 | merumuskan masalah dengan unit observasi, fitur tersedia saat prediksi, target dan manfaat keputusan | DAIML-Sub-CPMK082-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W02-LO01 | membuat profil tipe data, missingness, distribusi dan dugaan duplikasi | DAIML-Sub-CPMK102-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W02-LO02 | membedakan observasi data dari hipotesis penyebab dan memilih pemeriksaan lanjutan | DAIML-Sub-CPMK102-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W03-LO01 | memilih transformasi berdasarkan tipe fitur dan kebutuhan model | DAIML-Sub-CPMK102-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W03-LO02 | menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru | DAIML-Sub-CPMK102-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W04-LO01 | memilih strategi split/CV sesuai tujuan prediksi, unit independen, kelompok dan waktu | DAIML-Sub-CPMK102-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |
| W04-LO02 | mendeteksi leakage dan merancang batas fit serta penggunaan test | DAIML-Sub-CPMK102-1 | USULAN; ekuivalensi resmi PERLU KONFIRMASI SUMBER |

LO berasal dari planning/WEEKLY_BLUEPRINTS.md brief W01–W04 dan diturunkan sebagai kontrak desain. Klaim teknis/bahan pengajaran belum terverifikasi hanya karena LO mempunyai kata kerja terukur. Kriteria dan bukti ditelusuri pada [blueprint](assessment-blueprint.md#matriks-fokus-w01w04); tugas pada [RTM](rtm.md).

## Bahan kajian dan prasyarat

BK resmi: **PERLU KONFIRMASI SUMBER (S01)**. Domain kerja usulan dari judul minggu adalah problem framing, eksplorasi data, transformasi fitur, dan rancangan evaluasi; domain ini tidak diberi kode BK resmi.

| Tahap | Prasyarat belajar usulan | Lokasi penguatan yang direncanakan | Batas |
| --- | --- | --- | --- |
| W01 | Membaca tabel dan alasan logis; diagnosis pengalaman Python | W01-MOD/GUIDE planned | Bukan syarat penerimaan resmi |
| W02 | W01: unit observasi, fitur dan target; membaca frekuensi/grafik | W02-BOOK/MOD planned | Jembatan sintaks disiapkan bila diagnosis meminta |
| W03 | W02: tipe fitur, nilai hilang dan skala; makna data baru | W03-BOOK/MOD planned | Batas fit/transform perlu sumber teknis sebelum validasi |
| W04 | W01–W03: tujuan, unit data, transformasi yang belajar parameter | Bridge pada scope/bab pilot W04 planned | W04 boleh diproduksi dulu; tidak menyatakan W01–W03 sudah ada |

## Konflik, ketidakpastian dan keputusan

Belum ada konflik CPL/CPMK/RPS/RTM yang dapat dibuktikan: dokumen resminya belum dibaca. Status ini bukan kesimpulan bahwa semua dokumen selaras.

| Isu | Dua locator/bukti | Dampak | Keputusan sementara | Resolusi/penanggung jawab |
| --- | --- | --- | --- | --- |
| Identitas S06 v2 belum pasti | Sources!B7/E7 dan judul SRC-MASTER-PROMPT baris 1–2 | Versi SEM-11/turunan desain | DEC-0004: pisahkan dua record | Periksa v2 asli/konfirmasi spesifik; penanggung jawab konfirmasi belum ditetapkan |
| Urutan konsep dan intuisi bervariasi | Master §1.A baris 49; §1.H baris 261 dan §20 baris 1190 dst | Alur materi W01–W04 | DEC-0005: WHY → intuisi → formalisasi sebagai adaptasi | Review pedagogi P04; bukan perubahan kebijakan |
| Jumlah slide berupa target dan parameter | Master §20 baris 1177; §2 baris 384–385 | STORY/SLIDE/SEM-11 | DEC-0006: sekitar 20 sebagai target awal | Jumlah akhir mengikuti scope/durasi yang nanti diperiksa |
| T-04 disebut sudah mempunyai scope/weighting | Production_Backlog!R53:R54 dan N53:N54 kosong | ASSESS/RUBRIC W04 | Rancangan W04-ASM01 tidak diklaim sebagai T-04 asli | Peroleh rincian T-04 dari S03; penanggung jawab konfirmasi belum ditetapkan |

## Kebutuhan finalisasi dan dampak perubahan

1. Baca S01 versi yang berlaku: nama/kode/SKS/semester/prasyarat, CPL–CPMK–Sub-CPMK–BK dan locator. Simpan hasil aktual sebelum mengubah mapping.
2. Baca S02 untuk tiap kelas yang berlaku: peta 16 minggu, metode, durasi/bobot/bibliografi/kebijakan, status pengesahan. Periksa cakupan IF24H secara tersendiri.
3. Baca S03: instruksi/luaran/rubrik serta hubungan T-04 dengan rancangan ini. Konflik harus menyimpan dua locator dan dampak, tidak diselesaikan dari dugaan.
4. Jika data resmi mengubah kode/topik/tugas, gunakan impact/revision ticket yang diotorisasi; revisi RPS, RTM, blueprint, lalu artefak pekan terdampak. Pertahankan snapshot sumber P02.
5. P04 menggunakan rancangan ini sebagai input arsitektur; backreference SEM-05 belum ada dan bukan blocker awal P05. Penerapan akademik dan finalisasi tetap menunggu sumber/pengesahan.

## Pemenuhan DoD dan batas pemeriksaan

DoD asli SEM-01: identitas, CPL/CPMK/BK dan prasyarat selaras serta dikunci. Pada P05 baru audit baseline, crosswalk lokal dan daftar gap tersedia: fulfillment PARTIAL. G0/G1 pada struktur rancangan diperiksa dalam laporan; keselarasan resmi PROVISIONAL. Tidak ada bukti pelaksanaan atau pengesahan.

## Rekonsiliasi sesudah produksi W01–W04 — USULAN

Bagian awal mempertahankan desain P05 dan ketidakpastian sumber resmi. Kini dokumentasi teknis lokal sudah dibaca dan kode starter/reference W01–W04 sudah dijalankan; GAP-TECH untuk scope inti naskah fokus ditutup pada laporan teknis, bukan pada semua topik semester. Empat paket naskah tersedia; tidak ada klaim mahasiswa sudah mengikuti kelas. Slot W05–W16 tetap deferred. Governance tetap DRAFT/PARTIAL/PROVISIONAL sebab kurikulum/RPS/RTM/pengesahan/bobot/durasi belum terverifikasi.

| LO | Butir final | Bukti | Status |
| --- | --- | --- | --- |
| W01-LO01 | W01-Q01, W01-Q03 | [Paket W01](../weeks/w01/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W01-LO02 | W01-Q02 | [Paket W01](../weeks/w01/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W02-LO01 | W02-Q01, W02-Q02 | [Paket W02](../weeks/w02/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W02-LO02 | W02-Q03 | [Paket W02](../weeks/w02/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W03-LO01 | W03-Q01 | [Paket W03](../weeks/w03/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W03-LO02 | W03-Q02, W03-Q03 | [Paket W03](../weeks/w03/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W04-LO01 | W04-Q01 | [Paket W04](../weeks/w04/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |
| W04-LO02 | W04-Q02, W04-Q03 | [Paket W04](../weeks/w04/index.md) | Naskah VALIDATED, mapping resmi PROVISIONAL |

Skor operasional latihan USULAN: Q01/Q02/Q03 masing-masing maksimum2, total6; level0/1/2 mengoperasionalkan kualitas jawaban lokal. Ini bukan bobot nilai semester, ambang kelulusan atau penggantian nilai workbook. RC01/RC02 tetap menilai dua LO secara tersendiri, tanpa menyimpulkan mastery dari total. Contoh dan jawaban diperiksa sebagai simulasi; kalibrasi penilai/hasil mahasiswa belum tersedia. Sumber teknis/snapshot pada register; bank12 butir actual pada SEM-10. P04/SEM-05/06/11 dan SEM-08/09/10 kini tersedia sebagai fondasi, bukan publikasi.
