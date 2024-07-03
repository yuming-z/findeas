import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

import glob
import pandas as pd

from lib.dataOrg import dataOrg

# Get all csv files in the folder
DATASET_DIR = 'HLOCData/'
PROCESSED_DATASET_DIR = 'ProcessedHLOCData/'

# Get the dataset
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, DATASET_DIR, "*.csv"))

# Loop through all csv files
for file in csv_files:

    # Get the ticker name from csv file name
    ticker_name = os.path.basename(file).split(".")[0]

    # Print start message
    print(f"Calculating analytic metrics for {ticker_name}...")

    # Read the csv file
    data = pd.read_csv(file, parse_dates=['Date'])

    # Calculate all indicators
    data_analysis = dataOrg(data)

    # Export the data to csv
    data_analysis.to_csv(os.path.join(path, PROCESSED_DATASET_DIR, f'{ticker_name}_processed.csv'), index=False)

    # Print success message
    print(f"Analytic metrics for {ticker_name} saved.")