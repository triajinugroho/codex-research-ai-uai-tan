# DOSEN — W03 solusi reference

Helper LAB, bukan ID artefak utama tambahan. Jangan dibagikan lewat indeks mahasiswa. Kode berikut diuji utuh dari Markdown; bukan keluaran kelas.

```python
import json
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
train = pd.DataFrame({"volume":[1.,np.nan,3.,5.],"channel":["A","B","A","B"]})
new = pd.DataFrame({"volume":[np.nan,7.],"channel":["C","A"]})
num = Pipeline([("imputer",SimpleImputer(strategy="median")),("scale",StandardScaler())])
ct = ColumnTransformer([("numeric",num,["volume"]),("category",OneHotEncoder(handle_unknown="ignore",sparse_output=False),["channel"])])
z_train = ct.fit_transform(train)
z_new = ct.transform(new)
fitted = ct.named_transformers_["numeric"]
median = float(fitted.named_steps["imputer"].statistics_[0])
mu = float(fitted.named_steps["scale"].mean_[0])
scale = float(fitted.named_steps["scale"].scale_[0])
assert median == 3. and mu == 3. and np.isclose(scale,np.sqrt(2))
assert z_train.shape == (4,3) and z_new.shape == (2,3)
assert np.allclose(z_new[0],[0.,0.,0.])
assert np.isclose(z_new[1,0],4/np.sqrt(2)) and not np.isnan(z_new).any()
assert fitted.named_steps["imputer"].statistics_[0] == 3.
print(json.dumps({"median_training":median,"mean_training":mu,"scale_training":scale,"new_transformed":z_new.tolist(),"shape_training":list(z_train.shape)}))
```

Interpretasi: Median 3; mean 3; skala sqrt(2); batch baru 2×3 tanpa missing. Batas klaim sama dengan DATA/BOOK; demo test W04 bukan holdout proyek.
