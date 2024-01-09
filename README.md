# UCI_classification

UCI classification datasets ([csv of metadata included datasets](https://github.com/YutongWangUMich/UCI_classification/blob/main/UCI_classification/metadata/datasets_summary.csv))loading utilities. 



## Setup/Installation

### Method 1: download then install

Navigate to the root directory of this repository, then run the following in shell.

```
pip install .
```

### Method 2: pip install from github

```
pip install git+https://github.com/YutongWangUMich/UCI_classification.git
```

## Functionalities/Usage examples

### Load a dataset

```
import UCI_classification as uci
Xtrn, ytrn = uci.datasets.load_trn('iris', return_X_y=True)
```

### Get metadata of datasets

```
import UCI_classification as uci
all_datasets = uci.datasets.get_data_list('all')
uci.datasets.get_metadata(all_datasets)
```

Output:
```
           dataset_name  n_samples  n_train  n_test  n_features  n_classes  L2_dist_est
0               abalone       4177     3133    1044           8          3     8.669142
1    acute-inflammation        120       90      30           6          2    12.625558
2       acute-nephritis        120       90      30           6          2    12.537478
3                 adult      48842    32561   16281          14          2    23.300632
4             annealing        898      798     100          31          5    49.967534
..                  ...        ...      ...     ...         ...        ...          ...
116                wine        178      134      44          13          3    25.647811
117    wine-quality-red       1599     1199     400          11          6    16.271732
118  wine-quality-white       4898     3674    1224          11          7    18.127150
119               yeast       1484     1113     371           8         10     9.578626
120                 zoo        101       76      25          16          7    34.207623

[121 rows x 7 columns]
```
Note, see section below regarding the column `L2_dist_est`.


## Files and directories

Overview of the content in the `UCI_classification` module subdirectory:

- `UCI_classification/data_py.zip`: archive of the 121 UCI classification datasets originally downloaded from http://www.bioinf.jku.at/people/klambauer/data_py.zip hosted by Dr. Klambauer. These 121 UCI datasets were originally analyzed in [[Fernández-Delgado et al., 2014]](https://jmlr.org/papers/volume15/delgado14a/delgado14a.pdf).
- `UCI_classification/data_lists/*.txt`: curated sublists of datasets studied in the literature.
- `UCI_classification/metadata/*.csv`: metadata about each of the datasets.

### Raw data files

The datasets are stored in the directory `UCI_classification/data/` which is unzipped from `UCI_classification/data_py.zip` after installation.

The format is the same as in the original compilation in https://github.com/bioinf-jku/SNNs and is shown below:

```
data/
├── DATASETNAME/
│   ├── DATASETNAME_py.dat           # feature vectors
│   ├── folds_py.dat                 # the train and test split
│   ├── labels_py.dat                # labels (0,1,...,num_classes)
│   └── validation_folds_py.dat      # 4-fold splits of the training set
└── ...
```

where `DATASETNAME` stands for `abalone`, `iris`, etc.

### Curated lists of datasets

Lists of datasets

```
data_list/
├── all.txt                          # the list all datasets
├── arora2019harnessing.txt          # 90 datasets used in [Arora et al, 2019]
├── fathony2016adversarial.txt       # 12 datasets used in [Fathony et al, 2016]
└── testing.txt                      # three datasets: [iris, ionosphere, wine]. Useful for testing.
```

- [Arora et al, 2019](https://arxiv.org/abs/1910.01663) uses 90 datasets. See their "Appendix A Dataset Selection" for a description of their curation methodology. Also, see [their github repo](https://github.com/LeoYu/neural-tangent-kernel-UCI).

- [Fathony et al, 2016](https://proceedings.neurips.cc/paper/2016/hash/ad13a2a07ca4b7642959dc0c4c740ab6-Abstract.html) uses the following 12 datasets:

|    | name there   | name here                | # class | # samp | # trn | # tst | # feat |
|----|--------------|--------------------------|---------|--------|-------|-------|--------|
|  1 | iris         | iris                     |       3 |    150 |   105 |    45 |      4 |
|  2 | glass        | glass                    |       6 |    214 |   149 |    65 |      9 |
|  3 | redwine      | wine-quality-red         |      10 |   1599 |  1119 |   480 |     11 |
|  4 | ecoli        | ecoli                    |       8 |    336 |   235 |   101 |      7 |
|  5 | vehicle      | statlog-vehicle          |       4 |    846 |   592 |   254 |     18 |
|  6 | segment      | image-segmentation       |       7 |   2310 |  1617 |   693 |     19 |
|  7 | sat          | statlog-landsat          |       7 |   6435 |  4435 |  2000 |     36 |
|  8 | optdigits    | optical                  |      10 |   5620 |  3823 |  1797 |     64 |
|  9 | pageblocks   | page-blocks              |       5 |   5473 |  3831 |  1642 |     10 |
| 10 | libras       | libras                   |      15 |    360 |   252 |   108 |     90 |
| 11 | vertebral    | vertebral-column-3clases |       3 |    310 |   217 |    93 |      6 |
| 12 | breatstissue | breast-tissue            |       6 |    106 |    74 |    32 |      9 |

We note that the numbers reported in columns `# trn` and `# tst` are directly taken from their Table 1, which does not match the train-test split in this repository. See Fathony et al. 2016 Section 4 for details on their experimental setup.



### Metadata about the datasets `metadata/`

```
metadata/
├── datasets_summary.csv              # a table of summary of essential informations of each dataset
└── L2_dist_est.csv                   # precomputed values of L2_dist_est, see code chunk below and [Shankar et al 2020].
```    

### On `L2_dist_est`

This is a dataset level numerical value computed originally in [Shankar et al 2020](http://proceedings.mlr.press/v119/shankar20a/shankar20a.pdf).
The computation is performed as follows:

```
dist_est = kernel.est_dist(x_train, 1000)
# See https://github.com/modestyachts/neural_kernels_code/blob/0202718ce8da87f7c1682a6fd87f0caeeaba0859/UCI/UCI.py#L80
# The function est_dist is from 
# https://github.com/modestyachts/neural_kernels_code/blob/0202718ce8da87f7c1682a6fd87f0caeeaba0859/UCI/kernel.py
```
