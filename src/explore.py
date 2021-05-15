import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.express import parallel_categories as parallel_cats


########################################## Global Variables ###########################################
## Scatterplot Variables
STAR_NAMES = ['Hyper Giants', 'Super Giants', 'Main Sequence', 'White Dwarf', 'Brown Dwarf', 'Red Dwarf']
MARKERS = ['*','X','P','h','p','D']
MARKER_COLORS = ['blue', 'lightblue', 'gold', 'whitesmoke', 'saddlebrown', 'red']

## Boxplot Variables
BOXPLOT_FEATURES = ['temperature', 'luminosity', 'radius', 'absolute_magnitude', 'scaled_temperature',
                     'scaled_luminosity', 'scaled_radius', 'scaled_absolute_magnitude',
                     'quantiled_temperature', 'quantiled_luminosity', 'quantiled_radius',
                     'quantiled_absolute_magnitude']

TITLED_FEATURES = ['Temperature', 'Luminosity', 'Radius', 'Absolute Magnitude', 'Scaled Temperature',
                   'Scaled Luminosity', 'Scaled Radius', 'Scaled Absolute Magnitude',
                   'Quantiled Temperature', 'Quantiled Luminosity', 'Quantiled Radius',
                   'Quantiled Absolute Magnitude']

## Crosstab Variables
STAR_NAMES_SORTED = ['Red Dwarf', 'Brown Dwarf', 'White Dwarf',
                     'Main Sequence', 'Super Giants', 'Hyper Giants']

COLORS_SORTED = ['red', 'orange red', 'orange', 'pale yellow orange',
                 'yellow white', 'white', 'blue white', 'blue']

SPECTRAL_CLASS_SORTED = list('MKGFABO')

## Plotting Defaults
CBAR_FORMAT = {'ticks':list(np.arange(0, 21, 5))}


def pearson_correlations(train):
    '''
    Create a pearson correlation heatmap with correlated values less than .5 removed and 
    greater than -.5 removed.
    '''
    # Calculate the correlations between the numeric features and remove the original columns
    correlations = train.corr().iloc[4:, 4:]
    filtered_correlations = correlations[((correlations < -0.5)|(correlations > 0.5))]

    # Create a boolean array to use as a mask to remove the upper corner from the heatmap.
    mask = np.zeros_like(correlations)
    mask[np.triu_indices_from(mask)] = True

    # Set the context of the heatmap with a white background
    with sns.axes_style("white"):
        sns.set_context('talk')
        f, ax = plt.subplots(figsize=(20, 16))

        ax = sns.heatmap(filtered_correlations,
                         annot=True,
                         cmap='coolwarm',
                         vmin=-1,
                         vmax=1,
                         mask=mask,
                         fmt='.03f')

        ax.set_title("Correlation of Features and Star Type", fontsize=28)
        plt.tight_layout()
        plt.show()


def scaled_pairplot(train):
    '''
    Create a pairplot using features scaled with the MinMaxScaler. A KDE overlay is added to the
    pairplot to show overlapping groups and distinct groups.
    '''
    sns.set_context('notebook')

    pairs1 = sns.pairplot(data=train,
                          hue='star_type_name',
                          vars=['spectral_class_num',
                                'color_num',
                                'scaled_temperature',
                                'scaled_luminosity',
                                'scaled_radius',
                                'scaled_absolute_magnitude'],
                          palette='Set1',
                          corner=True)

    pairs1.map_lower(sns.kdeplot, levels=2, color=".2")
    pairs1.fig.suptitle("Scaled Features and Star Type",
                        fontsize=36)
    plt.tight_layout()

    plt.show()


def quantiled_pairplot(train):
    '''
    Create a pairplot using quantile scaled features.
    '''
    sns.set_context('notebook')

    pairs2 = sns.pairplot(data=train,
                          hue='star_type_name',
                          vars=['quantiled_temperature',
                                'quantiled_luminosity',
                                'quantiled_radius',
                                'quantiled_absolute_magnitude'],
                          palette='Set1',
                          corner=True)

    pairs2.fig.suptitle("Quantiled Features and Star Type",
                        fontsize=24)
    plt.tight_layout()
    plt.show()


def three_d_scatter(train):
    '''
    Create a 3-D scatterplot using `quantiled_radius`, `scaled_absolute_radius`,
    and `quantile_luminosity`.
    '''
    # List of star names and marker formatting options
    global STAR_NAMES, MARKERS, MARKER_COLORS

    # Create the 3-D canvas
    sns.set_context('talk')
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(projection='3d')

    # Visualize each star using the assigned marker and color
    for star, marker, color in zip(STAR_NAMES, MARKERS, MARKER_COLORS):
        data = train.loc[train['star_type_name'] == star]
        
        ax.scatter(xs=data["scaled_absolute_magnitude"],
                   ys=data["quantiled_luminosity"],
                   zs=data["quantiled_radius"],
                   c=color,
                   s=125,
                   alpha=.75,
                   marker=marker,
                   ec='black')

    # Label Axis
    ax.set(title='Brightness and Size Distinguish a Star')
    ax.set_xlabel('Absolute Magnitude (Scaled)', labelpad=10)
    ax.set_ylabel('Luminosity (Quantiled)', labelpad=10)
    ax.set_zlabel('Radius (Quantiled)', labelpad=10)

    plt.legend(STAR_NAMES)

    plt.show()



def two_d_scatter(train):
    '''
    Create a 2-D scatterplot using quantiled_radius, and scaled_absolute_radius.
    '''
    # List of star names and marker formatting options
    global STAR_NAMES, MARKERS, MARKER_COLORS

    # Create the 3-D canvas
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot()

    # Visualize each star type with its assigned marker and color
    with sns.axes_style("white"):
        sns.set_context('talk')
        for star, marker, color in zip(STAR_NAMES, MARKERS, MARKER_COLORS):
            data = train.loc[train['star_type_name'] == star]
            
            ax.scatter(x=data["scaled_absolute_magnitude"],
                       y=data["quantiled_radius"],
                       c=color,
                       s=100,
                       alpha=.75,
                       marker=marker,
                       ec='black')
    
        # Label Axis
        ax.set(title='Brightness and Size Distinguish a Star',
               xlabel='Absolute Magnitude (Scaled)',
               ylabel='Radius (Quantiled)')
    
        ax.tick_params(axis='both', pad=3)

        plt.legend(STAR_NAMES,
                   loc='best',
                   fancybox=True,
                   shadow=True)

        plt.tight_layout()
        plt.show()


def boxplots(train):
    '''
    Create boxplots for each feature across each star.
    '''
    # Create a list of numeric columns to visualize
    global BOXPLOT_FEATURES, TITLED_FEATURES, STAR_NAMES
    sns.set_context('talk')

    # Create the plotting area with 12 subplots split into 6 rows x 2 columns
    fig, axs = plt.subplots(6, 2, figsize=(24, 36))

    # Ravel the axis into a list to interate over
    axs = axs.ravel()

    with sns.axes_style("white"):
        plt.style.use('tableau-colorblind10')

        # Create a boxplot chart for each feature.
        for i, (col_name, fmt_col_name) in enumerate(zip(BOXPLOT_FEATURES, TITLED_FEATURES)):
            sns.boxplot(ax=axs[i],
                        x=train['star_type_name'],
                        y=train[col_name],
                        whis=3,
                        order=STAR_NAMES)

            # Label Axis
            axs[i].set(title=f'Distribution of {fmt_col_name}',
                       xlabel='',
                       ylabel=fmt_col_name)
        # Plot formatting
        plt.tight_layout()

    plt.subplots_adjust(hspace=.5)
    plt.show()


def stars_by_color(train):
    '''
    Create a crosstab heatmap of `star_type_name` and `color`.
    '''
    global STAR_NAMES_SORTED, COLORS_SORTED, CBAR_FORMAT

    star_color_ctb = pd.crosstab(train['star_type_name'], train['color'])
    data = star_color_ctb.loc[STAR_NAMES_SORTED, COLORS_SORTED]

    plt.figure(figsize=(10, 8))

    sns.heatmap(data,
                cmap='Greens',
                annot=True,
                cbar_kws=CBAR_FORMAT)

    plt.title('Count of Stars by Type and Color', fontsize=22)
    plt.xlabel('')
    plt.ylabel('')

    plt.xticks(ticks=np.arange(.5, len(data.columns)+.5),
               labels=[label.title() for label in list(data.columns)],
               ha='right',
               rotation=45)

    plt.tight_layout()
    plt.show()

    return data


def stars_by_spectral_class(train):
    '''
    Create a crosstab heatmap of `star_type_name` and `spectral_class`.
    '''
    global STAR_NAMES_SORTED, SPECTRAL_CLASS_SORTED, CBAR_FORMAT

    star_spectral_class_ctb = pd.crosstab(train['star_type_name'], train['spectral_class'])
    data = star_spectral_class_ctb.loc[STAR_NAMES_SORTED, SPECTRAL_CLASS_SORTED]

    plt.figure(figsize=(8, 6))

    sns.heatmap(data,
                cmap='Greens',
                annot=True,
                cbar_kws=CBAR_FORMAT)

    plt.title('Count of Stars by Type and Spectral Class', fontsize=18)
    plt.xlabel('')
    plt.ylabel('')

    plt.show()

    return data

def color_by_spectral_class(train):
    '''
    Create a crosstab heatmap of `color` and `spectral_class`
    '''
    global COLORS_SORTED, SPECTRAL_CLASS_SORTED

    color_spectral_class_ctb = pd.crosstab(train['color'], train['spectral_class'])
    data = color_spectral_class_ctb.loc[COLORS_SORTED, SPECTRAL_CLASS_SORTED]

    plt.figure(figsize=(8, 6))

    sns.heatmap(data,
                cmap='Greens',
                annot=True)

    plt.title('Count of Stars by Color and Spectral Class', fontsize=18)
    plt.xlabel('')
    plt.ylabel('')

    plt.yticks(ticks=np.arange(.5, len(data.index)+.5),
               labels=[label.title() for label in list(data.index)],
               ha='right')

    plt.show()

    return data


def parallel_plot(train):
    '''
    Create a Parallel Category plot for `star_type_name` and `spectral_class` with
    `scaled_absolute_magnitude` as the continuous feature
    '''
    fig = parallel_cats(train,
                        dimensions=['star_type_name', 'spectral_class'],
                        color='scaled_absolute_magnitude',
                        color_continuous_scale=px.colors.sequential.Bluered,
                        title='Larger Stars are Brighter, Regardless of Spectral Class',
                        labels={'star_type_name':'Star',
                                'spectral_class':'Spectral Class',
                                'scaled_absolute_magnitude':'Absolute Magnitude'})

    fig.update_layout(font_size=12,
                      width=800,
                      height=700)
    fig.show()