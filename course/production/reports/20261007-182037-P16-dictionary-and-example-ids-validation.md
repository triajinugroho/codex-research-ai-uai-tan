# Validasi 20261007-182037-P16-dictionary-and-example-ids

- Command authoring/run: tercatat di hasil exec dan recipe `/tmp`; pemeriksaan dilakukan pada output yang tersimpan.
- Hasil: PASS pada scope P16: nama kolom W01 dan contoh EX01–04 W04 konsisten. Link lokal diperiksa: 74. Sumber resmi PROVISIONAL; tidak ada klaim RPS/RTM disahkan.
- Gate G0: sumber lokal/runtime mendukung scope; G1: LO dan batas terpetakan. G3 berlaku hanya jika run kode tercatat. Gate yang tidak berlaku diberi alasan pada hasil berikut.

| Pemeriksaan | Hasil aktual |
| --- | --- |
| Finding DATA | CLOSED id/input/target cocok starter; method hanya anotasi dosen |
| Finding traceability | CLOSED empat contoh W04 mempunyai ID dan peran eksplisit |
| G3 affected W01 | PASS python3 /tmp/W01-dictionary-recheck.py exit0; {"case_ids": ["C1", "C2", "C3", "C4"], "kinds": 4, "fixed_rule_has_fit": false} |
| W04 code | Tidak berubah; hasil run sebelumnya tetap relevan |

## Versi output

| Path | SHA-256 |
| --- | --- |
| course/weeks/w01/dataset-case.md | 692355dee4a6b93cee934e7dde1f94e2570e3006384842cd41b0a93198d2da65 |
| course/weeks/w01/lab-solution.md | 146303f7e0f28d8d9929e8f8ed2a9e856db8a032f77e220cb629fd69f14342d9 |
| course/weeks/w04/book-chapter.md | 6b9ea940588ba7007673dbb399a3572573070ed6373871af02fdee30a091f107 |
| course/weeks/w04/student-module.md | 5665f8e71e619c4612e49ed7883eb43c3d5ba52426d9aa664fa61c2b0f900cb7 |
| course/weeks/w04/lecturer-guide.md | 8d77e19e447086adb05664537112803bd68930fd473c3ea60b37346e3d77e6cc |
| course/weeks/w04/storyboard.md | 19caea88f77ff994428a9aa7712909643407602438a9dc590642e8df5e585961 |
| course/weeks/w04/slides.md | 49e271f91dec4b3c3ea886ccb5cc8250ac1eccb810fe7bacaee06602148f19b9 |
| course/weeks/w04/dataset-case.md | 9354fb284498bef21f8b394b66ccf06bc7d8e208a56404d04b650cab47a6d088 |
| course/weeks/w04/lab.md | f3f551a6841758c20191a8929d74ed808673d810214f7e43c0cb752bb40e33ee |
| course/weeks/w04/worksheet.md | 73afc3ce772f7a96079376b6199dc4b37f5fdb70ca35e2579ba8283100c644c0 |
| course/weeks/w04/ai-learning-prompts.md | 5f3a3b7d0572060ea07d07c81e2c3ef0c287367bbfa0a3720d9d5e299b9c77ce |
| course/weeks/w04/assignment-quiz.md | 42966c007d6dec4a9fcda2407618e82bc419971130e290f337da4fd4af4960a7 |
| course/weeks/w04/rubric-answer-key.md | 9f0400b5cc9e79b7d3600100985fab91aed690bb2ffbaf711d6b9793ad4046d5 |
| course/weeks/w04/lms-package.md | 42f2bbe2101b8127cb7954d334af99c2d125c9a53dfe073156cbb7716c9ef89b |
| course/weeks/w04/evidence-spec.md | 5329b25c40936df6249250ed6def50567f3b4f9744284ed8897997a3f76dca88 |
| course/weeks/w04/post-class-qa.md | a4a95890966d73648e61ec124ffd7c8b72485d7ed5b59bf45583ed0e2633f3d7 |
| course/production/dashboard.md | 42ab1d72a4a92328d950b4d54dc236bd5e6c92f0211afc99afb9246b1c83f63a |
| course/production/semester-backlog.md | 87cb2f35479097d3bd930649008fe8744559365ce9021e3e4bc01e934ac1c9ac |
| course/production/weekly-backlog.md | c685107979ad782d5bf02ba4d02cfa5f005433518b05593c2ea3fad3bd6a83fb |
| course/production/reports/20261007-182037-P16-dictionary-and-example-ids-ticket.md | 4f5f79b57a07cce2f56658edadfeacfc56f37435ad0bdeed0bf3c70f4677b41b |
