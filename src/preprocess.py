import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, QuantileTransformer


def create_datasets(dataset):
    '''
    Splits the stars dataset into train, validate, and test sets.

    There are 40 observations for each of the 6 star types
    Training set contains 50% of the dataset
    
    -37.5%-12.5%
    
 

    Parameters
    ----------
    dataset :
    
    Returns
    -------
    train

    validate

    test

    '''
    # Split the dataset into train, and validation + test sets
    train, validate_test = train_test_split(dataset,
                                            test_size=.50,
                                            random_state=369,
                                            stratify=dataset['star_type'])

    # Split validate_test portion into validate and test sets
    validate, test = train_test_split(validate_test,
                                      test_size=0.25,
                                      random_state=369,
                                      stratify=validate_test['star_type'])

    return train, validate, test


def create_X_y_sets(train, validate, test):
    '''
    Removes all non-numeric columns from the train, validate, and test datasets.
    Remaining columns are in each dataset are split into X and y dataframes stratified 
    by `star_type` for data modeling.

    Parameters
    ----------
    train :

    validate :

    test : 
    
    Returns
    -------
    X_train
    y_train
    X_validate
    y_validate
    X_test
    y_test
    '''
    # Create a variable to store the target name to the list of columns dropped from
    # the X datasets
    TARGET = 'star_type'

    # Create a list of nonnumeric columns to remove from the dataset.
    columns_to_drop = list(train.select_dtypes(exclude='number').columns)
    columns_to_drop.append(TARGET)

    # Automate data splitting using python's built-in exec() function.
    for dataset in ['train', 'validate', 'test']:
        exec(f'X_{dataset}={dataset}.drop(columns=columns_to_drop)')
        exec(f'y_{dataset}={dataset}[[TARGET]]')

    return X_train, y_train, X_validate, y_validate, X_test, y_test


def arrange_columns(train, validate, test):
    '''

    '''
    arranged_cols = ['temperature',
    'luminosity',
    'radius',
    'absolute_magnitude',
    'color',
    'spectral_class',
    'spectral_class_num',
    'color_num',
    'scaled_temperature',
    'scaled_luminosity',
    'scaled_radius',
    'scaled_absolute_magnitude',
    'quantiled_temperature',
    'quantiled_luminosity',
    'quantiled_radius',
    'quantiled_absolute_magnitude',
    'star_type_name',
    'star_type']
    
    train = train[arranged_cols]
    validate = validate[arranged_cols]
    test = test[arranged_cols]

    return train, validate, test


def scale_data(train, validate, test):
    '''

    '''
    cols_to_scale = ['temperature', 'luminosity', 'radius', 'absolute_magnitude']
    scaled_cols = [f'scaled_{col}' for col in cols_to_scale]
    quantile_cols = [f'quantiled_{col}' for col in cols_to_scale]


    def min_max_scaler(train, validate, test):
        '''

        '''
        nonlocal cols_to_scale, scaled_cols

        scaler = MinMaxScaler()

        train[scaled_cols] = scaler.fit_transform(train[cols_to_scale])
        validate[scaled_cols] = scaler.transform(validate[cols_to_scale])
        test[scaled_cols] = scaler.transform(test[cols_to_scale])

        return train, validate, test



    def quantile_scaler(train, validate, test):
        '''

        '''
        nonlocal cols_to_scale, quantile_cols

        q_scaler = QuantileTransformer(20, output_distribution='normal')

        train[quantile_cols] = q_scaler.fit_transform(train[cols_to_scale])
        validate[quantile_cols] = q_scaler.transform(validate[cols_to_scale])
        test[quantile_cols] = q_scaler.transform(test[cols_to_scale])

        return train, validate, test


    train, validate, test = min_max_scaler(train, validate, test)
    train, validate, test = quantile_scaler(train, validate, test)
    train, validate, test = arrange_columns(train, validate, test)

    return train, validate, test


def arrange_columns(train, validate, test):
    '''

    '''
    arranged_cols = ['temperature',
    'luminosity',
    'radius',
    'absolute_magnitude',
    'color',
    'spectral_class',
    'spectral_class_num',
    'color_num',
    'scaled_temperature',
    'scaled_luminosity',
    'scaled_radius',
    'scaled_absolute_magnitude',
    'quantiled_temperature',
    'quantiled_luminosity',
    'quantiled_radius',
    'quantiled_absolute_magnitude',
    'star_type_name',
    'star_type']
    
    train = train[arranged_cols]
    validate = validate[arranged_cols]
    test = test[arranged_cols]

    return train, validate, test