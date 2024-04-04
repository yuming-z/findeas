import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

import glob
import pandas as pd
from website.models import Ticker, Stock

# Get all csv files in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "HLOCData/","*.csv"))

# Loop through all csv files
for file in csv_files:

    # Get the ticker name from csv file name
    ticker_name = os.path.basename(file).split(".")[0]

    # Print start message
    print(f"Importing data for {ticker_name}...")

    # Create the ticker in the database
    ticker = Ticker(
        ticker=ticker_name
    )

    # Save the ticker name
    ticker.save()

    # Read the csv file
    data = pd.read_csv(file)

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
            split=row["Stock Splits"]
        )

        # Save the stock
        stock.save()

    # Print success message
    print(f"Successfully imported data for {ticker_name}")

# Print completion message
print("Data import complete.")