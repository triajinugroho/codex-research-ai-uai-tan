---
artifact_id: SEM-03
title: RTM Master — RANCANGAN
course_code: IF52510031
period: 2026–2027
week: null
classes:
- IF24A
- IF24H
audience: keduanya
distribution: mixed_split_required
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
- SEM-02
integration_refs:
- SEM-04
- SEM-07
workbook_dependencies: SEM-02
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
# RTM Master — RANCANGAN

Run `20261008-004030-P05-W01-W04`, versi 0.1. **RANCANGAN / PERLU KONFIRMASI SUMBER**. Semua tugas, LO, indikator, level kognitif, bukti dan kriteria merupakan **USULAN**; tidak ada ketentuan resmi yang ditetapkan. Referensi kode outcome adalah baseline workbook, bukan rumusan resmi. S01–S03 belum dibaca menurut P03; P05 tidak menguji ulang konektivitas.

[Audit](curriculum-audit.md) · [RPS](rps.md) · [RTM](rtm.md) · [Blueprint](assessment-blueprint.md) · [Register sumber](../production/sources.md) · [Kendali](../production/dashboard.md)

SRC-WORKBOOK mendukung judul/kode/lifecycle produksi, sedangkan SRC-MASTER-PROMPT mendukung desain pedagogi. Planning/WEEKLY_BLUEPRINTS.md menjadi brief desain, bukan bukti kebenaran teknis atau kebijakan. Paket stimulus, dataset, soal, solusi dan runtime harus diverifikasi pada batch pekan. Dokumen ini belum membuktikan tugas siap diterapkan kepada mahasiswa.

## Katalog fokus dan batas penggunaan

Empat brief berikut adalah tugas lokal yang diusulkan, bukan salinan RTM resmi. W04-ASM01 tidak diklaim identik dengan T-04 asli. ASM adalah ID asesmen; EV adalah spesifikasi bukti; RC adalah kriteria rubrik. ID berlaku lintas file governance dan akan diteruskan ke paket pekan, bukan menjadi artefak utama tambahan.

| Tugas | Minggu | LO lokal | Bukti | Rubrik | Jenis/status |
| --- | --- | --- | --- | --- | --- |
| [W01-ASM01](#w01) | W01 | W01-LO01, W01-LO02 | W01-EV01 | W01-RC01, W01-RC02 | Latihan/checkpoint formatif USULAN; dinilai resmi belum ditetapkan |
| [W02-ASM01](#w02) | W02 | W02-LO01, W02-LO02 | W02-EV01 | W02-RC01, W02-RC02 | Latihan/checkpoint formatif USULAN; dinilai resmi belum ditetapkan |
| [W03-ASM01](#w03) | W03 | W03-LO01, W03-LO02 | W03-EV01 | W03-RC01, W03-RC02 | Latihan/checkpoint formatif USULAN; dinilai resmi belum ditetapkan |
| [W04-ASM01](#w04) | W04 | W04-LO01, W04-LO02 | W04-EV01 | W04-RC01, W04-RC02 | Latihan/checkpoint formatif USULAN; dinilai resmi belum ditetapkan |

Sebelum penerapan, dosen perlu memastikan sumber resmi, stimulus/input, paket ajar dan ketentuan tugas tersedia. Bagian instruksi calon mahasiswa dapat dipisahkan; catatan implementasi/kalibrasi dosen tetap terpisah. Dokumen belum dibagikan kepada mahasiswa dan tidak memuat kunci jawaban atau solusi kode.

## Bagian A — Brief instruksi calon mahasiswa (USULAN)

## W01

**W01-ASM01 — Klasifikasi kasus dan problem framing (USULAN)**

- LO: W01-LO01 dan W01-LO02; kode baseline DAIML-Sub-CPMK082-1 (ekuivalensi resmi belum diperiksa).
- Tujuan/indikator: mengklasifikasikan kasus AI/ML, supervised/unsupervised, klasifikasi/regresi dengan alasan; merumuskan masalah dengan unit observasi, fitur tersedia saat prediksi, target dan manfaat keputusan.
- Prasyarat: Membaca tabel sederhana; materi W01 tentang kategori masalah, unit observasi dan data tersedia saat keputusan. Diagnosis Python tidak menjadi syarat baru.
- Input/sumber daya: Kartu kasus sintetis W01-EX01, panduan unit/fitur/target dan contoh struktur problem statement. Input belum dibuat; dosen harus menyediakan konteks yang cukup dan tidak menyisipkan jawaban.
- Estimasi usaha mandiri: **USULAN 45–60 menit**, belum diuji pada mahasiswa; bukan durasi kelas resmi. Waktu pelaksanaan, tenggat, kanal dan bobot resmi PERLU KONFIRMASI SUMBER.

Langkah yang diusulkan:

1. Baca kartu dan catat tujuan keputusan serta data yang tersedia; tandai informasi yang belum diberikan.
2. Untuk tiap kasus, tentukan kategori yang relevan dan tulis alasan berdasarkan ciri kasus; nyatakan alternatif bila konteks belum cukup.
3. Pilih satu kasus dan rumuskan unit observasi, fitur, target serta manfaat keputusan.
4. Tandai waktu tiap fitur tersedia; revisi problem statement bila informasi muncul setelah keputusan.
5. Tuliskan pertanyaan klarifikasi atau batas asumsi; lampirkan revisi setelah umpan balik.

Luaran W01-EV01: Tabel kasus–kategori–alasan, satu problem statement empat komponen, daftar waktu ketersediaan fitur, dan refleksi revisi.

Format **USULAN**: naskah Markdown `W01-ASM01.md` dengan metadata tugas/versi input, tabel/diagram beruraian teks, alasan keputusan, sumber yang dipakai, dan revisi/refleksi. Ini nama luaran yang direncanakan, belum file yang dibuat di repo. Hindari identitas/data mahasiswa dalam contoh yang disimpan di repo; bukti aktual memerlukan pengaturan yang terpisah.

Rubrik: [W01-RC01 dan W01-RC02](assessment-blueprint.md#w01); masing-masing mengukur W01-LO01 dan W01-LO02. Penilaian kualitatif usulan tidak menjadi skor nilai semester. Remediasi: Ulangi satu kartu dengan tabel unit/fitur/target. Minta mahasiswa menunjuk bukti konteks bagi kategorinya; telaah ulang RC yang belum memadai.

## W02

**W02-ASM01 — Memo audit eksplorasi data (USULAN)**

- LO: W02-LO01 dan W02-LO02; kode baseline DAIML-Sub-CPMK102-1 (ekuivalensi resmi belum diperiksa).
- Tujuan/indikator: membuat profil tipe data, missingness, distribusi dan dugaan duplikasi; membedakan observasi data dari hipotesis penyebab dan memilih pemeriksaan lanjutan.
- Prasyarat: W01 unit/fitur/target; pembacaan frekuensi dan grafik. Dosen menyediakan jalur tabel/visual untuk mahasiswa yang memerlukan bridge sintaks.
- Input/sumber daya: Dataset sintetis W02-EX01 beserta data dictionary, tujuan kasus dan definisi pemeriksaan. Sumber/versi dataset dan tabel/visual harus tersedia serta diperiksa sebelum tugas diterapkan.
- Estimasi usaha mandiri: **USULAN 60–90 menit**, belum diuji pada mahasiswa; bukan durasi kelas resmi. Waktu pelaksanaan, tenggat, kanal dan bobot resmi PERLU KONFIRMASI SUMBER.

Langkah yang diusulkan:

1. Nyatakan unit observasi, kolom, tipe, satuan dan ruang lingkup data; jangan membuat definisi yang tidak diberikan.
2. Periksa missingness, distribusi dan dugaan duplikasi; catat cara pemeriksaan serta bagian data yang mendukungnya.
3. Pilih satu visual yang menjawab pertanyaan eksplisit; beri anotasi dan alternatif uraian teks.
4. Buat memo dengan bagian observasi, dugaan penyebab, keputusan sementara dan pemeriksaan/data tambahan.
5. Tunjukkan temuan yang relevan untuk preprocessing W03 dan revisi klaim yang melampaui bukti.

Luaran W02-EV01: Data dictionary/profil, satu visual beranotasi atau uraian setara, memo empat bagian dan daftar risiko. Tidak mengisi angka profil dari perkiraan.

Format **USULAN**: naskah Markdown `W02-ASM01.md` dengan metadata tugas/versi input, tabel/diagram beruraian teks, alasan keputusan, sumber yang dipakai, dan revisi/refleksi. Ini nama luaran yang direncanakan, belum file yang dibuat di repo. Hindari identitas/data mahasiswa dalam contoh yang disimpan di repo; bukti aktual memerlukan pengaturan yang terpisah.

Rubrik: [W02-RC01 dan W02-RC02](assessment-blueprint.md#w02); masing-masing mengukur W02-LO01 dan W02-LO02. Penilaian kualitatif usulan tidak menjadi skor nilai semester. Remediasi: Kembali ke satu kolom/visual dan bedakan kalimat observasi dari hipotesis. Perbaiki definisi duplikasi/ruang lingkup pemeriksaan, lalu kirim ulang bagian terkait.

## W03

**W03-ASM01 — Peta transformasi dan trace fit/transform (USULAN)**

- LO: W03-LO01 dan W03-LO02; kode baseline DAIML-Sub-CPMK102-1 (ekuivalensi resmi belum diperiksa).
- Tujuan/indikator: memilih transformasi berdasarkan tipe fitur dan kebutuhan model; menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru.
- Prasyarat: W02 tipe, missingness dan skala; W01 makna data baru saat prediksi; materi W03 tentang pilihan transformasi dan parameter yang dipelajari.
- Input/sumber daya: Kasus mixed-type W03-EX01 dan temuan audit W02, serta skenario data baru dengan kategori/nilai hilang. Input/kontrak API harus diperiksa pada produksi DATA/LAB; belum tersedia sekarang.
- Estimasi usaha mandiri: **USULAN 60–90 menit**, belum diuji pada mahasiswa; bukan durasi kelas resmi. Waktu pelaksanaan, tenggat, kanal dan bobot resmi PERLU KONFIRMASI SUMBER.

Langkah yang diusulkan:

1. Daftar fitur, tipe dan masalah data yang ditopang temuan audit; pisahkan temuan dari asumsi.
2. Usulkan transformasi per fitur beserta alasan dan batas penerapannya.
3. Gambar atau tulis trace: input training → fit parameter → transform training/data baru; tunjukkan asal setiap parameter yang dipelajari.
4. Jelaskan perlakuan kategori baru/nilai hilang dari stimulus; nyatakan perilaku yang perlu diuji dengan kode.
5. Tinjau apakah ada data evaluasi masuk ke fit dan perbaiki trace. Jika kode belum dijalankan, jangan menulis hasil run.

Luaran W03-EV01: Peta fitur–transformasi–alasan, trace fit/transform, catatan kategori baru dan batas parameter. Hasil kode hanya dilampirkan jika benar-benar dijalankan.

Format **USULAN**: naskah Markdown `W03-ASM01.md` dengan metadata tugas/versi input, tabel/diagram beruraian teks, alasan keputusan, sumber yang dipakai, dan revisi/refleksi. Ini nama luaran yang direncanakan, belum file yang dibuat di repo. Hindari identitas/data mahasiswa dalam contoh yang disimpan di repo; bukti aktual memerlukan pengaturan yang terpisah.

Rubrik: [W03-RC01 dan W03-RC02](assessment-blueprint.md#w03); masing-masing mengukur W03-LO01 dan W03-LO02. Penilaian kualitatif usulan tidak menjadi skor nilai semester. Remediasi: Pilih satu transformasi dan telusuri parameter dari baris training sampai data baru. Perbaiki alasan dan trace sebelum mengulang keseluruhan prosedur.

## W04

**W04-ASM01 — Audit rancangan evaluasi dan leakage (USULAN)**

- LO: W04-LO01 dan W04-LO02; kode baseline DAIML-Sub-CPMK102-1 (ekuivalensi resmi belum diperiksa).
- Tujuan/indikator: memilih strategi split/CV sesuai tujuan prediksi, unit independen, kelompok dan waktu; mendeteksi leakage dan merancang batas fit serta penggunaan test.
- Prasyarat: W01 problem framing, W02 struktur/unit data, W03 fit/transform. Pilot W04 memakai bridge prasyarat karena paket W01–W03 belum ada; jangan menganggap pengalaman mahasiswa sudah terbukti.
- Input/sumber daya: Tiga skenario W04-EX01/EX02/EX03 (data biasa, catatan berkelompok, urutan waktu) dan rancangan cacat W04-EX04. Dosen harus menyediakan tujuan deployment, unit, kelompok/waktu dan diagram yang cukup; dataset/trace belum diproduksi.
- Estimasi usaha mandiri: **USULAN 90–120 menit**, belum diuji pada mahasiswa; bukan durasi kelas resmi. Waktu pelaksanaan, tenggat, kanal dan bobot resmi PERLU KONFIRMASI SUMBER.

Langkah yang diusulkan:

1. Tulis tujuan prediksi, unit evaluasi dan struktur kelompok/waktu untuk masing-masing dari tiga skenario.
2. Pilih strategi split/validasi dan berikan alasan; jelaskan alternatif bila tujuan deployment berubah.
3. Audit rancangan cacat: tandai tahap yang memakai data di luar batas yang direncanakan dan jelaskan dampak terhadap klaim.
4. Usulkan perbaikan melalui diagram training/pengembangan/test; tandai lokasi fit transformasi, tuning dan evaluasi.
5. Tulis trace indeks/fold yang perlu diperiksa pada LAB: keterpisahan indeks, kelompok/waktu yang relevan dan asal parameter. Jangan mengarang nilai skor.
6. Tulis memo batas klaim: test yang pernah dibuka pada demo tidak dipakai lagi sebagai bukti final independen; hasil run dibedakan dari hipotesis.

Luaran W04-EV01: Matriks tiga skenario, diagram prosedur yang diperbaiki, trace/checklist indeks/fold dan memo batas klaim. Angka run hanya jika tersedia dari eksekusi terverifikasi.

Format **USULAN**: naskah Markdown `W04-ASM01.md` dengan metadata tugas/versi input, tabel/diagram beruraian teks, alasan keputusan, sumber yang dipakai, dan revisi/refleksi. Ini nama luaran yang direncanakan, belum file yang dibuat di repo. Hindari identitas/data mahasiswa dalam contoh yang disimpan di repo; bukti aktual memerlukan pengaturan yang terpisah.

Rubrik: [W04-RC01 dan W04-RC02](assessment-blueprint.md#w04); masing-masing mengukur W04-LO01 dan W04-LO02. Penilaian kualitatif usulan tidak menjadi skor nilai semester. Remediasi: Ulangi satu skenario dengan pertanyaan tujuan–unit–waktu, lalu telusuri satu parameter dari training fold. Telaah ulang rancangan yang masih memakai test untuk pengembangan.

## Bagian B — Ketentuan dan implementasi dosen

### AI, kolaborasi dan bantuan — PERLU KONFIRMASI SUMBER

Ketentuan resmi penggunaan AI, kerja individu/kelompok, atribusi, batas bantuan dan sanksi belum tersedia dari S02/S03. Rancangan pedagogi **USULAN** menyediakan jalur tanpa layanan AI berbayar, meminta alasan yang dapat dipertanggungjawabkan dan mencatat bantuan/sumber bila dipakai. Ini tidak mengizinkan penggunaan AI pada ujian/tugas resmi dan tidak menetapkan sanksi. Dosen harus menetapkan aturan yang benar-benar bersumber sebelum asesmen dinilai.

### Alur implementasi dan umpan balik — USULAN

1. Pastikan bahan ajar, stimulus, data dictionary, versi input dan sumber teknis tersedia; jalankan G2/G3/G4 pada paket yang diproduksi kemudian.
2. Selaraskan empat brief dengan S02/S03, termasuk task resmi T-04; tentukan jenis tugas, kanal, tenggat, akses dan bobot dari sumber yang berlaku.
3. Berikan instruksi mahasiswa tanpa catatan dosen/kunci. Jelaskan dua kriteria tiap tugas sebelum pengumpulan.
4. Telaah bukti per LO dengan rubrik; catat bagian bukti yang mendukung keputusan, data yang belum tersedia dan perbaikan spesifik.
5. Beri kesempatan revisi sebagai usulan pembelajaran; kebijakan penilaian ulang resmi masih menunggu sumber. Simpan versi awal/revisi bila izin/kanal sudah ditetapkan.
6. Kalibrasi rubrik memakai jawaban alternatif dan kualitas bukti setelah stimulus tersedia. Kalibrasi mahasiswa/penilai belum dijalankan pada P05.

### Slot semester selanjutnya — belum tugas operasional

| Slot | Topik baseline | Hubungan rencana | Status |
| --- | --- | --- | --- |
| W05 | Klasifikasi I: KNN dan Decision Tree | W05-LO01: membandingkan kandidat klasifikasi dengan alasan yang sesuai data | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W06 | Regresi Linear dan Metrik Evaluasi | W06-LO01: memilih evaluasi target numerik dan menafsirkan hasilnya | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W07 | Clustering dan Metrik Clustering | W07-LO01: menafsirkan hasil pengelompokan dan batas evaluasinya | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W08 | UTS | UTS-LO01: menunjukkan integrasi kemampuan fondasi W01–W07 | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W09 | Klasifikasi II dan Model Selection | W09-LO01: memilih kandidat model melalui protokol validasi | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W10 | Generalisasi, Overfitting, dan Regularisasi | W10-LO01: menganalisis diagnosis generalisasi dan pilihan perbaikan | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W11 | Jaringan Syaraf Tiruan | W11-LO01: menjelaskan alur jaringan sederhana dan rancangan evaluasi | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W12 | Pengantar Deep Learning dan Generative AI | W12-LO01: membandingkan penggunaan DL/GenAI beserta batasnya | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W13 | Responsible AI | W13-LO01: menganalisis risiko dan mitigasi pada kasus AI | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W14 | Pipeline ML End-to-End dan Reproduksibilitas | W14-LO01: merancang paket ML yang dapat direproduksi | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W15 | Presentasi Proyek Akhir | W15-LO01: mengomunikasikan bukti dan keterbatasan proyek | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |
| W16 | UAS | UAS-LO01: menunjukkan integrasi capaian akhir sesuai scope yang ditetapkan kelak | DEFERRED; hanya slot governance, instruksi/luaran rinci belum diproduksi |

Katalog operasional usulan batch ini hanya empat brief W01–W04. Slot W05–W16 tidak diberi klaim 100% tugas siap, bobot, tenggat atau stimulus rekaan. SEM-07/UTS/UAS dan rincian tugas selanjutnya menunggu batch terpisah serta sumber resmi.

## Pemenuhan dan gate

SEM-03 DRAFT/DRAFT/PARTIAL: empat brief mempunyai input, langkah dan luaran yang direncanakan, tetapi input/soal/solusi belum dibuat atau diuji. DoD asli meminta seluruh tugas operasional dan selaras RPS; hal itu belum terpenuhi. G4 pada konsistensi desain fokus diperiksa, sedangkan uji penyelesaian stimulus, kalibrasi penilai dan aturan resmi belum terpenuhi. Tidak ada data pengerjaan atau hasil kelas.

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
