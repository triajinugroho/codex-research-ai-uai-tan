#!/usr/bin/env python3
"""Pemeriksa traceability OBE untuk course/governance (RPS, RTM, blueprint).

Hanya memeriksa struktur dan keterhubungan ID. Tidak membuktikan keselarasan
resmi, kebenaran isi teknis, atau kualitas rubrik.

Pemakaian: python3 .claude/skills/rps-obe/scripts/check_obe_trace.py [repo_root]
Exit code 1 bila ada FAIL.
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[4]
GOV = ROOT / "course" / "governance"
LO_RE = re.compile(r"\bW\d{2}-LO\d{2}\b")
RC_RE = re.compile(r"\bW\d{2}-RC\d{2}\b")
EV_RE = re.compile(r"\bW\d{2}-EV\d{2}\b")

results = []


def check(name, ok, detail=""):
    results.append((name, ok, detail))


def read(name):
    return (GOV / name).read_text(encoding="utf-8")


def split_front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    return (m.group(1), m.group(2)) if m else ("", text)


def yaml_list(front, key):
    m = re.search(rf"^{key}:\s*\n((?:- .*\n?)*)", front, re.M)
    if not m:
        m2 = re.search(rf"^{key}:\s*\[(.*?)\]", front, re.M)
        return [x.strip() for x in m2.group(1).split(",") if x.strip()] if m2 else []
    return [line[2:].strip().strip("'\"") for line in m.group(1).splitlines() if line.startswith("- ")]


def section(body, heading):
    m = re.search(rf"^## {re.escape(heading)}.*?\n(.*?)(?=^## |\Z)", body, re.S | re.M)
    return m.group(1) if m else ""


def table_rows(text):
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|") and not re.match(r"^\|\s*-{3}", line):
            rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows[1:] if rows else []  # buang header


rps_front, rps = split_front_matter(read("rps.md"))
rtm_front, rtm = split_front_matter(read("rtm.md"))
bp_front, bp = split_front_matter(read("assessment-blueprint.md"))

# 1. Peta 16 minggu
peta = table_rows(section(rps, "Peta 16 minggu"))
weeks = {r[0] for r in peta if r and re.fullmatch(r"W\d{2}", r[0])}
missing = [f"W{i:02d}" for i in range(1, 17) if f"W{i:02d}" not in weeks]
check("RPS: peta 16 minggu lengkap W01–W16", not missing, f"hilang: {missing}" if missing else f"{len(weeks)} baris")
row = {r[0]: r for r in peta if r}
check("RPS: W08 = UTS", "UTS" in " ".join(row.get("W08", [])))
check("RPS: W16 = UAS", "UAS" in " ".join(row.get("W16", [])))
no_outcome = [w for w, r in row.items() if re.fullmatch(r"W\d{2}", w) and (len(r) < 3 or not r[2])]
check("RPS: setiap minggu punya kode outcome", not no_outcome, str(no_outcome) if no_outcome else "")

# 2. LO detail (tabel Capaian) vs blueprint & RTM
capaian = table_rows(section(rps, "Capaian dan bahan kajian"))
detail_los = [r[0] for r in capaian if r and LO_RE.fullmatch(r[0])]
check("RPS: tabel capaian berisi LO", bool(detail_los), f"{len(detail_los)} LO")

bp_matrix_los = {r[0] for r in table_rows(bp) if r and LO_RE.fullmatch(r[0])}
lo_to_rc, rc_to_lo = {}, {}
for r in table_rows(bp):
    if r and RC_RE.fullmatch(r[0]) and len(r) > 1:
        for lo in LO_RE.findall(r[1]):
            lo_to_rc.setdefault(lo, set()).add(r[0])
            rc_to_lo.setdefault(r[0], set()).add(lo)

for name, pool in [("blueprint (matriks)", bp_matrix_los), ("RTM", set(LO_RE.findall(rtm)))]:
    miss = [lo for lo in detail_los if lo not in pool]
    check(f"LO RPS ada di {name}", not miss, f"hilang: {miss}" if miss else "")

no_rc = [lo for lo in detail_los if lo not in lo_to_rc]
check("Setiap LO punya kriteria rubrik (RC)", not no_rc, f"tanpa RC: {no_rc}" if no_rc else "")
shared = {rc: sorted(los) for rc, los in rc_to_lo.items() if len(los) > 1}
check("Setiap RC menilai satu LO saja", not shared, str(shared) if shared else "")

orphan = sorted(bp_matrix_los - set(detail_los))
check("Tidak ada LO blueprint di luar RPS", not orphan, f"yatim: {orphan}" if orphan else "")

# 3. Katalog RTM: ASM → LO/EV/RC harus ada
bp_rcs = set(rc_to_lo)
bp_evs = set(EV_RE.findall(bp))
catalog = [r for r in table_rows(section(rtm, "Katalog fokus dan batas penggunaan")) if r and "ASM" in r[0]]
check("RTM: katalog ASM tidak kosong", bool(catalog), f"{len(catalog)} ASM")
for r in catalog:
    asm = re.search(r"W\d{2}-ASM\d{2}", r[0]).group(0)
    los, evs, rcs = LO_RE.findall(r[2]), EV_RE.findall(r[3]), RC_RE.findall(r[4])
    problems = []
    problems += [f"LO {x} tidak ada di RPS" for x in los if x not in detail_los]
    problems += [f"EV {x} tidak ada di blueprint" for x in evs if x not in bp_evs]
    problems += [f"RC {x} tidak ada di blueprint" for x in rcs if x not in bp_rcs]
    for lo in los:
        if lo in lo_to_rc and not (lo_to_rc[lo] & set(rcs)):
            problems.append(f"RC untuk {lo} tidak dicantumkan")
    if not los or not evs or not rcs:
        problems.append("kolom LO/EV/RC kosong")
    check(f"RTM {asm}: LO/EV/RC terhubung", not problems, "; ".join(problems))

# 4. Metadata learning_ids
for fname, front, body in [("rps.md", rps_front, rps), ("assessment-blueprint.md", bp_front, bp), ("rtm.md", rtm_front, rtm)]:
    meta = set(yaml_list(front, "learning_ids"))
    miss = [lo for lo in detail_los if lo not in meta]
    extra = sorted(lo for lo in meta if lo not in body)
    detail = "; ".join(x for x in [f"belum di metadata: {miss}" if miss else "", f"di metadata tapi tidak dipakai: {extra}" if extra else ""] if x)
    check(f"{fname}: metadata learning_ids konsisten", not miss and not extra, detail)

# 5. Label kejujuran status
check("RPS: judul tetap 'Rancangan RPS'", re.search(r"^# Rancangan RPS", rps, re.M) is not None)
for fname, front in [("rps.md", rps_front), ("rtm.md", rtm_front), ("assessment-blueprint.md", bp_front)]:
    val = re.search(r"^official_alignment:\s*(\S+)", front, re.M)
    srcs = (ROOT / "course/production/sources.md").read_text(encoding="utf-8")
    verified_official = re.search(r"\bS0[123]\b.*VERIFIED_(LOCAL|EXTERNAL)", srcs) is not None
    ok = val is not None and (val.group(1) == "PROVISIONAL" or verified_official)
    check(f"{fname}: official_alignment wajar terhadap register sumber", ok, val.group(1) if val else "field hilang")

# Laporan
fails = 0
for name, ok, detail in results:
    status = "PASS" if ok else "FAIL"
    fails += not ok
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
slot_los = sorted(set(LO_RE.findall(section(rps, "Peta 16 minggu"))) - set(detail_los))
if slot_los:
    print(f"[INFO] LO slot (belum dirinci, tidak diwajibkan punya RC): {', '.join(slot_los)}")
print(f"\n{len(results) - fails} PASS, {fails} FAIL")
sys.exit(1 if fails else 0)
