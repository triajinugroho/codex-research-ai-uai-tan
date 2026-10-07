---
artifact_id: SEM-04
title: Assessment Blueprint — RANCANGAN
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
source_status: DRAFT
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
- SEM-02
- SEM-03
integration_refs:
- SEM-01
- SEM-05
- SEM-07
- SEM-09
- SEM-10
workbook_dependencies: SEM-02, SEM-03
scope_record: course/production/reports/20261008-004030-P05-W01-W04-ticket.md
validation_records:
- course/production/reports/20261008-004030-P05-W01-W04-validation.md
- course/production/reports/20261007-182808-P16-governance-delta-validation.md
blockers:
- 'GAP-S01: kurikulum resmi belum dibaca'
- 'GAP-S02: bobot/kebijakan/bentuk asesmen resmi belum dibaca'
- 'GAP-S03: tugas/rubrik resmi belum dibaca'
class_adaptations: PROVISIONAL
delivery_evidence: []
---
# Assessment Blueprint — RANCANGAN

Run `20261008-004030-P05-W01-W04`, versi 0.1. **RANCANGAN / PERLU KONFIRMASI SUMBER**. Semua tugas, LO, indikator, level kognitif, bukti dan kriteria merupakan **USULAN**; tidak ada ketentuan resmi yang ditetapkan. Referensi kode outcome adalah baseline workbook, bukan rumusan resmi. S01–S03 belum dibaca menurut P03; P05 tidak menguji ulang konektivitas.

[Audit](curriculum-audit.md) · [RPS](rps.md) · [RTM](rtm.md) · [Blueprint](assessment-blueprint.md) · [Register sumber](../production/sources.md) · [Kendali](../production/dashboard.md)

SRC-WORKBOOK mendukung judul/kode/lifecycle produksi, sedangkan SRC-MASTER-PROMPT mendukung desain pedagogi. Planning/WEEKLY_BLUEPRINTS.md menjadi brief desain, bukan bukti kebenaran teknis atau kebijakan. Paket stimulus, dataset, soal, solusi dan runtime harus diverifikasi pada batch pekan. Dokumen ini belum membuktikan tugas siap diterapkan kepada mahasiswa.

## Model penilaian dan batas

Asesmen fokus berupa latihan/checkpoint formatif **USULAN**. Empat ASM mengukur delapan LO lokal, masing-masing dua kriteria. Bobot mata kuliah/angka nilai akhir **PERLU KONFIRMASI SUMBER**. Weight, Status Score dan Weighted Score workbook mengukur produksi; tidak dipakai sebagai bobot nilai, ambang lulus atau mastery mahasiswa.

Level kognitif di bawah merupakan label rancangan atas tindakan yang diminta, bukan taksonomi/level resmi kurikulum yang telah diperiksa. Kesulitan empiris belum diketahui. Semua link ke governance merujuk file nyata; ID BOOK/MOD/ACT/EX/ASSESS/RUBRIC pekan adalah rencana yang belum tersedia.

## Matriks fokus W01–W04

| LO | Outcome baseline + status | Tujuan operasional USULAN | Tindakan kognitif | Materi sebelum asesmen | Aktivitas/contoh | Asesmen | Rubrik | Bukti teramati | Sumber/batas |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| W01-LO01 | DAIML-Sub-CPMK082-1; BASELINE | mengklasifikasikan kasus AI/ML, supervised/unsupervised, klasifikasi/regresi dengan alasan | Mengklasifikasikan; menjelaskan (label USULAN) | W01-BOOK/MOD planned; Klasifikasi kasus dan problem framing | W01-ACT01 / W01-EX01 planned | W01-ASM01 | W01-RC01 | W01-EV01: Tabel kategori dan alasan yang merujuk ciri kasus | WEEKLY_BLUEPRINTS brief W01 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W01-LO02 | DAIML-Sub-CPMK082-1; BASELINE | merumuskan masalah dengan unit observasi, fitur tersedia saat prediksi, target dan manfaat keputusan | Merumuskan; menganalisis (label USULAN) | W01-BOOK/MOD planned; Klasifikasi kasus dan problem framing | W01-ACT01 / W01-EX01 planned | W01-ASM01 | W01-RC02 | W01-EV01: Problem statement dengan empat komponen dan waktu ketersediaan fitur | WEEKLY_BLUEPRINTS brief W01 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W02-LO01 | DAIML-Sub-CPMK102-1; BASELINE | membuat profil tipe data, missingness, distribusi dan dugaan duplikasi | Mendeskripsikan; menerapkan (label USULAN) | W02-BOOK/MOD planned; Memo audit eksplorasi data | W02-ACT01 / W02-EX01 planned | W02-ASM01 | W02-RC01 | W02-EV01: Data dictionary, profil data dan satu visual beranotasi | WEEKLY_BLUEPRINTS brief W02 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W02-LO02 | DAIML-Sub-CPMK102-1; BASELINE | membedakan observasi data dari hipotesis penyebab dan memilih pemeriksaan lanjutan | Menganalisis; mengevaluasi (label USULAN) | W02-BOOK/MOD planned; Memo audit eksplorasi data | W02-ACT01 / W02-EX01 planned | W02-ASM01 | W02-RC02 | W02-EV01: Memo yang memisahkan temuan, dugaan, keputusan sementara dan kebutuhan data | WEEKLY_BLUEPRINTS brief W02 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W03-LO01 | DAIML-Sub-CPMK102-1; BASELINE | memilih transformasi berdasarkan tipe fitur dan kebutuhan model | Menerapkan; menganalisis (label USULAN) | W03-BOOK/MOD planned; Peta transformasi dan trace fit/transform | W03-ACT01 / W03-EX01 planned | W03-ASM01 | W03-RC01 | W03-EV01: Peta fitur–transformasi dengan alasan, termasuk kategori baru | WEEKLY_BLUEPRINTS brief W03 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W03-LO02 | DAIML-Sub-CPMK102-1; BASELINE | menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru | Menjelaskan; menganalisis (label USULAN) | W03-BOOK/MOD planned; Peta transformasi dan trace fit/transform | W03-ACT01 / W03-EX01 planned | W03-ASM01 | W03-RC02 | W03-EV01: Trace fit/transform yang membedakan training dan data baru | WEEKLY_BLUEPRINTS brief W03 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W04-LO01 | DAIML-Sub-CPMK102-1; BASELINE | memilih strategi split/CV sesuai tujuan prediksi, unit independen, kelompok dan waktu | Menganalisis; mengevaluasi (label USULAN) | W04-BOOK/MOD planned; Audit rancangan evaluasi dan leakage | W04-ACT01 / W04-EX01/EX02/EX03/EX04 planned | W04-ASM01 | W04-RC01 | W04-EV01: Matriks tiga skenario dengan tujuan, unit, splitter dan alasan | WEEKLY_BLUEPRINTS brief W04 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |
| W04-LO02 | DAIML-Sub-CPMK102-1; BASELINE | mendeteksi leakage dan merancang batas fit serta penggunaan test | Menganalisis; merancang (label USULAN) | W04-BOOK/MOD planned; Audit rancangan evaluasi dan leakage | W04-ACT01 / W04-EX01/EX02/EX03/EX04 planned | W04-ASM01 | W04-RC02 | W04-EV01: Diagram aliran data, trace indeks/fold dan memo batas klaim evaluasi | WEEKLY_BLUEPRINTS brief W04 (desain); S01–S03/GAP-TECH belum terbaca/terpenuhi |

Setiap LO mempunyai satu kriteria tersendiri; memakai EV yang sama untuk dua LO tidak berarti keduanya otomatis tercapai. Dosen menelaah bagian berbeda dari paket bukti. Tugas W02 menggunakan framing W01, tugas W03 menggunakan profil W02, dan W04 menggunakan trace W03; pengulangan ini merupakan progres rancangan yang beralasan, bukan empat tugas identik. Saat produksi stimulus, periksa tidak ada tuntutan konsep yang belum diajarkan/di-bridge.

## Rubrik kualitatif fokus — USULAN

Tiga level kerja: **memadai**, **parsial/perlu perbaikan**, dan **belum menunjukkan indikator**. Ini deskriptor lokal untuk umpan balik; bukan skor numerik atau batas kelulusan resmi. Bukti tidak dikumpulkan atau belum ditelaah diberi catatan tersendiri, bukan dinilai otomatis sebagai gagal. Jawaban alternatif yang sesuai tujuan/data dapat diterima dengan alasan yang dapat ditelusuri. Tidak ada toleransi angka karena soal numerik/hasil run belum diproduksi.

## W01

| RC | LO/ASM | Dimensi | Memadai | Parsial/perlu perbaikan | Belum menunjukkan indikator |
| --- | --- | --- | --- | --- | --- |
| W01-RC01 | W01-LO01; W01-ASM01 | Klasifikasi kasus dan alasan | Kategori kasus dijustifikasi dengan ciri masalah, target dan cara belajar; alternatif dijelaskan bila konteks memungkinkan | Kategori tampak masuk akal tetapi alasan belum menunjukkan ciri kasus | Kategori tidak disertai alasan atau bertentangan dengan konteks |
| W01-RC02 | W01-LO02; W01-ASM01 | Problem statement dan ketersediaan fitur | Unit, fitur, target dan manfaat keputusan eksplisit; waktu ketersediaan fitur diperiksa | Komponen utama ada tetapi manfaat/unit/waktu data masih ambigu | Target/unit tidak jelas atau rancangan mengandalkan data yang belum tersedia saat keputusan |

## W02

| RC | LO/ASM | Dimensi | Memadai | Parsial/perlu perbaikan | Belum menunjukkan indikator |
| --- | --- | --- | --- | --- | --- |
| W02-RC01 | W02-LO01; W02-ASM01 | Profil dan keterlacakan data | Tipe/satuan, missingness, distribusi dan dugaan duplikasi tercatat serta menunjuk tabel/visual pendukung | Profil hanya sebagian atau referensi ke kolom/visual belum jelas | Pernyataan profil tidak memiliki bukti atau definisi pemeriksaan |
| W02-RC02 | W02-LO02; W02-ASM01 | Batas kesimpulan dan pemeriksaan lanjutan | Memo memisahkan observasi, hipotesis, keputusan sementara dan data/pemeriksaan tambahan | Hipotesis diakui tetapi rencana pemeriksaan belum terkait temuan | Dugaan sebab dilaporkan sebagai fakta atau keputusan tidak didukung temuan |

## W03

| RC | LO/ASM | Dimensi | Memadai | Parsial/perlu perbaikan | Belum menunjukkan indikator |
| --- | --- | --- | --- | --- | --- |
| W03-RC01 | W03-LO01; W03-ASM01 | Pilihan transformasi yang beralasan | Setiap fitur mempunyai perlakuan dan alasan sesuai tipe/kebutuhan; skenario kategori baru dipertimbangkan | Pilihan ada tetapi alasan/batas penerapan sebagian belum jelas | Transformasi hanya daftar API tanpa hubungan ke fitur/tujuan |
| W03-RC02 | W03-LO02; W03-ASM01 | Trace belajar parameter dan data baru | Trace menunjukkan asal parameter dari training dan penerapan pada data baru; batas fit/transform jelas | Batas disebut tetapi trace data/parameter belum lengkap | Batas belajar parameter tidak dibedakan atau data evaluasi dipakai sebagai input fit dalam rancangan |

## W04

| RC | LO/ASM | Dimensi | Memadai | Parsial/perlu perbaikan | Belum menunjukkan indikator |
| --- | --- | --- | --- | --- | --- |
| W04-RC01 | W04-LO01; W04-ASM01 | Tujuan–unit–strategi evaluasi | Ketiga skenario mempunyai tujuan, unit/kelompok/waktu, strategi dan alasan yang konsisten; alternatif terkait deployment dijelaskan | Strategi diberi alasan tetapi unit/kelompok/waktu belum lengkap pada satu skenario | Pilihan hanya nama splitter atau mengabaikan struktur kasus |
| W04-RC02 | W04-LO02; W04-ASM01 | Batas fit/test dan keterlacakan evaluasi | Diagram dan trace membedakan training, pengembangan dan test; asal fit/tuning serta batas klaim dapat diaudit | Batas disebut tetapi satu tahap/fold atau penggunaan test belum jelas | Diagram tidak menelusuri sumber parameter atau memakai test untuk pengembangan sambil mengklaim estimasi final |

## Cakupan semester dan ujian — slot governance

| Minggu | Topik baseline | Kode baseline | LO/checkpoint USULAN | Bukti/asesmen planned | Keputusan yang masih ditahan |
| --- | --- | --- | --- | --- | --- |
| W01 | Pengantar AI dan Machine Learning | DAIML-Sub-CPMK082-1 | W01-LO01, W01-LO02 | W01-ASM01 / W01-EV01 | S01–S03: mapping/ketentuan/bobot; detail fokus USULAN |
| W02 | Eksplorasi Data untuk ML | DAIML-Sub-CPMK102-1 | W02-LO01, W02-LO02 | W02-ASM01 / W02-EV01 | S01–S03: mapping/ketentuan/bobot; detail fokus USULAN |
| W03 | Preprocessing dan Feature Engineering | DAIML-Sub-CPMK102-1 | W03-LO01, W03-LO02 | W03-ASM01 / W03-EV01 | S01–S03: mapping/ketentuan/bobot; detail fokus USULAN |
| W04 | Pembagian Data dan Validasi | DAIML-Sub-CPMK102-1 | W04-LO01, W04-LO02 | W04-ASM01 / W04-EV01 | S01–S03: mapping/ketentuan/bobot; detail fokus USULAN |
| W05 | Klasifikasi I: KNN dan Decision Tree | DAIML-Sub-CPMK082-1 | W05-LO01: membandingkan kandidat klasifikasi dengan alasan yang sesuai data | Catatan perbandingan model dan batas klaim | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W06 | Regresi Linear dan Metrik Evaluasi | DAIML-Sub-CPMK102-1 | W06-LO01: memilih evaluasi target numerik dan menafsirkan hasilnya | Memo evaluasi regresi | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W07 | Clustering dan Metrik Clustering | DAIML-Sub-CPMK102-1 | W07-LO01: menafsirkan hasil pengelompokan dan batas evaluasinya | Catatan interpretasi dan keterbatasan | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W08 | UTS | DAIML-Sub-CPMK102-1 | UTS-LO01: menunjukkan integrasi kemampuan fondasi W01–W07 | Respons ujian planned; cakupan resmi belum ditetapkan | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W09 | Klasifikasi II dan Model Selection | DAIML-Sub-CPMK082-1 | W09-LO01: memilih kandidat model melalui protokol validasi | Catatan keputusan model selection | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W10 | Generalisasi, Overfitting, dan Regularisasi | DAIML-Sub-CPMK082-1 | W10-LO01: menganalisis diagnosis generalisasi dan pilihan perbaikan | Memo diagnosis generalisasi | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W11 | Jaringan Syaraf Tiruan | DAIML-Sub-CPMK082-1 | W11-LO01: menjelaskan alur jaringan sederhana dan rancangan evaluasi | Diagram beranotasi dan evaluasi planned | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W12 | Pengantar Deep Learning dan Generative AI | DAIML-Sub-CPMK082-1 | W12-LO01: membandingkan penggunaan DL/GenAI beserta batasnya | Proposal masalah dan batas klaim planned | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W13 | Responsible AI | DAIML-Sub-CPMK082-1 | W13-LO01: menganalisis risiko dan mitigasi pada kasus AI | Catatan risiko/mitigasi planned | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W14 | Pipeline ML End-to-End dan Reproduksibilitas | DAIML-Sub-CPMK082-1 | W14-LO01: merancang paket ML yang dapat direproduksi | Manifest reproduksi planned | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W15 | Presentasi Proyek Akhir | DAIML-Sub-CPMK082-1 | W15-LO01: mengomunikasikan bukti dan keterbatasan proyek | Paket demo/presentasi planned | S01–S03: mapping/ketentuan/bobot; rincian deferred |
| W16 | UAS | DAIML-Sub-CPMK082-1 | UAS-LO01: menunjukkan integrasi capaian akhir sesuai scope yang ditetapkan kelak | Respons/bukti akhir planned; bentuk resmi belum diketahui | S01–S03: mapping/ketentuan/bobot; rincian deferred |

Kedua kode baseline terpetakan sepanjang semester. Cakupan resmi UTS/UAS, bentuk soal, relasi proyek, jumlah butir, waktu dan aturan **PERLU KONFIRMASI SUMBER**. Usulan cakupan UTS W01–W07 dan UAS W09–W15 beserta fondasi berasal dari planning; belum ditetapkan sebagai aturan. P05 tidak membuat soal/kunci ujian atau paket proyek.

## Register komponen dan bobot

| Komponen | Fungsi USULAN | Bobot semester resmi | Skor lokal | Status |
| --- | --- | --- | --- | --- |
| W01-ASM01 | Diagnosis framing dan alasan kategori | PERLU KONFIRMASI SUMBER | Tidak ditetapkan; rubrik kualitatif | Rancangan, bukan tugas resmi |
| W02-ASM01 | Profil dan batas kesimpulan | PERLU KONFIRMASI SUMBER | Tidak ditetapkan; rubrik kualitatif | Rancangan, bukan tugas resmi |
| W03-ASM01 | Pilihan transformasi dan trace parameter | PERLU KONFIRMASI SUMBER | Tidak ditetapkan; rubrik kualitatif | Rancangan, bukan tugas resmi |
| W04-ASM01 | Rancangan evaluasi dan batas data | PERLU KONFIRMASI SUMBER | Tidak ditetapkan; rubrik kualitatif | Bukan bukti angka T-04 asli |
| Kuis/tugas lanjutan/proyek/UTS/UAS | Slot coverage semester | PERLU KONFIRMASI SUMBER | Belum ada butir/paket skor | Deferred; belum siap diterapkan |
| TOTAL | Agregasi nilai akhir | BELUM DAPAT DIHITUNG | Tidak menjumlahkan rubrik kualitatif | Tidak ditulis 0% atau 100% rekaan |

Proporsi kuantitatif usulan sengaja belum ditetapkan karena tidak diperlukan untuk fondasi traceability. Perhitungan total bobot tidak berlaku bagi desain kualitatif; verifikasi total nilai resmi belum dapat dijalankan sampai S02 tersedia.

## Umpan balik, mastery dan remediasi — USULAN

- Catat LO, bagian bukti, kriteria, komentar, versi revisi dan tanggal telaah yang benar-benar terjadi. Jangan mengisi data mahasiswa/pencapaian pada P05.
- Bedakan belum ada bukti, bukti belum ditelaah, indikator perlu perbaikan, dan indikator memadai pada scope tugas. Keputusan ini rancangan label kerja untuk SEM-09 kelak, bukan enum status artefak produksi.
- Beri satu tindakan perbaikan yang terkait RC: framing kasus W01, keterlacakan observasi W02, trace parameter W03, atau tujuan–unit–batas evaluasi W04.
- Jika suatu dimensi memadai dan dimensi lain parsial, jangan menyimpulkan seluruh LO tercapai dari rata-rata yang belum ditetapkan. Bobot/nilai resmi terpisah dari diagnostic mastery.
- Kalibrasi penilai memakai bukti nyata atau simulasi berlabel setelah stimulus/kunci tersedia; hasil kalibrasi saat ini UNRUN. Aturan pengumpulan ulang/penalti resmi belum ditentukan.

## Gap coverage dan tindakan

| Gap | Dampak | Tindakan berikut |
| --- | --- | --- |
| GAP-S01/S02/S03 | Mapping outcome/kebijakan/bobot tidak dapat difinalkan | Baca sumber yang berlaku lalu impact/revision ticket; pertahankan kode baseline |
| GAP-TECH dan input W01–W04 belum ada | Tidak membuktikan tugas/lab dapat diselesaikan atau klaim teknis valid | Produksi sumber/stimulus/solusi dan uji G2/G3/G4 pada paket pekan |
| SEM-05/06/11 belum ada | Arsitektur, TOC dan standar menunggu P04 | Gunakan draft governance sebagai input P04; bukan siklus prasyarat |
| Rincian W05–W16 deferred | Tidak ada klaim seluruh asesmen semester siap | Produksi pada fase semester selanjutnya |
| Pelaksanaan/kalibrasi belum ada | Tidak ada data mastery/kesulitan/reliabilitas empiris | Siapkan instrumen pada fase berikut, isi hanya setelah bukti aktual |

## Pemenuhan dan batas validasi

SEM-04 DRAFT/DRAFT/PARTIAL; source_verification PARTIAL, official_alignment PROVISIONAL. DoD asli meminta coverage, bobot, level dan traceability serta persetujuan blueprint semester; pada P05 tersedia desain fokus dan slot semester, sedangkan bobot/pengesahan/asesmen operasional belum tersedia. G1 dan konsistensi struktur G4 fokus diperiksa dalam laporan, tidak disamakan dengan teaching pass, kalibrasi penilai atau asesmen resmi tervalidasi.

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
