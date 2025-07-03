# Automated Sales Report Generator

A simple and efficient Python script to automate the process of generating daily sales summary reports from a CSV file. This tool is designed to eliminate repetitive manual work, reduce errors, and provide quick insights into sales performance.

## 🚀 Features

-   **Reads Data from CSV**: Seamlessly ingests sales data from a `.csv` file.
-   **Calculates Key Metrics**: Automatically computes total revenue from the sales data.
-   **Generates Formatted Reports**: Creates a clean, human-readable text file summarizing the calculated metrics.
-   **Robust File Handling**: Automatically creates the output directory if it doesn't exist, ensuring the script runs without errors.

## 🛠️ Tech Stack

-   **Language**: Python 3
-   **Libraries**:
    -   `pandas`: For efficient data manipulation and analysis.
    -   `os`: For cross-platform compatible path and directory management.

## ⚙️ Setup and Installation

To get this project running on your local machine, follow these steps.

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/automated-report-generator.git](https://github.com/your-username/automated-report-generator.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd automated-report-generator
    ```

3.  **Install the required dependencies:**
    *(Ensure you have a `requirements.txt` file in your project directory containing the line `pandas`)*
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1.  **Prepare Your Data**:
    Place your sales data in a file named `sales_data.csv` in the root of the project directory. The CSV file must contain at least a `Sale_Amount` column.

    *Example `sales_data.csv`:*
    ```csv
    Date,Product,Sale_Amount,Region
    2025-07-03,Product A,150.00,North
    2025-07-03,Product B,200.50,South
    2025-07-03,Product A,140.00,North
    ```

2.  **Run the script:**
    Execute the main script from your terminal.
    ```sh
    python report_generator.py
    ```

3.  **Find Your Report**:
    The script will generate a summary report and save it in the `reports` directory. The file will be named with the current date, e.g., `reports/summary_2025-07-03.txt`.

    *Example Output (`summary_2025-07-03.txt`):*
    ```
    Sales Summary Report
    Date: 2025-07-03
    --------------------
    Total Revenue: $490.50
    --------------------
    ```

## ✍️ Author

-   **S. M. Hozaifa Hossain**
-   **GitHub**: [your-github-username](https://github.com/your-username)

