# DOSEN — W01 solusi reference

Helper LAB, bukan ID artefak utama tambahan. Jangan dibagikan lewat indeks mahasiswa. Kode berikut diuji utuh dari Markdown; bukan keluaran kelas.

```python
import json
from sklearn.base import is_classifier, is_regressor
from sklearn.dummy import DummyClassifier, DummyRegressor
cards = [
    {"id":"C1","input":"email saat diterima","target":"spam/tidak","method":"supervised classification"},
    {"id":"C2","input":"konsumsi historis","target":"kWh esok","method":"supervised regression"},
    {"id":"C3","input":"profil belanja","target":None,"method":"clustering"},
    {"id":"C4","input":"suhu saat ini","target":None,"method":"fixed rule"},
]
assert len(cards) == 4 and len({c["id"] for c in cards}) == 4
assert is_classifier(DummyClassifier()) and is_regressor(DummyRegressor())
assert cards[2]["target"] is None
print(json.dumps({"case_ids":[c["id"] for c in cards],"kinds":len(cards),"fixed_rule_has_fit":False}))
```

Interpretasi: Empat kartu dan jenis kasus; bukan hasil akurasi model. Batas klaim sama dengan DATA/BOOK; demo test W04 bukan holdout proyek.
