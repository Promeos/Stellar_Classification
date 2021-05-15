# normally_distributed = []

# for star in [star0, star1, star2, star3, star4, star5]:
#     normal = 0
#     non_normal = 0
    
#     star_code = star.star_type.unique()[0]
#     for col in numeric_cols:
#             t, p = shapiro(star[col])

#             if p < .05:
#                 print(f'{col} is NOT normally distributed')
#                 non_normal += 1
#             else:
#                 print(f'{col} IS normally distributed')
#                 normal += 1
#                 normally_distributed.append((star_code, col))
#     print()
#     print('Normally Distributed', normal)
#     print('False', non_normal)
#     print()