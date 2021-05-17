import numpy as np
import pandas as pd

def split_X_y(train, validate, test):
    '''

    '''
    datasets = []
    TARGET = 'star_type'

    # Create a list of nonnumeric columns to remove from the dataset.
    cols_to_drop = ['temperature', 'luminosity', 'radius', 'absolute_magnitude', 
                    'color', 'spectral_class', 'star_type_name', 'star_type']

    # Automate data splitting using python's built-in exec() function.
    
    for dataset in ['train', 'validate', 'test']:
        exec(f'X_{dataset}={dataset}.drop(columns=cols_to_drop)')
        exec(f'y_{dataset}={dataset}[[TARGET]]')

        exec(f'datasets.extend([X_{dataset}, y_{dataset}])')

    return datasets
