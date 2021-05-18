import numpy as np
import pandas as pd


def get_model_data(train, validate, test):
    '''

    '''
    train, validate, test = add_parse_categories(train, validate, test)
    X_train, y_train, X_validate, y_validate, X_test, y_test = split_X_y(train, validate, test)

    return X_train, y_train, X_validate, y_validate, X_test, y_test


def add_parse_categories(train, validate, test, cols=['color', 'spectral_class']):
    '''
    Add parse matrix to the dataset using `color` and `spectral_class`
    '''
    train = pd.get_dummies(data=train, columns=cols)
    validate = pd.get_dummies(data=validate, columns=cols)
    test = pd.get_dummies(data=test, columns=cols)
    
    return train, validate, test


def split_X_y(train, validate, test):
    '''
    Split train, validate, and test datasets into X and y sets for modeling.
    '''
    # Create an empty list to capture each X and y set in the loop.
    datasets = []
    TARGET = 'star_type'

    # Create a list of nonnumeric columns to remove from the dataset.
    cols_to_drop = ['star_type_name',
                    'star_type',
                    'scaled_luminosity',
                    'scaled_radius',
                    'quantiled_luminosity',
                    'quantiled_absolute_magnitude']

    # Automate data splitting using python's built-in exec() function.
    for dataset in ['train', 'validate', 'test']:
        exec(f'X_{dataset}={dataset}.drop(columns=cols_to_drop)')
        exec(f'y_{dataset}={dataset}[[TARGET]]')

        exec(f'datasets.extend([X_{dataset}, y_{dataset}])')

    # Return the list of datasets: X_train, y_train, X_validate, y_validate, X_test, y_test
    return datasets
