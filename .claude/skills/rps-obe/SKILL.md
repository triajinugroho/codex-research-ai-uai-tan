---
name: rps-obe
description: Menyusun, memperbarui, atau memeriksa RPS dan rantai OBE (CPL → CPMK → Sub-CPMK → LO lokal → materi → aktivitas → asesmen → rubrik → bukti) untuk mata kuliah Dasar AI & ML IF52510031 di repo ini. Pakai setiap kali menyentuh course/governance/ (rps.md, rtm.md, assessment-blueprint.md, curriculum-audit.md), menambah LO/asesmen/rubrik untuk pekan baru (W05–W16, UTS, UAS), menyelaraskan paket pekan dengan RPS, atau saat diminta "cek keselarasan OBE", "update RPS", "buat RTM/rubrik pekan N".
---

# RPS & OBE — Dasar AI & ML (IF52510031)

Skill ini menjaga agar setiap perubahan pada RPS dan paket ajar tetap berbentuk **rantai OBE yang dapat ditelusuri** dan **jujur terhadap status sumber**. Aturan rinci sudah ada di repo; skill ini menunjuk ke sana dan merangkum hal yang paling sering salah.

## Sumber kebenaran (baca dulu bagian yang relevan)

| Kebutuhan | File |
| --- | --- |
| Kontrak metadata, enum status, pola ID, matriks penelusuran | `planning/ARTIFACT_SPECS.md` §2, §2.1, §2.2 |
| Isi wajib SEM-01…SEM-04 (audit, RPS, RTM, blueprint) | `planning/ARTIFACT_SPECS.md` §3 |
| Gate G0–G7, aturan blocker, PASS/FAIL/UNRUN/PROVISIONAL | `planning/QUALITY_GATES.md` |
| DNA pedagogi dan standar paket | `course/standards/teaching-package-os.md` |
| RPS saat ini (peta 16 minggu, LO W01–W04) | `course/governance/rps.md` |
| Katalog tugas ASM, brief mahasiswa vs ketentuan dosen | `course/governance/rtm.md` |
| Matriks LO–ASM–RC–EV dan rubrik kualitatif | `course/governance/assessment-blueprint.md` |
| Outcome baseline, konflik, gap sumber | `course/governance/curriculum-audit.md` |
| Register sumber dan statusnya | `course/production/sources.md` |
| Keputusan produksi (DEC-xxxx) | `course/production/decisions.md` |
| Template artefak | `course/templates/*.md` |

## Rantai OBE yang harus utuh

```
CPL (resmi) → CPMK (resmi) → Sub-CPMK (kode baseline, mis. DAIML-Sub-CPMK102-1)
  → Wnn-LOxx (LO lokal USULAN, verba teramati)
    → materi sebelum asesmen (Wnn-BOOK/MOD + heading)
    → aktivitas/contoh (Wnn-ACTxx / Wnn-EXxx)
    → asesmen/soal (Wnn-ASMxx / Wnn-Qxx)
    → kriteria rubrik (Wnn-RCxx, satu RC per LO)
    → spesifikasi bukti (Wnn-EVxx)
    → sumber substansi (SRC-… + locator)
```

Aturan rantai:
- Setiap LO punya **minimal satu RC tersendiri** dan muncul di RPS, RTM, dan blueprint. Satu EV boleh dipakai dua LO, tetapi tidak menandakan keduanya tercapai.
- Setiap ASM hanya mengukur LO yang **sudah diajarkan** sebelum asesmen. Sebutkan materi prasyaratnya.
- LO memakai verba teramati (mengklasifikasikan, merumuskan, memilih dengan alasan, menghitung, membandingkan, mendeteksi, merancang). Jangan pakai "memahami"/"mengetahui".
- Level kognitif adalah **label rancangan**, bukan taksonomi resmi, sampai sumber kurikulum dibaca.
- ID stabil: jangan membuat ID baru hanya karena isi pindah file. Pola ID ada di `ARTIFACT_SPECS.md` §2.1.

## Kejujuran status (aturan paling penting)

Sumber resmi S01–S03 (kurikulum, RPS resmi, RTM resmi) **belum dibaca**. Karena itu:

1. **Jangan mengarang** rumusan CPL/CPMK, SKS, prasyarat formal, bobot nilai, durasi, tanggal pengesahan, tanda tangan, SK, kebijakan AI/kolaborasi, atau bibliografi (judul, DOI, tahun, penulis).
2. Isi yang belum bersumber ditulis **`PERLU KONFIRMASI SUMBER`**; rancangan lokal diberi label **`USULAN`**. Nilai yang belum ada ditulis "belum tersedia", **bukan nol**.
3. Kode Sub-CPMK dari workbook ditulis apa adanya dengan keterangan **BASELINE** (ekuivalensi resmi belum diperiksa).
4. Judul dokumen tetap **"Rancangan RPS"** sampai sumber resmi diperiksa.
5. Bobot/score produksi di workbook **bukan** bobot nilai mahasiswa.
6. `official_alignment` tetap `PROVISIONAL` sampai ada sumber resmi yang dibaca. `source_status` immutable.
7. `VALIDATED` ≠ deck jadi, LMS terbit, kelas terlaksana, atau DoD terpenuhi. Jangan mengisi `delivery_evidence` tanpa bukti nyata.
8. Dokumen untuk mahasiswa tidak boleh menautkan kunci/solusi.

Jika pengguna memberikan dokumen resmi (kurikulum, RPS institusi, pedoman OBE prodi), daftarkan dulu di `course/production/sources.md` dengan status `VERIFIED_LOCAL`/`VERIFIED_EXTERNAL` dan locator, lalu baru ubah label `PERLU KONFIRMASI SUMBER` yang benar-benar didukung sumber itu.

## Alur kerja

### A. Menambah LO/asesmen untuk pekan baru (mis. W05)

1. Baca baris pekan itu di `rps.md` → *Peta 16 minggu* (topik, kode Sub-CPMK baseline, slot LO usulan) dan brief di `planning/WEEKLY_BLUEPRINTS.md`.
2. Rumuskan 2 LO (`Wnn-LO01`, `Wnn-LO02`) dengan verba teramati dan bukti yang dapat diamati. Periksa kesinambungan dengan pekan sebelumnya (luaran pekan n−1 menjadi input pekan n).
3. Tambahkan secara konsisten di **ketiga** dokumen:
   - `rps.md`: tabel *Capaian dan bahan kajian*, baris pekan di *Peta 16 minggu*, dan tabel *Rancangan belajar*.
   - `rtm.md`: baris katalog `Wnn-ASM01` + brief mahasiswa (Bagian A) + ketentuan dosen (Bagian B).
   - `assessment-blueprint.md`: baris matriks per LO + tabel rubrik tiga level (memadai / parsial / belum menunjukkan indikator).
4. Perbarui metadata YAML tiap file: `learning_ids`, `assessment_ids`, `evidence_requirement_ids`, `official_outcome_refs`, `updated_at` (tanggal nyata), `version`.
5. Jalankan pemeriksa (bagian C) dan perbaiki semua temuan.

### B. Memperbarui RPS dari sumber resmi

1. Daftarkan sumber (lihat aturan 8 di atas).
2. Ubah hanya bagian yang didukung sumber; cantumkan locator (halaman/heading).
3. Catat konflik antara baseline dan sumber resmi di `curriculum-audit.md` → *Konflik, ketidakpastian dan keputusan*, dan keputusan baru di `course/production/decisions.md`.
4. Jika rumusan resmi mengubah makna LO lokal, telusuri dampaknya ke paket pekan (`course/weeks/wNN/`) yang memakai LO tersebut (`grep -rn "Wnn-LOxx" course/`).

### C. Memeriksa keselarasan

```bash
python3 .claude/skills/rps-obe/scripts/check_obe_trace.py
```

Skrip memeriksa: peta 16 minggu lengkap (W01–W16, W08 UTS, W16 UAS), setiap LO di RPS ada di blueprint dan RTM, setiap LO punya RC tersendiri, setiap ASM di katalog RTM menunjuk LO/EV/RC yang ada, serta ID di metadata `learning_ids` cocok dengan isi. Hasilnya PASS/FAIL per cek. FAIL harus diperbaiki atau dijelaskan.

Skrip hanya memeriksa struktur/traceability. Ia **tidak** membuktikan keselarasan resmi, kebenaran isi teknis, atau kualitas rubrik. Untuk itu ikuti gate G1, G2, dan G4 di `planning/QUALITY_GATES.md`.

## Format laporan

Setelah menyelesaikan batch, tulis laporan di `course/production/reports/` mengikuti pola nama yang ada (`YYYYMMDD-HHMMSS-<run>-<scope>-validation.md`) dan sebutkan: scope, file yang diubah, hasil pemeriksa, gate yang dijalankan (PASS/FAIL/UNRUN/NOT_APPLICABLE), serta blocker yang tersisa. Jangan menulis PASS untuk pemeriksaan yang tidak dijalankan.
