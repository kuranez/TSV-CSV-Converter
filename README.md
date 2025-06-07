# TSV to CSV Converter

## Description

This Python script converts `.tsv` (Tab-Separated Values) files to `.csv` (Comma-Separated Values) format. It is designed for simple data preprocessing tasks, particularly when working with public datasets that use TSV format — such as those from [Eurostat](https://ec.europa.eu/eurostat). The script reads a specified TSV file from an `input/` folder and writes the converted CSV file to an `output/` folder.

## Features

* Automatically creates `input/` and `output/` directories if they do not exist.
* Converts a TSV file to CSV format using Python’s built-in `csv` module.
* Minimal dependencies and easy to modify for other file names or formats.

## Requirements

* Python 3.x
* No external packages required (uses standard library only)

## Usage Instructions

1. Download the desired `.tsv` dataset (e.g., from [Eurostat’s data explorer](https://ec.europa.eu/eurostat/data/database)).

2. Save the file into the `input/` directory of the project.

3. Open the script and locate this line near the top:

   ```python
   tsv_file = os.path.join(input_folder, 'estat_nrg_cb_sff.tsv')
   ```

   Replace `'estat_nrg_cb_sff.tsv'` with the filename of your TSV dataset, if different.

4. Run the script:

   ```bash
   python convert_tsv_to_csv.py
   ```

5. After execution, the converted CSV file will appear in the `output/` directory with the same base filename.

## Example Folder Structure

```
project-folder/
│
├── convert_tsv_to_csv.py
├── input/
│   └── estat_nrg_cb_sff.tsv  ← your Eurostat TSV file
└── output/
    └── estat_nrg_cb_sff.csv  ← converted output
```

## Notes

* This script assumes UTF-8 encoding; ensure the TSV file is saved accordingly.
* Only the filename variable needs to be changed to adapt the script for other datasets.

## License

This project is open source and available under the MIT License. You may modify, distribute, and use it freely in your own projects.
