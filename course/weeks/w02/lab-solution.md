# DOSEN — W02 solusi reference

Helper LAB, bukan ID artefak utama tambahan. Jangan dibagikan lewat indeks mahasiswa. Kode berikut diuji utuh dari Markdown; bukan keluaran kelas.

```python
import json
import pandas as pd
import numpy as np
df = pd.DataFrame({"row_id":[1,2,3,4,5],"duration_min":[10.,20.,np.nan,20.,90.],"channel":["A","B","A","B","B"]})
missing = int(df["duration_min"].isna().sum())
median = float(df["duration_min"].median())
mean = float(df["duration_min"].mean())
dup = int(df.duplicated(subset=["duration_min","channel"]).sum())
assert df.shape == (5,3) and missing == 1
assert np.isclose(median,20.) and np.isclose(mean,35.) and dup == 1
assert np.isclose(missing/len(df),0.2)
print(json.dumps({"shape":list(df.shape),"missing":missing,"missing_pct":missing/len(df)*100,"median":median,"mean":mean,"duplicates_subset":dup}))
```

Interpretasi: 5×3, satu missing (20%), median 20, mean 35, satu duplikat subset. Batas klaim sama dengan DATA/BOOK; demo test W04 bukan holdout proyek.
