---
artifact_id: W02-STORY
title: Eksplorasi Data untuk ML — STORY
course_code: IF52510031
period: 2026–2027
week: 2
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
version: '0.3'
updated_at: '2026-10-07'
owner: Codex — penyusun; owner sumber dipertahankan di backlog
source_status: REVIEW
production:
  repo_status: REVIEW
markdown_readiness: VALIDATED
fulfillment: PARTIAL
source_verification: VERIFIED_FOR_SCOPE
official_alignment: PROVISIONAL
learning_ids:
- W02-LO01
- W02-LO02
official_outcome_refs:
- DAIML-Sub-CPMK102-1
assessment_ids:
- W02-ASM01
example_ids:
- W02-EX01
evidence_requirement_ids:
- W02-EV01
source_ids:
- SRC-WORKBOOK
- SRC-TECH-001
- SRC-TECH-002
- SRC-TECH-003
dependencies: []
integration_refs: []
workbook_dependencies: Book Chapter + Lecturer Guide
scope_record: course/weeks/w02/scope.md
validation_records:
- course/production/reports/20261007-181601-P21-W02-E1-validation.md
- course/production/reports/20261007-181603-P15-P16-W02-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Eksplorasi Data untuk ML — STORY

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Journey 20 slide

Target desain, bukan render/deck. Empat student-action SL04/10/15/20; aksi terkait worksheet dan exit ticket. Semua waktu1–3 menit USULAN, bukan jumlah durasi kelas resmi.

### W02-SL01

- Nomor: 1; role: explanation.
- Headline: Alasan belajar — Profil dahulu, kesimpulan dibatasi bukti.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Transformasi tanpa profil dapat menghapus pola yang benar atau mempertahankan cacat data.
- Primary visual: Daftar risiko audit; label/relasi: Apa yang dapat salah jika transformasi dilakukan tanpa profil?. Uraian teks tetap tersedia.
- Information architecture: Daftar risiko audit sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Apa yang dapat salah jika transformasi dilakukan tanpa profil?.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL02

- Nomor: 2; role: explanation.
- Headline: Tujuan keputusan — Membuat profil tipe data, missingness, distribusi dan dugaan duplikasi.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Membuat profil tipe data, missingness, distribusi dan dugaan duplikasi
- Primary visual: Panel profil; label/relasi: Tipe/satuan | missing | distribusi | dugaan duplikasi. Uraian teks tetap tersedia.
- Information architecture: Panel profil sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Tipe/satuan | missing | distribusi | dugaan duplikasi.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL03

- Nomor: 3; role: explanation.
- Headline: Tujuan batas bukti — Membedakan observasi dari hipotesis penyebab dan memilih pemeriksaan lanjutan.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Membedakan observasi dari hipotesis penyebab dan memilih pemeriksaan lanjutan
- Primary visual: Memo empat kotak; label/relasi: Observasi → hipotesis → keputusan sementara → data tambahan. Uraian teks tetap tersedia.
- Information architecture: Memo empat kotak sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Observasi → hipotesis → keputusan sementara → data tambahan.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL04

- Nomor: 4; role: student-action.
- Headline: Prediksi sebelum kode — Hitung missing count dan proporsi duration_min; jelaskan penyebutnya.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Hitung missing count dan proporsi duration_min; jelaskan penyebutnya.
- Primary visual: Tabel lima baris; label/relasi: Durasi10,20,missing,20,90; kanalA,B,A,B,B. Uraian teks tetap tersedia.
- Information architecture: Tabel lima baris sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: jawab WK01 pada stimulus DATA; output alasan/trace tertulis; debrief menunjuk kunci Q01 pada GUIDE/RUBRIC DOSEN.
- Bottom takeaway: Durasi10,20,missing,20,90.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL05

- Nomor: 5; role: explanation.
- Headline: Mental model — Profil dahulu, kesimpulan dibatasi bukti.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Profil dahulu, kesimpulan dibatasi bukti
- Primary visual: Lensa audit; label/relasi: Tabel mentah → pemeriksaan yang didefinisikan → klaim terbatas. Uraian teks tetap tersedia.
- Information architecture: Lensa audit sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Tabel mentah → pemeriksaan yang didefinisikan → klaim terbatas.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL06

- Nomor: 6; role: explanation.
- Headline: Istilah pertama — Ketiadaan nilai, dihitung per kolom dengan isna.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Ketiadaan nilai, dihitung per kolom dengan isna.
- Primary visual: Mask missing; label/relasi: false,false,true,false,false; tiap posisi dikaitkan row_id. Uraian teks tetap tersedia.
- Information architecture: Mask missing sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: false,false,true,false,false.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL07

- Nomor: 7; role: explanation.
- Headline: Istilah kedua — Ringkasan nilai yang terlihat pada data, bukan otomatis populasi.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Ringkasan nilai yang terlihat pada data, bukan otomatis populasi.
- Primary visual: Garis nilai teramati; label/relasi: 10,20,20,90; missing tidak menjadi nol. Uraian teks tetap tersedia.
- Information architecture: Garis nilai teramati sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: 10,20,20,90.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL08

- Nomor: 8; role: explanation.
- Headline: Istilah ketiga — Baris identik menurut kolom yang dipilih; harus disebut definisinya.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Baris identik menurut kolom yang dipilih; harus disebut definisinya.
- Primary visual: Dua definisi duplikat; label/relasi: Semua kolom versus subset duration+channel. Uraian teks tetap tersedia.
- Information architecture: Dua definisi duplikat sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Semua kolom versus subset duration+channel.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL09

- Nomor: 9; role: explanation.
- Headline: Mekanisme awal — isna menghasilkan mask nilai hilang; jumlah True memberi count.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: isna menghasilkan mask nilai hilang; jumlah True memberi count. Proporsi hilang adalah count/n pada kolom dengan n baris. Missing bukan nol; nol dapat merupakan nilai yang sah.
- Primary visual: Pecahan missing; label/relasi: 1/5 = 20%; penyebut seluruh baris. Uraian teks tetap tersedia.
- Information architecture: Pecahan missing sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: 1/5 = 20%.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL10

- Nomor: 10; role: student-action.
- Headline: Trace keputusan — Hitung median dan mean nilai teramati.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Hitung median dan mean nilai teramati. Tentukan duplikat berdasarkan duration_min+channel, keep=first.
- Primary visual: Trace median/mean; label/relasi: Urutkan empat nilai, tandai dua tengah, catat jumlah140. Uraian teks tetap tersedia.
- Information architecture: Trace median/mean sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: jawab WK02 pada stimulus DATA; output alasan/trace tertulis; debrief menunjuk kunci Q02 pada GUIDE/RUBRIC DOSEN.
- Bottom takeaway: Urutkan empat nilai, tandai dua tengah, catat jumlah140.
- LO: W02-LO01; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL11

- Nomor: 11; role: worked-example.
- Headline: Worked example — Tabel SIMULASI lima baris: durasi menit [10,20,missing,20,90], kelas kanal [A,B,A,B,B].
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Tabel SIMULASI lima baris: durasi menit [10,20,missing,20,90], kelas kanal [A,B,A,B,B]. Missing durasi=1/5=20%; median nilai teramati [10,20,20,90]=20; mean=35. Dengan subset durasi+kanal dan keep=first, baris keempat mengulang baris kedua sehingga count duplikat=1. Angka 90 adalah observasi jauh dari nilai lain; salah ukur hanya hipotesis sampai proses ukur diperiksa.
- Primary visual: Tabel ringkasan terverifikasi; label/relasi: n5, missing1, median20, mean35, duplicate_subset1. Uraian teks tetap tersedia.
- Information architecture: Tabel ringkasan terverifikasi sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: n5, missing1, median20, mean35, duplicate_subset1.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL12

- Nomor: 12; role: explanation.
- Headline: Mekanisme berikutnya — duplicated menghitung pengulangan sesuai subset kolom; mempertahankan kemunculan pertama membuat jumlah duplikat lebih kecil daripada jumlah baris pada kelompok berulang.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: duplicated menghitung pengulangan sesuai subset kolom; mempertahankan kemunculan pertama membuat jumlah duplikat lebih kecil daripada jumlah baris pada kelompok berulang. Nyatakan subset dan keep yang dipakai.
- Primary visual: Panel duplikat; label/relasi: Baris4 dibanding baris2; row_id dikecualikan dengan alasan. Uraian teks tetap tersedia.
- Information architecture: Panel duplikat sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Baris4 dibanding baris2.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL13

- Nomor: 13; role: explanation.
- Headline: Batas metode — describe merangkum kolom numerik.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: describe merangkum kolom numerik. Mean dan median merangkum data berbeda; pada contoh kecil bandingkan keduanya tanpa klaim distribusi populasi atau sebab.
- Primary visual: Peta batas data; label/relasi: Observasi pada lima baris berbeda dari dugaan populasi. Uraian teks tetap tersedia.
- Information architecture: Peta batas data sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Observasi pada lima baris berbeda dari dugaan populasi.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL14

- Nomor: 14; role: explanation.
- Headline: Miskonsepsi — Satuan, duplikasi, bias cakupan dan waktu tetap perlu diperiksa.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Satuan, duplikasi, bias cakupan dan waktu tetap perlu diperiksa.
- Primary visual: Mitos–koreksi; label/relasi: Nilai jarang bukan bukti salah ukur. Uraian teks tetap tersedia.
- Information architecture: Mitos–koreksi sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Nilai jarang bukan bukti salah ukur.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL15

- Nomor: 15; role: student-action.
- Headline: Kritik klaim — Nilai 90 membuktikan kesalahan ukur? Tulis observasi, hipotesis, keputusan sementara dan pemeriksaan lanjutan.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Nilai 90 membuktikan kesalahan ukur? Tulis observasi, hipotesis, keputusan sementara dan pemeriksaan lanjutan.
- Primary visual: Memo kosong; label/relasi: 90 → apa observasi dan apa hipotesis? Mahasiswa isi. Uraian teks tetap tersedia.
- Information architecture: Memo kosong sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: jawab WK03 pada stimulus DATA; output alasan/trace tertulis; debrief menunjuk kunci Q03 pada GUIDE/RUBRIC DOSEN.
- Bottom takeaway: 90 → apa observasi dan apa hipotesis? Mahasiswa isi.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL16

- Nomor: 16; role: explanation.
- Headline: Periksa asumsi — Korelasi/pola bersama belum membuktikan sebab.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Korelasi/pola bersama belum membuktikan sebab. Memo harus memisahkan observasi, dugaan, keputusan sementara dan data tambahan. Jangan menghapus outlier semata karena jarang; periksa satuan dan proses ukur.
- Primary visual: Checklist proses ukur; label/relasi: Periksa satuan, log, konteks, waktu dan provenance. Uraian teks tetap tersedia.
- Information architecture: Checklist proses ukur sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Periksa satuan, log, konteks, waktu dan provenance.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL17

- Nomor: 17; role: explanation.
- Headline: Koreksi kekeliruan — Nilai 90 bisa sah; audit konteks sebelum menghapus.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Nilai 90 bisa sah; audit konteks sebelum menghapus.
- Primary visual: Kartu kualitas; label/relasi: Tidak missing tetap dapat duplikasi/satuan salah/bias cakupan. Uraian teks tetap tersedia.
- Information architecture: Kartu kualitas sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Tidak missing tetap dapat duplikasi/satuan salah/bias cakupan.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL18

- Nomor: 18; role: explanation.
- Headline: Rangkuman — Profil dahulu, kesimpulan dibatasi bukti.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Profil dahulu, kesimpulan dibatasi bukti; keputusan dan alasan ditelusuri dari input.
- Primary visual: Ringkasan profil; label/relasi: Pemeriksaan yang jelas → angka → interpretasi terbatas. Uraian teks tetap tersedia.
- Information architecture: Ringkasan profil sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Pemeriksaan yang jelas → angka → interpretasi terbatas.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL19

- Nomor: 19; role: explanation.
- Headline: Remediasi — Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.
- Primary visual: Tangga audit ulang; label/relasi: Pilih satu kolom, ulangi definisi, tautkan bukti. Uraian teks tetap tersedia.
- Information architecture: Tangga audit ulang sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: tidak ada tugas baru; amati satu hubungan.
- Bottom takeaway: Pilih satu kolom, ulangi definisi, tautkan bukti.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.

### W02-SL20

- Nomor: 20; role: student-action.
- Headline: Exit ticket — Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.
- Subtitle: Eksplorasi Data untuk ML; satu langkah yang dapat dijelaskan.
- Pesan utama: Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.
- Primary visual: Exit card; label/relasi: Satu temuan | satu dugaan | pemeriksaan tambahan. Uraian teks tetap tersedia.
- Information architecture: Exit card sebagai pusat; judul singkat, label relasi, lalu takeaway; panel berbeda menurut fungsi.
- Supporting elements: label unit/kolom/data pada DATA; contoh W02-EX01, SIMULASI.
- Student action: exit ticket: satu keputusan, bukti dan batas; debrief periksa kedua LO, bukan skor saja.
- Bottom takeaway: Satu temuan | satu dugaan | pemeriksaan tambahan.
- LO: W02-LO02; source/locator: BOOK definisi/konsep/worked example dan snapshot runtime.
- Speaker cue DOSEN: cek asal alasan; gunakan GUIDE untuk expected responses, jangan salin kunci ke layar.
- Waktu: USULAN 1–3 menit; render/proyeksi belum dibuat.
