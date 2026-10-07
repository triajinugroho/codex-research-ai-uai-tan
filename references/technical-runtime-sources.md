# Sumber teknis lokal — snapshot dokumentasi runtime

Sumber dibaca dari API paket yang terpasang; bukan hasil akses situs web. Kutipan tetap bahasa asli. Snapshot untuk verifikasi substansi W01–W04, bukan kebijakan akademik.

Versi: scikit-learn 1.8.0; pandas 2.2.3; NumPy 2.3.5.

ID: SRC-TECH-001 (sklearn), SRC-TECH-002 (pandas), SRC-TECH-003 (NumPy).

Tanggal pembacaan UTC: 2026-10-07T18:03:57.634594+00:00

## ClassifierMixin

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/base.py:499`; SHA-256 file sumber `10992a4472940aa33f499e3bfc2477c2fe82509963907127fbd71ce3f7380ec6`.

```text
Mixin class for all classifiers in scikit-learn.

This mixin defines the following functionality:

- set estimator type to `"classifier"` through the `estimator_type` tag;
- `score` method that default to :func:`~sklearn.metrics.accuracy_score`.
- enforce that `fit` requires `y` to be passed through the `requires_y` tag,
  which is done by setting the classifier type tag.

Read more in the :ref:`User Guide <rolling_your_own_estimator>`.

Examples
--------
>>> import numpy as np
>>> from sklearn.base import BaseEstimator, ClassifierMixin
>>> # Mixin classes should always be on the left-hand side for a correct MRO
>>> class MyEstimator(ClassifierMixin, BaseEstimator):
...     def __init__(self, *, param=1):
...         self.param = param
...     def fit(self, X, y=None):
...         self.is_fitted_ = True
...         return self
...     def predict(self, X):
...         return np.full(shape=X.shape[0], fill_value=self.param)
>>> estimator = MyEstimator(param=1)
>>> X = np.array([[1, 2], [2, 3], [3, 4]])
>>> y = np.array([1, 0, 1])
>>> estimator.fit(X, y).predict(X)
array([1, 1, 1])
>>> estimator.score(X, y)
0.66...
```

## RegressorMixin

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/base.py:569`; SHA-256 file sumber `10992a4472940aa33f499e3bfc2477c2fe82509963907127fbd71ce3f7380ec6`.

```text
Mixin class for all regression estimators in scikit-learn.

This mixin defines the following functionality:

- set estimator type to `"regressor"` through the `estimator_type` tag;
- `score` method that default to :func:`~sklearn.metrics.r2_score`.
- enforce that `fit` requires `y` to be passed through the `requires_y` tag,
  which is done by setting the regressor type tag.

Read more in the :ref:`User Guide <rolling_your_own_estimator>`.

Examples
--------
>>> import numpy as np
>>> from sklearn.base import BaseEstimator, RegressorMixin
>>> # Mixin classes should always be on the left-hand side for a correct MRO
>>> class MyEstimator(RegressorMixin, BaseEstimator):
...     def __init__(self, *, param=1):
...         self.param = param
...     def fit(self, X, y=None):
...         self.is_fitted_ = True
...         return self
...     def predict(self, X):
...         return np.full(shape=X.shape[0], fill_value=self.param)
>>> estimator = MyEstimator(param=0)
>>> X = np.array([[1, 2], [2, 3], [3, 4]])
>>> y = np.array([-1, 0, 1])
>>> estimator.fit(X, y).predict(X)
array([0, 0, 0])
>>> estimator.score(X, y)
0.0
```

## KMeans

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/cluster/_kmeans.py:1192`; SHA-256 file sumber `67115e4a9e4bace9aabd6f75f2da173d0be7ee07526f4de12cc5e42c125169d7`.

```text
K-Means clustering.

Read more in the :ref:`User Guide <k_means>`.

Parameters
----------

n_clusters : int, default=8
    The number of clusters to form as well as the number of
    centroids to generate.

    For an example of how to choose an optimal value for `n_clusters` refer to
    :ref:`sphx_glr_auto_examples_cluster_plot_kmeans_silhouette_analysis.py`.

init : {'k-means++', 'random'}, callable or array-like of shape             (n_clusters, n_features), default='k-means++'
    Method for initialization:

    * 'k-means++' : selects initial cluster centroids using sampling             based on an empirical probability distribution of the points'             contribution to the overall inertia. This technique speeds up             convergence. The algorithm implemented is "greedy k-means++". It             differs from the vanilla k-means++ by making several trials at             each sampling step and choosing the best centroid among them.

    * 'random': choose `n_clusters` observations (rows) at random from         data for the initial centroids.

    * If an array is passed, it should be of shape (n_clusters, n_features)        and gives the initial centers.

    * If a callable is passed, it should take arguments X, n_clusters and a        random state and return an initialization.

    For an example of how to use the different `init` strategies, see
    :ref:`sphx_glr_auto_examples_cluster_plot_kmeans_digits.py`.

    For an evaluation of the impact of initialization, see the example
    :ref:`sphx_glr_auto_examples_cluster_plot_kmeans_stability_low_dim_dense.py`.

n_init : 'auto' or int, default='auto'
    Number of times the k-means algorithm is run with different centroid
    seeds. The final results is the best output of `n_init` consecutive runs
    in terms of inertia. Several runs are recommended for sparse
    high-dimensional problems (see :ref:`kmeans_sparse_high_dim`).

    When `n_init='auto'`, the number of runs depends on the value of init:
    10 if using `init='random'` or `init` is a callable;
    1 if using `init='k-means++'` or `init` is an array-like.

    .. versionadded:: 1.2
       Added 'auto' option for `n_init`.

    .. versionchanged:: 1.4
       Default value for `n_init` changed to `'auto'`.
```

## TransformerMixin

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/base.py:813`; SHA-256 file sumber `10992a4472940aa33f499e3bfc2477c2fe82509963907127fbd71ce3f7380ec6`.

```text
Mixin class for all transformers in scikit-learn.

This mixin defines the following functionality:

- a `fit_transform` method that delegates to `fit` and `transform`;
- a `set_output` method to output `X` as a specific container type.

If :term:`get_feature_names_out` is defined, then :class:`BaseEstimator` will
automatically wrap `transform` and `fit_transform` to follow the `set_output`
API. See the :ref:`developer_api_set_output` for details.

:class:`OneToOneFeatureMixin` and
:class:`ClassNamePrefixFeaturesOutMixin` are helpful mixins for
defining :term:`get_feature_names_out`.

Examples
--------
>>> import numpy as np
>>> from sklearn.base import BaseEstimator, TransformerMixin
>>> class MyTransformer(TransformerMixin, BaseEstimator):
...     def __init__(self, *, param=1):
...         self.param = param
...     def fit(self, X, y=None):
...         return self
...     def transform(self, X):
...         return np.full(shape=len(X), fill_value=self.param)
>>> transformer = MyTransformer()
>>> X = [[1, 2], [2, 3], [3, 4]]
>>> transformer.fit_transform(X)
array([1, 1, 1])
```

## DummyClassifier

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/dummy.py:34`; SHA-256 file sumber `3c4c1eeb7afc2017981fe018e8a33256546bfc282480cd83f19dd3e353a137ee`.

```text
DummyClassifier makes predictions that ignore the input features.

This classifier serves as a simple baseline to compare against other more
complex classifiers.

The specific behavior of the baseline is selected with the `strategy`
parameter.

All strategies make predictions that ignore the input feature values passed
as the `X` argument to `fit` and `predict`. The predictions, however,
typically depend on values observed in the `y` parameter passed to `fit`.

Note that the "stratified" and "uniform" strategies lead to
non-deterministic predictions that can be rendered deterministic by setting
the `random_state` parameter if needed. The other strategies are naturally
deterministic and, once fit, always return the same constant prediction
for any value of `X`.

Read more in the :ref:`User Guide <dummy_estimators>`.

.. versionadded:: 0.13

Parameters
----------
strategy : {"most_frequent", "prior", "stratified", "uniform",             "constant"}, default="prior"
    Strategy to use to generate predictions.

    * "most_frequent": the `predict` method always returns the most
      frequent class label in the observed `y` argument passed to `fit`.
      The `predict_proba` method returns the matching one-hot encoded
      vector.
    * "prior": the `predict` method always returns the most frequent
      class label in the observed `y` argument passed to `fit` (like
      "most_frequent"). ``predict_proba`` always returns the empirical
      class distribution of `y` also known as the empirical class prior
      distribution.
    * "stratified": the `predict_proba` method randomly samples one-hot
      vectors from a multinomial distribution parametrized by the empirical
      class prior probabilities.
      The `predict` method returns the class label which got probability
      one in the one-hot vector of `predict_proba`.
      Each sampled row of both methods is therefore independent and
      identically distributed.
    * "uniform": generates predictions uniformly at random from the list
      of unique classes observed in `y`, i.e. each class has equal
      probability.
```

## make_classification

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/utils/_param_validation.py:40`; SHA-256 file sumber `db4c637d064073e83533bcb920cc2b544a26b92d517b09d8a07c59780a3594fd`.

```text
Generate a random n-class classification problem.

This initially creates clusters of points normally distributed (std=1)
about vertices of an ``n_informative``-dimensional hypercube with sides of
length ``2*class_sep`` and assigns an equal number of clusters to each
class. It introduces interdependence between these features and adds
various types of further noise to the data.

Without shuffling, ``X`` horizontally stacks features in the following
order: the primary ``n_informative`` features, followed by ``n_redundant``
linear combinations of the informative features, followed by ``n_repeated``
duplicates, drawn randomly with replacement from the informative and
redundant features. The remaining features are filled with random noise.
Thus, without shuffling, all useful features are contained in the columns
``X[:, :n_informative + n_redundant + n_repeated]``.

Read more in the :ref:`User Guide <sample_generators>`.

Parameters
----------
n_samples : int, default=100
    The number of samples.

n_features : int, default=20
    The total number of features. These comprise ``n_informative``
    informative features, ``n_redundant`` redundant features,
    ``n_repeated`` duplicated features and
    ``n_features-n_informative-n_redundant-n_repeated`` useless features
    drawn at random.

n_informative : int, default=2
    The number of informative features. Each class is composed of a number
    of gaussian clusters each located around the vertices of a hypercube
    in a subspace of dimension ``n_informative``. For each cluster,
    informative features are drawn independently from  N(0, 1) and then
    randomly linearly combined within each cluster in order to add
    covariance. The clusters are then placed on the vertices of the
    hypercube.

n_redundant : int, default=2
    The number of redundant features. These features are generated as
    random linear combinations of the informative features.

n_repeated : int, default=0
    The number of duplicated features, drawn randomly from the informative
    and the redundant features.
```

## train_test_split

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/utils/_param_validation.py:2757`; SHA-256 file sumber `db4c637d064073e83533bcb920cc2b544a26b92d517b09d8a07c59780a3594fd`.

```text
Split arrays or matrices into random train and test subsets.

Quick utility that wraps input validation,
``next(ShuffleSplit().split(X, y))``, and application to input data
into a single call for splitting (and optionally subsampling) data into a
one-liner.

Read more in the :ref:`User Guide <cross_validation>`.

Parameters
----------
*arrays : sequence of indexables with same length / shape[0]
    Allowed inputs are lists, numpy arrays, scipy-sparse
    matrices or pandas dataframes.

test_size : float or int, default=None
    If float, should be between 0.0 and 1.0 and represent the proportion
    of the dataset to include in the test split. If int, represents the
    absolute number of test samples. If None, the value is set to the
    complement of the train size. If ``train_size`` is also None, it will
    be set to 0.25.

train_size : float or int, default=None
    If float, should be between 0.0 and 1.0 and represent the
    proportion of the dataset to include in the train split. If
    int, represents the absolute number of train samples. If None,
    the value is automatically set to the complement of the test size.

random_state : int, RandomState instance or None, default=None
    Controls the shuffling applied to the data before applying the split.
    Pass an int for reproducible output across multiple function calls.
    See :term:`Glossary <random_state>`.

shuffle : bool, default=True
    Whether or not to shuffle the data before splitting. If shuffle=False
    then stratify must be None.

stratify : array-like, default=None
    If not None, data is split in a stratified fashion, using this as
    the class labels.
    Read more in the :ref:`User Guide <stratification>`.

Returns
-------
splitting : list, length=2 * len(arrays)
    List containing train-test split of inputs.
```

## StratifiedKFold

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/model_selection/_split.py:688`; SHA-256 file sumber `68965624259adcaaa50981d0ef4493de4ec3753f43a798808fe2ee7bac4042fe`.

```text
Class-wise stratified K-Fold cross-validator.

Provides train/test indices to split data in train/test sets.

This cross-validation object is a variation of KFold that returns
stratified folds. The folds are made by preserving the percentage of
samples for each class in `y` in a binary or multiclass classification
setting.

Read more in the :ref:`User Guide <stratified_k_fold>`.

For visualisation of cross-validation behaviour and
comparison between common scikit-learn split methods
refer to :ref:`sphx_glr_auto_examples_model_selection_plot_cv_indices.py`

.. note::

    Stratification on the class label solves an engineering problem rather
    than a statistical one. See :ref:`stratification` for more details.

Parameters
----------
n_splits : int, default=5
    Number of folds. Must be at least 2.

    .. versionchanged:: 0.22
        ``n_splits`` default value changed from 3 to 5.

shuffle : bool, default=False
    Whether to shuffle each class's samples before splitting into batches.
    Note that the samples within each split will not be shuffled.

random_state : int, RandomState instance or None, default=None
    When `shuffle` is True, `random_state` affects the ordering of the
    indices, which controls the randomness of each fold for each class.
    Otherwise, leave `random_state` as `None`.
    Pass an int for reproducible output across multiple function calls.
    See :term:`Glossary <random_state>`.

Examples
--------
>>> import numpy as np
>>> from sklearn.model_selection import StratifiedKFold
>>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
>>> y = np.array([0, 0, 1, 1])
>>> skf = StratifiedKFold(n_splits=2)
```

## GroupKFold

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/model_selection/_split.py:534`; SHA-256 file sumber `68965624259adcaaa50981d0ef4493de4ec3753f43a798808fe2ee7bac4042fe`.

```text
K-fold iterator variant with non-overlapping groups.

Each group will appear exactly once in the test set across all folds (the
number of distinct groups has to be at least equal to the number of folds).

The folds are approximately balanced in the sense that the number of
samples is approximately the same in each test fold when `shuffle` is True.

Read more in the :ref:`User Guide <group_k_fold>`.

For visualisation of cross-validation behaviour and
comparison between common scikit-learn split methods
refer to :ref:`sphx_glr_auto_examples_model_selection_plot_cv_indices.py`

Parameters
----------
n_splits : int, default=5
    Number of folds. Must be at least 2.

    .. versionchanged:: 0.22
        ``n_splits`` default value changed from 3 to 5.

shuffle : bool, default=False
    Whether to shuffle the groups before splitting into batches.
    Note that the samples within each split will not be shuffled.

    .. versionadded:: 1.6

random_state : int, RandomState instance or None, default=None
    When `shuffle` is True, `random_state` affects the ordering of the
    indices, which controls the randomness of each fold. Otherwise, this
    parameter has no effect.
    Pass an int for reproducible output across multiple function calls.
    See :term:`Glossary <random_state>`.

    .. versionadded:: 1.6

Notes
-----
Groups appear in an arbitrary order throughout the folds.

Examples
--------
>>> import numpy as np
>>> from sklearn.model_selection import GroupKFold
>>> X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
```

## TimeSeriesSplit

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/model_selection/_split.py:1109`; SHA-256 file sumber `68965624259adcaaa50981d0ef4493de4ec3753f43a798808fe2ee7bac4042fe`.

```text
Time Series cross-validator.

Provides train/test indices to split time-ordered data, where other
cross-validation methods are inappropriate, as they would lead to training
on future data and evaluating on past data.
To ensure comparable metrics across folds, samples must be equally spaced.
Once this condition is met, each test set covers the same time duration,
while the train set size accumulates data from previous splits.

This cross-validation object is a variation of :class:`KFold`.
In the k-th split, it returns the first k folds as the train set and the
(k+1)-th fold as the test set.

Note that, unlike standard cross-validation methods, successive
training sets are supersets of those that come before them.

Read more in the :ref:`User Guide <time_series_split>`.

For visualisation of cross-validation behaviour and
comparison between common scikit-learn split methods
refer to :ref:`sphx_glr_auto_examples_model_selection_plot_cv_indices.py`

.. versionadded:: 0.18

Parameters
----------
n_splits : int, default=5
    Number of splits. Must be at least 2.

    .. versionchanged:: 0.22
        ``n_splits`` default value changed from 3 to 5.

max_train_size : int, default=None
    Maximum size for a single training set.

test_size : int, default=None
    Used to limit the size of the test set. Defaults to
    ``n_samples // (n_splits + 1)``, which is the maximum allowed value
    with ``gap=0``.

    .. versionadded:: 0.24

gap : int, default=0
    Number of samples to exclude from the end of each train set before
    the test set.

```

## cross_validate

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/utils/_param_validation.py:75`; SHA-256 file sumber `db4c637d064073e83533bcb920cc2b544a26b92d517b09d8a07c59780a3594fd`.

```text
Evaluate metric(s) by cross-validation and also record fit/score times.

Read more in the :ref:`User Guide <multimetric_cross_validation>`.

Parameters
----------
estimator : estimator object implementing 'fit'
    The object to use to fit the data.

X : {array-like, sparse matrix} of shape (n_samples, n_features)
    The data to fit. Can be for example a list, or an array.

y : array-like of shape (n_samples,) or (n_samples, n_outputs), default=None
    The target variable to try to predict in the case of
    supervised learning.

groups : array-like of shape (n_samples,), default=None
    Group labels for the samples used while splitting the dataset into
    train/test set. Only used in conjunction with a "Group" :term:`cv`
    instance (e.g., :class:`GroupKFold`).

    .. versionchanged:: 1.4
        ``groups`` can only be passed if metadata routing is not enabled
        via ``sklearn.set_config(enable_metadata_routing=True)``. When routing
        is enabled, pass ``groups`` alongside other metadata via the ``params``
        argument instead. E.g.:
        ``cross_validate(..., params={'groups': groups})``.

scoring : str, callable, list, tuple, or dict, default=None
    Strategy to evaluate the performance of the `estimator` across cross-validation
    splits.

    If `scoring` represents a single score, one can use:

    - a single string (see :ref:`scoring_string_names`);
    - a callable (see :ref:`scoring_callable`) that returns a single value.
    - `None`, the `estimator`'s
      :ref:`default evaluation criterion <scoring_api_overview>` is used.

    If `scoring` represents multiple scores, one can use:

    - a list or tuple of unique strings;
    - a callable returning a dictionary where the keys are the metric
      names and the values are the metric scores;
    - a dictionary with metric names as keys and callables a values.

```

## Pipeline

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/pipeline.py:91`; SHA-256 file sumber `cb1e71252f678047189e00d78fa5dd612cf1945e9f3b2426c02570c86ca68296`.

```text
A sequence of data transformers with an optional final predictor.

`Pipeline` allows you to sequentially apply a list of transformers to
preprocess the data and, if desired, conclude the sequence with a final
:term:`predictor` for predictive modeling.

Intermediate steps of the pipeline must be transformers, that is, they
must implement `fit` and `transform` methods.
The final :term:`estimator` only needs to implement `fit`.
The transformers in the pipeline can be cached using ``memory`` argument.

The purpose of the pipeline is to assemble several steps that can be
cross-validated together while setting different parameters. For this, it
enables setting parameters of the various steps using their names and the
parameter name separated by a `'__'`, as in the example below. A step's
estimator may be replaced entirely by setting the parameter with its name
to another estimator, or a transformer removed by setting it to
`'passthrough'` or `None`.

For an example use case of `Pipeline` combined with
:class:`~sklearn.model_selection.GridSearchCV`, refer to
:ref:`sphx_glr_auto_examples_compose_plot_compare_reduction.py`. The
example :ref:`sphx_glr_auto_examples_compose_plot_digits_pipe.py` shows how
to grid search on a pipeline using `'__'` as a separator in the parameter names.

Read more in the :ref:`User Guide <pipeline>`.

.. versionadded:: 0.5

Parameters
----------
steps : list of tuples
    List of (name of step, estimator) tuples that are to be chained in
    sequential order. To be compatible with the scikit-learn API, all steps
    must define `fit`. All non-last steps must also define `transform`. See
    :ref:`Combining Estimators <combining_estimators>` for more details.

transform_input : list of str, default=None
    The names of the :term:`metadata` parameters that should be transformed by the
    pipeline before passing it to the step consuming it.

    This enables transforming some input arguments to ``fit`` (other than ``X``)
    to be transformed by the steps of the pipeline up to the step which requires
    them. Requirement is defined via :ref:`metadata routing <metadata_routing>`.
    For instance, this can be used to pass a validation set through the pipeline.

```

## SimpleImputer

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/impute/_base.py:170`; SHA-256 file sumber `a93bc045c240bed7b5b1fc129a7ac42e7bca6fb104d113c4d096018bbfaf61f9`.

```text
Univariate imputer for completing missing values with simple strategies.

Replace missing values using a descriptive statistic (e.g. mean, median, or
most frequent) along each column, or using a constant value.

Read more in the :ref:`User Guide <impute>`.

.. versionadded:: 0.20
   `SimpleImputer` replaces the previous `sklearn.preprocessing.Imputer`
   estimator which is now removed.

Parameters
----------
missing_values : int, float, str, np.nan, None or pandas.NA, default=np.nan
    The placeholder for the missing values. All occurrences of
    `missing_values` will be imputed. For pandas' dataframes with
    nullable integer dtypes with missing values, `missing_values`
    can be set to either `np.nan` or `pd.NA`.

strategy : str or Callable, default='mean'
    The imputation strategy.

    - If "mean", then replace missing values using the mean along
      each column. Can only be used with numeric data.
    - If "median", then replace missing values using the median along
      each column. Can only be used with numeric data.
    - If "most_frequent", then replace missing using the most frequent
      value along each column. Can be used with strings or numeric data.
      If there is more than one such value, only the smallest is returned.
    - If "constant", then replace missing values with fill_value. Can be
      used with strings or numeric data.
    - If an instance of Callable, then replace missing values using the
      scalar statistic returned by running the callable over a dense 1d
      array containing non-missing values of each column.

    .. versionadded:: 0.20
       strategy="constant" for fixed value imputation.

    .. versionadded:: 1.5
       strategy=callable for custom value imputation.

fill_value : str or numerical value, default=None
    When strategy == "constant", `fill_value` is used to replace all
    occurrences of missing_values. For string or object data types,
    `fill_value` must be a string.
    If `None`, `fill_value` will be 0 when imputing numerical
```

## StandardScaler

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/preprocessing/_data.py:740`; SHA-256 file sumber `f9a1f300ddc85cd4ca08e5cbcb8151b625d487ec2a6796ec2758344f20d9ce0e`.

```text
Standardize features by removing the mean and scaling to unit variance.

The standard score of a sample `x` is calculated as:

.. code-block:: text

    z = (x - u) / s

where `u` is the mean of the training samples or zero if `with_mean=False`,
and `s` is the standard deviation of the training samples or one if
`with_std=False`.

Centering and scaling happen independently on each feature by computing
the relevant statistics on the samples in the training set. Mean and
standard deviation are then stored to be used on later data using
:meth:`transform`.

Standardization of a dataset is a common requirement for many
machine learning estimators: they might behave badly if the
individual features do not more or less look like standard normally
distributed data (e.g. Gaussian with 0 mean and unit variance).

For instance many elements used in the objective function of
a learning algorithm (such as the RBF kernel of Support Vector
Machines or the L1 and L2 regularizers of linear models) assume that
all features are centered around 0 and have variance in the same
order. If a feature has a variance that is orders of magnitude larger
than others, it might dominate the objective function and make the
estimator unable to learn from other features correctly as expected.

`StandardScaler` is sensitive to outliers, and the features may scale
differently from each other in the presence of outliers. For an example
visualization, refer to :ref:`Compare StandardScaler with other scalers
<plot_all_scaling_standard_scaler_section>`.

This scaler can also be applied to sparse CSR or CSC matrices by passing
`with_mean=False` to avoid breaking the sparsity structure of the data.

Read more in the :ref:`User Guide <preprocessing_scaler>`.

Parameters
----------
copy : bool, default=True
    If False, try to avoid a copy and do inplace scaling instead.
    This is not guaranteed to always work inplace; e.g. if the data is
    not a NumPy array or scipy.sparse CSR matrix, a copy may still be
```

## OneHotEncoder

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/preprocessing/_encoders.py:473`; SHA-256 file sumber `451b5163af3138f67f63bfd435254332a5c6a88ed5bb08ba09ade09a08ced161`.

```text
Encode categorical features as a one-hot numeric array.

The input to this transformer should be an array-like of integers or
strings, denoting the values taken on by categorical (discrete) features.
The features are encoded using a one-hot (aka 'one-of-K' or 'dummy')
encoding scheme. This creates a binary column for each category and
returns a sparse matrix or dense array (depending on the ``sparse_output``
parameter).

By default, the encoder derives the categories based on the unique values
in each feature. Alternatively, you can also specify the `categories`
manually.

This encoding is needed for feeding categorical data to many scikit-learn
estimators, notably linear models and SVMs with the standard kernels.

Note: a one-hot encoding of y labels should use a LabelBinarizer
instead.

Read more in the :ref:`User Guide <preprocessing_categorical_features>`.
For a comparison of different encoders, refer to:
:ref:`sphx_glr_auto_examples_preprocessing_plot_target_encoder.py`.

Parameters
----------
categories : 'auto' or a list of array-like, default='auto'
    Categories (unique values) per feature:

    - 'auto' : Determine categories automatically from the training data.
    - list : ``categories[i]`` holds the categories expected in the ith
      column. The passed categories should not mix strings and numeric
      values within a single feature, and should be sorted in case of
      numeric values.

    The used categories can be found in the ``categories_`` attribute.

    .. versionadded:: 0.20

drop : {'first', 'if_binary'} or an array-like of shape (n_features,),             default=None
    Specifies a methodology to use to drop one of the categories per
    feature. This is useful in situations where perfectly collinear
    features cause problems, such as when feeding the resulting data
    into an unregularized linear regression model.

    However, dropping one category breaks the symmetry of the original
    representation and can therefore induce a bias in downstream models,
```

## ColumnTransformer

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/sklearn/compose/_column_transformer.py:67`; SHA-256 file sumber `44a51afe0d6e4fbcdf0349eca933e86571dbc1e9c8dd03e2d68899258af74ae0`.

```text
Applies transformers to columns of an array or pandas DataFrame.

This estimator allows different columns or column subsets of the input
to be transformed separately and the features generated by each transformer
will be concatenated to form a single feature space.
This is useful for heterogeneous or columnar data, to combine several
feature extraction mechanisms or transformations into a single transformer.

Read more in the :ref:`User Guide <column_transformer>`.

.. versionadded:: 0.20

Parameters
----------
transformers : list of tuples
    List of (name, transformer, columns) tuples specifying the
    transformer objects to be applied to subsets of the data.

    name : str
        Like in Pipeline and FeatureUnion, this allows the transformer and
        its parameters to be set using ``set_params`` and searched in grid
        search.
    transformer : {'drop', 'passthrough'} or estimator
        Estimator must support :term:`fit` and :term:`transform`.
        Special-cased strings 'drop' and 'passthrough' are accepted as
        well, to indicate to drop the columns or to pass them through
        untransformed, respectively.
    columns :  str, array-like of str, int, array-like of int,                 array-like of bool, slice or callable
        Indexes the data on its second axis. Integers are interpreted as
        positional columns, while strings can reference DataFrame columns
        by name.  A scalar string or int should be used where
        ``transformer`` expects X to be a 1d array-like (vector),
        otherwise a 2d array will be passed to the transformer.
        A callable is passed the input data `X` and can return any of the
        above. To select multiple columns by name or dtype, you can use
        :obj:`make_column_selector`.

remainder : {'drop', 'passthrough'} or estimator, default='drop'
    By default, only the specified columns in `transformers` are
    transformed and combined in the output, and the non-specified
    columns are dropped. (default of ``'drop'``).
    By specifying ``remainder='passthrough'``, all remaining columns that
    were not specified in `transformers`, but present in the data passed
    to `fit` will be automatically passed through. This subset of columns
    is concatenated with the output of the transformers. For dataframes,
    extra columns not seen during `fit` will be excluded from the output
```

## DataFrame.describe

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/pandas/core/generic.py:11734`; SHA-256 file sumber `504217660fbe1aa74ff98b31bea093bd9043cd61c35aba272073464f38e46f22`.

```text
Generate descriptive statistics.

Descriptive statistics include those that summarize the central
tendency, dispersion and shape of a
dataset's distribution, excluding ``NaN`` values.

Analyzes both numeric and object series, as well
as ``DataFrame`` column sets of mixed data types. The output
will vary depending on what is provided. Refer to the notes
below for more detail.

Parameters
----------
percentiles : list-like of numbers, optional
    The percentiles to include in the output. All should
    fall between 0 and 1. The default is
    ``[.25, .5, .75]``, which returns the 25th, 50th, and
    75th percentiles.
include : 'all', list-like of dtypes or None (default), optional
    A white list of data types to include in the result. Ignored
    for ``Series``. Here are the options:

    - 'all' : All columns of the input will be included in the output.
    - A list-like of dtypes : Limits the results to the
      provided data types.
      To limit the result to numeric types submit
      ``numpy.number``. To limit it instead to object columns submit
      the ``numpy.object`` data type. Strings
      can also be used in the style of
      ``select_dtypes`` (e.g. ``df.describe(include=['O'])``). To
      select pandas categorical columns, use ``'category'``
    - None (default) : The result will include all numeric columns.
exclude : list-like of dtypes or None (default), optional,
    A black list of data types to omit from the result. Ignored
    for ``Series``. Here are the options:

    - A list-like of dtypes : Excludes the provided data types
      from the result. To exclude numeric types submit
      ``numpy.number``. To exclude object columns submit the data
      type ``numpy.object``. Strings can also be used in the style of
      ``select_dtypes`` (e.g. ``df.describe(exclude=['O'])``). To
      exclude pandas categorical columns, use ``'category'``
    - None (default) : The result will exclude nothing.

Returns
-------
```

## DataFrame.isna

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/pandas/core/frame.py:6488`; SHA-256 file sumber `9b813159606b62af03bfe76a7089da282d2d6091f308cf2f4d90dd0661a01105`.

```text
Detect missing values.

Return a boolean same-sized object indicating if the values are NA.
NA values, such as None or :attr:`numpy.NaN`, gets mapped to True
values.
Everything else gets mapped to False values. Characters such as empty
strings ``''`` or :attr:`numpy.inf` are not considered NA values
(unless you set ``pandas.options.mode.use_inf_as_na = True``).

Returns
-------
DataFrame
    Mask of bool values for each element in DataFrame that
    indicates whether an element is an NA value.

See Also
--------
DataFrame.isnull : Alias of isna.
DataFrame.notna : Boolean inverse of isna.
DataFrame.dropna : Omit axes labels with missing values.
isna : Top-level isna.

Examples
--------
Show which entries in a DataFrame are NA.

>>> df = pd.DataFrame(dict(age=[5, 6, np.nan],
...                        born=[pd.NaT, pd.Timestamp('1939-05-27'),
...                              pd.Timestamp('1940-04-25')],
...                        name=['Alfred', 'Batman', ''],
...                        toy=[None, 'Batmobile', 'Joker']))
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

>>> df.isna()
     age   born   name    toy
0  False   True  False   True
1  False  False  False  False
2   True  False  False  False

Show which entries in a Series are NA.

>>> ser = pd.Series([5, 6, np.nan])
```

## DataFrame.duplicated

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/pandas/core/frame.py:6828`; SHA-256 file sumber `9b813159606b62af03bfe76a7089da282d2d6091f308cf2f4d90dd0661a01105`.

```text
Return boolean Series denoting duplicate rows.

Considering certain columns is optional.

Parameters
----------
subset : column label or sequence of labels, optional
    Only consider certain columns for identifying duplicates, by
    default use all of the columns.
keep : {'first', 'last', False}, default 'first'
    Determines which duplicates (if any) to mark.

    - ``first`` : Mark duplicates as ``True`` except for the first occurrence.
    - ``last`` : Mark duplicates as ``True`` except for the last occurrence.
    - False : Mark all duplicates as ``True``.

Returns
-------
Series
    Boolean series for each duplicated rows.

See Also
--------
Index.duplicated : Equivalent method on index.
Series.duplicated : Equivalent method on Series.
Series.drop_duplicates : Remove duplicate values from Series.
DataFrame.drop_duplicates : Remove duplicate values from DataFrame.

Examples
--------
Consider dataset containing ramen rating.

>>> df = pd.DataFrame({
...     'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
...     'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
...     'rating': [4, 4, 3.5, 15, 5]
... })
>>> df
    brand style  rating
0  Yum Yum   cup     4.0
1  Yum Yum   cup     4.0
2  Indomie   cup     3.5
3  Indomie  pack    15.0
4  Indomie  pack     5.0

By default, for each set of duplicated values, the first occurrence
```

## DataFrame.median

Locator runtime: `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/lib/python3.12/site-packages/pandas/core/frame.py:11698`; SHA-256 file sumber `9b813159606b62af03bfe76a7089da282d2d6091f308cf2f4d90dd0661a01105`.

```text
Return the median of the values over the requested axis.

Parameters
----------
axis : {index (0), columns (1)}
    Axis for the function to be applied on.
    For `Series` this parameter is unused and defaults to 0.

    For DataFrames, specifying ``axis=None`` will apply the aggregation
    across both axes.

    .. versionadded:: 2.0.0

skipna : bool, default True
    Exclude NA/null values when computing the result.
numeric_only : bool, default False
    Include only float, int, boolean columns. Not implemented for Series.

**kwargs
    Additional keyword arguments to be passed to the function.

Returns
-------
Series or scalar

            Examples
            --------
            >>> s = pd.Series([1, 2, 3])
            >>> s.median()
            2.0

            With a DataFrame

            >>> df = pd.DataFrame({'a': [1, 2], 'b': [2, 3]}, index=['tiger', 'zebra'])
            >>> df
                   a   b
            tiger  1   2
            zebra  2   3
            >>> df.median()
            a   1.5
            b   2.5
            dtype: float64

            Using axis=1

            >>> df.median(axis=1)
```

## numpy.mean

Locator runtime: `Tidak tersedia dari inspect:tidak diketahui`; SHA-256 file sumber `tidak diketahui`.

```text
Compute the arithmetic mean along the specified axis.

Returns the average of the array elements.  The average is taken over
the flattened array by default, otherwise over the specified axis.
`float64` intermediate and return values are used for integer inputs.

Parameters
----------
a : array_like
    Array containing numbers whose mean is desired. If `a` is not an
    array, a conversion is attempted.
axis : None or int or tuple of ints, optional
    Axis or axes along which the means are computed. The default is to
    compute the mean of the flattened array.

    If this is a tuple of ints, a mean is performed over multiple axes,
    instead of a single axis or all the axes as before.
dtype : data-type, optional
    Type to use in computing the mean.  For integer inputs, the default
    is `float64`; for floating point inputs, it is the same as the
    input dtype.
out : ndarray, optional
    Alternate output array in which to place the result.  The default
    is ``None``; if provided, it must have the same shape as the
    expected output, but the type will be cast if necessary.
    See :ref:`ufuncs-output-type` for more details.
    See :ref:`ufuncs-output-type` for more details.

keepdims : bool, optional
    If this is set to True, the axes which are reduced are left
    in the result as dimensions with size one. With this option,
    the result will broadcast correctly against the input array.

    If the default value is passed, then `keepdims` will not be
    passed through to the `mean` method of sub-classes of
    `ndarray`, however any non-default value will be.  If the
    sub-class' method does not implement `keepdims` any
    exceptions will be raised.

where : array_like of bool, optional
    Elements to include in the mean. See `~numpy.ufunc.reduce` for details.

    .. versionadded:: 1.20.0

Returns
-------
```

## Additional precision notes

Pembacaan tambahan saat pilot W04, tetap sumber lokal.

### StandardScaler notes

```text
Standardize features by removing the mean and scaling to unit variance.

The standard score of a sample `x` is calculated as:

.. code-block:: text

    z = (x - u) / s

where `u` is the mean of the training samples or zero if `with_mean=False`,
and `s` is the standard deviation of the training samples or one if
`with_std=False`.

Centering and scaling happen independently on each feature by computing
the relevant statistics on the samples in the training set. Mean and
standard deviation are then stored to be used on later data using
:meth:`transform`.

Standardization of a dataset is a common requirement for many
machine learning estimators: they might behave badly if the
individual features do not more or less look like standard normally
distributed data (e.g. Gaussian with 0 mean and unit variance).

For instance many elements used in the objective function of
a learning algorithm (such as the RBF kernel of Support Vector
Machines or the L1 and L2 regularizers of linear models) assume that
all features are centered around 0 and have variance in the same
order. If a feature has a variance that is orders of magnitude larger
than others, it might dominate the objective function and make the
estimator unable to learn from other features correctly as expected.

`StandardScaler` is sensitive to outliers, and the features may scale
differently from each other in the presence of outliers. For an example
visualization, refer to :ref:`Compare StandardScaler with other scalers
<plot_all_scaling_standard_scaler_section>`.

This scaler can also be applied to sparse CSR or CSC matrices by passing
`with_mean=False` to avoid breaking the sparsity structure of the data.

Read more in the :ref:`User Guide <preprocessing_scaler>`.

Parameters
----------
copy : bool, default=True
    If False, try to avoid a copy and do inplace scaling instead.
    This is not guaranteed to always work inplace; e.g. if the data is
    not a NumPy array or scipy.sparse CSR matrix, a copy may still be
    returned.

with_mean : bool, default=True
    If True, center the data before scaling.
    This does not work (and will raise an exception) when attempted on
    sparse matrices, because centering them entails building a dense
    matrix which in common use cases is likely to be too large to fit in
    memory.

with_std : bool, default=True
    If True, scale the data to unit variance (or equivalently,
    unit standard deviation).

Attributes
----------
scale_ : ndarray of shape (n_features,) or None
    Per feature relative scaling of the data to achieve zero mean and unit
    variance. Generally this is calculated using `np.sqrt(var_)`. If a
    variance is zero, we can't achieve unit variance, and the data is left
    as-is, giving a scaling factor of 1. `scale_` is equal to `None`
    when `with_std=False`.

    .. versionadded:: 0.17
       *scale_*

mean_ : ndarray of shape (n_features,) or None
    The mean value for each feature in the training set.
    Equal to ``None`` when ``with_mean=False`` and ``with_std=False``.

var_ : ndarray of shape (n_features,) or None
    The variance for each feature in the training set. Used to compute
    `scale_`. Equal to ``None`` when ``with_mean=False`` and
    ``with_std=False``.

n_features_in_ : int
    Number of features seen during :term:`fit`.

    .. versionadded:: 0.24

feature_names_in_ : ndarray of shape (`n_features_in_`,)
    Names of features seen during :term:`fit`. Defined only when `X`
    has feature names that are all strings.

    .. versionadded:: 1.0

n_samples_seen_ : int or ndarray of shape (n_features,)
    The number of samples processed by the estimator for each feature.
    If there are no missing samples, the ``n_samples_seen`` will be an
    integer, otherwise it will be an array of dtype int. If
    `sample_weights` are used it will be a float (if no missing data)
    or an array of dtype float that sums the weights seen so far.
    Will be reset on new calls to fit, but increments across
    ``partial_fit`` calls.

See Also
--------
scale : Equivalent function without the estimator API.

:class:`~sklearn.decomposition.PCA` : Further removes the linear
    correlation across features with 'whiten=True'.

Notes
-----
NaNs are treated as missing values: disregarded in fit, and maintained in
transform.

We use a biased estimator for the standard deviation, equivalent to
`numpy.std(x, ddof=0)`. Note that the choice of `ddof` is unlikely to
affect model performance.

Examples
--------
>>> from sklearn.preprocessing import StandardScaler
>>> data = [[0, 0], [0, 0], [1, 1], [1, 1]]
>>> scaler = StandardScaler()
>>> print(scaler.fit(data))
StandardScaler()
>>> print(scaler.mean_)
[0.5 0.5]
>>> print(scaler.transform(data))
[[-1. -1.]
 [-1. -1.]
 [ 1.  1.]
 [ 1.  1.]]
>>> print(scaler.transform([[2, 2]]))
[[3. 3.]]
```

### OneHotEncoder notes

```text
Encode categorical features as a one-hot numeric array.

The input to this transformer should be an array-like of integers or
strings, denoting the values taken on by categorical (discrete) features.
The features are encoded using a one-hot (aka 'one-of-K' or 'dummy')
encoding scheme. This creates a binary column for each category and
returns a sparse matrix or dense array (depending on the ``sparse_output``
parameter).

By default, the encoder derives the categories based on the unique values
in each feature. Alternatively, you can also specify the `categories`
manually.

This encoding is needed for feeding categorical data to many scikit-learn
estimators, notably linear models and SVMs with the standard kernels.

Note: a one-hot encoding of y labels should use a LabelBinarizer
instead.

Read more in the :ref:`User Guide <preprocessing_categorical_features>`.
For a comparison of different encoders, refer to:
:ref:`sphx_glr_auto_examples_preprocessing_plot_target_encoder.py`.

Parameters
----------
categories : 'auto' or a list of array-like, default='auto'
    Categories (unique values) per feature:

    - 'auto' : Determine categories automatically from the training data.
    - list : ``categories[i]`` holds the categories expected in the ith
      column. The passed categories should not mix strings and numeric
      values within a single feature, and should be sorted in case of
      numeric values.

    The used categories can be found in the ``categories_`` attribute.

    .. versionadded:: 0.20

drop : {'first', 'if_binary'} or an array-like of shape (n_features,),             default=None
    Specifies a methodology to use to drop one of the categories per
    feature. This is useful in situations where perfectly collinear
    features cause problems, such as when feeding the resulting data
    into an unregularized linear regression model.

    However, dropping one category breaks the symmetry of the original
    representation and can therefore induce a bias in downstream models,
    for instance for penalized linear classification or regression models.

    - None : retain all features (the default).
    - 'first' : drop the first category in each feature. If only one
      category is present, the feature will be dropped entirely.
    - 'if_binary' : drop the first category in each feature with two
      categories. Features with 1 or more than 2 categories are
      left intact.
    - array : ``drop[i]`` is the category in feature ``X[:, i]`` that
      should be dropped.

    When `max_categories` or `min_frequency` is configured to group
    infrequent categories, the dropping behavior is handled after the
    grouping.

    .. versionadded:: 0.21
       The parameter `drop` was added in 0.21.

    .. versionchanged:: 0.23
       The option `drop='if_binary'` was added in 0.23.

    .. versionchanged:: 1.1
        Support for dropping infrequent categories.

sparse_output : bool, default=True
    When ``True``, it returns a :class:`scipy.sparse.csr_matrix`,
    i.e. a sparse matrix in "Compressed Sparse Row" (CSR) format.

    .. versionadded:: 1.2
       `sparse` was renamed to `sparse_output`

dtype : number type, default=np.float64
    Desired dtype of output.

handle_unknown : {'error', 'ignore', 'infrequent_if_exist', 'warn'},                      default='error'
    Specifies the way unknown categories are handled during :meth:`transform`.

    - 'error' : Raise an error if an unknown category is present during transform.
    - 'ignore' : When an unknown category is encountered during
      transform, the resulting one-hot encoded columns for this feature
      will be all zeros. In the inverse transform, an unknown category
      will be denoted as None.
    - 'infrequent_if_exist' : When an unknown category is encountered
      during transform, the resulting one-hot encoded columns for this
      feature will map to the infrequent category if it exists. The
      infrequent category will be mapped to the last position in the
      encoding. During inverse transform, an unknown category will be
      mapped to the category denoted `'infrequent'` if it exists. If the
      `'infrequent'` category does not exist, then :meth:`transform` and
      :meth:`inverse_transform` will handle an unknown category as with
      `handle_unknown='ignore'`. Infrequent categories exist based on
      `min_frequency` and `max_categories`. Read more in the
      :ref:`User Guide <encoder_infrequent_categories>`.
    - 'warn' : When an unknown category is encountered during transform
      a warning is issued, and the encoding then proceeds as described for
      `handle_unknown="infrequent_if_exist"`.

    .. versionchanged:: 1.1
        `'infrequent_if_exist'` was added to automatically handle unknown
        categories and infrequent categories.

    .. versionadded:: 1.6
       The option `"warn"` was added in 1.6.

min_frequency : int or float, default=None
    Specifies the minimum frequency below which a category will be
    considered infrequent.

    - If `int`, categories with a smaller cardinality will be considered
      infrequent.

    - If `float`, categories with a smaller cardinality than
      `min_frequency * n_samples`  will be considered infrequent.

    .. versionadded:: 1.1
        Read more in the :ref:`User Guide <encoder_infrequent_categories>`.

max_categories : int, default=None
    Specifies an upper limit to the number of output features for each input
    feature when considering infrequent categories. If there are infrequent
    categories, `max_categories` includes the category representing the
    infrequent categories along with the frequent categories. If `None`,
    there is no limit to the number of output features.

    .. versionadded:: 1.1
        Read more in the :ref:`User Guide <encoder_infrequent_categories>`.

feature_name_combiner : "concat" or callable, default="concat"
    Callable with signature `def callable(input_feature, category)` that returns a
    string. This is used to create feature names to be returned by
    :meth:`get_feature_names_out`.

    `"concat"` concatenates encoded feature name and category with
    `feature + "_" + str(category)`.E.g. feature X with values 1, 6, 7 create
    feature names `X_1, X_6, X_7`.

    .. versionadded:: 1.3

Attributes
----------
categories_ : list of arrays
    The categories of each feature determined during fitting
    (in order of the features in X and corresponding with the output
    of ``transform``). This includes the category specified in ``drop``
    (if any).

drop_idx_ : array of shape (n_features,)
    - ``drop_idx_[i]`` is the index in ``categories_[i]`` of the category
      to be dropped for each feature.
    - ``drop_idx_[i] = None`` if no category is to be dropped from the
      feature with index ``i``, e.g. when `drop='if_binary'` and the
      feature isn't binary.
    - ``drop_idx_ = None`` if all the transformed features will be
      retained.

    If infrequent categories are enabled by setting `min_frequency` or
    `max_categories` to a non-default value and `drop_idx[i]` corresponds
    to an infrequent category, then the entire infrequent category is
    dropped.

    .. versionchanged:: 0.23
       Added the possibility to contain `None` values.

infrequent_categories_ : list of ndarray
    Defined only if infrequent categories are enabled by setting
    `min_frequency` or `max_categories` to a non-default value.
    `infrequent_categories_[i]` are the infrequent categories for feature
    `i`. If the feature `i` has no infrequent categories
    `infrequent_categories_[i]` is None.

    .. versionadded:: 1.1

n_features_in_ : int
    Number of features seen during :term:`fit`.

    .. versionadded:: 1.0

feature_names_in_ : ndarray of shape (`n_features_in_`,)
    Names of features seen during :term:`fit`. Defined only when `X`
    has feature names that are all strings.

    .. versionadded:: 1.0

feature_name_combiner : callable or None
    Callable with signature `def callable(input_feature, category)` that returns a
    string. This is used to create feature names to be returned by
    :meth:`get_feature_names_out`.

    .. versionadded:: 1.3

See Also
--------
OrdinalEncoder : Performs an ordinal (integer)
  encoding of the categorical features.
TargetEncoder : Encodes categorical features using the target.
sklearn.feature_extraction.DictVectorizer : Performs a one-hot encoding of
  dictionary items (also handles string-valued features).
sklearn.feature_extraction.FeatureHasher : Performs an approximate one-hot
  encoding of dictionary items or strings.
LabelBinarizer : Binarizes labels in a one-vs-all
  fashion.
MultiLabelBinarizer : Transforms between iterable of
  iterables and a multilabel format, e.g. a (samples x classes) binary
  matrix indicating the presence of a class label.

Examples
--------
Given a dataset with two features, we let the encoder find the unique
values per feature and transform the data to a binary one-hot encoding.

>>> from sklearn.preprocessing import OneHotEncoder

One can discard categories not seen during `fit`:

>>> enc = OneHotEncoder(handle_unknown='ignore')
>>> X = [['Male', 1], ['Female', 3], ['Female', 2]]
>>> enc.fit(X)
OneHotEncoder(handle_unknown='ignore')
>>> enc.categories_
[array(['Female', 'Male'], dtype=object), array([1, 2, 3], dtype=object)]
>>> enc.transform([['Female', 1], ['Male', 4]]).toarray()
array([[1., 0., 1., 0., 0.],
       [0., 1., 0., 0., 0.]])
>>> enc.inverse_transform([[0, 1, 1, 0, 0], [0, 0, 0, 1, 0]])
array([['Male', 1],
       [None, 2]], dtype=object)
>>> enc.get_feature_names_out(['gender', 'group'])
array(['gender_Female', 'gender_Male', 'group_1', 'group_2', 'group_3'], ...)

One can always drop the first column for each feature:

>>> drop_enc = OneHotEncoder(drop='first').fit(X)
>>> drop_enc.categories_
[array(['Female', 'Male'], dtype=object), array([1, 2, 3], dtype=object)]
>>> drop_enc.transform([['Female', 1], ['Male', 2]]).toarray()
array([[0., 0., 0.],
       [1., 1., 0.]])

Or drop a column for feature only having 2 categories:

>>> drop_binary_enc = OneHotEncoder(drop='if_binary').fit(X)
>>> drop_binary_enc.transform([['Female', 1], ['Male', 2]]).toarray()
array([[0., 1., 0., 0.],
       [1., 0., 1., 0.]])

One can change the way feature names are created.

>>> def custom_combiner(feature, category):
...     return str(feature) + "_" + type(category).__name__ + "_" + str(category)
>>> custom_fnames_enc = OneHotEncoder(feature_name_combiner=custom_combiner).fit(X)
>>> custom_fnames_enc.get_feature_names_out()
array(['x0_str_Female', 'x0_str_Male', 'x1_int_1', 'x1_int_2', 'x1_int_3'],
      dtype=object)

Infrequent categories are enabled by setting `max_categories` or `min_frequency`.

>>> import numpy as np
>>> X = np.array([["a"] * 5 + ["b"] * 20 + ["c"] * 10 + ["d"] * 3], dtype=object).T
>>> ohe = OneHotEncoder(max_categories=3, sparse_output=False).fit(X)
>>> ohe.infrequent_categories_
[array(['a', 'd'], dtype=object)]
>>> ohe.transform([["a"], ["b"]])
array([[0., 0., 1.],
       [1., 0., 0.]])
```
