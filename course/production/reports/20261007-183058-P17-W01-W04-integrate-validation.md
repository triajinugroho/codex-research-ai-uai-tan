# Validasi 20261007-183058-P17-W01-W04-integrate

- Command authoring/run: tercatat di hasil exec dan recipe `/tmp`; pemeriksaan dilakukan pada output yang tersimpan.
- Hasil: PASS pada scope P17: 56/56 naskah fokus terintegrasi; sumber/akademik/delivery terpisah. Link lokal diperiksa: 63. Sumber resmi PROVISIONAL; tidak ada klaim RPS/RTM disahkan.
- Gate G0: sumber lokal/runtime mendukung scope; G1: LO dan batas terpetakan. G3 berlaku hanya jika run kode tercatat. Gate yang tidak berlaku diberi alasan pada hasil berikut.

| Pemeriksaan | Hasil aktual |
| --- | --- |
| G6 initial checker | FAIL checker menolak link folder references/ yang sudah ada di README; bukan berkas hilang. Checker dikoreksi untuk link folder bertanda /. |
| G6 corrected | PASS link file dan folder existing resolve |
| Focus | 56/56 VALIDATED pada scope pedagogi/teknis/spec |
| Official/DoD | PROVISIONAL/PARTIAL; bukan final akademik/deck/LMS/delivery |
| Input/publication | Tidak ada commit/push/publish |

## Versi output

| Path | SHA-256 |
| --- | --- |
| course/index.md | 1604d1896313bcf35b8461013c382924483a6d379c0277d62b22556e92129943 |
| course/instructor-index.md | 21577d9bee1c2953037b8b12b4cc763d096520604da3165c8f3d5bf72954b196 |
| README.md | 7063805f879ef7328589a2b3858f2d2d628294d9fd970a729697eabe35ac27a0 |
| course/production/sources.md | 0ed3d7cb95731bf44bf4403b2339991050d94ced1cf7b6bbedcdabf77c9cad6f |
| course/production/decisions.md | 45ff0d3efa75fe6f1af51bd36dcf01cfb6dc50ba0fd47da3fbc759d8a395166d |
| course/production/dashboard.md | a49305c6d65481be2e16ef2d5af947e9be0ae7909810d90b7749c67ce73ac90e |
| course/production/semester-backlog.md | 5c1e29e9bdc6f4b7a1aa7d1e8ccf0b6f005f4121f6c8c413223754cbee5864b6 |
| course/production/weekly-backlog.md | 17f666dc50a15c2a4dec37327080e919cbdc36886cde28304d1d21d05c80f60f |
| course/production/reports/20261007-183058-P17-W01-W04-integrate-ticket.md | 13b17912a572b92eb325bbf6c23ecc8b610b666c5234f2754c4aab58dcd37044 |

## Bukti audit final

[Audit terakhir](20261007-183058-P17-W01-W04-integrate-final-validation.md) selesai PASS pada sembilan pemeriksaan aktual. Berisi hash56 artefak final, inventory/source preservation, seluruh link/anchor, rute student, tag final dan bukti run teknis. Angka kesiapan bukan dari jumlah file helper.
