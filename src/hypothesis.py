import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import f_oneway, ttest_1samp, ttest_ind, chi2_contingency, ttest_ind, kruskal


########################################## Global Hypothesis Variables #########################################
CONFIDENCE_INTERVAL = .95
ALPHA = 1 - CONFIDENCE_INTERVAL


def evaluate_p_value(p):
    '''
    Determine if the p-value is less than alpha.
    '''
    global ALPHA

    if p < ALPHA:
        print(f"{p:.03f} < {ALPHA:.2f}")
        print("Reject the null hypothesis")
    else:
        print("Fail to reject the null hypothesis")


def ttest_datasets(train, col='quantiled_radius'):
    '''
    Create Series of Data for each star type.
    '''
    hyper = train[train.star_type_name == 'Hyper Giants'][col]
    super_ = train[train.star_type_name == 'Super Giants'][col]
    sequence = train[train.star_type_name == 'Main Sequence'][col]
    white = train[train.star_type_name == 'White Dwarf'][col]
    brown = train[train.star_type_name == 'Brown Dwarf'][col]
    red = train[train.star_type_name == 'Red Dwarf'][col]

    return hyper, super_, sequence, white,  brown, red
