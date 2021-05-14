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