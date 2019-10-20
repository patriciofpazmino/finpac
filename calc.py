#!/usr/bin/env python
# coding: utf-8

# In[25]:


import pandas as pd
import numpy as np

#datamaster=pd.read_csv('C:/Users/a.yang8/Downloads/datamaster.csv', encoding = 'unicode_escape')


# In[26]:


#datamaster.columns.values


# In[162]:


import scipy
from scipy import stats

df = pd.read_csv('data/datacondensed.csv', encoding = 'unicode_escape')

# slope, intercept, r_value, p_value, std_err = stats.linregress([df['coa_books_supp_d'], df['coa_on_other_d'], df['coa_other_d'], df['coa_tuit_fees_d']], df['fa_loans_debt_avg_d'])
# print(slope, intercept, r_value, p_value, std_err)
# print(df.head())
# df2 = df.dropna()
series = [df['name'], df['data_yr_string'], df['state'], df['coa_books_supp_d'], df['coa_on_other_d'], df['coa_off_other_d'], df['coa_on_room_board_d'], df['coa_off_room_board_d'], df['coa_tuit_fees_d'], df['fa_loans_debt_avg_d']]

df2 = pd.concat(series, axis=1)
df3 = df2.dropna()
# print(df3.shape)
#print(df3)
# print(df3.head())
# scipy.stats.linregress()
# series = [df['coa_books_supp_d'].dropna(), df['coa_on_other_d'].dropna(), df['coa_other_d'].dropna(), df['coa_tuit_fees_d'].dropna(), df['fa_loans_debt_avg_d'].dropna()]
# df2 = pd.concat(series, axis=1)
# print(df2.head(5))
# # df2 = pd.DataFrame([df['coa_books_supp_d'].dropna(), df['coa_on_other_d'].dropna(), df['coa_other_d'].dropna(), df['coa_tuit_fees_d'].dropna(), df['fa_loans_debt_avg_d'].dropna()])
# print(df2.columns)
# df3 = df2.reset_index()
# print(df3.head(5))
# print(df3.shape)
# print(df3.columns)
# print(df.shape)
# def clean_dataset(df):
#     assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
#     df.dropna(inplace=True)
#     indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
#     return df[indices_to_keep].astype(np.float64)

# df2 = clean_dataset(df)
# x = df3[['coa_on_other_d', 'coa_other_d', 'coa_books_supp_d', 'coa_tuit_fees_d']]
# # x = [df3['coa_books_supp_d'], df3['coa_on_other_d'], df3['coa_other_d'], df3['coa_tuit_fees_d']]
# Y = df3['fa_loans_debt_avg_d']
# from sklearn import linear_model
# clf = linear_model.LinearRegression()
# clf.fit(x, Y)
# print(clf.coef_)
# print(clf.intercept_)


# In[146]:


#df3


# In[111]:


df['name']


# In[163]:


#monthly_pmt = tuition + books + transport+ misc/personal + books + housing + food

df3.head()
#'NY', 'NJ' 'PA'
df_2017 = df3[df3.data_yr_string == '2017-18'] 


# In[210]:


df_2017


# In[202]:


#df_2017 = df_2017.set_index()


# In[132]:


# df_baruch.index.values


# In[133]:


# df_baruch.loc['2017-18']


# In[134]:


# df_baruch


# In[154]:


# def payment(school)


# In[203]:


df_five_random = df_2017.sample(5)


# In[219]:


df_clean = df_five_random.reset_index()


# In[256]:


df_clean


# In[258]:


df_off = df_clean.drop(['coa_on_other_d', 'coa_on_room_board_d'], axis = 1)


# In[266]:


df_on = df_clean.drop(['coa_off_other_d', 'coa_off_room_board_d'], axis = 1)


# In[274]:


df_off


# In[273]:


df_on


# In[292]:


df_clean.index.values
#calculates monthly payment per school in the random five
#possible to separate it into on or off campus
def monthlyPayment(ind):
    sum_off = 0.0
    sum_on = 0.0
#     print(df_clean.loc[ind])
    for i in df_off.columns:
        if i != 'fa_loans_debt_avg_d':
            x = df_off.iloc[ind][i]
    #         print(type(x))
            if type(x) is np.float64:
                sum_off += x
#                 print(x)
    
    for j in df_on.columns:
        if j != 'fa_loans_debt_avg_d':
            z = df_on.iloc[ind][j]
    #         print(type(x))
            if type(z) is np.float64:
                sum_on += z
#                 print(z)

    stored = 'Off-Campus:  ' + str(sum_off/10) + '\nOn-Campus: ' + str(sum_on/10)
    print(stored)
    return stored
    
        

    
y = monthlyPayment(0)
print(y)


# In[293]:


# for i in df_clean.index.values:
#     monthlyPayment(i)


# In[300]:


def financed(loan, interest, years):
    debt = (loan*8) * ((1 + ((interest/12)/100)))**(years*12)
    return debt
    
    
financed(300, 5, 3)


# In[ ]:




