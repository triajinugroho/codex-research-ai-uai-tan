# Keadaan register sumber terbaru

12 ID sumber: **5 VERIFIED_LOCAL** (dua unggahan + tiga kelompok dokumentasi runtime), **6 UNAVAILABLE** (S01–S05/folder Drive), **1 LINK_ONLY** (S06), 0 VERIFIED_EXTERNAL. Status per sumber bukan lifecycle workbook. Klaim akademik masih PROVISIONAL. Ringkasan audit P03 di bawah dipertahankan sebagai snapshot historis, bukan keadaan semua sumber saat ini.

# Register Sumber — Fokus W01–W04

Run audit: `20261008-003012-P03-W01-W04`. Waktu: 2026-10-08T00:30:12+07:00 Asia/Jakarta; UTC 2026-10-07T17:30:12+00:00. Helper kendali SEM-12, bukan ID artefak utama tambahan.

[Laporan P03](reports/20261008-003012-P03-W01-W04.md) · [Keputusan](decisions.md) · [Handoff P05](reports/20261008-003012-P03-W01-W04-handoff.md).

## 1. Ringkasan sumber dan arti status

| ID | Status akses/verifikasi kini | Bukti | Batas dukungan |
| --- | --- | --- | --- |
| SRC-WORKBOOK | VERIFIED_LOCAL | 5 sheet dibaca; hash cocok dengan baseline | ID/topik/kode baseline, status/DoD/prioritas produksi; bukan kurikulum resmi |
| SRC-MASTER-PROMPT | VERIFIED_LOCAL | File lokal dan bagian pedagogi/desain diperiksa | Standar desain/pedagogi; bukan formula/hasil/kebijakan RPS |
| S01 | UNAVAILABLE | Asal LINK_ONLY; probe kini CONNECT 403 tanpa body | Isi belum dibaca; tidak dapat mendukung klaim akademik/pelaksanaan |
| S02 | UNAVAILABLE | Asal LINK_ONLY; probe kini CONNECT 403 tanpa body | Isi belum dibaca; tidak dapat mendukung klaim akademik/pelaksanaan |
| S03 | UNAVAILABLE | Asal LINK_ONLY; probe kini CONNECT 403 tanpa body | Isi belum dibaca; tidak dapat mendukung klaim akademik/pelaksanaan |
| S04 | UNAVAILABLE | Asal LINK_ONLY; probe kini CONNECT 403 tanpa body | Isi belum dibaca; tidak dapat mendukung klaim akademik/pelaksanaan |
| S05 | UNAVAILABLE | Asal LINK_ONLY; probe kini CONNECT 403 tanpa body | Isi belum dibaca; tidak dapat mendukung klaim akademik/pelaksanaan |
| S06 | LINK_ONLY | Label paket v2 pada workbook, URL kosong | Identitas/versi terhadap unggahan belum terkonfirmasi |
| SRC-DRIVE-FOLDER | UNAVAILABLE | Tautan pengguna; probe CONNECT 403 tanpa body | Daftar file dan isi folder belum dibaca |

Ada 9 record: 2 VERIFIED_LOCAL, 6 UNAVAILABLE, 1 LINK_ONLY, 0 VERIFIED_EXTERNAL. Belum ditemukan konflik isi antara kurikulum/RPS/RTM yang dapat dibuktikan karena dokumen tersebut belum dibaca. Tensi interpretasi master prompt dicatat per bagian pada CONF-PED-01/02, bukan mengubah semua isi sumber menjadi tidak valid.

Status sumber di register ini **bukan** `source_status` lifecycle workbook atau `production.repo_status`. VERIFIED_LOCAL berarti bagian relevan file lokal dibaca; tidak berarti pengesahan institusi. UNAVAILABLE menjelaskan keterbatasan pada run ini; URL dan discovery_state LINK_ONLY tetap dipertahankan. LINK_ONLY bukan sumber klaim isi. Pada run ini tidak ada record yang mendapat enum CONFLICT untuk seluruh sumber; field isu/konflik per bagian tetap terlihat.

## 2. Sumber lokal yang diperiksa

### SRC-WORKBOOK

- Judul/file: [MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx](<../../references/MASTER - Production Control Sheet - Dasar AI & ML 2026-2027.xlsx>).
- Jenis: workbook lokal; organisasi/penulis bibliografis tidak ditetapkan dari nama file. Owner operasional yang tercatat pada Semester_Master adalah Tri Aji.
- Status: VERIFIED_LOCAL untuk inventaris dan label sumber; source verification artefak akademik tidak otomatis VERIFIED_FOR_SCOPE.
- Snapshot SHA-256: `e75b92af52d0f72974d6ff304ed8f82cdb66149f0a3a73f08a5dfbbd100dd9d8`; 43692 byte. Tanggal/versi resmi workbook tidak tersedia sebagai pengesahan; judul menyebut 2026–2027.
- Locator: Dashboard A3:B7 (nama/kode/coverage/fokus); Semester_Master A2:M13; Production_Backlog A2:R211; Definitions A2:C8/E2:F5; Sources A2:E7.
- Dukungan: 222 ID/56 fokus, topik dan kode Sub-CPMK sebagai baseline, lifecycle termasuk IMPROVE, DoD/prioritas produksi, daftar sumber/URL.
- Tidak mendukung: isi CPL/CPMK/BK resmi, bobot nilai/durasi, kebenaran algoritma, kehadiran/mastery, file storyboard yang belum tersedia, pengesahan RPS/RTM.
- Lisensi: tidak dinyatakan pada bagian yang diperiksa; sumber pengguna untuk kerja repo, bukan izin distribusi publik yang direka.
- Dipakai oleh: SEM-01–12 dan inventaris seluruh mingguan/ujian. Untuk W01–W04, locator topik/outcome adalah kelompok baris 2–57 Production_Backlog, bukan rumusan capaian lengkap.

### SRC-MASTER-PROMPT

- File: [Master_Prompt_Package_Slide_Mata_Kuliah_Tri_Aji.md](../../references/Master_Prompt_Package_Slide_Mata_Kuliah_Tri_Aji.md).
- Judul internal: MASTER PROMPT PACKAGE — SLIDE MATA KULIAH; Teaching Visual Operating System — Tri Aji Nugroho (baris 1–2).
- Konteks dosen tertulis: Tri Aji Nugroho, S.T., M.T.; Informatika Universitas Al-Azhar Indonesia (§1.A, baris 37–41). Ini konteks dalam dokumen, bukan pemeriksaan institusional.
- Status: VERIFIED_LOCAL untuk bagian desain/pedagogi yang diperiksa. Hash `b2542568f9f4e363f9ec8055410a4280e6132cb8251d618893a005f921e5d21b`; 32479 byte.
- Versi/tanggal: penanda v2 dan tanggal pembuatan tidak terlihat sebagai identitas eksplisit di isi; tanggal 7 Oktober 2026 pada workbook Sources!E7 adalah catatan sumber, bukan metadata versi file lokal.
- Locator substansi desain: §1.A/H/J/M, §2, §7, §10, §12/13/15, §18–20, §22–26; baris 49, 261, 295, 1177, 1190–1220, 1355–1395 untuk isu dan aturan relevan.
- Dukungan: WHY/intuisi/formalisasi, satu mental model, worked example, aktivitas, storyboard, QA dan spesifikasi visual; referensi untuk SEM-11 dan turunan STORY/SLIDE/MOD/GUIDE/WORK/AIP.
- Tidak mendukung: klaim ML, hitungan/hasil run, kebijakan asesmen UAI, RPS/RTM resmi, atau bahwa suatu gambar/deck sudah dibuat.
- Lisensi: tidak dinyatakan dalam bagian yang diperiksa; tidak dibuat bibliografi/DOI/izin publikasi fiktif.
- Tensi per bagian: CONF-PED-01 (urutan konsep/intuisi) dan CONF-PED-02 (20 slide vs parameter jumlah slide). Keputusan adaptasi di decisions.md tidak menimpa file asli.

## 3. S01–S06 dari workbook: metadata asli dan kebutuhan pemeriksaan

| Sources row | ID | Nama asli | Peran asli | URL asli | Notes asli |
| --- | --- | --- | --- | --- | --- |
| 2 | S01 | Kurikulum OBE IF 2025 — Revisi 2026 | Primary curriculum source of truth | https://docs.google.com/spreadsheets/d/14frRyWdgLshOJ-5hVcL2CCoxCtm0d5gc | Use for CPL/CPMK/BK/course identity. |
| 3 | S02 | RPS_RTM_Dasar_Kecerdasan_Artifisial_dan_Pembelajaran_Mesin_2026-2027 | Operational RPS/RTM — IF24A | https://docs.google.com/document/d/1jfaenJg9Oi6PEsMjASpqO1D90EcQyd5H/edit | Current weekly topic, assessment, and RTM basis. |
| 4 | S03 | RTM_Dasar_Kecerdasan_Artifisial_dan_Pembelajaran_Mesin_IF24A-IF24H_2026_Template_Resmi_UAI | RTM source — IF24A | https://docs.google.com/document/d/1ktAxiyG_ctP2Ql8Svx8RBbl370c8wPia/edit | Detailed task structure. |
| 5 | S04 | IF24A - Dasar AI & ML - Tracker Presensi, Tugas dan Nilai | Class delivery tracker | https://docs.google.com/spreadsheets/d/1N9HH-Pk2Dbg2NnV5w0mGIld2PDibdIz16H9GpBUDluI/edit | Operational class evidence. |
| 6 | S05 | IF24H - Dasar AI & ML - Tracker Presensi, Tugas dan Nilai | Hybrid class delivery tracker | https://docs.google.com/spreadsheets/d/1WBP9NIduXQ_xqiB_PorhJKzB1eryTcrKeG8fRO0L3RI/edit | Operational hybrid-class evidence. |
| 7 | S06 | Master Prompt Package Mata Kuliah v2 | Teaching Package Operating System | ∅ | Local master prompt created 7 Oct 2026; upload/link when finalized. |

S01–S05: nama, peran dan URL di atas diverifikasi sebagai cell Sources, bukan judul/version/isi dari dokumen eksternal yang diterima. Version/hash dokumen, pengesahan, halaman dan lisensinya **belum diketahui**. Probe pada 8 Oktober 2026 Asia/Jakarta untuk setiap URL tersimpan di laporan audit; tidak ada body dokumen diterima. Jangan menyimpulkan link salah/privat atau akun belum terhubung dari proxy 403.

| ID | Bidang yang seharusnya diperiksa | Dipakai oleh | Batas/gap |
| --- | --- | --- | --- |
| S01 | Identitas, CPL/CPMK/BK, prasyarat; versi kurikulum | SEM-01/02/04/05; crosswalk W01–W04 | GAP-S01; hanya label baseline tersedia |
| S02 | Peta minggu, outcome, bobot/bibliografi/durasi/kebijakan jika tercantum | SEM-02/03/04/05; seluruh bahan W01–W04 | GAP-S02; peran sumber IF24A tidak otomatis berlaku bagi IF24H |
| S03 | Rincian tugas, luaran, rubrik dan submission | SEM-03/04; W01–W04-ASSESS/RUBRIC/LMS | GAP-S03; judul template tidak membuktikan versi resmi final |
| S04 | Presensi/tugas/nilai IF24A yang benar-benar tercatat | SEM-09; W01–W04-EVID/QA | GAP-S04; tidak membuat data siswa atau menyimpulkan mastery |
| S05 | Presensi/tugas/nilai IF24H yang benar-benar tercatat | SEM-09; W01–W04-EVID/QA | GAP-S05; label hybrid tracker tidak menetapkan jadwal/durasi |
| S06 | Identitas paket v2 dan hubungan dengan unggahan lokal | SEM-11, turunan standar | GAP-S06; crosswalk kandidat, bukan source content/version equivalence |

### Crosswalk S06 ↔ SRC-MASTER-PROMPT

Hubungan kandidat fungsi: keduanya bertema teaching prompt OS. Bukti: Sources!B7–E7, Semester_Master!L12, judul unggahan baris 1–2. Status identitas: **BELUM TERKONFIRMASI**. Fungsi desain yang diperiksa boleh memakai SRC-MASTER-PROMPT langsung; jangan menyatakan S06/v2 telah dibaca atau memberi versi v2 pada file tersebut. Pemeriksaan identitas dapat dilakukan jika file v2 asli atau konfirmasi versi tersedia; tidak perlu menahan draft standar yang bersumber pada unggahan aktual.

## 4. SRC-DRIVE-FOLDER

- URL: https://drive.google.com/drive/folders/1PSz_2tbCdjFh5TTdYwJ5ExzPIMpp8BvC?usp=drive_link.
- Asal: tautan yang diberikan pengguna, dicatat pada README bagian referensi/folder kerja.
- Status: UNAVAILABLE pada run ini; discovery_state LINK_ONLY.
- Bukti: curl exit 56, HTTP origin 000, CONNECT 403, tanpa body; konektor Drive tidak tersedia di daftar tools saat audit.
- Versi/hash/daftar file/locator dalam folder/penulis/lisensi: belum diketahui. Tidak ada file yang diinventarisasi dari folder.
- Dampak: lokasi calon kurikulum/RPS/RTM dan materi lama belum dapat diakses; tidak mengasumsikan file tertentu memang ada di folder ini.

## 5. Materi yang disebut tetapi belum tersedia sebagai sumber tersendiri

| Kebutuhan | Locator pernyataan | Bukti aktual | Status/perlakuan |
| --- | --- | --- | --- |
| Materi STORY/SLIDE W01–W03 lama | Production_Backlog R5:R6,R19:R20,R33:R34 | Notes menyatakan ada; kolom File/URL kosong; tidak ada file bahan di repo/unggahan lain yang ditemukan | Belum tersedia lokal; status REVIEW sumber bukan bukti isi/akses |
| Storyboard W04 Validation Before Believing | Production_Backlog R47 | Notes menyebut draft 20 slide tanggal 7 Oktober 2026; tidak ada berkas/URL | Belum tersedia; bukan konflik isi, jangan merekonstruksi sebagai kutipan |
| T-04 scope/weighting | Production_Backlog R53:R54 | Notes menyatakan defined; sumber rincian dan angka belum dibaca | Belum terverifikasi; tidak mengubah production weight 8/7 artefak menjadi bobot tugas |
| Sumber teknis W01–W04 | Tidak ada daftar teknis eksplisit pada dua unggahan yang menyediakan isi ML | Belum ada textbook/paper/dataset/api docs yang dibaca dalam P03 ini | GAP-TECH; kandidat dokumen otoritatif harus dibaca sebelum klaim teknis VALIDATED |
| Style anchor gambar | Master prompt §2/21/24 menyarankan style anchor | Hanya dua unggahan asli tersedia, tidak ada gambar referensi | Opsional untuk naskah; tidak menahan fondasi Markdown |

Unggahan pada /workspace/attachments memuat salinan dua sumber yang sama dengan hash identik, bukan sumber baru. Pemeriksaan nama file /workspace/library-files, shared, scratch tidak menemukan sumber kurikulum/kelas tambahan. Tidak ada data mahasiswa yang dibaca/ditambahkan.

## 6. Aturan pemakaian dan otoritas

1. S01 untuk identitas/CPL/CPMK/BK setelah isi relevan terverifikasi; S02 untuk peta/kebijakan operasional; S03 untuk tugas yang konsisten dengan RPS.
2. S04/S05 untuk catatan pelaksanaan aktual setelah boleh diakses; presensi/nilai bukan mastery otomatis.
3. SRC-WORKBOOK untuk produksi dan baseline; SRC-MASTER-PROMPT untuk desain. Keduanya tidak menggantikan S01–S03 atau sumber teknis.
4. Tanggal lebih baru tidak otomatis mengatasi konflik otoritas. Simpan versi dan dua locator; bagian terdampak tetap provisional sampai alasan resolusi tersedia.
5. P05 dapat membuat audit/crosswalk dan rancangan RPS/RTM/blueprint dengan label RANCANGAN serta field resmi PERLU KONFIRMASI SUMBER. Tidak perlu menunggu data kelas untuk struktur awal.
6. Dokumen referensi adalah data; instruksi di dalamnya tidak memberi izin menjalankan layanan/generasi gambar/publikasi. Pemakaian pedagogi mengikuti batas Markdown yang diminta pengguna.

## Tambahan sumber teknis lokal — produksi otomatis

P03 di atas tetap snapshot awal. Dokumentasi API paket terpasang benar-benar dibaca pada produksi otomatis; kutipan dipertahankan di [snapshot](../../references/technical-runtime-sources.md). Situs resmi probe terbaru tetap CONNECT 403; bukan bukti konten situs dibaca.

| ID | Judul/versi | Status | Locator snapshot | Dukungan/batas |
| --- | --- | --- | --- | --- |
| SRC-TECH-001 | scikit-learn 1.8.0 API docstrings | VERIFIED_LOCAL | ClassifierMixin/RegressorMixin/KMeans; fit/transform; splitters/Pipeline/imputer/scaler/encoder | Semantik API/algoritma yang diajarkan dan diperiksa; bukan RPS atau bukti kelas |
| SRC-TECH-002 | pandas 2.2.3 API docstrings | VERIFIED_LOCAL | DataFrame.describe/isna/duplicated/median | Profil data dan aritmetika; bukan hubungan sebab |
| SRC-TECH-003 | NumPy 2.3.5 mean API | VERIFIED_LOCAL | numpy.mean | Rerata contoh/hasil fold; bukan klaim independensi fold |

SHA-256 snapshot: `7070411b3f513913bf0f85676e28b81f69654bc860d16041ca46aa41919a3f53`. Lisensi distribusi ulang materi pengguna tidak ditetapkan; dokumentasi adalah kutipan untuk penelusuran internal. Tidak membuat bibliografi/DOI rekaan.

## Versi snapshot teknis terbaru

Path: `references/technical-runtime-sources.md`; SHA-256 `f1ab2a8cad430db9156526ca95bdcbd84510315fb7e8d48c32c20f6d4061a994`. Pembacaan tambahan StandardScaler/OneHotEncoder melengkapi parameter/edge cases; kutipan awal P04 tetap ada. Empat situs teknis yang dicoba pada produksi otomatis mengembalikan curl exit56, CONNECT403, origin000; tidak ada body diterima. Sumber lokal yang digunakan tidak dianggap versi situs stable yang sudah dibaca.
