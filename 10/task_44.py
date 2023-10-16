import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

categories = data['whoAmI'].unique()
one_hot = pd.DataFrame(0, columns=categories, index=data.index)

for category in categories:
    one_hot[category] = (data['whoAmI'] == category).astype(int)

one_hot = one_hot.reset_index(drop=True)
one_hot.columns.name = None
print(one_hot.to_string(index=False))