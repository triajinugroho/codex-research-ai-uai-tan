# Catatan Keputusan — Fondasi W01–W04

Run: `20261008-003012-P03-W01-W04`; 2026-10-08T00:30:12+07:00 Asia/Jakarta; UTC 2026-10-07T17:30:12+00:00. [Register sumber](sources.md) · [Laporan P03](reports/20261008-003012-P03-W01-W04.md).

Keputusan berikut mencatat aturan kerja dan adaptasi pada scope yang telah diberikan. ADOPTED_PROVISIONAL tidak berarti pengesahan akademik. VERIFIED dipakai hanya untuk fakta yang benar-benar diperiksa atau instruksi pengguna yang eksplisit.

## DEC-0001 — Inventaris tidak sama dengan kesiapan materi

- Status: VERIFIED pada scope inventaris/provenance.
- Bukti: P02 validation, workbook Sources/Definitions/Production_Backlog; tidak ada folder course/weeks/governance pada inspeksi P03.
- Keputusan: pertahankan 222 ID/56 fokus, source_status asli, production.repo_status/markdown_readiness/fulfillment terpisah. Source READY/REVIEW tidak diubah menjadi kesiapan bahan.
- Berlaku: SEM-12 dan kendali produksi seluruh item. Menggantikan: tidak ada.
- Dampak perubahan: bila sumber/target baru tersedia, nilai ulang versi dan bukti per item; jangan reset status lain.

## DEC-0002 — Otoritas sumber berdasarkan bidang fakta

- Status: ADOPTED_PROVISIONAL sebagai aturan provenance; sumber resmi masih belum dibaca.
- Bukti: Sources!C2:C7; planning/QUALITY_GATES.md §3.1.
- Keputusan: gunakan register sources.md §6; kurikulum/RPS/RTM berbeda fungsi dari workbook produksi/master prompt.
- Berlaku: SEM-01–04/05, semua LO/outcome/ketentuan W01–W04.
- Masih perlu: isi/versi/kesesuaian S01–S03 dan cakupan tiap kelas. Tidak membuat tanda tangan, SK, bobot, jam atau aturan AI.
- Dampak perubahan: audit per bidang; konflik yang nyata dicatat dengan dua locator dan artefak terdampak.

## DEC-0003 — P05 tetap menghasilkan rancangan substantif

- Status: ADOPTED_PROVISIONAL.
- Bukti: permintaan pengguna P03/P05; roadmap dan PROMPT_LIBRARY P05; probe akses S01–S03 yang belum menerima body.
- Keputusan: P05 menulis audit dan rancangan RPS/RTM/blueprint memakai topik/kode baseline serta tujuan lokal usulan; kebijakan resmi tetap PERLU KONFIRMASI SUMBER. Kelengkapan daftar field bukan verifikasi terhadap RPS asli.
- Berlaku: SEM-01/02/03/04. Masih perlu: kurikulum, RPS, RTM aktual yang dapat dibaca.
- Dampak: ketika dokumen diterima, gunakan P18/P16 atau ticket revisi sah untuk menyelaraskan; jangan mengesahkan usulan melalui keheningan pengguna.

## DEC-0004 — Identitas S06 belum setara file lokal

- Status: PROPOSED untuk crosswalk versi, VERIFIED untuk perbedaan label yang terbaca.
- Bukti: Sources!B7 dan E7; Semester_Master!L12; master prompt baris 1–2. Workbook menyebut v2; judul lokal tidak menetapkan v2.
- Keputusan: catat S06 LINK_ONLY dan SRC-MASTER-PROMPT VERIFIED_LOCAL terpisah; hubungan fungsi kandidat saja. Jangan memberi tag v2 atau tanggal resmi file yang tidak terbukti.
- Masih perlu: sumber v2 asli/konfirmasi identitas yang spesifik. Perbedaan nama bukan bukti isi berbeda atau konflik akademik.
- Berlaku: SEM-11, register sumber, semua turunan desain.

## DEC-0005 / CONF-PED-01 — Intuisi sebelum formalisasi

- Status: ADOPTED_PROVISIONAL, keputusan adaptasi pedagogi.
- Dua locator: master §1.A baris 49 “Concept → intuition...” dan §1.H baris 261 “ELI5 intuition first”; §20 baris 1190 dan seterusnya menempatkan WHY → INTUITION → CONCEPT. Ini variasi urutan dalam satu sumber, bukan perbedaan kurikulum.
- Keputusan: gunakan WHY → intuisi → definisi/konsep formal → mekanisme → contoh → praktik → refleksi, konsisten dengan rencana yang sudah ditetapkan. Bedakan mental model/analogi dari definisi formal.
- Berlaku: BOOK/MOD/GUIDE/STORY/SLIDE W01–W04; SEM-11 pada tahapnya.
- Batas: tidak mengedit sumber asli dan tidak mengklaim urutan wajib institusi. Variasi yang cocok dengan topik dapat diberi alasan pada scope.
- Dampak: reviewer memeriksa koherensi dan tidak memperlakukan kedua urutan sebagai dua prasyarat bertentangan.

## DEC-0006 / CONF-PED-02 — Dua puluh slide sebagai target desain, bukan kebijakan

- Status: ADOPTED_PROVISIONAL.
- Dua locator: master §20 baris 1177 meminta 20 slide; §2 baris 384–385 menyediakan NUMBER OF SLIDES variabel. PRODUCTION_PLAN §6 mengadaptasi sekitar 20 slide dan durasi belum diketahui.
- Keputusan: draft storyboard memakai target sekitar 20 slide sebagai awal, dengan perubahan beralasan oleh cakupan/aktivitas/durasi yang nanti diperiksa. Pertahankan worked example, miskonsepsi, aksi mahasiswa dan mastery penutup.
- Berlaku: W01–W04-STORY/SLIDE; template/SEM-11. Tidak membuat visual/deck pada P03.
- Masih perlu: durasi/moda kelas dan scope isi; perubahan jumlah bukan alasan menghilangkan konsep inti.

## DEC-0007 — Catatan materi lama bukan materi yang tersedia

- Status: VERIFIED untuk pernyataan ketersediaan lokal saat audit; isi materi lama masih belum terverifikasi.
- Bukti: Production_Backlog R5/6,R19/20,R33/34,R47,R53/54; File/URL kolom N kosong; hanya dua unggahan lokal.
- Keputusan: materi W01–W03 lama/storyboard W04/T-04 dicatat GAP; draft baru tidak disebut rekonstruksi resmi. Source REVIEW/DRAFT dipertahankan, belum memicu pemakaian isi yang tidak dibaca.
- Berlaku: seluruh 56 bahan; khusus STORY/SLIDE/ASSESS/RUBRIC.
- Dampak: bila materi lama tersedia, bandingkan konsep/urutan/angka, laporkan dampak, revisi bagian terkait tanpa menimpa keputusan semula diam-diam.

## DEC-0008 — Diagnosis jaringan dibatasi pada bukti probe

- Status: VERIFIED untuk enam probe; akses dokumen tetap belum terverifikasi.
- Bukti: laporan P03 mencatat curl exit 56, HTTP origin 000 dan CONNECT 403 tanpa body, bagi S01–S05 dan folder Drive.
- Keputusan: status UNAVAILABLE dengan sebab akses proxy; tidak menyebut izin Google, token hilang, ID salah, VPN rusak atau folder privat. Tidak meminta token/secret dan tidak mengubah konfigurasi jaringan dalam P03.
- Berlaku: register sumber eksternal. Masih perlu: akses domain yang diizinkan dan otorisasi akun bila nantinya diminta layanan, atau salinan ekspor lokal sumber.
- Dampak: retry saat ada perubahan state yang berarti; jangan loop request sama atau memakai cache kosong sebagai isi dokumen.

## DEC-0009 — Scope P03 berhenti pada audit

- Status: VERIFIED dari instruksi pengguna.
- Keputusan: hanya sources.md, decisions.md, ticket, laporan, handoff ditulis. Backlog/dashboard/P02/planning/references dipertahankan. Tidak menjalankan P05, menambah materi, mengunggah, commit atau push.
- Dampak: dashboard P02 masih berisi catatan “P03 belum dijalankan” pada snapshot lamanya. Laporan P03/register ini adalah bukti lebih baru; P05 dapat memperbarui kendali hanya jika tiga pathnya masuk ticket eksplisit. Tidak menganggap teks snapshot lama sebagai keadaan terbaru.
- Berlaku: sesi ini. Menggantikan: tidak ada.

## Tindak lanjut dan urutan

1. Jalankan P05 untuk SEM-01–04 sebagai rancangan, bukan pengesahan. Scope boleh mencakup delta kendali SEM-12 jika ditulis eksplisit.
2. S01–S03 lokal/akses yang bekerja diperlukan untuk finalisasi akademik; S04/S05 tidak perlu dipenuhi sebelum draft bahan pra-kelas.
3. Sumber teknis yang belum dibaca harus dipenuhi sebelum klaim teknis contoh/formula/lab ditandai terverifikasi. P03 ini tidak menyediakan bukti algoritma atau runtime ML.
4. P04 dan pilot W04 menyusul sesuai roadmap, setelah diinstruksikan. Data pelaksanaan dan publikasi tetap tahap terpisah.

## DEC-0010 — Produksi otomatis dengan scope naskah

Status VERIFIED untuk otorisasi pengguna; keputusan pedagogi ADOPTED_PROVISIONAL. Instruksi pengguna terbaru mengizinkan kelanjutan antarbatch sampai 56 naskah siap atau semua sisa terblokir. Ketentuan resmi tetap PROVISIONAL. Gunakan dokumentasi runtime lokal dan run CPU/offline untuk substansi; jangan menaikkan READY deliverable visual/LMS/bukti pelaksanaan dari naskah. Simpan ticket/check/handoff per batch.

## DEC-0011 — Kesiapan naskah dan skor formatif lokal

Status ADOPTED_PROVISIONAL untuk desain; VERIFIED untuk fakta run/otorisasi pada laporan actual. Seluruh 56 naskah fokus telah diperiksa pada scope pedagogi/teknis/spec; official_alignment tetap PROVISIONAL, fulfillment asli PARTIAL, repo_status REVIEW. Rubrik lokal USULAN maksimum 2 per 3 butir=6 mengoperasionalkan latihan, bukan bobot semester/ambang kelulusan. Bukti EVID/QA masih menunggu pelaksanaan. Sumber teknis lokal dibaca dan kontrol negatif/edge diuji; tidak ada performa umum, data kelas atau pengesahan rekaan. Lihat 20261007-183058-P17-W01-W04-integrate-validation.md.
