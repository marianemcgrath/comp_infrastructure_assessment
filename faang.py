#! /usr/bin/env python3

# Import yfinance and getting the data ready to run
from fileinput import filename
import yfinance as yf

# Import Dates and Times
import datetime as dt

# Import matplotlib for plotting the data
import matplotlib.pyplot as plt

# Download data for the required stocks (FAANG)
df = yf.download(['META', 'AAPL','AMZN', 'NFLX', 'GOOG'], period='5d', interval='1h', auto_adjust=True)

# Save the data frame to CSV
now= dt.datetime.now()

# Create the filename (and add formatting date and time) 
filename_csv = 'data/' + now.strftime('%Y%m%d_%H%M%S') + ".csv"

# Save data to CSV File
df.to_csv(filename_csv)

# Plot the closing prices
fig, ax = plt.subplots(figsize=(12, 6))
df['Close'].plot(ax=ax)
ax.set_title('FAANG Closing Prices')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.legend(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG'])

# Filename with today's date
filename_png = 'plots/FAANG_closing_prices_' + now.strftime('%Y%m%d_%H%M%S') + '.png'

# Save figure as an image file as today's date
fig.savefig(filename_png, dpi=300)