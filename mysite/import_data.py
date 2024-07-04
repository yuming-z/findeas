import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

import glob
import pandas as pd
from website.models import Ticker, Stock

DATASET_DIR = 'ProcessedHLOCData/'

# Get all csv files in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, DATASET_DIR,"*.csv"))

# Loop through all csv files
for file in csv_files:

    # Get the ticker name from csv file name
    ticker_name = os.path.basename(file).split(".")[0].strip('_processed')

    # Print start message
    print(f"Importing data for {ticker_name}...")

    # Create the ticker in the database
    ticker = Ticker(
        ticker=ticker_name
    )

    # Save the ticker name
    ticker.save()

    # Read the csv file
    data = pd.read_csv(file, parse_dates=['Date'])

    # Set the index to date
    data.set_index('Date', inplace=True)

    # Loop through all rows in the csv file
    for index, row in data.iterrows():

        # Create the stock in the database
        stock = Stock(
            ticker=ticker,
            date=pd.to_datetime(row["Date"]).date(),
            open=row["Open"],
            close=row["Close"],
            high=row["High"],
            low=row["Low"],
            volume=row["Volume"],
            dividend=row["Dividends"],
            split=row["Stock Splits"],

            # Analytic metrics
            sma=row["SMA"],
            sd=row["SD"],
            ub=row["UB"],
            lb=row["LB"],
            macd=row["MACD"],
            macd_signal=row["MACDSignal"],
            gain=row["gain"],
            loss=row["loss"],
            avg_gain=row["avg_gain"],
            avg_loss=row["avg_loss"],
            rs=row["RS"],
            rsi=row["RSI"],
            rsi_6=row["RSI6"],
            rsi_12=row["RSI12"],
            weakMACD=row["WeakMACD"],
            macd_diff=row["MACDDiff"],
            
            isLoss=row["Loss"],
            isCausion=row["Causion"],
            isSafe=row["Safe"],
            isGain=row["Gain"],
            flag=row["flag"]
        )

        # Save the stock
        stock.save()

    # Print success message
    print(f"Successfully import data for {ticker_name}")

# Print completion message
print("Data import complete.")