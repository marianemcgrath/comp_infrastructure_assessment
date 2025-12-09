


# Import yfinance and getting the data ready to run
import yfinance as yf

# Import Dates and Times
import datetime as dt

# Download data for the required stocks (FAANG)
df = yf.download(['META', 'AAPL','AMZN', 'NFLX', 'GOOG'], period='5d', interval='1h', auto_adjust=True)

# Save the data frame to CSV
now= dt.datetime.now()

# Create the filename (and add formatting date and time) 
filename = 'data/' + now.strftime('%Y%m%d_%H%M%S') + ".csv"

# Save data to CSV File
df.to_csv(filename)
