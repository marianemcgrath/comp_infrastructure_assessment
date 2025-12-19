#!/usr/bin/env python3

import pandas as pd
import yfinance as yf
import os
import datetime as dt
import matplotlib.pyplot as plt

def get_data():
    tickers = ["META", "AAPL", "AMZN", "NFLX", "GOOG"] 
    df = yf.download(tickers, period='5d', interval='1h', auto_adjust=True) 
    
    if not os.path.exists('data'):      
        os.makedirs('data')
    
    now = dt.datetime.now()
    filename = f'data/{now.strftime("%Y%m%d-%H%M%S")}.csv'
    df.to_csv(filename)

    print(f"Data saved to {filename}")
    
    return df

def plot_data():    
    data_files = os.listdir('data')
    data_files = [f for f in data_files if f.endswith('.csv')]
    data_files.sort(reverse=True)
    latest_file = data_files[0]

    df = pd.read_csv(f'data/{latest_file}', header=[0, 1], index_col=0, parse_dates=True)

    if not os.path.exists('plots'):
        os.makedirs('plots')
    
    closing_data = df['Close']
    
    now = dt.datetime.now()
    fig, ax = plt.subplots(figsize=(12, 6))
    closing_data.plot(ax=ax)

    ax.set_title(f'FAANG Stock Closing Prices - {now.strftime("%Y-%m-%d")}')
    ax.set_xlabel('Date and Time')
    ax.set_ylabel('Closing Price (USD)')
    ax.grid(True, alpha=0.3)
    ax.legend(title='Stocks')
    
    plot_filename = f'plots/{now.strftime("%Y%m%d-%H%M%S")}.png'
    fig.savefig(plot_filename, dpi=300, bbox_inches='tight')
    plt.close(fig)

    print(f"Plot saved to {plot_filename}")
    
if __name__ == "__main__":
    get_data()
    plot_data()

# Source: https://stackoverflow.com/questions/419163/what-does-if-name-main-do