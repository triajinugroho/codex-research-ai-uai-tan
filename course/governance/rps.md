---
artifact_id: SEM-02
title: Rancangan RPS
course_code: IF52510031
period: 2026–2027
week: null
classes:
- IF24A
- IF24H
audience: keduanya
distribution: student_candidate
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
dependencies:
- SEM-01
integration_refs:
- SEM-04
- SEM-05
workbook_dependencies: SEM-01
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
# Rancangan RPS

Run P05: `20261008-004030-P05-W01-W04`; versi rancangan 0.1. **RANCANGAN / PERLU KONFIRMASI SUMBER**. Dokumen ini membantu produksi bahan W01–W04; belum menjadi kontrak akademik atau dokumen yang disahkan. `official_outcome_refs` pada metadata adalah kode baseline, bukan outcome resmi yang telah diperiksa. Semua tujuan, aktivitas, tugas, indikator dan rubrik lokal di bawah adalah **USULAN**.

[Audit](curriculum-audit.md) · [RPS](rps.md) · [RTM](rtm.md) · [Blueprint](assessment-blueprint.md) · [Register sumber](../production/sources.md) · [Kendali](../production/dashboard.md)

Provenance: SRC-WORKBOOK untuk identitas/topik/kode/inventaris; SRC-MASTER-PROMPT untuk desain pedagogi saja. S01–S03 belum dibaca menurut audit P03. Tidak ada akses ulang eksternal pada P05; status akses mengacu pada hasil P03, bukan klaim pemeriksaan jaringan baru. Dua file lokal tetap mempunyai hash yang sama. Isi ML, dataset, kode dan hitungan belum diuji pada batch governance ini.

## Identitas dan deskripsi

Dasar Kecerdasan Artifisial dan Pembelajaran Mesin, IF52510031, kelas IF24A/IF24H, periode baseline 2026–2027. Locator: SRC-WORKBOOK Dashboard!B3:B5; periode dari nama workbook/label sumber. Identitas final, SKS, posisi semester, prasyarat formal dan pengesahan **PERLU KONFIRMASI SUMBER**, sebagaimana [audit](curriculum-audit.md#identitas-dan-fakta-yang-tersedia).

Deskripsi **USULAN**: mahasiswa membangun bahasa bersama tentang masalah AI/ML, membaca dan menyiapkan data, merancang evaluasi, lalu mengintegrasikan pemodelan, generalisasi dan komunikasi bukti. Fokus produksi sekarang hanya W01–W04. Deskripsi ini mengikuti judul baseline; bukan kutipan deskripsi RPS resmi.

## Capaian dan bahan kajian

CPL/CPMK/BK resmi: **PERLU KONFIRMASI SUMBER (S01)**. Referensi Sub-CPMK baseline DAIML-Sub-CPMK082-1 dan DAIML-Sub-CPMK102-1 dipertahankan persis. Rumusan lengkap dan hubungan ke CPL/CPMK belum diperiksa. Daftar delapan LO fokus tersedia pada [audit](curriculum-audit.md#tujuan-operasional-fokus--usulan) dan matriks berikut.

| LO lokal USULAN | Rumusan operasional | Bukti rencana |
| --- | --- | --- |
| W01-LO01 | mengklasifikasikan kasus AI/ML, supervised/unsupervised, klasifikasi/regresi dengan alasan | Tabel kategori dan alasan yang merujuk ciri kasus |
| W01-LO02 | merumuskan masalah dengan unit observasi, fitur tersedia saat prediksi, target dan manfaat keputusan | Problem statement dengan empat komponen dan waktu ketersediaan fitur |
| W02-LO01 | membuat profil tipe data, missingness, distribusi dan dugaan duplikasi | Data dictionary, profil data dan satu visual beranotasi |
| W02-LO02 | membedakan observasi data dari hipotesis penyebab dan memilih pemeriksaan lanjutan | Memo yang memisahkan temuan, dugaan, keputusan sementara dan kebutuhan data |
| W03-LO01 | memilih transformasi berdasarkan tipe fitur dan kebutuhan model | Peta fitur–transformasi dengan alasan, termasuk kategori baru |
| W03-LO02 | menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru | Trace fit/transform yang membedakan training dan data baru |
| W04-LO01 | memilih strategi split/CV sesuai tujuan prediksi, unit independen, kelompok dan waktu | Matriks tiga skenario dengan tujuan, unit, splitter dan alasan |
| W04-LO02 | mendeteksi leakage dan merancang batas fit serta penggunaan test | Diagram aliran data, trace indeks/fold dan memo batas klaim evaluasi |

Prasyarat belajar usulan W01 → W02 → W03 → W04 ditulis dalam audit; bukan prasyarat administrasi. P05 tidak mengklaim bahan/bab/pengalaman mahasiswa sudah tersedia.

## Peta 16 minggu

Semua aktivitas, luaran dan LO lokal merupakan USULAN. Kolom ketentuan mencakup durasi, tenggat dan bobot nilai resmi; nilainya belum tersedia, **bukan nol**. Rujukan workbook mendukung topik/kode saja, bukan akurasi isi teknis. W05–W16 tetap slot governance, bukan produksi paket pekan/proyek/ujian.

| Minggu | Topik baseline | Kode outcome | LO lokal | Aktivitas USULAN | Luaran/bukti USULAN | Rujukan dan batas | Ketentuan resmi | Scope produksi |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W01 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 (BASELINE) | W01-LO01, W01-LO02 | Klasifikasi kartu kasus dan problem framing | Tabel kategori dan alasan yang merujuk ciri kasus; Problem statement dengan empat komponen dan waktu ketersediaan fitur | [RTM W01](rtm.md#w01); [blueprint](assessment-blueprint.md#matriks-fokus-w01w04); WEEKLY_BLUEPRINTS brief W01 | PERLU KONFIRMASI SUMBER | DETAIL USULAN; naskah pedagogi VALIDATED, resmi PROVISIONAL |
| W02 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 (BASELINE) | W02-LO01, W02-LO02 | Profil tabel/visual dan kritik kesimpulan | Data dictionary, profil data dan satu visual beranotasi; Memo yang memisahkan temuan, dugaan, keputusan sementara dan kebutuhan data | [RTM W02](rtm.md#w02); [blueprint](assessment-blueprint.md#matriks-fokus-w01w04); WEEKLY_BLUEPRINTS brief W02 | PERLU KONFIRMASI SUMBER | DETAIL USULAN; naskah pedagogi VALIDATED, resmi PROVISIONAL |
| W03 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 (BASELINE) | W03-LO01, W03-LO02 | Peta transformasi dan trace fit/transform | Peta fitur–transformasi dengan alasan, termasuk kategori baru; Trace fit/transform yang membedakan training dan data baru | [RTM W03](rtm.md#w03); [blueprint](assessment-blueprint.md#matriks-fokus-w01w04); WEEKLY_BLUEPRINTS brief W03 | PERLU KONFIRMASI SUMBER | DETAIL USULAN; naskah pedagogi VALIDATED, resmi PROVISIONAL |
| W04 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 (BASELINE) | W04-LO01, W04-LO02 | Matriks split tiga skenario dan audit batas fit/test | Matriks tiga skenario dengan tujuan, unit, splitter dan alasan; Diagram aliran data, trace indeks/fold dan memo batas klaim evaluasi | [RTM W04](rtm.md#w04); [blueprint](assessment-blueprint.md#matriks-fokus-w01w04); WEEKLY_BLUEPRINTS brief W04 | PERLU KONFIRMASI SUMBER | DETAIL USULAN; naskah pedagogi VALIDATED, resmi PROVISIONAL |
| W05 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 (BASELINE) | W05-LO01: membandingkan kandidat klasifikasi dengan alasan yang sesuai data | Bandingkan keputusan kandidat pada kasus planned | Catatan perbandingan model dan batas klaim | Production_Backlog!C58:D58; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W06 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 (BASELINE) | W06-LO01: memilih evaluasi target numerik dan menafsirkan hasilnya | Bahas contoh error dan konteks keputusan | Memo evaluasi regresi | Production_Backlog!C72:D72; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W07 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 (BASELINE) | W07-LO01: menafsirkan hasil pengelompokan dan batas evaluasinya | Kritik interpretasi cluster | Catatan interpretasi dan keterbatasan | Production_Backlog!C86:D86; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W08 | UTS | DAIML-Sub-CPMK102-1 (BASELINE) | UTS-LO01: menunjukkan integrasi kemampuan fondasi W01–W07 | USULAN checkpoint UTS; bentuk/waktu belum ditetapkan | Respons ujian planned; cakupan resmi belum ditetapkan | Production_Backlog!C100:D100; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W09 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 (BASELINE) | W09-LO01: memilih kandidat model melalui protokol validasi | Bandingkan kandidat pada data pengembangan | Catatan keputusan model selection | Production_Backlog!C107:D107; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W10 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 (BASELINE) | W10-LO01: menganalisis diagnosis generalisasi dan pilihan perbaikan | Kritik pola evaluasi yang direncanakan | Memo diagnosis generalisasi | Production_Backlog!C121:D121; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W11 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 (BASELINE) | W11-LO01: menjelaskan alur jaringan sederhana dan rancangan evaluasi | Telusuri alur input–prediksi–pembaruan planned | Diagram beranotasi dan evaluasi planned | Production_Backlog!C135:D135; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W12 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 (BASELINE) | W12-LO01: membandingkan penggunaan DL/GenAI beserta batasnya | Diskusi peluang dan proposal proyek USULAN | Proposal masalah dan batas klaim planned | Production_Backlog!C149:D149; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W13 | Responsible AI | DAIML-Sub-CPMK082-1 (BASELINE) | W13-LO01: menganalisis risiko dan mitigasi pada kasus AI | Audit risiko proyek USULAN | Catatan risiko/mitigasi planned | Production_Backlog!C163:D163; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W14 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 (BASELINE) | W14-LO01: merancang paket ML yang dapat direproduksi | Audit manifest data, versi dan langkah run | Manifest reproduksi planned | Production_Backlog!C177:D177; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W15 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 (BASELINE) | W15-LO01: mengomunikasikan bukti dan keterbatasan proyek | Klinik, demo dan refleksi USULAN | Paket demo/presentasi planned | Production_Backlog!C191:D191; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |
| W16 | UAS | DAIML-Sub-CPMK082-1 (BASELINE) | UAS-LO01: menunjukkan integrasi capaian akhir sesuai scope yang ditetapkan kelak | USULAN checkpoint UAS; hubungan proyek belum ditetapkan | Respons/bukti akhir planned; bentuk resmi belum diketahui | Production_Backlog!C205:D205; sumber akademik S01–S03 belum dibaca | PERLU KONFIRMASI SUMBER | SLOT USULAN; konten/tugas rinci deferred |

## Rancangan belajar fokus W01–W04

Urutan per pertemuan **USULAN**: WHY (alasan belajar) → intuisi → konsep formal → mekanisme → contoh → praktik → refleksi. Adaptasi mengikuti SRC-MASTER-PROMPT dan DEC-0005; tidak menetapkan durasi kelas.

| Minggu | Materi yang harus diajarkan sebelum asesmen | Tindakan mahasiswa | Umpan balik/remediasi | Penerus |
| --- | --- | --- | --- | --- |
| W01 | Unit observasi, fitur/target, kategori masalah dan waktu ketersediaan data | Klasifikasi kasus dan rumuskan problem statement | Minta alasan kategori dan koreksi fitur yang belum tersedia saat keputusan | Data dictionary W02 |
| W02 | Tipe/satuan, missingness, distribusi, duplikasi dan batas inferensi | Profil data dan pisahkan observasi dari dugaan sebab | Kembali ke tabel/visual pendukung; tandai klaim yang membutuhkan data tambahan | Keputusan transformasi W03 |
| W03 | Pilihan transformasi dan makna fit/transform pada data baru | Peta fitur–transformasi dan telusuri asal parameter | Perbaiki trace parameter serta penanganan fitur/kategori | Rancangan batas data W04 |
| W04 | Tujuan evaluasi, unit independen, split/CV dan batas fit/test | Audit tiga skenario, diagram pipeline dan memo batas klaim | Uji kembali asumsi tiap skenario dan batas akses data | Protokol evaluasi W05 dan seterusnya planned |

Definisi teknis, contoh dan kode harus diperiksa terhadap sumber teknis yang benar-benar dibaca ketika paket pekan diproduksi. G3 runtime dan teaching pass belum dijalankan pada P05; RPS ini merencanakan cakupan, tidak membuktikan lab dapat dijalankan.

## Asesmen, umpan balik dan ketentuan

Empat tugas fokus W01-ASM01–W04-ASM01 adalah rancangan latihan/checkpoint formatif dengan opsi menjadi tugas dinilai setelah keselarasan S02/S03 diperiksa. [RTM](rtm.md) mengatur alur/luaran usulan; [blueprint](assessment-blueprint.md) menghubungkan LO, bukti dan kriteria. Hasil formative tidak otomatis menjadi nilai mata kuliah atau statistik mastery.

| Komponen | Status saat ini | Yang harus diperoleh sebelum final |
| --- | --- | --- |
| Kuis/tugas W01–W04 | USULAN; belum ada bobot nilai semester | S02/S03: bentuk, scope, bobot dan ketentuan |
| UTS W08 | Slot baseline; cakupan W01–W07 hanya usulan desain | S02: cakupan, bentuk, waktu, skor, aturan dan akses |
| UAS W16 | Slot baseline; hubungan ujian/proyek belum ditetapkan | S02/S03: cakupan dan bentuk resmi |
| Proyek W12–W15 | Slot usulan dari planning/baseline; SEM-07 belum diproduksi | S02/S03 dan rancangan proyek yang diotorisasi kemudian |
| Nilai akhir dan total bobot | PERLU KONFIRMASI SUMBER; tidak dapat dijumlahkan | Daftar komponen/bobot resmi dan aturan agregasi |
| AI, kolaborasi, submit dan penalti | PERLU KONFIRMASI SUMBER; tidak ada sanksi yang ditetapkan | Kebijakan yang berlaku untuk tiap kelas |

## Adaptasi kelas — PROVISIONAL

Fakta tersedia hanya cakupan IF24A/IF24H pada workbook. Label S05 sebagai hybrid tracker tidak menetapkan moda aktual. Inti LO dan bukti diusulkan sama. Jika sesi langsung tersedia, gunakan diskusi/anotasi berpasangan; jika belajar mandiri diperlukan, gunakan kartu kasus dan anotasi teks dengan checkpoint. Pilihan ini belum jadwal/moda resmi. Sediakan representasi tabel/diagram berupa teks serta jalur tanpa layanan AI berbayar; kemampuan awal dan beban kerja ditelaah saat pilot.

## Rujukan yang dibaca dan bibliografi yang belum tersedia

- SRC-WORKBOOK, file lokal pengguna, SHA-256 `e75b92af52d0f72974d6ff304ed8f82cdb66149f0a3a73f08a5dfbbd100dd9d8`: mendukung baseline produksi.
- SRC-MASTER-PROMPT, file lokal pengguna, SHA-256 `b2542568f9f4e363f9ec8055410a4280e6132cb8251d618893a005f921e5d21b`: mendukung desain pedagogi; bukan textbook ML.

Keduanya merupakan rujukan kerja produksi, **bukan bibliografi akademik resmi**. Bibliografi RPS dan sumber substansi ML **PERLU KONFIRMASI SUMBER**. Tidak ada textbook/paper/DOI/lisensi rekaan. S01–S03 tetap kandidat/UNAVAILABLE menurut register, tidak dimasukkan sebagai dokumen yang telah dibaca.

## Status dan pemenuhan

SEM-02 DRAFT, markdown_readiness DRAFT, fulfillment PARTIAL. DoD asli meminta RPS yang konsisten dan siap sebagai kontrak semester; sumber resmi/pengesahan/bibliografi belum tersedia. Empat rancangan saling terhubung; integrasi SEM-05 dari P04 menunggu produksinya. Laporan validasi memeriksa struktur dan traceability, tidak mengesahkan RPS.

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
