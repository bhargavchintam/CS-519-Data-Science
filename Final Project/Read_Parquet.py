import numpy as np
import pandas as pd
import pyarrow
import os

# df = pd.read_parquet("trail-data/yellow_tripdata_2023-01.parquet", engine='pyarrow')
# print(df.info())
# print("\n\nLength of DataFrame", len(df))


# df = pd.read_parquet("trail-data/green_tripdata_2023-01.parquet", engine='pyarrow')
# print(df.info())
# print("\n\nLength of DataFrame", len(df))


# df = pd.read_parquet("trail-data/fhv_tripdata_2023-01.parquet", engine='pyarrow')
# print(df.info())
# print("\n\nLength of DataFrame", len(df))


# df = pd.read_parquet("trail-data/fhvhv_tripdata_2023-01.parquet", engine='pyarrow')
# print(df.info())
# print("\n\nLength of DataFrame", len(df))


import os

def list_files(directory):
    file_names = []
    try:
        # List all files and directories in the specified path
        for filename in os.listdir(directory):
            file_names.append(filename)
            # print(filename)
    except FileNotFoundError:
        print(f"The directory '{directory}' was not found.")
    return file_names

# Replace '/path/to/directory' with the path of your directory
directory_path = 'datasets/'
# list_files(directory_path)


def create_expected_filenames(start_year, end_year, prefix):
    expected_files = []
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            expected_files.append(f"{prefix}_{year}-{str(month).zfill(2)}.parquet")
    return expected_files

def find_missing_files(actual_files, expected_files):
    return [file for file in expected_files if file not in actual_files]

# List of actual filenames
actual_files = list_files(directory_path)

# Generate expected filenames for each category and the respective year range
expected_fhvhv = create_expected_filenames(2019, 2023, "fhvhv_tripdata")
expected_fhv = create_expected_filenames(2015, 2023, "fhv_tripdata")
expected_green = create_expected_filenames(2014, 2023, "green_tripdata")
expected_yellow = create_expected_filenames(2013, 2023, "yellow_tripdata")

# Combine all expected filenames
expected_files = expected_fhvhv + expected_fhv + expected_green + expected_yellow

# Find missing files
missing_files = find_missing_files(actual_files, expected_files)

print("Missing files:", missing_files)

for x in missing_files:
    print(x)