import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


def pearson_correlations(train):
    '''
    Create a pearson correlation heatmap with correlated values less than .5 removed and 
    greater than -.5 removed.
    '''
    sns.set_context('talk')

    # Calculate the correlations between the numeric features and remove the original columns
    correlations = train.corr().iloc[4:, 4:]
    correlations = correlations[((correlations < -0.5)|(correlations > 0.5))]

    # Create a boolean array to use as a mask to remove the upper corner from the heatmap.
    mask = np.zeros_like(correlations)
    mask[np.triu_indices_from(mask)] = True

    # Set the context of the heatmap with a white background
    with sns.axes_style("white"):
        
        f, ax = plt.subplots(figsize=(20, 16))

        ax.set_title("Absolute Magnitude, Luminosity, and Radius correlate with Star Type", fontsize=28)


        ax = sns.heatmap(correlations,
                         annot=True,
                         cmap='coolwarm',
                         vmin=-1,
                         vmax=1,
                         mask=mask,
                         fmt='.03f')
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

    pairs1.fig.suptitle("Absolute Magnitude and Temperature contain Star Type Clusters",
                        fontsize=26,
                        y=1.03)

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

    pairs2.fig.suptitle("Quantiled Radius and Quantiled Luminosity contain Star Type Clusters",
                        fontsize=18,
                        y=1.05)

    plt.show()


def three_d_scatter(train):
    '''
    Create a 3-D scatterplot using quantiled_radius, scaled_absolute_radius,
    and quantiled luminosity.
    '''
    # Plot Formatters
    star_names = ['Hyper Giants', 'Super Giants', 'Main Sequence', 'White Dwarf', 'Brown Dwarf', 'Red Dwarf']
    markers = ['*','X','P','h','p','D']
    marker_color = ['blue', 'lightblue', 'gold', 'whitesmoke', 'saddlebrown', 'red']

    sns.set_context('talk')

    # Create the 3d canvas
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(projection='3d')

    # Visualize each star type with its assigned marker and color
    for star, marker, color in zip(star_names, markers, marker_color):
        temp = train.loc[train['star_type_name'] == star]
        
        ax.scatter(xs=temp["quantiled_radius"],
                   ys=temp["scaled_absolute_magnitude"],
                   zs=temp["quantiled_luminosity"],
                   c=color,
                   s=125,
                   alpha=.75,
                   marker=marker,
                   ec='black')

    # Label Formatting
    ax.set(title='Brightness and Size are Distinct for Each Star Type',
           xlabel='Radius (Quantiled)',
           ylabel='Absolute Magnitude (Scaled)',
           zlabel='Luminosity (Quantiled)')

    ax.view_init(45,45)

    plt.tight_layout()
    plt.legend(star_names)
    plt.show()



def two_d_scatter(train):
    '''
    Create a 2-D scatterplot using quantiled_radius, and scaled_absolute_radius.
    '''
    # Plot formatters
    star_names = ['Hyper Giants', 'Super Giants', 'Main Sequence', 'White Dwarf', 'Brown Dwarf', 'Red Dwarf']
    markers = ['*','X','P','h','p','D']
    marker_color = ['blue', 'lightblue', 'gold', 'whitesmoke', 'saddlebrown', 'red']

    sns.set_context('talk')

    # Create the 3d canvas
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(projection='3d')

    # Visualize each star type with its assigned marker and color
    for star, marker, color in zip(star_names, markers, marker_color):
        temp = train.loc[train['star_type_name'] == star]
        
        ax.scatter(xs=temp["quantiled_radius"],
                   ys=temp["scaled_absolute_magnitude"],
                   zs=temp["quantiled_luminosity"],
                   c=color,
                   s=100,
                   alpha=.75,
                   marker=marker,
                   ec='black')
    
    # Label Formatting
    ax.set(title='Brightness and Size are Distinct for Each Star Type: Top View',
           xlabel='Radius (Quantiled)',
           ylabel='Absolute Magnitude (Scaled)',
           zlabel='')

    ax.view_init(90,0)

    plt.legend(star_names)
    plt.show()


def boxplots(train):
    '''
    Create boxplots for each star type and feature.
    '''
    # Create a list of numeric columns to visualize
    boxplot_column_names = list(train.select_dtypes(include='number').columns)
    boxplot_column_names.remove('star_type')
    boxplot_column_names.remove('spectral_class_num')
    boxplot_column_names.remove('color_num')

    # Create a variable to store the name of the target variable.
    TARGET = 'star_type'

    # Format names to substitute for plot labels
    fmt_column_names = [column.replace('_', ' ').title() for column in boxplot_column_names]
    fmt_target_name = TARGET.replace('_', ' ').title()

    sns.set_context('talk')

    # Create the plotting area with 12 subplots split into 6 rows x 2 columns
    fig, axs = plt.subplots(6, 2, figsize=(24, 36))

    # Ravel the axis into a list to interate over
    axs = axs.ravel()

    with sns.axes_style("white"):
        plt.style.use('tableau-colorblind10')

        # Create a boxplot of each feature for all stars
        for i, (col_name, fmt_col_name) in enumerate(zip(boxplot_column_names, fmt_column_names)):
            sns.boxplot(ax=axs[i],
                        x=train['star_type_name'],
                        y=train[col_name],
                        whis=3)

            axs[i].set(title=f'Distribution of {fmt_col_name}',
                       xlabel='',
                       ylabel=fmt_col_name)

        plt.tight_layout()

    plt.subplots_adjust(hspace=.5)
    plt.show()


def startype_by_color(train):
    '''
    Create a catego
    '''
    star_color_ctb = pd.crosstab(train['star_type_name'], train['color'])

    plt.figure(figsize=(10, 8))
    cbar_format = {'ticks':list(np.arange(0, 21, 5))}

    sns.heatmap(star_color_ctb,
                cmap='Greens',
                annot=True,
                cbar_kws=cbar_format)

    plt.title('Count of Stars by Type and Color', fontsize=22)
    plt.xlabel('')
    plt.ylabel('')

    plt.xticks(ticks=np.arange(.5, len(star_color_ctb.columns)+.5),
            labels=[label.title() for label in list(star_color_ctb.columns)],
            ha='right',
            rotation=45)

    plt.tight_layout()
    plt.show()


def startype_by_spectral_class(train):
    '''

    '''
    star_spectral_class_ctb = pd.crosstab(train['star_type_name'], train['spectral_class'])

    plt.figure(figsize=(8, 6))
    cbar_format = {'ticks':list(np.arange(0, 21, 5))}

    sns.heatmap(star_spectral_class_ctb,
                cmap='Greens',
                annot=True,
                cbar_kws=cbar_format)

    plt.title('Count of Stars by Type and Spectral Class', fontsize=18)
    plt.xlabel('')
    plt.ylabel('')

    plt.show()


def color_by_spectral_class(train):
    '''

    '''
    color_spectral_class_ctb = pd.crosstab(train['color'], train['spectral_class'])


# sns.set_context('talk')

# fig, axs = plt.subplots(6, 2, figsize=(24, 36))

# axs = axs.ravel()

# with sns.axes_style("white"):
#     plt.style.use('tableau-colorblind10')
#     for i, (col_name, fmt_col_name) in enumerate(zip(boxplot_column_names, fmt_column_names)):
#         sns.boxplot(ax=axs[i],
#                     x=train['star_type_name'],
#                     y=train[col_name],
#                     whis=3)

#         axs[i].set_title(f'Distribution of {fmt_col_name}')
#         axs[i].xaxis.set_label_text('')
#         axs[i].yaxis.set_label_text(fmt_col_name)
        
#         axs[i].set_yscale('symlog')
#     plt.tight_layout()
        
# plt.subplots_adjust(hspace=.5)