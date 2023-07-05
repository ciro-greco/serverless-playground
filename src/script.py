import csv
import json
import duckdb
import pandas as pd

CSV_PATH = 'sales-data-set.csv'
JSON_PATH = 'sales-data-set.json'


def convert_csv_to_json(csv_file_path, json_file_path):
    # Read the CSV file
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        csv_data = [dict(row, Uid=count) for count, row in enumerate(reader, start=200)]
        # Write the JSON data
    with open(json_file_path, 'w') as file:
        json.dump(csv_data, file, indent=4)


data = duckdb.read_csv(CSV_PATH)
query = f"""SELECT * FROM read_csv_auto('{CSV_PATH}') LIMIT 2"""
print(duckdb.sql(query))


