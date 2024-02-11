import numpy as np
import pandas as pd
import yfinance as yf

###################################
# HYPER-PARAMETERS:

# dates are of the form: YYYY-MM-DD
start_date = '2021-01-01'
end_date = '2023-12-31'
tickers_file = 'task_1/tickers.txt'
###################################

tickers_list = [] # list of ticker symbols
tickers_dict = {} # (key : ticker symbols) --> (value : pandas dataframe of relevant values)

# file IO processing, read the needed input file (tickers.txt) and
# initialize both tickers_list and tickers_dict
file = open(tickers_file, 'r')
while True:
    ticker = file.readline().strip() # read each ticker symbol
    if len(ticker) == 0: # check if this is the end of the file
        break

    if ticker not in tickers_dict: # if this is a new ticker symbol add it to tickers_list
        tickers_list.append(ticker)
    
    tickers_dict[ticker] = [] # set the current ticker symbol as a key in tickers_dict and set the value to an empty list
file.close()

data = yf.download(tickers_list, start_date, end_date) # get the stock data from yahoo finance

for col in data:
    metric, ticker = col
    
    # data wrangling (converting pandas series to pandas dataframe with needed column names)
    curr_col = data[col].to_frame()
    curr_col.columns = curr_col.columns.get_level_values(0)

    tickers_dict[ticker].append(curr_col) # add the data to the respective list in tickers_dict

for ticker in tickers_dict:
    tickers_dict[ticker] = pd.concat(tickers_dict[ticker], axis=1) # concatenate each list of pandas dataframes
    tickers_dict[ticker].to_csv(f'task_1/data/{ticker}.csv', na_rep=np.nan) # create a csv file with the data