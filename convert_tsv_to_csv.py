# TSV-CSV-Converter

import csv
import os

# Define the input and output folder paths
input_folder = 'input'  # Folder for the TSV file
output_folder = 'output'  # Folder for the CSV file

# Ensure that input and output folders exist, create them if not
os.makedirs(input_folder, exist_ok=True)  # This will create the folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define file paths (make sure your TSV file is inside the 'input' folder)
tsv_file = os.path.join(input_folder, 'estat_nrg_cb_sff.tsv')  # Input file in 'input' folder
csv_file = os.path.join(output_folder, 'estat_nrg_cb_sff.csv')  # Output file in 'output' folder

# Open the TSV file and the CSV file
with open(tsv_file, mode='r', newline='', encoding='utf-8') as tsv_infile, \
     open(csv_file, mode='w', newline='', encoding='utf-8') as csv_outfile:
    
    # Create CSV reader and writer
    tsv_reader = csv.reader(tsv_infile, delimiter='\t')  # Reading TSV (Tab separated)
    csv_writer = csv.writer(csv_outfile, delimiter=',')  # Writing CSV (Comma separated)
    
    # Write rows from TSV to CSV
    for row in tsv_reader:
        csv_writer.writerow(row)

print(f"Conversion from TSV to CSV completed: {csv_file}")
