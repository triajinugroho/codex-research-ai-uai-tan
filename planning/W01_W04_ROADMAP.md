# Jalur Produksi sampai Pekan 1–4 Siap dalam Markdown

Fokus aktif: **W01, W02, W03, W04**. Ini panduan langkah berikutnya sesuai sasaran pengguna; belum menjalankan prompt produksi.

## 1. Sasaran dan arti siap

Target utama adalah **56 artefak mingguan: 4 pekan × 14 artefak**, beserta indeks mahasiswa/dosen, kendali produksi, sumber, dan laporan pemeriksaan. Artefak fondasi/helper tidak menambah denominator 56.

“Siap Markdown” berarti `markdown_readiness: VALIDATED` pada scope yang dinyatakan: isi substantif, sumber klaim inti memadai, praktik penting diuji, soal/kunci cocok, tautan dan dependensi konsisten, serta temuan material ditutup. Tetap bedakan:

- Naskah slide siap bukan deck visual yang sudah dirender.
- Lab Markdown dengan kode teruji bukan notebook terbit.
- Paket LMS siap adalah teks dan petunjuk implementasi, bukan LMS yang sudah diisi.
- EVID/QA siap adalah spesifikasi dan instrumen; bukti mahasiswa/analisis pascakelas menunggu pelaksanaan.
- Jika RPS/RTM/kurikulum belum dibaca, keselarasan/kebijakan resmi tetap PROVISIONAL. Jangan menyebut tugas/rubrik resmi disahkan. Sumber inti teknis yang belum mendukung klaim akan menahan validasi scope terkait.

Untuk semua keputusan status, gunakan [spesifikasi](ARTIFACT_SPECS.md) dan [gate mutu](QUALITY_GATES.md). `production.repo_status` tetap menilai DoD asli dan `fulfillment` mencatat pemenuhan sebenarnya; readiness Markdown tidak menimpa keduanya.

## 2. Langkah dan prompt

| Urutan | Prompt | Penalaran | Hasil yang dituju |
| --- | --- | --- | --- |
| 1 | P02 | Sedang | Kendali produksi: seluruh 222 ID tetap terimpor, 56 item W01–W04 ditandai sebagai fokus aktif |
| 2 | P03 | Tinggi | Register sumber, gap kurikulum/RPS/RTM/materi lama, konflik, dan sumber teknis yang benar-benar tersedia |
| 3 | P05 | Tinggi | SEM-01–04 sebagai audit/rancangan tata kelola; final resmi hanya jika sumber mendukung |
| 4 | P04 | Tinggi | Peta belajar, TOC, standar, dan template; rincian produksi difokuskan W01–W04 |
| 5 | P20, TARGET_IDS=SEM-08/09/10 | Sedang untuk scaffold yang deterministik; tinggi untuk keputusan mastery/asesmen | Kerangka LMS, mastery, dan bank soal yang diperlukan paket awal; diisi bertahap dari butir yang diperiksa |
| 6 | P21 per batch W04 | Sesuai tabel batch | Pilot 14 artefak lengkap; review dan koreksi pola sebelum dipakai ulang |
| 7 | P21 per batch W01, lalu W02, lalu W03 | Sesuai tabel batch | Paket lengkap pekan awal; gunakan pola pilot yang sudah diperiksa |
| 8 | P15/P16 untuk W04 dan sambungan W01–W04; refresh P20 subset yang perlu | Tinggi; sedang untuk koreksi rutin | Sesuaikan pilot dengan prasyarat yang kini benar-benar tersedia; tutup inkonsistensi; isi bank dari soal/kunci terverifikasi |
| 9 | P17 dengan TARGET_IDS=56 ID W01–W04 | Tinggi | Integrasi paket awal dan fondasi pendukungnya, indeks, dashboard, serta laporan kesiapan 56 artefak |

P00 tidak wajib karena repo dan rencana sudah diketahui. P02 tetap diperlukan: baseline di `planning/` adalah snapshot, sedangkan kendali produksi berjalan belum dibuat.

Pertahankan struktur semester penuh sebagai konteks. W05–W16 dan SEM-07 proyek tidak menjadi target produksi isi pada fase ini. Jangan menghapus item lain dari baseline, membuatnya READY, atau mereset status yang sudah ada. P20 pada langkah 5 membuat struktur pendukung; bank soal tetap DRAFT sampai butir/kunci nyata W01–W04 selesai diperiksa, sedangkan tracker belum berisi bukti mastery mahasiswa. Perbarui subset pendukung lewat P20 setelah produksi W01–W04. Pembacaan blueprint W12–W15 pada prompt P20 bukan instruksi memproduksi proyek.

P17 pada langkah 9 memeriksa isi nyata 56 artefak aktif dan fondasi yang dipakai. Inventaris seluruh 222 ID tetap diperiksa, tetapi konten/transisi W05 sampai UAS yang belum diproduksi berada di luar pemeriksaan kesiapan fase ini. Kebutuhan semester selanjutnya dicatat sebagai planned, bukan blocker buatan bagi materi awal yang sudah memenuhi scope-nya.

Urutan **W04 → W01 → W02 → W03** mengikuti prioritas workbook dan rencana pilot. Urutan belajar mahasiswa tetap W01 → W02 → W03 → W04. Pilot memakai bridge prasyarat di scope/bab W04; bridge itu bukan pengganti tiga paket awal.

## 3. Prompt pertama: P02

Pilih penalaran sedang di antarmuka, lalu salin:

```text
Mulai produksi fondasi pada repo /workspace/codex-research-ai-uai-tan.
Baca planning/W01_W04_ROADMAP.md dan planning/PROMPT_LIBRARY.md.
Terapkan Kontrak Universal V1 dan jalankan hanya P02.

Sasaran fase ini: seluruh bahan W01–W04 siap dalam Markdown, 56 artefak utama.
Impor tetap seluruh 222 ID dari workbook asli; tandai W01–W04 sebagai fokus aktif
di dashboard tanpa mengubah status/prioritas baseline sumber.
Verifikasi workbook terhadap planning/WORKBOOK_BASELINE.md dan file aktual.

Simpan course/production/semester-backlog.md, weekly-backlog.md, dashboard.md,
serta ticket, laporan validasi, dan handoff di course/production/reports/ dengan
RUN unik. Gunakan schema ARTIFACT_SPECS; pisahkan source_status,
production.repo_status, markdown_readiness, fulfillment dan blocker.
Verifikasi 222 ID unik, 56 ID fokus dan pemetaan path yang benar.

Berhenti setelah P02. Belum menulis bahan mingguan atau menjalankan prompt berikut.
Di handoff, berikan instruksi siap salin untuk P03 dengan penalaran tinggi.
Jangan commit/push, mengubah sumber asli, atau memublikasikan.
```

## 4. Fondasi setelah P02

Gunakan wrapper yang sama untuk satu prompt berikutnya dan ganti ID. Setiap hasil harus memberi handoff/prompt lanjutan dengan input aktual; jangan mengisi RUN, hasil pemeriksaan, atau path handoff secara fiktif.

```text
Lanjutkan fondasi untuk sasaran W01–W04.
Baca handoff aktual dari batch sebelumnya dan planning/W01_W04_ROADMAP.md.
Terapkan Kontrak Universal V1 dari planning/PROMPT_LIBRARY.md, jalankan hanya [P03].
Gunakan penalaran tinggi yang dipilih di antarmuka. Tetapkan read/write set konkret.
Selesaikan keluaran prompt itu, laporkan sumber yang dibaca dan blocker,
lalu simpan handoff dengan next prompt. Jangan lanjut otomatis ke batch berikut.
```

Urutan pengganti `[P03]` pada sesi berikut adalah **P03 → P05 → P04**. Untuk P20, tambahkan `TARGET_IDS=[SEM-08, SEM-09, SEM-10]` dan fokuskan detail struktur pendukung ke W01–W04. SEM-08 tetap mempunyai kerangka 16 minggu; halaman minggu lain sebatas slot planned, bukan produksi isinya.

Jika sumber resmi belum tersedia, selesaikan bagian independen sebagai rancangan, daftarkan gap spesifik, dan lanjutkan paket teknis/pedagogi yang mempunyai dukungan. Finalisasi kebijakan dan keselarasan resmi dilakukan setelah sumber tersedia, memakai P18 untuk dampak dan P16 untuk revisi terarah jika diperlukan.

## 5. Batch untuk setiap pekan

| Batch | Isi | Penalaran | Keluaran utama |
| --- | --- | --- | --- |
| A | Scope + bab | Tinggi | BOOK dan helper scope |
| B | Jalur mahasiswa + panduan dosen | Sedang | MOD, GUIDE |
| C1 | Kasus/dataset + lab | Tinggi | DATA, LAB; kode solusi dan perilaku penting diuji |
| C2 | Worksheet + prompt belajar AI | Sedang; tinggi jika konsep baru | WORK, AIP |
| D | Tugas/kuis + kunci/rubrik | Tinggi | ASSESS, RUBRIC |
| E1 | Storyboard | Tinggi | STORY; audit isi sebelum E2 |
| E2 | Naskah slide | Sedang | SLIDE, berasal dari storyboard yang diperiksa |
| F | Teks LMS + spesifikasi bukti + QA | Sedang | LMS, EVID, QA dan indeks |
| R | Review dan revisi terarah | Tinggi | Laporan; revisi hanya file temuan dalam scope; handoff |

Satu pekan memiliki 14 artefak meskipun terdapat 9 batch. Review R tidak menambah artefak utama. Batch dapat dipecah jika terlalu panjang; jangan membuat semua file sekaligus dengan isi dangkal.

Contoh awal pilot setelah fondasi minimum:

```text
Produksi W04 batch A pada /workspace/codex-research-ai-uai-tan.
Baca planning/W01_W04_ROADMAP.md dan planning/PROMPT_LIBRARY.md.
Terapkan Kontrak Universal V1 + P21. WEEK=W04, BATCH=A.
Gunakan penalaran tinggi yang dipilih di antarmuka.
Kerjakan course/weeks/w04/scope.md dan book-chapter.md secara substantif;
scope boleh memuat bridge prasyarat W01–W03 tanpa mengedit folder minggu lain.
Tambahkan index.md bila diperlukan untuk navigasi file yang telah ada dan
laporan ticket/validasi/handoff dengan RUN unik sesuai P21.
Fokus split, validasi, cross-validation, leakage dan pipeline sesuai blueprint.
Periksa substansi, hitungan, sumber dan batas klaim. Tandai gap resmi.
Berhenti setelah A; berikan next prompt B dengan read/write set konkret.
```

Untuk sesi berikutnya, gunakan P01/P21 dengan WEEK dan BATCH yang tepat serta path handoff nyata. Ulangi A→B→C1→C2→D→E1→E2→F→R untuk W04, W01, W02, W03. Setiap laporan harus menunjuk tahap terkecil berikutnya, bukan menganggap batch lain sudah selesai.

## 6. Checklist keluar: W01–W04 siap Markdown

1. Ada 56 ID utama dengan isi sesuai peran, metadata, sumber, dan catatan validasi; helper tidak dihitung sebagai materi tambahan.
2. Paket mahasiswa dan dosen mempunyai navigasi yang dapat digunakan. Kunci/solusi tidak masuk paket yang dibagikan kepada mahasiswa; label/folder bukan kontrol akses repo.
3. Bab, modul, panduan, lab, worksheet, asesmen, rubric, storyboard, dan naskah memakai tujuan/istilah/angka yang konsisten.
4. Kode penting benar-benar dijalankan dan hasilnya tercatat; soal/kunci/rubrik diperiksa. Pemeriksaan UNRUN/FAIL tidak disulap menjadi PASS.
5. Pengantar → data → preprocessing → validasi tersambung. Data test yang telah terekspos pada demo tidak dianggap holdout final baru setelah pengembangan berikutnya.
6. Gate relevan terpenuhi pada scope yang dinyatakan; sumber resmi yang belum terverifikasi dan kebutuhan pelaksanaan tetap terlihat.
7. Setiap item dinilai terpisah: VALIDATED pada Markdown, PROVISIONAL/VERIFIED_AGAINST_SOURCE pada keselarasan resmi, serta NOT_FULFILLED/PARTIAL/FULFILLED pada DoD asli.
8. Dashboard melaporkan kesiapan fokus **x/56** dan inventaris semester **222** secara terpisah. Tidak menyebut seluruh semester sudah selesai.

Setelah checklist ini, pengguna dapat memutuskan finalisasi sumber akademik, produksi format visual/notebook, implementasi LMS, atau perluasan ke pekan berikutnya. Langkah itu tidak otomatis dijalankan oleh roadmap ini.
