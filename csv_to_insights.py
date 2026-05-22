import csv
import statistics
import json

try:
    values = []
    with open('sample-superstore.csv', 'r', encoding='utf-8-sig') as file:
        rows = csv.DictReader(file)
        # for each row in the CSV file
        for row in rows:
            try:
                values.append(float(row['Sales']))
            except ValueError:
                continue #Skip the row where the Sales is not a valid number
            
        # Calculate the min, max, mean
        
        if len(values) == 0:
            print("No numeric data found.")
            
        result = {
            "min": min(values),
            "max": max(values),
            "mean": statistics.mean(values)
        }
            
        with open('results.json', 'w') as json_file:
            json.dump(result, json_file, indent=4)

except FileNotFoundError:
    print("The file 'sample-superstore.csv' was not found.")
    exit()