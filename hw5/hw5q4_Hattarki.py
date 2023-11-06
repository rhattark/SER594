import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
import numpy as np

__author__ = "Rhishabh Hattarki"
__date__ = "6 November 2023"
__assignment = "SER594: Homework 5 Q4 Programming"

def custom_linear_regression(A_, b_):
    A_with_ones = np.column_stack((A_, np.ones(A_.shape[0])))
    A_transpose = np.transpose(A_with_ones)
    A_transpose_dot_A = np.dot(A_transpose, A_with_ones)
    inverse = np.linalg.inv(A_transpose_dot_A)
    inverse_dot_A_transpose = np.dot(inverse, A_transpose)
    weights = np.dot(inverse_dot_A_transpose, b_)

    return weights

def build_models(input_filename, fraction_training=.8):
    """
    See homework assignment.
    :param input_filename: Filename for input datafile.
    """

    df = pd.read_csv(input_filename)
    random_state = 69
    shuffled_df = shuffle(df, random_state=random_state)
    split_idx = int(fraction_training * len(df))

    # split data into train and test
    train_df = shuffled_df.iloc[:split_idx]
    test_df = shuffled_df.iloc[split_idx:]

    # separate X and y
    X_train = train_df.iloc[:, 0]
    X_test = test_df.iloc[:, 0]
    y_train = train_df.iloc[:, -1]
    y_test = test_df.iloc[:, -1]

    custom_weights = custom_linear_regression(X_train.values, y_train.values)
    print("custom weights", [x for x in custom_weights])
    
    sklearnLinReg = LinearRegression()
    sklearnLinReg.fit(np.array(X_train).reshape(-1, 1), y_train)
    print("sklearn weights", [sklearnLinReg.coef_[0], sklearnLinReg.intercept_])
    
    pass


if __name__ == '__main__':
    filename = "q4_data.csv"
    build_models(filename)
