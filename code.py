# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here

df = pd.read_csv(path)
df['state'] = df['state'].apply(lambda x:x.lower())
df['total'] = df['Jan'] + df['Feb'] + df['Mar']

sum_row = df[['Jan','Feb','Mar','total']].sum()

df_final = df.append(sum_row,ignore_index=True)
print(df_final.tail(3))
# Code ends here


# --------------
import requests

# Code starts here

url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)

df1 = pd.read_html(response.content)[0]
#print(df1.head(2))
df1 = df1.iloc[11:]
df1 = df1.rename(columns = df1.iloc[0])
df1.drop(df1.index[0],inplace = True)

df_new = df1['United States of America']
df1['United States of America'] = df_new.apply(lambda x:x.replace(" ",""))

# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here

mapping = df1.set_index('United States of America')['US'].to_dict()
df_final['abbr'] = df_final['state'].map(mapping)
print(df_final.head())
# Code ends here


# --------------
# Code stars here

state_mississpi = df_final[df_final['state'] == 'mississipi']

state_mississpi = state_mississpi.replace(np.nan,'MS')

state_tenessee = df_final[df_final['state'] == 'tenessee']

state_tenessee = state_tenessee.replace(np.nan,'TN')

df_final.replace(df_final.iloc[6],state_mississpi,inplace = True)
df_final.replace(df_final.iloc[10],state_tenessee,inplace = True)
print(df_final)
# Code ends here


# --------------
# Code starts here

df_sub = df_final[['abbr','Jan','Feb','Mar','total']].groupby('abbr').sum()
formatted_df = df_sub.applymap(lambda x : '${:.0f}'.format(x))
formatted_df
# Code ends here


# --------------
# Code starts here
sum_row = df_final[['Jan','Feb','Mar','total']].sum()
df_sum = pd.DataFrame(sum_row)
df_sub_sum = df_sum.T

df_sub_sum = df_sub_sum.applymap(lambda x : '${:.0f}'.format(x))

final_table = formatted_df.append(df_sub_sum)
print(final_table)

final_table = final_table.rename(index={final_table.index[-1]:'Total'})
print(final_table)
# Code ends here


# --------------
# Code starts here

plt.pie(df_sub['total'],labels = df_sub.index,autopct='%2.1f%%', shadow=True)
plt.show()
# Code ends here


