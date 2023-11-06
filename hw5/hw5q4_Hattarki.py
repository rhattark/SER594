import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.utils import shuffle
import numpy as np

__author__ = "Rhishabh Hattarki"
__date__ = "6 November 2023"
__assignment = "SER594: Homework 5 Q4 Programming"


def build_models(input_filename, fraction_training=.8):
    """
    See homework assignment.
    :param input_filename: Filename for input datafile.
    """

    df = pd.read_csv(input_filename)
    random_state = 69
    shuffled_df = df.sample(frac=1, random_state=random_state)
    split_idx = int(fraction_training * len(df))

    train_df = shuffled_df.iloc[:split_idx]
    test_df = shuffled_df.iloc[split_idx:]
    print(len(train_df), len(test_df))
    
    pass


if __name__ == '__main__':
    filename = "q4_data.csv"
    build_models(filename)
