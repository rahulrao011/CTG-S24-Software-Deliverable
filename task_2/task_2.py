import numpy as np
import pandas as pd
import yfinance as yf
import os

###################################
# HYPER-PARAMETERS:

# dates are of the form: YYYY-MM-DD
momentum_period = 5
data_dir = 'task_1/data'
out_file_name = 'task_2_factor'
metric = 'Close'
###################################

# FACTOR 1


out_file = open(f'task_2/{out_file_name}_1.csv', 'w+')
for csv in os.listdir(data_dir):
    ticker = csv[:-4]

    data = pd.read_csv(data_dir + '/' + csv, usecols=['Date', metric])
    data.set_index('Date', inplace=True)
    df_curr = data.iloc[:-momentum_period, :]
    df_lagging = data.iloc[momentum_period:, :]
    df_lagging.set_index(df_curr.index, inplace=True)
    factor = (df_curr - df_lagging) / df_lagging * 100
    factor.rename(columns={metric: ticker}, inplace=True)


out_file.close()
# FACTOR 2

# FACTOR 3