# DOSEN — W04 solusi reference

Helper LAB, bukan ID artefak utama tambahan. Jangan dibagikan lewat indeks mahasiswa. Kode berikut diuji utuh dari Markdown; bukan keluaran kelas.

```python
import json
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, StratifiedKFold, GroupKFold, TimeSeriesSplit
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier
X, y = make_classification(n_samples=120,n_features=6,n_informative=4,n_redundant=0,random_state=42)
X[::13,0] = np.nan
idx = np.arange(len(y))
dev, test = train_test_split(idx,test_size=.25,stratify=y,random_state=42)
assert len(dev)==90 and len(test)==30 and not set(dev)&set(test)
cv = StratifiedKFold(n_splits=3,shuffle=True,random_state=42)
scores = []
for tr_local, va_local in cv.split(X[dev],y[dev]):
    tr, va = dev[tr_local], dev[va_local]
    assert not set(tr)&set(va) and not (set(tr)|set(va))&set(test)
    pipe = Pipeline([("imputer",SimpleImputer(strategy="median")),("scale",StandardScaler()),("model",DummyClassifier(strategy="most_frequent"))])
    pipe.fit(X[tr],y[tr])
    assert np.allclose(pipe.named_steps["imputer"].statistics_,np.nanmedian(X[tr],axis=0))
    scores.append(float(pipe.score(X[va],y[va])))
groups = np.repeat(np.arange(20),6)
for tr, va in GroupKFold(n_splits=3).split(X,y,groups):
    assert not set(groups[tr])&set(groups[va])
    assert not set(tr)&set(va)
time = np.arange(60)
last_fold = None
for tr, va in TimeSeriesSplit(n_splits=3,test_size=10,gap=2).split(time):
    assert tr.max()<va.min() and va.min()-tr.max()-1 == 2
    last_fold = [int(tr.max()),int(va.min()),int(va.max())]
# Kandidat dummy tetap: tidak tuning memakai test. Ini demo; jangan daur ulang test untuk proyek.
final = Pipeline([("imputer",SimpleImputer(strategy="median")),("scale",StandardScaler()),("model",DummyClassifier(strategy="most_frequent"))])
final.fit(X[dev],y[dev])
pred = final.predict(X[test])
assert len(pred)==30
print(json.dumps({"seed":42,"n_dev":len(dev),"n_test":len(test),"fold_scores":scores,"mean_cv":float(np.mean(scores)),"group_overlap":False,"last_time_fold":last_fold,"holdout_demo_now_exposed":True}))
```

Interpretasi: Dev90/test30; tiga fold tanpa test; kelompok tidak overlap; waktu forward dengan gap2. Batas klaim sama dengan DATA/BOOK; demo test W04 bukan holdout proyek.
