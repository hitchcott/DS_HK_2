# coding=utf-8

import pandas as pd
import numpy as np

df = pd.read_csv('../../../data/nytimes.csv')

# data itself
# print df

# sumamry
print df.describe()

# head
print df[:10]

# aggregate
dfg = df[ ['Age', 'Impressions', 'Clicks'] ].groupby(['Age']).agg([np.mean])
print dfg[:10]


# new variables
df['log_impressions'] = df['Impressions'].apply(np.log)
print df['log_impressions']

# Or even recluster our values into more specific age groups:

def map_age_category(x):
    """
    Function that groups users by age.
    """
    if x == 0:
        return 0
    elif x < 18:
        return 1
    elif x < 25:
        return 2
    elif x < 32:
        return 3
    elif x < 45:
        return 4
    else:
        return 5

df['age_categories'] = df['Age'].apply(map_age_category)
print df[['age_categories']].describe()

