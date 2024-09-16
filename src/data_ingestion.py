import os
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:, 3:]  # remove all text containing columns

df = df[df['Length of Membership'] > 1]  # Length of Membership column filter criteria for exp2 is greater than 1
df.drop(columns=['Avg. Session Length'], inplace=True) # drop col for exp 2 
df.to_csv(os.path.join('data','customer.csv'))

