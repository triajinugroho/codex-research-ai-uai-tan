# Validasi 20261007-182157-P22-P16-final-technical

- Command authoring/run: tercatat di hasil exec dan recipe `/tmp`; pemeriksaan dilakukan pada output yang tersimpan.
- Hasil: PASS pada scope P22 akhir: delapan eksekusi kode tersimpan, kontrol negatif/edge dan oracle aritmetika. Link lokal diperiksa: 177. Sumber resmi PROVISIONAL; tidak ada klaim RPS/RTM disahkan.
- Gate G0: sumber lokal/runtime mendukung scope; G1: LO dan batas terpetakan. G3 berlaku hanya jika run kode tercatat. Gate yang tidak berlaku diberi alasan pada hasil berikut.

| Pemeriksaan | Hasil aktual |
| --- | --- |
| W01 lab.md | PASS exit0: {'id': 'C1', 'input': 'email saat diterima', 'target': 'spam/tidak'}<br>{'id': 'C2', 'input': 'konsumsi historis', 'target': 'kWh esok'}<br>{'id': 'C3', 'input': 'profil belanja', 'target': None}<br>{'id': 'C4', 'input': 'suhu saat ini, aturan tetap', 'target': None}; elapsed_s=0.0103 max_rss_kib=17012; command python3 /tmp/course_time_wrapper.py /tmp/W01-lab.md-verify.py |
| W01 lab-solution.md | PASS exit0: {"case_ids": ["C1", "C2", "C3", "C4"], "kinds": 4, "fixed_rule_has_fit": false}; elapsed_s=1.0062 max_rss_kib=111268; command python3 /tmp/course_time_wrapper.py /tmp/W01-lab-solution.md-verify.py |
| W02 lab.md | PASS exit0: row_id  duration_min channel<br>      1          10.0       A<br>      2          20.0       B<br>      3           NaN       A<br>      4          20.0       B<br>      5          90.0       B<br>row_id            int64<br>duration_min    float64<br>channel          object<br>dtype: object; elapsed_s=0.2379 max_rss_kib=54136; command python3 /tmp/course_time_wrapper.py /tmp/W02-lab.md-verify.py |
| W02 lab-solution.md | PASS exit0: {"shape": [5, 3], "missing": 1, "missing_pct": 20.0, "median": 20.0, "mean": 35.0, "duplicates_subset": 1}; elapsed_s=0.2602 max_rss_kib=54388; command python3 /tmp/course_time_wrapper.py /tmp/W02-lab-solution.md-verify.py |
| W03 lab.md | PASS exit0: volume channel<br>    1.0       A<br>    NaN       B<br>    3.0       A<br>    5.0       B<br> volume channel<br>    NaN       C<br>    7.0       A; elapsed_s=0.2343 max_rss_kib=54136; command python3 /tmp/course_time_wrapper.py /tmp/W03-lab.md-verify.py |
| W03 lab-solution.md | PASS exit0: {"median_training": 3.0, "mean_training": 3.0, "scale_training": 1.4142135623730951, "new_transformed": [[0.0, 0.0, 0.0], [2.82842712474619, 1.0, 0.0]], "shape_training": [4, 3]}; elapsed_s=1.0853 max_rss_kib=122012; command python3 /tmp/course_time_wrapper.py /tmp/W03-lab-solution.md-verify.py |
| W04 lab.md | PASS exit0: Ukuran dev/test: 90 30; elapsed_s=1.0121 max_rss_kib=118852; command python3 /tmp/course_time_wrapper.py /tmp/W04-lab.md-verify.py |
| W04 lab-solution.md | PASS exit0: {"seed": 42, "n_dev": 90, "n_test": 30, "fold_scores": [0.5333333333333333, 0.5333333333333333, 0.5], "mean_cv": 0.5222222222222223, "group_overlap": false, "last_time_fold": [47, 50, 59], "holdout_demo_now_exposed": true}; elapsed_s=1.1710 max_rss_kib=125144; command python3 /tmp/course_time_wrapper.py /tmp/W04-lab-solution.md-verify.py |
| W02 negative | PASS: all_columns=0; intended_subset=1; definition matters; command independent duplicated all/subset |
| W03 negative | PASS: 3 versus4; wrong fit diagnosed; not performance comparison; command independent median train/combined |
| W03 edge | PASS: ValueError unknown; constant outputs0; matches local documentation; command OneHotEncoder default unknown; StandardScaler constant |
| W04 negative | PASS: at least1 group overlap; stratification != group exclusion; command stratified split with repeated group IDs |
| Runtime | {"numpy": "2.3.5", "pandas": "2.2.3", "scikit-learn": "1.8.0", "PyYAML": "6.0.3"} |
| Source hashes | Dokumentasi snapshot dan metadata/file aktual disimpan pada report |
| Scope | Kode inti aktual; bukan hasil mahasiswa atau benchmark generalisasi |

## Versi output

| Path | SHA-256 |
| --- | --- |
| course/weeks/w01/book-chapter.md | 08033eec5e4520b52579e696b774c8f5b8c7e2f38d1a34e1ed8b67a30b7f640b |
| course/weeks/w01/student-module.md | d05c371802718c388a51cf6e9821eb00d1031c13bd8bd6ec582987c180fa39d8 |
| course/weeks/w01/lecturer-guide.md | c11f10552f3f4cfaca317178a44b80fb02378771221eb0572e3079660398d90d |
| course/weeks/w01/storyboard.md | 923df568d1cfc283e3cb4fc528a449a7efffe1a8b3de727be7078431e2fd89dc |
| course/weeks/w01/slides.md | 6f4cdc87c7aface77cc67bea1aa581826af6428ac761221af1b882e06da523df |
| course/weeks/w01/dataset-case.md | 547700876eaa66ae0fea4eac3a5e511a04cf3d461f684ba458dfa8c9ccb62cff |
| course/weeks/w01/lab.md | 3482ed5c1785d55e19d3c27982cd5a44391f5b33c90a357015279f769faa0a41 |
| course/weeks/w01/worksheet.md | 8ba31294b6652b48ef282cceba656f156107af808ad90bae0afea43d6e06543f |
| course/weeks/w01/ai-learning-prompts.md | dc50ecec61c4dd5600caad1684e874f76e49e8e6f4e52adf73616c63493898bf |
| course/weeks/w01/assignment-quiz.md | 176dd3eb216aec8f5ff1dca029ed364b6caff46b17e5a8c6a656a1d2183e44dd |
| course/weeks/w01/rubric-answer-key.md | 02d5200ba9974ebfe7031487cde088363a2b26a105f8af19137842eefdbeec68 |
| course/weeks/w01/lms-package.md | 2bf43a63564974bf0d53dc658f60e575b5fc0c0e7c966aa3559e984a7ef43ec8 |
| course/weeks/w01/evidence-spec.md | 1e65e4a7f1282b46c570dbd0f7e345c156f6623fdf61a206ac4c71c988183db4 |
| course/weeks/w01/post-class-qa.md | 3ed6f270f3971231a719d9839baf22203d050a526faa39a8ea03516dd0e552d2 |
| course/weeks/w02/book-chapter.md | 9540d099d2508612e39f902c3dbc76014ac30e238dd5a14b51589296abc08324 |
| course/weeks/w02/student-module.md | ac6f954c08473cae129638fe11a9b45646cbbc44e5fb040bc517788f930381ff |
| course/weeks/w02/lecturer-guide.md | 24ec130b4159624cfe86279b7186b218331fef3dc1edf4130fc02473612b66ca |
| course/weeks/w02/storyboard.md | a9854b5b6a422590b6d6dcb3d000f11408ac0b81610218fc30142d19527b5327 |
| course/weeks/w02/slides.md | 4c0b086159a1011165969a55651e65f7e2ded7b8cc8104cc8b22b43af34d28c8 |
| course/weeks/w02/dataset-case.md | abfaf3353f1d35cf87ec8f70195daef519b7d8e5079918d161e8364c7caa0293 |
| course/weeks/w02/lab.md | 70c1abd370ae775809188049925e4ba13923b45ee71580f629fb73aa9e3f7dae |
| course/weeks/w02/worksheet.md | 8019561b0a1a76e2d172a87a1c4a1049b39329880b5b90406dcad80f166ec125 |
| course/weeks/w02/ai-learning-prompts.md | b5af6d8429f342fa0f485af71ae926cd07aa97e9e387c908e2f77c9f2b35cf42 |
| course/weeks/w02/assignment-quiz.md | 144ac7232ffb85d3d58478d378bb55f67d1eb41ba455501c958232d1dd97a994 |
| course/weeks/w02/rubric-answer-key.md | dd3128fcf64777bfc6abdde561347b4d48eb82c7bb881267acb2c8162c11d42c |
| course/weeks/w02/lms-package.md | 0a8c09c6ec9e18570caf3b9ddf644aa953f2e86e0eefc556ea42d75c6db7aa38 |
| course/weeks/w02/evidence-spec.md | 924ca505584ef927d7e85e9faf480c40b6d0c6eac5eabb31e10aeeb5d55eac45 |
| course/weeks/w02/post-class-qa.md | 35de5b8aabe159c4b8f46030534f5151e9da00b1205ee576ab2aa6da39a6e716 |
| course/weeks/w03/book-chapter.md | a5d6c4beae40860bfaa36386d49c29cbc33391fe149a173e007206772bebf4a0 |
| course/weeks/w03/student-module.md | 97a2b3cd9d74a1b0a70ca399869430f420e1cf568be05e41fc5368387a15d976 |
| course/weeks/w03/lecturer-guide.md | dc692e6f5d0d77ef755bb50f4d2f041e7f8c12875b11e31aaa4dc1208ccb49dd |
| course/weeks/w03/storyboard.md | 932ea7dd91fc7c52417c67522e480a1deb0882b8440d1595f634d95674111007 |
| course/weeks/w03/slides.md | b16b784e1b0e230c58ec47529b96d732c318a6d882c1dad545917c013c0f6946 |
| course/weeks/w03/dataset-case.md | 6249b4098571d4a0b3758f474e6b82c3a17baf7072836621117512d97a6e4d2b |
| course/weeks/w03/lab.md | 1db054f15e6322e2129ae413eb9b6e44639ef09b514fba9ed3fbe1e4a5b20c92 |
| course/weeks/w03/worksheet.md | d4f9b6727cca951635e858f81cf04041d53e8d2bd2fc08a5c88d0618e0f4b3d4 |
| course/weeks/w03/ai-learning-prompts.md | 75863fec2fa39c6a6cc2b1959d2808b83a2a22d1fede52b1910c73aa6b06d3f9 |
| course/weeks/w03/assignment-quiz.md | 6c52d699be14bc9264efc952869b5cb809177f3f0b97e11100ce3c968e7e6fe7 |
| course/weeks/w03/rubric-answer-key.md | 750f77d03b48b513791798c11809e7c16a668660947d6752bb6cd72423768038 |
| course/weeks/w03/lms-package.md | 9f3736231669c54c0097b1fe7cbefdd26a5cad71a036ff32ec854074d36033d0 |
| course/weeks/w03/evidence-spec.md | 2b619406d5e63c21ef91e59457f05179c69edd469cb1fbee372bfdb7b764e18d |
| course/weeks/w03/post-class-qa.md | 501694e49a7071a44b63dc50e36556c9e8a069c1ec7e3f5dd1ede01e813da47b |
| course/weeks/w04/book-chapter.md | 7c36ecd57a42d114d3a6b2e0e9c60b364c57d666f5af593f07e648f72c773900 |
| course/weeks/w04/student-module.md | 85103fda5894d0102d3f3b4816effdeae57a4cfd326cef5f80ccb6021280d392 |
| course/weeks/w04/lecturer-guide.md | 51c695d203ab96c254691926f208b3b4df65b8e982df94500fb52b5279766452 |
| course/weeks/w04/storyboard.md | 379a60f72b9a4d57237dae70acc933a85a106d9c789e6e3154ae8bc6372e4286 |
| course/weeks/w04/slides.md | abdb434f745371bd6399d56f217b0e02d68987744af44a06d41a199e6a414248 |
| course/weeks/w04/dataset-case.md | 10fe813418d9a8a2b34fd27dbb604fef58db51a81d665d148b42e73897872bb9 |
| course/weeks/w04/lab.md | 99d13b418c5984b5ab2bcff9767ccf2debea750df7471240ed628b7337659f4a |
| course/weeks/w04/worksheet.md | 4ccbdf69244b4cab76618ca5ce9f3aa31debc73d7359874d5021b4f72e16f3b7 |
| course/weeks/w04/ai-learning-prompts.md | f974218bccf3380d0c324ebd008851034e831317b4e79762426f69daf5b876c9 |
| course/weeks/w04/assignment-quiz.md | dc53e607c513ebe6a90fe376e84907409497bee401604dd41705b78e2fefe1ed |
| course/weeks/w04/rubric-answer-key.md | 3df33b89ce6ccbd964578865685db1b11a9962fae36b07ff48a5ec2fba5540a0 |
| course/weeks/w04/lms-package.md | 18c7fae281944fc196a872a6f348d950a0d4c208355110a62edfa8772e83fbb5 |
| course/weeks/w04/evidence-spec.md | a4839646869b29c0859c26019dcb69785693c3ceb3768d2faed1bfd795d971fe |
| course/weeks/w04/post-class-qa.md | 0238f2b952d8bde11a742620a5d9fa0e8017bd52e68983ea381d844859fa588f |
| course/production/dashboard.md | 67f85cb5409a7c97ebf8a2b141a559a9b470aea97fa46b2e2f1fc67861e6285a |
| course/production/semester-backlog.md | 87cb2f35479097d3bd930649008fe8744559365ce9021e3e4bc01e934ac1c9ac |
| course/production/weekly-backlog.md | c685107979ad782d5bf02ba4d02cfa5f005433518b05593c2ea3fad3bd6a83fb |
| course/production/reports/20261007-182157-P22-P16-final-technical-ticket.md | 1694b5cb714990dd0c977f5308a6805b1e686187aa9ccb3c68b8693b1955c8a9 |

## Perintah, runtime, output dan versi input aktual

| Target | Command | Outcome | stdout | Timing/memory/batas | SHA-256 Markdown |
| --- | --- | --- | --- | --- | --- |
| W01 lab.md | python3 /tmp/course_time_wrapper.py /tmp/W01-lab.md-verify.py | PASS exit0 | {'id': 'C1', 'input': 'email saat diterima', 'target': 'spam/tidak'}<br>{'id': 'C2', 'input': 'konsumsi historis', 'target': 'kWh esok'}<br>{'id': 'C3', 'input': 'profil belanja', 'target': None}<br>{'id': 'C4', 'input': 'suhu saat ini, aturan tetap', 'target': None} | elapsed_s=0.0103 max_rss_kib=17012 | 5d9204694a1acfcb2d4512bebe4361a9d5a316ca8b8b5f463e481146fd3c1840 |
| W01 lab-solution.md | python3 /tmp/course_time_wrapper.py /tmp/W01-lab-solution.md-verify.py | PASS exit0 | {"case_ids": ["C1", "C2", "C3", "C4"], "kinds": 4, "fixed_rule_has_fit": false} | elapsed_s=1.0062 max_rss_kib=111268 | 146303f7e0f28d8d9929e8f8ed2a9e856db8a032f77e220cb629fd69f14342d9 |
| W02 lab.md | python3 /tmp/course_time_wrapper.py /tmp/W02-lab.md-verify.py | PASS exit0 | row_id  duration_min channel<br>      1          10.0       A<br>      2          20.0       B<br>      3           NaN       A<br>      4          20.0       B<br>      5          90.0       B<br>row_id            int64<br>duration_min    float64<br>channel          object<br>dtype: object | elapsed_s=0.2379 max_rss_kib=54136 | a4546eec2477bf37ce145d74fe182d8cd3c4ec1913d0ef33fb2be089d74d1f16 |
| W02 lab-solution.md | python3 /tmp/course_time_wrapper.py /tmp/W02-lab-solution.md-verify.py | PASS exit0 | {"shape": [5, 3], "missing": 1, "missing_pct": 20.0, "median": 20.0, "mean": 35.0, "duplicates_subset": 1} | elapsed_s=0.2602 max_rss_kib=54388 | 5626da11423f36b53fe9e5d9226853ce811bd1ef1559a5d150e6f668ddcb0d7f |
| W03 lab.md | python3 /tmp/course_time_wrapper.py /tmp/W03-lab.md-verify.py | PASS exit0 | volume channel<br>    1.0       A<br>    NaN       B<br>    3.0       A<br>    5.0       B<br> volume channel<br>    NaN       C<br>    7.0       A | elapsed_s=0.2343 max_rss_kib=54136 | 9cd172bc77a71e3fc7d0cb46a6543c3661de91afbadf53440d45457eb9ca5bd3 |
| W03 lab-solution.md | python3 /tmp/course_time_wrapper.py /tmp/W03-lab-solution.md-verify.py | PASS exit0 | {"median_training": 3.0, "mean_training": 3.0, "scale_training": 1.4142135623730951, "new_transformed": [[0.0, 0.0, 0.0], [2.82842712474619, 1.0, 0.0]], "shape_training": [4, 3]} | elapsed_s=1.0853 max_rss_kib=122012 | 96678b6bf940cfc3fc744f2fec3c09aee1200449cdce4c46965181322ddc8725 |
| W04 lab.md | python3 /tmp/course_time_wrapper.py /tmp/W04-lab.md-verify.py | PASS exit0 | Ukuran dev/test: 90 30 | elapsed_s=1.0121 max_rss_kib=118852 | f3f551a6841758c20191a8929d74ed808673d810214f7e43c0cb752bb40e33ee |
| W04 lab-solution.md | python3 /tmp/course_time_wrapper.py /tmp/W04-lab-solution.md-verify.py | PASS exit0 | {"seed": 42, "n_dev": 90, "n_test": 30, "fold_scores": [0.5333333333333333, 0.5333333333333333, 0.5], "mean_cv": 0.5222222222222223, "group_overlap": false, "last_time_fold": [47, 50, 59], "holdout_demo_now_exposed": true} | elapsed_s=1.1710 max_rss_kib=125144 | a9f6009094190bbb5579416b0cca0751e95c5ac844f0f0bf7b51d7f629e6b2eb |
| W02 negative | independent duplicated all/subset | PASS | all_columns=0; intended_subset=1 | definition matters | n/a |
| W03 negative | independent median train/combined | PASS | 3 versus4; wrong fit diagnosed | not performance comparison | n/a |
| W03 edge | OneHotEncoder default unknown; StandardScaler constant | PASS | ValueError unknown; constant outputs0 | matches local documentation | n/a |
| W04 negative | stratified split with repeated group IDs | PASS | at least1 group overlap | stratification != group exclusion | n/a |

Python 3.12.14; paket {"numpy": "2.3.5", "pandas": "2.2.3", "scikit-learn": "1.8.0", "PyYAML": "6.0.3"}. CPU, input literal atau seed42; kode diekstrak utuh, assertion tidak dihapus. Timing/RSS adalah pengukuran proses saat ini, bukan batas kelas. Kode tidak perlu jaringan saat run.

## Cara mengulang dari repo

Jalankan dari root repo setelah paket tersedia. Recipe berikut mengekstrak starter/reference yang sebenarnya; tidak menyalin solusi alternatif.

```python
from pathlib import Path
import re, subprocess, tempfile
root = Path.cwd()
for week in range(1, 5):
    for name in ["lab.md", "lab-solution.md"]:
        source = root / f"course/weeks/w{week:02d}" / name
        block = re.findall(r"```python\n(.*?)\n```", source.read_text(), re.S)[0]
        with tempfile.TemporaryDirectory() as task_tmp:
            script = Path(task_tmp) / "run.py"
            script.write_text(block + "\n")
            result = subprocess.run(["python3", str(script)], text=True, capture_output=True)
            assert result.returncode == 0, result.stderr
            print(source, result.stdout)
```
