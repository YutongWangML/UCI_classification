# UCI_classification

UCI classification datasets loading utilities. What is included 

- `setup.sh`: a shell script to automatically download and clean the 121 datasets curated by https://github.com/bioinf-jku/SNNs onto your machine.
- `data_lists/*.txt`: curated sublists of datasets studied in the literature.
- `metadata/*.csv`: metadata about each of the datasets.
- `jupyter_notebooks/*.ipynb`: notes for using this repository.

## Setup/Installation

You need to be in the same directory as the `setup.sh` file. Run the following in shell.

```
source setup.sh
```

I've left comments in `setup.sh` regarding what the code is doing. In a nutshell, the script downloads the data and clean up the naming schemes.


## Usage/Example

See `jupyter_notebooks/02_LR_TF_example.ipynb` for a logistic regression example implemented in TensorFlow.


## Files and directories


### Raw data files

`data/` - contains the raw data files (feature vectors, labels, validation sets)

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

[Arora et al, 2019](https://arxiv.org/abs/1910.01663) uses 90 datasets. See their "Appendix A Dataset Selection" for a description of their curation methodology. Also, see their [github repo](https://github.com/LeoYu/neural-tangent-kernel-UCI).

[Fathony et al, 2016](https://proceedings.neurips.cc/paper/2016/hash/ad13a2a07ca4b7642959dc0c4c740ab6-Abstract.html) uses the following 12 datasets:

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

[Shankar et al 2020](http://proceedings.mlr.press/v119/shankar20a/shankar20a.pdf)

```
dist_est = kernel.est_dist(x_train, 1000)
# See https://github.com/modestyachts/neural_kernels_code/blob/0202718ce8da87f7c1682a6fd87f0caeeaba0859/UCI/UCI.py#L80
# The function est_dist is from 
# https://github.com/modestyachts/neural_kernels_code/blob/0202718ce8da87f7c1682a6fd87f0caeeaba0859/UCI/kernel.py
```

### Jupyter notebooks and tutorials `jupyter_notebooks/`


```
jupyter_notebooks/
├── 01_datasets_summary.ipynb              # display the table of summary
└── 02_LR_TF_example.ipynb                 # Logistic regression in TensorFlow example
```
