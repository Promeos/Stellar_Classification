import pandas as pd

from sklearn.model_selection import train_test_split


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