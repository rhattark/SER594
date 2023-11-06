import pandas as pd
import numpy as np
from sklearn.utils import shuffle

__author__ = "Rhishabh Hattarki"
__date__ = "6 November 2023"
__assignment = "SER594: Homework 5 Q5 Programming"

def custom_predict(X_values, weights):
    return np.array([weights[0] * x + weights[1] for x in X_values])

def mean_squared_error(actual, predicted):
    error_sum = .0
    
    for cur_actual, cur_predicted in zip(actual, predicted):
        error_sum += (cur_actual - cur_predicted) ** 2
    
    return error_sum / len(actual)

def run_gd(input_filename, fraction_training=.8):
    """
    See homework assignment.
    :param input_filename: Filename for input datafile.
    """

    # load file and shuffle
    df = pd.read_csv(input_filename)
    random_state = 69
    shuffled_df = shuffle(df, random_state=random_state)

    # split data into train and test
    split_idx = int(fraction_training * len(df))
    train_df = shuffled_df.iloc[:split_idx]
    test_df = shuffled_df.iloc[split_idx:]
    print(f'Selected {len(train_df)} samples for training.\n')

    # separate X and y
    X_train = train_df.iloc[:, 0]
    X_test = test_df.iloc[:, 0]
    y_train = train_df.iloc[:, -1]
    y_test = test_df.iloc[:, -1]

    alpha = .01
    epochs = 2500
    w0 = 0 # intercept
    w1 = 0 # slope
    N_train = X_train.shape[0]

    for i in range(epochs):
        print(f'Iteration: {i}')
        dw0 = 1 / N_train * (-1) * sum(y_train - (w0 + w1 * X_train))
        dw1 = 1 / N_train * (-1) * sum(X_train * (y_train - (w0 + w1 * X_train)))
        w0 -= alpha * dw0
        w1 -= alpha * dw1
        print(f'\tw0_updated: {w0}, w1_updated: {w1}')
        predictions = w1 * X_train + w0
        cur_mse = mean_squared_error(y_train, predictions)
        print(f'\tMSE: {cur_mse}')


if __name__ == '__main__':
    filename = "q5_data.csv"
    run_gd(filename)
