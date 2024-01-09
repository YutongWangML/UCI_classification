import os
import pandas as pd
import numpy as np
from sklearn.utils import Bunch
from pkg_resources import resource_filename


def get_data_list(name):
    """Retrieve a list of data from a specified text file."""
    # Construct the path to the file relative to the package
    file_path = resource_filename('UCI_classification', os.path.join('data_lists', f'{name}.txt'))

    # Open the file and return its contents as a list of lines
    with open(file_path, "r") as file:
        return file.read().splitlines()


def load_trn(dataset_name, return_X_y=False):
    """Load the training datasets."""
    # Construct the path to the data directory relative to the package
    data_dir = resource_filename('UCI_classification', os.path.join('data', dataset_name))

    # Construct file paths
    data_file = os.path.join(data_dir, dataset_name + "_py.dat")
    label_file = os.path.join(data_dir, "labels_py.dat")
    validation_folds_file = os.path.join(data_dir, "validation_folds_py.dat")
    test_folds_file = os.path.join(data_dir, "folds_py.dat")

    # Load the data
    data = pd.read_csv(data_file, header=None).values
    label = pd.read_csv(label_file, header=None).values.flatten()
    validation_folds = pd.read_csv(validation_folds_file, header=None).values
    test_folds = pd.read_csv(test_folds_file, header=None).values

    # Process the data
    train_index = (test_folds[:, 0] == 0)
    test_index = (test_folds[:, 0] == 1)

    cv_folds = []
    for i in range(validation_folds.shape[1]):
        val = (validation_folds[:, i] == 1)
        validation_index = (train_index & (val == 1))
        validation_index = validation_index[train_index]
        cv_folds += [(~validation_index, validation_index)]

    train_x = data[train_index, :]
    train_y = label[train_index]
    train_y[np.isnan(train_y)] = -1

    # Return the data
    if return_X_y:
        return (train_x, train_y)
    else:
        return Bunch(data=train_x, target=train_y, cv_folds=cv_folds)


def load_tst(dataset_name, return_X_y=False):
    """Load the testing datasets."""
    # Construct the path to the data directory relative to the package
    data_dir = resource_filename('UCI_classification', os.path.join('data', dataset_name))

    # Construct file paths
    data_file = os.path.join(data_dir, dataset_name + "_py.dat")
    label_file = os.path.join(data_dir, "labels_py.dat")
    test_folds_file = os.path.join(data_dir, "folds_py.dat")

    # Load the data
    data = pd.read_csv(data_file, header=None).values
    label = pd.read_csv(label_file, header=None).values.flatten()
    test_folds = pd.read_csv(test_folds_file, header=None).values

    # Process the data
    test_index = (test_folds[:, 0] == 1)

    test_x = data[test_index, :]
    test_y = label[test_index]
    test_y[np.isnan(test_y)] = -1

    # Return the data
    if return_X_y:
        return (test_x, test_y)
    else:
        return Bunch(data=test_x, target=test_y)


def load_all(dataset_name):
    """Load the merged training and testing datasets."""
    # Useful if you want to create your own train-test splits
    Xtrn, ytrn = load_trn(dataset_name,return_X_y=True)
    Xtst, ytst = load_tst(dataset_name,return_X_y=True)
    Xall = np.vstack([Xtrn,Xtst])
    yall = np.concatenate([ytrn, ytst])
    return (Xall,yall)


def get_metadata(dataset_names):
    """Load dataset summary and subset it based on datasets in 'tiny.txt'."""

    # Load datasets summary from 'datasets_summary.csv'
    summary_file_path = resource_filename('UCI_classification', os.path.join('metadata','datasets_summary.csv'))
    datasets_summary = pd.read_csv(summary_file_path)

    # Subset the DataFrame to include only rows with names in 'tiny.txt'
    subset_summary = datasets_summary[datasets_summary['dataset_name'].isin(dataset_names)]

    return subset_summary
