import os
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/araj2/customer-database/master/Ecommerce%20Customers.csv')

df = df.iloc[:, 3:]  # remove all text containing columns

df = df[df['Length of Membership'] > 3]  # Length of Membership column filter criteria greater than 3

df.to_csv(os.path.join('data','customer.csv'))

