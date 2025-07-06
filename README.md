# Advanced Sales Report Generator & Business Intelligence Tool

An advanced, command-line Python utility that transforms raw sales CSV data into a comprehensive business intelligence report. This tool is engineered for robustness, performing sophisticated data cleaning, multi-level aggregations, and in-depth analytics to provide actionable insights from complex datasets.

## 🚀 Features

-   **Flexible Command-Line Interface**:
    -   Accepts the input file path as a command-line argument, allowing it to process any CSV file without modifying the source code.
-   **Dynamic Data Cleaning**:
    -   Intelligently detects and handles a wide variety of currency symbols (e.g., $, €, ₹, £) within sales data using regular expressions.
    -   Strips commas and other non-numeric characters to prepare data for accurate calculations.
    -   Gracefully handles and removes rows with corrupted or non-convertible sales figures to prevent analysis errors.
-   **In-Depth Business Analytics**:
    -   Calculates key performance indicators (KPIs) including Grand Total, Average, Maximum, and Minimum Revenue, and Total Transaction Count.
    -   Performs multi-level `groupby` aggregations to provide detailed breakdowns of revenue by **Product**, **Category**, and **User**.
    -   Identifies the top and bottom performing entities within each category, providing immediate insights.
-   **Timestamped & Organized Reporting**:
    -   Generates a uniquely named report file for each run using a full `YYYY-MM-DD_HH-MM-SS` timestamp, preventing overwrites and creating a clean historical archive.
    -   Automatically creates the `Reports` output directory if it doesn't exist, ensuring the script runs smoothly in any environment.
-   **Comprehensive Error Handling**:
    -   Built with multiple `try...except` blocks to ensure stability and provide clear, user-friendly error messages.
    -   Gracefully handles critical errors such as missing input files (`FileNotFoundError`), missing data columns (`KeyError`), and data processing failures.

## 🛠️ Tech Stack

-   **Language**: Python 3
-   **Libraries**:
    -   `pandas`: For high-performance data manipulation and analysis.
    -   `argparse`: For parsing command-line arguments.
    -   `os`: For cross-platform compatible path and directory management.
    -   `datetime`: For generating report timestamps.
    -   `re`: For advanced string manipulation and pattern matching (Regular Expressions).

## ⚙️ Setup and Installation

To get this project running on your local machine, follow these steps.

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/hozaifa1/Automated-Report-Generator.git](https://github.com/hozaifa1/Automated-Report-Generator.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Automated-Report-Generator
    ```

3.  **Install the required dependencies:**
    *(The project requires pandas. A `requirements.txt` file is included for easy installation.)*
    ```sh
    pip install -r requirements.txt
    ```

## Usage

This script is a command-line tool. You must provide the path to your data file when you run it.

1.  **Prepare Your Data**:
    Ensure your sales data is saved as a CSV file. For the script to function correctly, the file must contain columns that can be mapped to `sales_amount`, `product_name`, `category`, and `user_id`.

2.  **Run the script from your terminal:**
    Execute the script using `python` and provide the path to your data file as an argument.

    *Example on Windows:*
    ```sh
    python report_generator.py "C:\Users\YourUser\Documents\data\amazon_sales.csv"
    ```

    *Example on Mac/Linux:*
    ```sh
    python report_generator.py /home/youruser/data/amazon_sales.csv
    ```

3.  **Find Your Report**:
    A new, detailed report will be generated and saved in the `Reports/` directory. The file will be uniquely named with a timestamp, e.g., `Reports/report_2025-07-06_11-30-05.txt`.

    *Example Report Output:*
    ```
    Sales Summary Report
    Date: 2025-07-06
    --------------------

     Total Transactions: 1465

    Grand Total Revenue: ₹6491583.00
     Max Revenue: ₹139900.00
     Min Revenue: ₹39.00
     Average Revenue: ₹4431.11


    --- Revenue by Category ---

    Max Revenue Category: Electronics (₹1035918.00)
    Min Revenue Category: Home Decor & Festive Needs (₹13498.00)


    --- Revenue by User ---

    Max Revenue User: A3LDPF5F2YDE5L (₹139900.00)
    Min Revenue User: A253G22O39S124 (₹39.00)


    --- Revenue by Product ---

    Max Revenue Product: Croma 236 L Frost Free Double Door 3 Star Refrigerator (₹139900.00)
    Min Revenue Product: A-YUD-K-101-12... (₹39.00)
    --------------------
    ```

## ✍️ Author

-   **S. M. Hozaifa Hossain**
-   **GitHub**: [hozaifa1](https://github.com/hozaifa1)

