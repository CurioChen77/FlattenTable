# FlattenTable

## Project Overview
FlattenTable is a professional data preprocessing tool designed to transform two-dimensional cross-tables into one-dimensional normalized tables. This tool primarily addresses the following issues:

1. **Data Structure Normalization**: Converts 2D tables containing row headers, column headers, and value areas into a database-friendly "key-value" structure.
2. **Analysis-Friendly Format**: Output results can be directly used for Pandas data processing, SQL database imports, or BI tool analysis.
3. **Automated Processing**: Handles batch processing for multi-sheet or multi-file scenarios, improving data preparation efficiency.

## Example
**Below is an example of a 2D table. Please prepare an Excel file in xlsx format based on this example. You can refer to the sample files in the `example` folder.**

**Input: 2D Table (Typical Financial Data Format)**
| Item       | 2020 | 2021 | 2022 |
|------------|----------------|----------------|----------------|
| Short-term Loans   | 500            | 600            | 550            |
| Long-term Loans   | 1000           | 1200           | 1500           |
| Accounts Payable   | 300            | 400            | 450            |
| Total Liabilities     | 1800           | 2200           | 2500           |

**Output: 1D Normalized Table**
| Item       | Year   | Value |
|------------|--------|--------------|
| Short-term Loans   | 2020   | 500          |
| Short-term Loans   | 2021   | 600          |
| Short-term Loans   | 2022   | 550          |
| ...   | ...   | ...         |
| Total Liabilities     | 2021   | 2200         |
| Total Liabilities     | 2022   | 2500         |

## Quick Start
### Environment Setup (Optional)

```
conda create -n flattentable python=3.12
conda activate flattentable
```

### Install Required Libraries
```
pip install pandas openpyxl
```

### Get the Project Code
```
git clone https://github.com/CurioChen77/FlattenTable.git
cd FlattenTable/main
```

### Run the Conversion Program
```
python excel_converter.py
```

### Interactive Guide
#### Input File Path
```
Example input: /path/to/your/file.xlsx
```
The program will automatically create a timestamped and UUID-labeled folder in the `output` directory, where both the original file and the converted results will be saved.

#### Set Output Column Names
Define the column names for the converted table as prompted:
```
First column name (original row header) → Project
Second column name (original column header) → Year
Third column name (data value) → Value
```

#### Completion Prompt
Upon successful conversion, the output path will be displayed:
```
Conversion complete! Output file: output/20250423_210823_6941b353/Demo001_converted.xlsx
```

## Acknowledgments

Thanks to the following projects and developers for supporting this tool:
- **[Pandas](https://pandas.pydata.org/)**
- **[OpenPyXL](https://openpyxl.readthedocs.io/)**
- **[Python](https://www.python.org/)**

Contributions and suggestions are welcome!

## License
This project is licensed under **MIT License**. For full license terms, see the [LICENSE](LICENSE) file.