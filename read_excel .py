""" reading normal excel file"""
import pandas as pd


dataframe_1 = pd.read_excel('first_excel.xlsx')
master_df   = pd.read_excel('master_excel.xlsx')
index_count = 0

product_dict = {}

for name in master_df['Name']:
    product_dict[name] = 1 #assuming no duplicate value in master excel file 

for product in dataframe_1['Name']:
    if product in product_dict:
        master_df['Purchase price'][index_count] = dataframe_1['Purchase Price'].iloc[index_count]
        master_df['Category'][index_count] = dataframe_1['Category'].iloc[index_count]
        master_df['MRP'][index_count] = dataframe_1['MRP'].iloc[index_count]
        master_df['Quantity'][index_count] = dataframe_1['Quantity'].iloc[index_count]
        index_count+=1
    else:
        master_df = master_df.append({'Name' : dataframe_1['Purchase Price'].iloc[index_count],
                    'Category' : dataframe_1['Category'].iloc[index_count],'MRP':dataframe_1['MRP'].iloc[index_count],
                    'Quantity':dataframe_1['Quantity'].iloc[index_count]
                    } , 
                    ignore_index=True)
        index_count+=1

"""
Time Complexity - O(no. of rows) >> O(n)
"""