---
artifact_id: SEM-05
title: Arsitektur belajar semester
course_code: IF52510031
period: 2026–2027
week: null
classes:
- IF24A
- IF24H
audience: dosen
distribution: instructor_only
version: '0.1'
updated_at: '2026-10-07'
owner: Codex — penyusun; owner sumber dipertahankan di backlog
source_status: REVIEW
production:
  repo_status: DRAFT
markdown_readiness: DRAFT
fulfillment: PARTIAL
source_verification: PARTIAL
official_alignment: PROVISIONAL
learning_ids: []
official_outcome_refs: []
assessment_ids: []
example_ids: []
evidence_requirement_ids: []
source_ids:
- SRC-WORKBOOK
- SRC-MASTER-PROMPT
dependencies:
- SEM-02
integration_refs: []
workbook_dependencies: SEM-02
scope_record: course/production/reports/20261007-180725-P04-foundation-ticket.md
validation_records:
- course/production/reports/20261007-180725-P04-foundation-validation.md
blockers:
- 'S01–S03: keselarasan/ketentuan resmi PROVISIONAL; tidak menahan scope naskah pedagogi'
class_adaptations: PROVISIONAL
delivery_evidence: []
---

# Arsitektur belajar semester

RANCANGAN; identitas/topik/kode dari workbook, pedagogi adalah USULAN. S01–S03 belum terbaca; tidak menetapkan jam, bobot, AI, mode kelas atau pengesahan. Fokus detail W01–W04; minggu lain konteks planned.

## Spine dan prasyarat

Govern mengunci baseline dan gap; Know membangun istilah/konsep; Learn menggerakkan tindakan; Prove memeriksa bukti per LO; Compound menyimpan revisi yang ditelusuri. Urutan belajar: masalah → profil data → transformasi → validasi → pemodelan → generalisasi → sintesis proyek. Urutan produksi pilot W04 lebih dahulu berbeda dari urutan mahasiswa.

| Transisi | Bekal yang harus ada | Aksi penguatan | Bukti sebelum beralih |
| --- | --- | --- | --- |
| W01 → W02 | Unit, fitur, target, waktu fitur | Klasifikasikan kasus dan tulis problem statement | W01-EV01: alasan kategori dan framing |
| W02 → W03 | Tipe, satuan, missingness, duplikasi | Profil data lalu pisahkan fakta/hipotesis | W02-EV01: profil serta memo |
| W03 → W04 | fit/transform dan asal parameter | Trace transformasi training ke data baru | W03-EV01: peta dan trace |
| W04 → W05/06/07 | Batas training/dev/test; unit/kelompok/waktu | Pilih evaluasi sebelum model | W04-EV01: matriks skenario, diagram, trace |
| W04+W05 → W09/10 | Validasi kandidat dan generalisasi | Jaga data test independen dari pemilihan | Memo model selection planned |
| W03+W04+W10 → W11/12 | Transformasi dan evaluasi jaringan | Gunakan jalur CPU/konseptual usulan | Artefak semester selanjutnya deferred |
| W13 → W14 → W15 | Risiko, reproduksi dan komunikasi | Audit keputusan dan paket demo | Proyek belum diproduksi |

## Bridge pilot W04

Pilot mengulang empat istilah: unit observasi adalah objek satu baris; fitur adalah input tersedia pada saat prediksi; target adalah keluaran yang hendak ditaksir; parameter transformasi diperoleh saat fit dan dipakai saat transform. Uraian bersumber pada dokumentasi API lokal, bukan rumusan kurikulum. Masukkan diagnosis fitur masa depan, tabel berkelompok dan trace fit/transform sebelum skenario W04. Jika diagnosis gagal, gunakan bridge di scope/bab W04; jangan menyatakan mahasiswa telah mengambil W01–W03.

## Peta minggu WHY/WHAT/HOW

| Minggu | Topik baseline | WHY/tujuan rancangan | HOW/bukti rencana |
| --- | --- | --- | --- |
| W01 | Pengantar AI dan Machine Learning | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W02 | Eksplorasi Data untuk ML | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W03 | Preprocessing dan Feature Engineering | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W04 | Pembagian Data dan Validasi | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W05 | Klasifikasi I: KNN dan Decision Tree | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W06 | Regresi Linear dan Metrik Evaluasi | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W07 | Clustering dan Metrik Clustering | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W08 | UTS | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W09 | Klasifikasi II dan Model Selection | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W10 | Generalisasi, Overfitting, dan Regularisasi | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W11 | Jaringan Syaraf Tiruan | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W12 | Pengantar Deep Learning dan Generative AI | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W13 | Responsible AI | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W14 | Pipeline ML End-to-End dan Reproduksibilitas | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W15 | Presentasi Proyek Akhir | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |
| W16 | UAS | Mengembangkan keputusan yang ditopang bukti, sesuai topik | Fokus W01–W04: LO/ASM/EV pada governance; lainnya slot usulan, deferred |

W08=UTS dan W16=UAS; masing-masing tujuh artefak ujian, bukan bab. Cakupan/bentuk resmi belum diketahui. W15 merupakan klinik/presentasi, tidak menambah algoritma demi simetri.

## IF24A/IF24H dan beban

| Kelas | Fakta | Pilihan USULAN | Risiko/cek |
| --- | --- | --- | --- |
| IF24A | Tercantum Dashboard!B5; sumber operasional belum dibaca | Diskusi langsung bila mode mendukung; alternatif anotasi mandiri | Periksa durasi dan pengalaman Python melalui diagnosis |
| IF24H | Tercantum Dashboard!B5; label tracker tidak menetapkan jadwal | Tabel/trace teks dan checkpoint asinkron bila diperlukan | Pertahankan LO/bukti yang sama; jangan mengasumsikan akses jaringan |

Rencana beban per minggu dimulai dari modul, diukur saat pilot; tidak ditetapkan dari SKS yang belum tersedia. Core tidak memerlukan GPU/AI berbayar. Integrasi governance: SEM-01–04 sudah draft; crosswalk resmi tetap provisional. Sumber: workbook Production_Backlog!C:D dan master §1.H/§20; lihat register untuk batas otoritas.
