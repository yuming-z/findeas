import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

import glob
import pandas as pd

from website.models import Ticker, Stock, Indicator

# Get all csv files in the folder
PROCESSED_DATASET_DIR = 'ProcessedHLOCData/'    

path = os.getcwd()
dataset = glob.glob(os.path.join(path, PROCESSED_DATASET_DIR, "*.csv"))

# Loop through all csv files
for file in dataset:

    # Get the ticker name from csv file name
    ticker_name = os.path.basename(file).split(".")[0].strip('_processed')

    # Print start message
    print(f"Importing data for {ticker_name}...")

    # Read the csv file
    data = pd.read_csv(file, parse_dates=['Date'])

    # Set the index to date
    data.set_index('Date', inplace=True)

    # Get the ticker object
    ticker = Ticker.objects.get(ticker=ticker_name)

    # Loop through all rows in the csv file
    for index, row in data.iterrows():

        # Get the stock object
        stock = Stock.objects.get(ticker=ticker, date=index)

        # Create the indicator in the database
        indicator = Indicator(
            stock=stock,

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

        # Save the indicator
        indicator.save()

    # Print success message
    print(f"Successfully importing data for {ticker_name}")

# Print completion message
print("Data import complete.")