# Scope W03

Fokus: Preprocessing dan Feature Engineering. Dua LO USULAN: W03-LO01 Memilih transformasi berdasarkan tipe fitur dan kebutuhan model; W03-LO02 Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru. Kode baseline: DAIML-Sub-CPMK102-1; bukan rumusan resmi.

## Cakupan dan batas

Must-cover: Fit, Transform, Imputasi, Scaling, One-hot, Pipeline. Must-not-add: klaim performa populasi, kebijakan institusi, data pribadi, katalog algoritma lanjutan atau eksperimen yang tidak dijalankan. Pengayaan nested CV pada W04 hanya penjelasan batas, bukan tuntutan algoritma.

## Prasyarat dan bridge

Unit observasi=baris objek kasus; fitur=input tersedia saat keputusan; target=keluaran yang diminta; fit=belajar keadaan pada training; transform=terapkan pada data berikutnya. Diagnosis: tunjukkan unit, target dan informasi yang belum tersedia pada waktu prediksi. W04 pilot memakai bridge ini karena W01–W03 belum diproduksi saat pilot; prasyarat belajar tidak berubah oleh urutan produksi.

## Kontrak contoh dan traceability

W03-EX01 SIMULASI; angka/konteks tercantum pada DATA. LO01 → BOOK konsep → ACT01 prediksi → ASM01/Q01 → RC01 → EV01 tabel alasan. LO02 → BOOK mekanisme → ACT02 trace/kritik → ASM01/Q02,Q03 → RC02 → EV01 diagram/memo. Worksheet menggunakan WK01–WK03; asesmen Q01–Q03 lokal formatif. DATA/LAB tidak mengklaim notebook/dataset fisik terbit. Sumber teknis runtime; hasil run di reports. Test demo W04 tidak menjadi final holdout proyek.

## Kelas dan distribusi

IF24A/IF24H tercantum baseline; mode/jam resmi belum diketahui. Pilihan diskusi langsung atau anotasi mandiri USULAN dengan LO/bukti sama. Mahasiswa: BOOK/MOD/SLIDE/DATA/LAB/WORK/AIP/ASSESS. Dosen: GUIDE/STORY/RUBRIC/LMS/EVID/QA dan lab-solution; metadata bukan akses kontrol. Target 20 naskah slide, empat aksi; render tidak dibuat.

## Keadaan setelah rekonsiliasi

Keempat paket W01–W04 kini tersedia; bridge tetap dapat dipakai untuk diagnosis. Urutan belajar W01→W02→W03→W04, produksi dimulai W04. Data contoh tiap pekan berbeda dan diberi provenance; parameter/angka tidak dipindahkan lintas kasus. Klaim test independen proyek belum dibuat.

## Matriks butir final

| LO | Soal/worksheet | Rubrik | Bukti |
| --- | --- | --- | --- |
| W03-LO01 | W03-Q01/WK01 | W03-RC01 | W03-EV01: Memilih transformasi berdasarkan tipe fitur dan kebutuhan model |
| W03-LO02 | W03-Q02/WK02, W03-Q03/WK03 | W03-RC02 | W03-EV01: Menjelaskan batas belajar parameter transformasi dan penggunaan kembali pada data baru |
