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

    return [x for x in weights]

def custom_predict(X_values, weights):
    return np.array([weights[0] * x + weights[1] for x in X_values])

def mean_squared_error(actual, predicted):
    error_sum = .0
    
    for cur_actual, cur_predicted in zip(actual, predicted):
        error_sum += (cur_actual - cur_predicted) ** 2
    
    return error_sum / len(actual)

def build_models(input_filename, fraction_training=.8):
    """
    See homework assignment.
    :param input_filename: Filename for input datafile.
    """

    # load file and shuffle
    df = pd.read_csv(input_filename)
    random_state = 69
    shuffled_df = shuffle(df, random_state=random_state)
    split_idx = int(fraction_training * len(df))

    # split data into train and test
    train_df = shuffled_df.iloc[:split_idx]
    test_df = shuffled_df.iloc[split_idx:]
    print(f'Used {len(train_df)} samples for training.')

    # separate X and y
    X_train = train_df.iloc[:, 0]
    X_test = test_df.iloc[:, 0]
    y_train = train_df.iloc[:, -1]
    y_test = test_df.iloc[:, -1]

    # custom/manual linear regression
    custom_weights = custom_linear_regression(X_train.values, y_train.values)
    print(f'Manual Model: y={custom_weights[0]}x + {custom_weights[1]}')
    custom_predictions = custom_predict(X_test, custom_weights)
    custom_mse = mean_squared_error(y_test, custom_predictions)
    print(f'MSE: {custom_mse}')
    
    # sklearn linear regression
    sklearnLinReg = LinearRegression()
    sklearnLinReg.fit(np.array(X_train).reshape(-1, 1), y_train)
    sklearn_weights = [sklearnLinReg.coef_[0], sklearnLinReg.intercept_]
    print(f'Sklearn Model: y={sklearn_weights[0]}x + {sklearn_weights[1]}')
    sklearn_predictions = sklearnLinReg.predict(np.array(X_test).reshape(-1, 1))
    sklearn_mse = mean_squared_error(y_test, sklearn_predictions)
    print(f'MSE: {sklearn_mse}')


if __name__ == '__main__':
    filename = "q4_data.csv"
    build_models(filename)
