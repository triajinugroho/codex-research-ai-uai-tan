# Quality Gates Produksi Bahan Ajar

Status: **rencana pemeriksaan**, bukan laporan QA terhadap bahan ajar yang sudah dibuat. Gate ini berlaku untuk [222 artefak baseline](WORKBOOK_BASELINE.md) dan adaptasi Markdown pada [spesifikasi artefak](ARTIFACT_SPECS.md). Gunakan bersama [rencana produksi](../PRODUCTION_PLAN.md), [playbook](EXECUTION_PLAYBOOK.md), [peta mingguan](WEEKLY_BLUEPRINTS.md), dan [prompt library](PROMPT_LIBRARY.md).

Tujuan gate adalah membuat keputusan kesiapan dapat ditelusuri: materi yang benar, bisa diajarkan, konsisten, dapat dinilai, dan aman dibagikan kepada audiens yang tepat. Review internal naskah dan penutupan temuan berjalan dalam scope produksi yang sudah diotorisasi; setiap revisi draft tidak membutuhkan permintaan izin baru.

## 1. Empat hal yang tidak boleh dicampur

| Dimensi | Makna | Bukti yang diperlukan |
| --- | --- | --- |
| Status baseline workbook | Snapshot impor, termasuk lifecycle/DoD/prioritas asal | Sel/baris workbook dan waktu snapshot yang benar-benar diketahui |
| Status produksi repo | Pekerjaan terhadap isi/file versi tertentu | File, perubahan, review/run sesuai status |
| Readiness Markdown | Kesiapan naskah untuk ditelaah/dipakai pada scope tertentu | Gate wajib + temuan/blocker + manifest versi |
| Pemenuhan DoD asli / penggunaan nyata | Keluaran asli dan tindakan yang diminta workbook | Deck/notebook/LMS/evidence/analisis aktual sesuai item; publikasi/pelaksanaan tidak disimpulkan dari file |

`source_status` immutable dan `production.repo_status` mengikuti istilah workbook: **NOT STARTED, DRAFT, REVIEW, READY, PUBLISHED, DELIVERED, IMPROVE**. Status repo menilai DoD asli. IMPROVE adalah tahap perbaikan bila ada penggunaan/review yang memicunya; tidak harus menjadi lintasan linear untuk setiap file. Jangan mengubah status baseline atau menghitung nilai score workbook sebagai kesiapan nyata tanpa menjelaskan konteksnya.

Semua keputusan menyebut versi dan scope. `markdown_readiness` memakai **NOT_STARTED, DRAFT, IN_REVIEW, VALIDATED**, sedangkan `fulfillment` memakai **NOT_FULFILLED, PARTIAL, FULFILLED**. `VALIDATED` tidak setara dengan “deck selesai”, “LMS dipublikasikan”, “ujian terlaksana”, atau “DoD asli terpenuhi”. READY repo hanya boleh dipakai bila DoD asli terbukti. Untuk EVID/QA, laporkan **spesifikasi/instrumen tervalidasi** dan **bukti/analisis aktual belum tersedia** secara terpisah.

Sumber kebijakan yang belum tersedia tidak otomatis memblokir VALIDATED untuk naskah pedagogi yang klaimnya terverifikasi pada scope tersebut. `official_alignment: PROVISIONAL` dan `fulfillment: PARTIAL` dapat tetap berlaku. Sumber inti teknis yang belum diperiksa atau aturan final yang belum bersumber memblokir VALIDATED pada scope yang mengandalkan klaim tersebut. Kontrak status/verifikasi sumber lengkap ada di [spesifikasi metadata](ARTIFACT_SPECS.md#2-kontrak-metadata-bersama).

## 2. Hasil gate dan aturan blocker

| Hasil | Kapan dipakai | Dampak |
| --- | --- | --- |
| PASS | Semua cek wajib pada versi/scope itu terpenuhi dengan bukti | Dapat melanjutkan tahap terkait |
| FAIL | Ada cek wajib gagal atau bukti bertentangan | Tahan transisi yang bergantung pada masalah tersebut; perbaiki lalu cek ulang |
| PROVISIONAL | Draft dapat dibuat, tetapi keputusan tertentu menunggu sumber/kondisi | Lanjutkan produksi yang tidak bergantung pada nilai final; label batas pemakaian |
| UNRUN | Gate/pemeriksaan belum dilakukan | Tidak menjadi PASS; catat alasan dan langkah berikut |
| NOT_APPLICABLE | Cek memang tidak relevan, dengan alasan spesifik | Tidak dianggap pass terselubung; jangan gunakan untuk menyembunyikan bukti yang belum tersedia |

Hasil **check/run aktual** menggunakan **PASS, FAIL, UNRUN, NOT_APPLICABLE**. Keputusan **gate** dapat pula memakai **PROVISIONAL** untuk batas scope/keputusan yang masih menunggu sumber. `blocked` adalah kondisi dengan alasan/temuan, bukan enum hasil atau readiness baru.

PROVISIONAL bukan pengganti PASS pada kode inti yang salah, soal tanpa kunci, atau paket yang membocorkan jawaban. Sumber resmi yang belum tersedia membolehkan draft pedagogi/kasus/struktur, tetapi menahan klaim final kebijakan, keselarasan resmi, bobot, durasi, atau cakupan ujian yang bergantung padanya.

| Kondisi | Yang dapat diteruskan | Yang tertahan |
| --- | --- | --- |
| RPS/kurikulum/RTM belum dibaca | Template, crosswalk baseline, draft isi dan rancangan asesmen berlabel | Pengesahan identitas/outcome/kebijakan/bobot/durasi/cakupan resmi |
| Mode/durasi IF24A/IF24H belum diketahui | Inti materi sama, agenda proporsi, opsi adaptasi usulan | Klaim kelas tertentu hybrid/malam atau alokasi menit final |
| Sumber teknis klaim inti belum memadai | Struktur, daftar sumber yang perlu dibaca, draft dengan tanda verifikasi | VALIDATED pada scope isi yang masih memakai klaim/formula utama belum diperiksa |
| Kode inti belum dijalankan | Bab nonkode atau rencana lab dengan catatan technical_unverified dan check UNRUN | Klaim runnable/hasil numerik/run lulus pada lab/demo inti |
| Tidak ada dataset berlisensi jelas | Kasus/generator sintetis berlabel yang telah diperiksa | Distribusi ulang data eksternal tanpa hak penggunaan yang diketahui |
| Tidak ada bukti kelas/ujian | EVID/QA sebagai spesifikasi/instrumen | Statistik mastery, analisis aktual, DELIVERED, atau IMPROVE berdasarkan pelaksanaan rekaan |
| Render/PPTX/notebook/LMS belum dibuat | Naskah dan manifest Markdown | Klaim keluaran asli selesai atau publikasi terjadi |
| Batas akses repo belum diperiksa | Draft dan manifest instructor-only | Pembagian paket dengan kunci/soal rahasia yang mungkin terbaca audiens tidak tepat |

Tidak ada gate yang meminta persetujuan untuk setiap draft teks. Keputusan institusi hanya diperlukan untuk hal yang memang memerlukan sumber/pengesahan akademik; publikasi/perubahan akses/generasi visual dilakukan ketika scope tindakan itu telah diotorisasi. Persyaratan approval storyboard pada master prompt adalah alur untuk produksi gambar/deck lanjutan, bukan alasan menghentikan penulisan Markdown.

## 3. Gate G0 — Sumber dan provenance

**Berlaku:** semua artefak; terutama SEM-01–04, DATA, BOOK, SLIDE, ASSESS, INSTR. **Input:** register sumber, baseline, isi versi review. **Keluaran:** tabel klaim–sumber–locator, daftar konflik/missing sources.

- [ ] Sumber yang disebut benar-benar tersedia/dibaca; ID S01–S06 workbook dipertahankan dan source state tidak ditukar dengan repo state.
- [ ] SRC-WORKBOOK/SRC-MASTER-PROMPT dibedakan dari sumber substansi teknis. Crosswalk S06 menyimpan ketidakpastian label/versi yang memang belum dibuktikan.
- [ ] Identitas/outcome/bobot/durasi/aturan memiliki locator sumber primer atau label baseline/usulan yang terlihat.
- [ ] Klaim teknis inti, formula, data, lisensi, dan angka mempunyai sumber yang mendukung bagian tersebut; tidak ada sitasi, DOI, kutipan, tahun, atau riset rekaan.
- [ ] Contoh sintetis/ilustrasi/pengayaan berbeda dari data/hasil aktual; sumber desain tidak dipakai sebagai bukti performa model.
- [ ] Konflik antarversi tersimpan dengan dampak dan keputusan sementara, bukan dihilangkan diam-diam.

### 3.1 Otoritas sumber menurut jenis keputusan

Prioritas berikut adalah aturan kerja provenance berdasarkan peran sumber baseline, **bukan klaim bahwa S01–S05 telah dibaca atau resmi disahkan di repo**. Otoritas dilihat per jenis fakta, bukan satu urutan yang membolehkan semua sumber saling menggantikan.

| Jenis fakta/keputusan | Sumber yang diperiksa terlebih dahulu | Batas pemakaian |
| --- | --- | --- |
| Identitas, CPL/CPMK/BK, prasyarat formal | S01 kurikulum setelah isi/versi relevan diverifikasi | Workbook hanya baseline; tidak membuat rumusan outcome resmi baru |
| Peta operasional minggu, bobot, cakupan/aturan asesmen, durasi jika tersedia | S02 RPS/RTM yang relevan dan terverifikasi, konsisten dengan kurikulum | Jangan menganggap isi khusus IF24A otomatis berlaku identik bagi IF24H |
| Rincian tugas, luaran, rubrik, alur submit | S03 RTM yang relevan dan terverifikasi, konsisten dengan RPS | Judul template/label workbook tidak membuktikan versi final/pengesahan |
| Pelaksanaan, presensi, tugas/nilai yang memang tercatat | S04/S05 dan bukti aktual yang boleh digunakan | Label tracker tidak membuktikan mode/durasi aktual; nilai/presensi tidak otomatis menjadi mastery per LO |
| Cakupan produksi, ID, lifecycle/status/DoD/prioritas asli | SRC-WORKBOOK | Tidak menggantikan kebijakan akademik, bobot nilai mahasiswa, atau bukti keberadaan file |
| Pedagogi, storyboard, DNA visual | SRC-MASTER-PROMPT; crosswalk S06 | Tidak mendukung kebenaran formula, hasil algoritma, atau klaim performance |
| Definisi/algoritma/kode teknis | Dokumentasi/buku otoritatif yang benar-benar dibaca, dengan locator dan versi | Sumber teknis tidak menetapkan kebijakan institusi; hasil run mendukung perilaku kode pada environment tertentu |

Versi lebih baru/tanggal terbaru tidak otomatis mengalahkan sumber resmi lain tanpa bukti perubahan yang berlaku. Bila dua sumber bertentangan, simpan keduanya beserta locator, bidang yang konflik, dampak, dan keputusan sementara pada register keputusan. Bagian terdampak tetap PROVISIONAL; jangan memilih satu diam-diam. Bagian lain yang dukungannya memadai tetap dapat diproduksi/divalidasi.

**PASS:** seluruh klaim wajib untuk scope yang akan dipakai memiliki dukungan/verifikasi; fakta belum resmi diberi batas jelas dan tidak dipakai sebagai final. **PROVISIONAL:** keputusan resmi yang masuk scope gate belum dapat difinalkan karena sumber kebijakan belum tersedia. Naskah teknis mandiri tetap dapat memperoleh PASS pada sumber substansinya dan VALIDATED pada scope pedagoginya. **Blocker:** sitasi rekaan, aturan resmi tanpa sumber, konflik kritis outcome/cakupan, atau distribusi data yang hak penggunaannya belum jelas. Draft struktur tetap dapat berjalan pada bagian yang tidak terdampak.

## 4. Gate G1 — Scope, outcome, dan kontinuitas

**Berlaku:** SEM-02/04/05/06/07, scope minggu, seluruh paket mingguan/ujian. **Input:** scope, LO lokal, crosswalk resmi, matriks penelusuran. **Keluaran:** coverage report dan daftar gap.

- [ ] Nomor minggu benar: 14 minggu belajar W01–W07/W09–W15; UTS W08; UAS W16.
- [ ] Must-cover, batas kedalaman, must-not-add, prasyarat, dan keluaran paket dinyatakan sebelum draft panjang.
- [ ] LO lokal stabil dan teramati; kode outcome resmi dipertahankan sebagai referensi, bukan diganti oleh LO buatan.
- [ ] Setiap LO inti punya materi → kegiatan/contoh → asesmen → rubrik → bukti, atau alasan eksplisit untuk bagian yang belum dinilai.
- [ ] Setiap asesmen mengukur LO yang diajarkan; prasyarat punya lokasi pengajaran/penguatan.
- [ ] Hubungan W03 preprocessing–W04 validasi, W09 selection–W10 generalisasi–W11 NN, serta W12–W15 proyek tidak bertentangan.
- [ ] W15 menggunakan sintesis/presentasi/klinik; adaptasi tidak menjadi artefak kosong atau algoritma baru tanpa dasar.
- [ ] IF24A/IF24H mempunyai catatan fakta versus usulan; mode/durasi dan karakter mahasiswa tidak ditebak dari kode kelas.

**PASS:** 100% LO inti dan asesmen terlacak, nomor/cakupan konsisten, gap telah ditutup atau secara eksplisit berada di luar scope yang sah. **Blocker:** asesmen inti meminta konsep yang belum diajarkan, outcome berbeda antarartefak, salah minggu ujian, atau cakupan final ujian bertumpu pada asumsi kebijakan. **PROVISIONAL:** crosswalk kurikulum belum resmi, sementara scope lokal dan batasnya sudah jelas.

## 5. Gate G2 — Akurasi isi dan pedagogi

**Berlaku:** BOOK, MOD, GUIDE, DATA, WORK, AIP, SLIDE, instruksi/soal, bab proyek. **Input:** draft, sumber, contoh yang disepakati. **Keluaran:** review substansi dan teaching pass.

- [ ] WHY jelas sebelum detail; intuisi ditautkan ke definisi formal; analogi tidak menggantikan makna teknis.
- [ ] Formula/simbol/satuan/asumsi/input/output konsisten; batas metode dan keterbatasan dijelaskan.
- [ ] Minimal satu worked example dan satu miskonsepsi/kritik pada pertemuan reguler; W15 mempunyai contoh/kritik proyek yang sesuai.
- [ ] Contoh memiliki langkah, keputusan, hasil, dan interpretasi; tidak hanya memberi jawaban akhir.
- [ ] Mahasiswa melakukan tindakan teramati: memprediksi, menghitung, menjelaskan, membandingkan, menguji, mengkritik, atau menghasilkan output.
- [ ] Kesalahan umum punya koreksi/debrief; ada checkpoint/refleksi/mastery map atau exit ticket.
- [ ] Bahasa Indonesia jelas; istilah teknis diperkenalkan; materi inti tidak mensyaratkan konteks yang belum diberikan.
- [ ] Bab–modul–lab–worksheet–soal–kunci memakai data/istilah/simbol yang sama atau perbedaannya dijelaskan.
- [ ] Aktivitas/AI prompt mengajarkan verifikasi; alternatif tanpa layanan AI tersedia; contoh respons yang belum diuji tidak diklaim sebagai hasil validasi.

**PASS:** semua cek relevan terpenuhi dan reviewer dapat menjelaskan jalur belajar tanpa menebak instruksi. **Blocker:** kesalahan konsep utama, klaim hasil palsu, contoh yang bertentangan dengan mekanisme, atau instruksi inti tidak dapat dikerjakan. **Minor:** perbaikan gaya/ritme yang tidak mengubah pemahaman; tetap dicatat dengan alasan bila ditunda.

## 6. Gate G3 — Validasi teknis dan reproduksibilitas

**Berlaku:** DATA, LAB, demo GUIDE/SLIDE, solusi RUBRIC/KEY, contoh numerik, proyek/pipeline. **Input:** blok kode dan data versi review, runtime tersedia. **Keluaran:** laporan run aktual di `course/production/reports/` atau lokasi bantu yang konsisten.

- [ ] Setiap blok inti diklasifikasikan runnable/pseudocode/starter incomplete; urutan eksekusi dan input jelas.
- [ ] Solusi referensi dijalankan dari awal dengan versi paket/seed/data yang dicatat; starter tidak diam-diam berisi jawaban.
- [ ] Output aktual, shape/jenis, unit, dan toleransi cocok dengan naskah; angka naskah tidak dibuat dari perkiraan.
- [ ] Split dilakukan sesuai konteks; data test tidak dipakai memilih model; preprocessing di-fit pada train/fold; leakage diperiksa.
- [ ] Metrik sesuai task/target dan dibandingkan baseline yang relevan; training score dibedakan dari hasil evaluasi generalisasi.
- [ ] Jalur inti CPU/offline bekerja sesuai tujuan; setup yang memerlukan jaringan dibedakan dari kebutuhan jaringan selama belajar.
- [ ] Target runtime/memori yang dipakai sebagai janji sudah diukur pada environment yang disebut; jika belum, statusnya target usulan.
- [ ] Dataset/folder/file/output yang disebut ada atau cara membuatnya jelas; naskah tidak mengklaim notebook/data fisik/PPTX tersedia tanpa bukti.
- [ ] Tautan relatif yang sudah seharusnya tersedia dan Mermaid/code fence diperiksa; referensi planned belum dibuat ditandai.
- [ ] Run gagal/skipped/unrun dan keterbatasan environment dilaporkan; tidak menyebut “lulus” untuk perintah yang tidak dijalankan.

**PASS:** contoh/lab/solusi inti yang akan digunakan benar-benar lolos pemeriksaan yang sesuai. **Blocker:** kode inti gagal, leakage, angka salah, ketergantungan GPU/API wajib tanpa jalur dasar yang disepakati, atau log tidak sesuai versi kode. **PROVISIONAL:** naskah rencana lab dapat dibuat dengan catatan technical_unverified dan check UNRUN; belum VALIDATED sebagai naskah lab runnable.

Pemeriksaan dipilih menurut risiko/LO. Jangan menulis tes yang hanya mengulang implementasi atau menguji setiap edit ejaan. Cek ulang bagian yang berubah dan dependensi terdampak; run penuh diulang jika data, split, pipeline, versi, atau hasil utama berubah.

### 6.1 Template laporan run

```text
Run ID / artefak / versi / blok kode: [...]
Waktu aktual / environment / versi paket: [...]
Data / sumber / generator / seed: [...]
Command aktual + working directory: [...]
Perilaku/output yang diharapkan: [...]
Output aktual + lokasi log: [...]
PASS/FAIL + toleransi/edge case: [...]
Bagian tidak diuji + alasan: [...]
Dampak ke naskah/soal/kunci: [...]
```

Template tidak dianggap log run. Nilai hanya diisi setelah eksekusi dilakukan.

## 7. Gate G4 — Asesmen, kunci, rubrik, dan fairness

**Berlaku:** SEM-03/04/07/09/10, WORK, ASSESS, RUBRIC, seluruh paket UTS/UAS. **Input:** blueprint, soal, kunci/rubrik, materi, sumber kebijakan. **Keluaran:** assessment review dan hasil kalibrasi penilai.

- [ ] 100% butir punya ID/LO/indikator dan kunci atau rubrik yang sesuai; stimulus cukup untuk dikerjakan.
- [ ] Reviewer mencoba soal tanpa melihat kunci dahulu; jawaban alternatif yang sah ditangani.
- [ ] Total skor per butir/bagian/paket konsisten; bobot resmi jika tersedia berasal dari sumber, bukan dipilih tanpa label.
- [ ] Kriteria rubrik teramati; partial credit, kesalahan umum, dan toleransi numerik dinyatakan jika relevan.
- [ ] Pertanyaan mengukur tujuan belajar, bukan akses ke alat berbayar atau ketidakjelasan instruksi.
- [ ] Estimasi beban/durasi ditelaah; mode/durasi belum diketahui tetap ditulis sebagai usulan.
- [ ] Kebijakan AI/kolaborasi/submit/penalti bersumber atau provisional; jangan menginventarisasi aturan sebagai resmi.
- [ ] Latihan shareable, soal dinilai, soal ujian rahasia, rubrik transparan, dan kunci instructor-only dibedakan.
- [ ] Definisi mastery memisahkan data hilang/belum dinilai/tidak memenuhi/memenuhi; ambang tidak berasal dari score produksi workbook.
- [ ] Tingkat kesulitan rancangan berbeda dari kesulitan empiris; statistik ujian baru diisi dari hasil nyata.

**PASS:** semua butir/score/kunci/traceability konsisten dan temuan kalibrasi yang memengaruhi skor ditutup. **Blocker:** soal tidak dapat diselesaikan, kunci salah, skor bertentangan, LO tidak tercakup, aturan belum resmi digunakan untuk asesmen final, atau kunci masuk paket mahasiswa. Draft butir tetap boleh ditulis sambil menunggu kebijakan resmi.

## 8. Gate G5 — Storyboard dan naskah slide

**Berlaku:** STORY, SLIDE, standar SEM-11; GUIDE/MOD sebagai konteks. **Input:** substansi dan contoh yang telah melewati gate relevan. **Keluaran:** review storyline/naskah, bukan persetujuan render yang belum ada.

- [ ] Setiap slide punya ID/nomor, role, headline, subtitle, satu key message, primary visual, information architecture, supporting elements, contoh, student action, takeaway; field yang tidak relevan diberi alasan.
- [ ] Pesan utama dapat diringkas satu kalimat; isi tampil mendukung headline/takeaway; notes menampung detail pengajaran yang tidak perlu tampil.
- [ ] Alur WHY → intuisi → konsep → mekanisme → contoh → praktik → aplikasi → kritik → mastery tampak tanpa repetisi yang tidak perlu.
- [ ] Target awal sekitar 20 slide; durasi/format menentukan jumlah final. Penyimpangan dan format W15 dicatat, bukan diisi dengan slide dekoratif.
- [ ] Pada reguler ada target 2–4 slide student-action, minimal satu worked example, satu miskonsepsi/kritik, dan penutup mastery/exit ticket; aksi memiliki output/debrief.
- [ ] Slide, bab, lab, dan soal memakai contoh/angka/simbol konsisten; perubahan contoh menuntut pemeriksaan dependensi.
- [ ] Visual brief menyatakan hubungan/label/data; diagram bermakna dan mempunyai uraian teks; tidak mengandalkan dekorasi robot/gambar generik untuk menjelaskan konsep.
- [ ] Spesifikasi 16:9, navy/cyan, footer/takeaway, nomor dan variasi layout dicatat sebagai desain. Keterbacaan proyektor/10–20 detik adalah target yang baru dapat divalidasi setelah render.
- [ ] Tidak ada kunci/solusi dosen di teks tampil/notes yang ikut dibagikan mahasiswa.

**PASS:** storyboard dan naskah konsisten serta memenuhi fungsi pedagogi. **Blocker:** pesan/angka utama salah, slide menghilangkan konsep yang dibutuhkan LO, aksi tak dapat dikerjakan, atau isi dosen bocor. **Batas:** PASS Markdown tidak memenuhi DoD deck visual; pemeriksaan estetika, proyeksi, font, layout, gambar, dan formula hasil render menjadi gate tambahan bila produksi visual diminta.

## 9. Gate G6 — Paket, navigasi, dan batas distribusi

**Berlaku:** index, LMS, seluruh artefak yang akan masuk manifest, SEM-08/12. **Input:** file nyata versi review dan manifest. **Keluaran:** paket mahasiswa/dosen yang dapat ditelaah dan daftar planned assets.

- [ ] Setiap file/bagian punya audiens dan status; manifest menulis ID/path/heading/versi/readiness.
- [ ] Paket mahasiswa lengkap untuk belajar: bacaan, input, starter, instruksi, luaran, kriteria transparan, submit, dan dukungan.
- [ ] Kunci/rubrik jawaban, solusi, bank/soal rahasia, expected responses, dan data hasil individual tidak ikut rute mahasiswa.
- [ ] Metadata `instructor_only`, path folder, collapsible section, atau komentar Markdown tidak dianggap akses kontrol; repo/riwayat Git dapat terbaca jika aksesnya diberikan.
- [ ] Batas akses/distribusi yang sebenarnya diperiksa sebelum berbagi; tidak menyebut kunci rahasia hanya karena nama file berbeda.
- [ ] Tautan yang ditandai tersedia resolvable; planned files/link LMS/deck/notebook jelas belum tersedia. Tidak ada klaim upload dari checklist unggah saja.
- [ ] Skor/bobot/nama file dan ID LMS cocok dengan asesmen; aturan waktu/attempt/visibility belum resmi diberi tanda.
- [ ] Data pribadi tidak dibuat untuk mengisi tracker; contoh sintetis diberi label dan tidak tampil seperti hasil nyata.

**PASS:** paket versi tertentu lengkap, jalur audiens benar, dan status aset jujur. **Blocker:** kunci/soal rahasia terbuka bagi audiens yang tidak semestinya, file penting hilang tanpa fallback, link menipu tentang ketersediaan, atau data pribadi/hasil rekaan masuk paket. Draft manifest tetap dapat dibuat; publikasi/LMS/perubahan akses memerlukan tindakan terpisah yang memang diotorisasi.

## 10. Gate G7 — Integrasi dan laporan semester

**Berlaku:** semua 222 artefak + file pendukung. **Input:** backlog, gate records, source register, manifest, actual evidence jika tersedia. **Keluaran:** laporan kesiapan semester dengan batas klaim.

- [ ] Jumlah ID unik **12 semester, 196 mingguan, 14 ujian = 222**; setiap minggu belajar 14 dan setiap ujian 7.
- [ ] Tidak ada ID/file dihitung selesai dua kali; SEM-12 multifile tetap satu ID; index/template/log tidak menaikkan denominator.
- [ ] Istilah, simbol, data/contoh, outcome, asesmen, rubrik, dan sumber konsisten lintas minggu.
- [ ] Peta W01–W16, prasyarat, checkpoint UTS/UAS, dan milestone proyek koheren; W08/W16 bukan minggu belajar biasa.
- [ ] Dashboard direkonsiliasi dengan backlog; baseline immutable terpisah dari perubahan repo; prioritas/dependensi asli versus usulan baru dapat dibedakan.
- [ ] Setiap Markdown VALIDATED punya gate/versi/bukti review; unresolved blockers tidak hilang dari summary. Setiap READY repo mempunyai bukti sesuai DoD asli.
- [ ] Laporan memisahkan file/spec lengkap, isi siap review, Markdown siap, sumber resmi belum verified, DoD asli belum terpenuhi, dan bukti aktual menunggu.
- [ ] Klaim PUBLISHED/DELIVERED/IMPROVE memiliki provenance tindakan/pelaksanaan yang sesuai; tidak diturunkan dari status workbook atau simulasi.
- [ ] Adaptasi IF24A/IF24H, CPU/offline, dan keterbatasan akses/mode tetap terlihat; tidak ada janji durasi/hasil siswa tanpa bukti.

**PASS kesiapan Markdown semester:** cakupan naskah yang dinyatakan siap lengkap, gate relevan lulus, dan pengecualian/provisional dibatasi secara eksplisit. **FAIL integrasi:** ID hilang/ganda, angka dashboard tidak dapat direkonsiliasi, kontradiksi lintas paket, atau klaim selesai yang tidak didukung. Penyelesaian naskah tidak menjadi PASS pemenuhan seluruh DoD asli bila deck/notebook/LMS/evidence belum tersedia.

### 10.1 Format laporan semester

```text
Tanggal/versi snapshot repo: [...]
Baseline: 222 ID; sumber workbook snapshot [...]
Isi belum mulai / draft / review: [jumlah + cara hitung]
Markdown siap: [jumlah + manifest/gate records]
Provisional/blocked: [jumlah + blocker utama + artefak terdampak]
DoD asli: [NOT_FULFILLED / PARTIAL / FULFILLED per ID; bukan satu klaim kabur]
EVID/QA: [spec siap; bukti/analisis aktual tersedia atau menunggu]
Publikasi/penggunaan nyata: [bukti tersedia / belum dilakukan]
Sumber/keputusan resmi yang masih dibutuhkan: [...]
Tindakan berikut yang dapat dilakukan: [...]
```

## 11. Penerapan gate menurut kelompok artefak

Huruf **W** berarti cek wajib pada fungsi inti; **K** berarti kondisional bila artefak memuat hal yang diuji. Semua gate tetap memakai scope/versi dan alasan NOT_APPLICABLE, bukan checklist mekanis.

| Kelompok | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SEM-01–04 | W | W | K | K | W untuk SEM-03/04; K untuk SEM-01/02 | K | K | W |
| SEM-05–07 | W | W | W | K | K | K | K | W |
| SEM-08–12 | W | W | K | K | K | K | W | W |
| BOOK/MOD/GUIDE | W | W | W | K | K | K | W | W |
| STORY/SLIDE | W | W | W | K | K | W | W | W |
| DATA/LAB/WORK/AIP | W | W | W | W untuk DATA/LAB dan hitungan/kode inti | K | K | W | W |
| ASSESS/RUBRIC | W | W | W | K | W | K | W | W |
| LMS/EVID/QA | W | W | K | K | K | K | W | W |
| UTS/UAS-BLUEPRINT/QUESTION/KEY/INSTR | W | W | W | K | W | K | W | W |
| UTS/UAS-LMS/EVID/QA | W | W | K | K | W untuk aturan/nilai/analisis | K | W | W |

G7 merupakan pemeriksaan integrasi saat paket/semester direkonsiliasi, bukan tuntutan mengulang audit 222 item untuk setiap edit. G3 wajib untuk data/solusi/angka yang menjadi dasar pembelajaran/penilaian; instrumen kosong tanpa kode dapat NOT_APPLICABLE beralasan.

## 12. Severity temuan dan penutupan

| Severity | Contoh | Keputusan |
| --- | --- | --- |
| S0 Critical | Klaim/bukti pelaksanaan rekaan, kunci ujian bocor, aturan resmi direka, leakage yang membatalkan evaluasi utama | Tahan distribusi/penggunaan bagian terkait; perbaiki dan review ulang seluruh dependensi terdampak |
| S1 Major | Konsep/kunci salah, kode inti gagal, LO inti tak dinilai, skor tidak konsisten, instruksi tidak cukup | Tahan VALIDATED naskah dan READY DoD asli terkait sampai bukti perbaikan tersedia |
| S2 Minor | Istilah tidak konsisten di bagian kecil, kalimat sulit, visual brief kurang rinci tanpa mengubah konsep utama | Perbaiki dalam batch; dapat diterima sementara dengan alasan/owner/next action yang jelas |
| S3 Suggestion | Tambahan analogi/pengayaan atau variasi layout yang tidak diperlukan untuk LO | Opsional; tidak menjadi blocker atau menambah scope diam-diam |

Severity ditentukan dari dampak pada akurasi, penilaian, keterlaksanaan, dan distribusi. Masalah ejaan pada nama variabel yang membuat kode gagal adalah S1, bukan S2. “Belum ada data kelas” adalah batas evidence yang sah pada tahap spesifikasi; baru menjadi temuan kritis jika dilaporkan seolah data sudah ada.

```text
Finding ID: QA-[paket]-[nomor]
Artefak/versi/heading/baris: [...]
Gate + severity: [...]
Temuan + bukti/locator: [...]
Dampak + artefak dependen: [...]
Perbaikan yang diminta: [...]
Owner/status: [...]
Bukti perbaikan + cek ulang aktual: [...]
Reviewer/penutupan/tanggal: [...]
```

Temuan ditutup setelah perbaikan diperiksa, bukan hanya setelah penulis menyatakan “fixed”. Scope yang tidak berubah tidak perlu diulang; perubahan data, LO, soal, rubrik, atau hasil teknis memicu cek ulang dependensi yang terpengaruh.

## 13. Kalibrasi reviewer dan penilai

1. **Paket kalibrasi:** gunakan W04 sebagai pola pertama. Penulis dan reviewer menyepakati scope, LO, ID, data/contoh, arti VALIDATED Markdown versus READY/FULFILLED DoD asli, serta gate wajib sebelum memberi nilai mutu.
2. **Review independen:** reviewer memeriksa contoh teknis/soal tanpa kunci terlebih dahulu. Checklist yang hanya ditandai penulis tidak menggantikan pemeriksaan independen pada bagian berisiko tinggi.
3. **Jawaban jangkar:** sebelum rubrik digunakan, pilih beberapa contoh yang mewakili benar, sebagian benar, miskonsepsi, dan pendekatan alternatif. Contoh dibuat/dipilih dengan status sintetis/aktual yang eksplisit; jangan mengklaim respons mahasiswa bila bukan.
4. **Skoring terpisah:** reviewer/penilai menilai contoh tanpa melihat skor pihak lain; bandingkan per kriteria, partial credit, dan alasan, bukan total skor saja.
5. **Resolusi:** selesaikan perbedaan yang dapat mengubah hasil/kategori penilaian; revisi descriptor/kunci dan uji kembali contoh terdampak. Target toleransi kesepakatan merupakan usulan kerja yang ditetapkan sebelum kalibrasi, bukan kebijakan institusi rekaan.
6. **Rekam:** simpan versi rubrik, contoh, perbedaan, keputusan, dan hasil cek ulang. Penilai baru membaca contoh jangkar dan aturan skor sebelum menilai paket nyata.
7. **Perluas pola:** setelah masalah W04 tertutup, gunakan pola untuk minggu lain. W15/proyek/ujian tetap direview sesuai bentuknya; pola 20 slide atau rubrik W04 tidak dipaksakan.

Reviewer boleh menggunakan reasoning medium untuk cek format/ID/koherensi yang spesifik dan reasoning high untuk konsep, leakage, kesetaraan asesmen, ambigu kunci, dan konflik sumber. Level reasoning tidak menjadi bukti kebenaran; hasil tetap memerlukan sumber, run, dan catatan review yang sesuai.

## 14. Urutan keputusan praktis

1. Scope dan sumber tersedia diperiksa lewat G0–G1; draft yang tidak tergantung kebijakan final langsung dikerjakan.
2. Isi/contoh diperiksa melalui G2–G3; soal/kunci berpasangan melewati G4 sebelum dipakai membangun slide.
3. Storyboard/naskah melewati G5; paket audiens melewati G6; backlog dan keseluruhan paket direkonsiliasi lewat G7.
4. S0/S1 ditutup sebelum VALIDATED naskah atau READY DoD asli untuk fungsi terdampak. S2 yang ditunda tetap terlihat; S3 tidak memblokir.
5. Laporan menyebut apa yang siap, apa yang provisional, apa yang belum dibuat, dan bukti apa yang belum ada. Penulisan draft terus berjalan pada area yang tidak terblokir.

Gate ini disiapkan untuk produksi berikutnya. Dokumen perencanaan dapat lengkap dan direview sementara **222 bahan ajar utama masih belum diproduksi**; jangan memperbarui status materi hanya karena spesifikasi/checklist ini tersedia.
