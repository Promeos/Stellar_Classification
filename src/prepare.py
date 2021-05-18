import pandas as pd
import numpy as np

from pandas.api.types import CategoricalDtype


def prep_star_data(dataset):
    '''
    Returns 

    Parameters
    ----------
    None 
    
    Returns
    -------
    '''
    dataset = format_column_names(dataset)
    dataset = star_names(dataset)
    dataset = normalize_colors(dataset)
    dataset = categorize_features(dataset)
    dataset = arrange_columns(dataset)

    return dataset


def format_column_names(dataset):
    '''
    Formats all column names to be lowecase and replaces column names
    with descriptive names.

    Parameters
    ----------
    dataset
    
    Returns
    -------
    dataset
    '''
    # Lowercase the column names
    dataset.columns = [column.lower() for column in dataset.columns]

    # Rename columns with more descriptive names
    dataset.rename(columns={'l':'luminosity',
                            'r':'radius',
                            'a_m':'absolute_magnitude',
                            'type':'star_type'},
                   inplace=True)

    return dataset


def star_names(dataset, col='star_type'):
    '''
    Creates a new column name called `star_type_name` with the explicit name
    of each star.

    Parameters
    ----------
    dataset :

    col :
    
    Returns
    -------
    dataset
    '''
    # Mapping dict to decode the meaning of each number to the stars' explicit type.
    star_type_map = {0: 'Red Dwarf',
                     1: 'Brown Dwarf',
                     2: 'White Dwarf',
                     3: 'Main Sequence',
                     4: 'Super Giants',
                     5: 'Hyper Giants'}

    dataset['star_type_name'] = dataset[[col]].applymap(star_type_map.get)

    return dataset


def normalize_colors(dataset, col='color'):
    '''
    Formats all string values in the `color` column to be lowercase
    and removes all non-string characters.

    Parameters
    ----------
    dataset :

    col :
    
    Returns
    -------
    dataset
    '''
    # Lowercase all color names
    dataset[col] = dataset[col].apply(str.lower)

    # Remove the hyphen from all color names
    dataset[col] = dataset[col].str.replace('-', ' ')

    # Replace redundant color names with normalized version.
    dataset.replace({col:{'yellowish white': 'yellow white',
                          'white yellow': 'yellow white'}},
                     inplace=True)

    return dataset


def categorize_features(dataset, cols=['spectral_class', 'color']):
    '''
    Casts object columns to Categorical and creates numeric encodings of each
    Category.

    Parameters
    ----------
    dataset :

    cols :
    
    Returns
    -------
    dataset
    '''
    # Create an Ordinal Category Type for Spectral Class
    spectral_cat_type = CategoricalDtype(categories=list('MKGFABO'), ordered=True)

    # Create categorized versions of the column names.
    dataset[cols[0]] = dataset[cols[0]].astype(spectral_cat_type)
    dataset[cols[1]] = dataset[cols[1]].astype('category')

    return dataset


def arrange_columns(dataset):
    '''
    Rearranges column names to move the target column, `star_type` to the last
    column of the dataframe.

    Parameters
    ----------
    dataset 
    
    Returns
    -------
    dataset
    '''
    dataset = dataset[['temperature',
                       'luminosity',
                       'radius',
                       'absolute_magnitude',
                       'color',
                       'spectral_class',
                       'star_type_name',
                       'star_type']]

    return dataset





