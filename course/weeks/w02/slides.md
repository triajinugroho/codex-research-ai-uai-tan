---
artifact_id: W02-SLIDE
title: Eksplorasi Data untuk ML — SLIDE
course_code: IF52510031
period: 2026–2027
week: 2
classes:
- IF24A
- IF24H
audience: mahasiswa
distribution: student_candidate
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
workbook_dependencies: Storyboard
scope_record: course/weeks/w02/scope.md
validation_records:
- course/production/reports/20261007-181602-P21-W02-E2-validation.md
- course/production/reports/20261007-181603-P15-P16-W02-R-validation.md
- course/production/reports/20261007-181842-P16-coherence-and-visuals-validation.md
- course/production/reports/20261007-182157-P22-P16-final-technical-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Eksplorasi Data untuk ML — SLIDE

Scope naskah pedagogi/teknis lokal; LO/tugas adalah USULAN, outcome workbook BASELINE. Official_alignment PROVISIONAL: S01–S03 belum dibaca. Tidak menetapkan bobot semester, durasi resmi, tenggat, aturan AI atau pengesahan. SIMULASI bukan data/hasil kelas.

## Naskah tampilan mahasiswa

20 slide sama dengan STORY; visual brief adalah spesifikasi teks, bukan gambar. Notes aman hanya mengarahkan urutan; kunci tidak ditampilkan.

### W02-SL01 — Alasan belajar

Transformasi tanpa profil dapat menghapus pola yang benar atau mempertahankan cacat data.

Visual brief: **Daftar risiko audit**. Label/relasi: Apa yang dapat salah jika transformasi dilakukan tanpa profil?. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Apa yang dapat salah jika transformasi dilakukan tanpa profil?.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL02 — Tujuan keputusan

Membuat profil tipe data, missingness, distribusi dan dugaan duplikasi

Visual brief: **Panel profil**. Label/relasi: Tipe/satuan | missing | distribusi | dugaan duplikasi. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Tipe/satuan | missing | distribusi | dugaan duplikasi.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL03 — Tujuan batas bukti

Membedakan observasi dari hipotesis penyebab dan memilih pemeriksaan lanjutan

Visual brief: **Memo empat kotak**. Label/relasi: Observasi → hipotesis → keputusan sementara → data tambahan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Observasi → hipotesis → keputusan sementara → data tambahan.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL04 — Prediksi sebelum kode

Hitung missing count dan proporsi duration_min; jelaskan penyebutnya.

Visual brief: **Tabel lima baris**. Label/relasi: Durasi10,20,missing,20,90; kanalA,B,A,B,B. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Durasi10,20,missing,20,90.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W02-SL05 — Mental model

Profil dahulu, kesimpulan dibatasi bukti

Visual brief: **Lensa audit**. Label/relasi: Tabel mentah → pemeriksaan yang didefinisikan → klaim terbatas. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Tabel mentah → pemeriksaan yang didefinisikan → klaim terbatas.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL06 — Istilah pertama

Ketiadaan nilai, dihitung per kolom dengan isna.

Visual brief: **Mask missing**. Label/relasi: false,false,true,false,false; tiap posisi dikaitkan row_id. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: false,false,true,false,false.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL07 — Istilah kedua

Ringkasan nilai yang terlihat pada data, bukan otomatis populasi.

Visual brief: **Garis nilai teramati**. Label/relasi: 10,20,20,90; missing tidak menjadi nol. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: 10,20,20,90.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL08 — Istilah ketiga

Baris identik menurut kolom yang dipilih; harus disebut definisinya.

Visual brief: **Dua definisi duplikat**. Label/relasi: Semua kolom versus subset duration+channel. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Semua kolom versus subset duration+channel.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL09 — Mekanisme awal

isna menghasilkan mask nilai hilang; jumlah True memberi count. Proporsi hilang adalah count/n pada kolom dengan n baris. Missing bukan nol; nol dapat merupakan nilai yang sah.

Visual brief: **Pecahan missing**. Label/relasi: 1/5 = 20%; penyebut seluruh baris. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: 1/5 = 20%.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL10 — Trace keputusan

Hitung median dan mean nilai teramati. Tentukan duplikat berdasarkan duration_min+channel, keep=first.

Visual brief: **Trace median/mean**. Label/relasi: Urutkan empat nilai, tandai dua tengah, catat jumlah140. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Urutkan empat nilai, tandai dua tengah, catat jumlah140.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W02-SL11 — Worked example

Tabel SIMULASI lima baris: durasi menit [10,20,missing,20,90], kelas kanal [A,B,A,B,B]. Missing durasi=1/5=20%; median nilai teramati [10,20,20,90]=20; mean=35. Dengan subset durasi+kanal dan keep=first, baris keempat mengulang baris kedua sehingga count duplikat=1. Angka 90 adalah observasi jauh dari nilai lain; salah ukur hanya hipotesis sampai proses ukur diperiksa.

Visual brief: **Tabel ringkasan terverifikasi**. Label/relasi: n5, missing1, median20, mean35, duplicate_subset1. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: n5, missing1, median20, mean35, duplicate_subset1.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL12 — Mekanisme berikutnya

duplicated menghitung pengulangan sesuai subset kolom; mempertahankan kemunculan pertama membuat jumlah duplikat lebih kecil daripada jumlah baris pada kelompok berulang. Nyatakan subset dan keep yang dipakai.

Visual brief: **Panel duplikat**. Label/relasi: Baris4 dibanding baris2; row_id dikecualikan dengan alasan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Baris4 dibanding baris2.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL13 — Batas metode

describe merangkum kolom numerik. Mean dan median merangkum data berbeda; pada contoh kecil bandingkan keduanya tanpa klaim distribusi populasi atau sebab.

Visual brief: **Peta batas data**. Label/relasi: Observasi pada lima baris berbeda dari dugaan populasi. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Observasi pada lima baris berbeda dari dugaan populasi.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL14 — Miskonsepsi

Satuan, duplikasi, bias cakupan dan waktu tetap perlu diperiksa.

Visual brief: **Mitos–koreksi**. Label/relasi: Nilai jarang bukan bukti salah ukur. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Nilai jarang bukan bukti salah ukur.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL15 — Kritik klaim

Nilai 90 membuktikan kesalahan ukur? Tulis observasi, hipotesis, keputusan sementara dan pemeriksaan lanjutan.

Visual brief: **Memo kosong**. Label/relasi: 90 → apa observasi dan apa hipotesis? Mahasiswa isi. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: 90 → apa observasi dan apa hipotesis? Mahasiswa isi.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.

### W02-SL16 — Periksa asumsi

Korelasi/pola bersama belum membuktikan sebab. Memo harus memisahkan observasi, dugaan, keputusan sementara dan data tambahan. Jangan menghapus outlier semata karena jarang; periksa satuan dan proses ukur.

Visual brief: **Checklist proses ukur**. Label/relasi: Periksa satuan, log, konteks, waktu dan provenance. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Periksa satuan, log, konteks, waktu dan provenance.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL17 — Koreksi kekeliruan

Nilai 90 bisa sah; audit konteks sebelum menghapus.

Visual brief: **Kartu kualitas**. Label/relasi: Tidak missing tetap dapat duplikasi/satuan salah/bias cakupan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Tidak missing tetap dapat duplikasi/satuan salah/bias cakupan.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL18 — Rangkuman

Profil dahulu, kesimpulan dibatasi bukti; keputusan dan alasan ditelusuri dari input.

Visual brief: **Ringkasan profil**. Label/relasi: Pemeriksaan yang jelas → angka → interpretasi terbatas. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Pemeriksaan yang jelas → angka → interpretasi terbatas.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL19 — Remediasi

Jika indikator belum teramati, ulangi satu contoh dan telusuri asal informasi.

Visual brief: **Tangga audit ulang**. Label/relasi: Pilih satu kolom, ulangi definisi, tautkan bukti. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Pilih satu kolom, ulangi definisi, tautkan bukti.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; hubungkan ke tahap berikutnya. Tidak memuat kunci/solusi.

### W02-SL20 — Exit ticket

Tulis satu keputusan, satu bukti dan satu batas; ajukan pertanyaan yang masih harus diperiksa.

Visual brief: **Exit card**. Label/relasi: Satu temuan | satu dugaan | pemeriksaan tambahan. Tidak menghasilkan aset gambar atau menambah angka di luar contoh.

Takeaway: Satu temuan | satu dugaan | pemeriksaan tambahan.

Sitasi: BOOK konsep/worked example; [snapshot sumber](../../../references/technical-runtime-sources.md).

Notes aman: baca pesan lalu periksa pemahaman; minta output mahasiswa sebelum debrief dosen. Tidak memuat kunci/solusi.
