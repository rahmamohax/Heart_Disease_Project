#!/usr/bin/env python3
"""
Convert cleveland.data to CSV format with proper column headers.
"""

def extract_column_names():
    column_names = [
        "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
        "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"
    ]
    return column_names

def convert_data_to_csv():
    """Convert the cleveland.data file to CSV format."""
    column_names = extract_column_names()
    
    # Read the data file
    with open('cleveland.data', 'r', encoding='latin1') as f:
        lines = f.readlines()
    
    # Parse all values from the file
    all_values = []
    for line in lines:
        values = line.strip().split()
        all_values.extend(values)
    
    # Group values into records (14 attributes per patient)
    records = []
    for i in range(0, len(all_values), 14):
        if i + 14 <= len(all_values):  # Ensure we have a complete record
            record = all_values[i:i+14]
            records.append(record)
    
    # Write to CSV
    import csv
    with open('cleveland.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(column_names)
        
        # Write data rows
        for record in records:
            writer.writerow(record)
    
    print(f"Successfully converted {len(records)} patient records to cleveland.csv")
    print(f"Each record has {len(column_names)} attributes")
    
    # Display first few rows for verification
    print("\nFirst 3 rows of data:")
    for i, record in enumerate(records[:3]):
        print(f"Patient {i+1}: {record[:10]}...")  # Show first 10 attributes

if __name__ == "__main__":
    convert_data_to_csv() 