# Acquire File
import pandas as pd
import numpy as np
import os


###################### Acquire Star Data ########################
def get_star_data():
    '''
    Acquires the stars dataset from `stars.csv`.
    Returns a Pandas DataFrame.

    Parameters
    ----------
    None 
    
    Returns
    -------
    df : pandas.core.frame.DataFrame
       Stars dataset. 
    '''

    try:
        if os.path.isfile('./data/stars.csv'):
            return pd.read_csv('./data/stars.csv')
    except:
        raise FileNotFoundError("Oh my stars, you're missing the file named 'stars.csv'. You can acquire the data here: https://www.kaggle.com/brsdincer/star-type-classification")