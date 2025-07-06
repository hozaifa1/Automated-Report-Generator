import os
import re
import pandas as pd
from datetime import datetime
import argparse

def generate_sales_report():
    parser = argparse.ArgumentParser(description="Generate a sales report from a CSV file.")
    parser.add_argument('filepath', help="The full path to the input sales CSV file.")
    args = parser.parse_args()
    filepath = args.filepath
    try:
        # Load CSV
        filepath = 'C:/Users/User/.cache/kagglehub/datasets/karkavelrajaj/amazon-sales-dataset/versions/1/amazon.csv'
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"❌ ERROR: File not found at path: {filepath}")
        return
    except Exception as e:
        print(f"❌ ERROR while loading CSV: {str(e)}")
        return

    try:

        currency_symbols = [
            "$", "€", "£", "¥", "₩", "₹", "₽", "₺", "₫", "₪", "₣",
            "د.إ", "ر.س", "د.ك", "ر.ع.", "Rs", "Tk", "₨",
            "CHF", "C$", "A$", "NZ$", "R$", "R", "₱", "Kč", "Ft", "kr",
        ]

        # Extract currency symbols from 'sales_amount'
        symbols_found = set()
        pattern = '|'.join(map(re.escape, currency_symbols))
        for val in df['sales_amount'].astype(str):
            match = re.findall(pattern, val)
            symbols_found.update(match)

        if not symbols_found:
            print("⚠️ WARNING: No currency symbols found in 'sales_amount' column.")
            symbol = ''
        else:
            symbol = list(symbols_found)[0]

        # Clean sales_amount
        df['sales_amount'] = df['sales_amount'].replace(currency_symbols + [','], '', regex=True)
        df['sales_amount'] = df['sales_amount'].replace(r'[^\d\.]', '', regex=True)
        df['sales_amount'] = pd.to_numeric(df['sales_amount'], errors='coerce')
        df = df.dropna(subset=['sales_amount'])

    except Exception as e:
        print(f"❌ ERROR while cleaning or processing 'sales_amount': {str(e)}")
        return

    # --- Add this new validation block ---
    REQUIRED_COLUMNS = ['discounted_price', 'product_name', 'category', 'user_id']

    missing_columns = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing_columns:
        print(f"❌ ERROR: Input CSV is missing required columns: {', '.join(missing_columns)}")
        print("Script cannot continue. Please ensure your CSV file contains all necessary columns.")
        return # Stop execution immediately
        # --- End of validation block ---
    try:
        # Aggregations
        total_revenue = df['sales_amount'].sum()
        if total_revenue == 0:
            print("⚠️ WARNING: Total revenue is zero. Check your data.")
            return
        
        revenue_by_product = df.groupby('product_name')['sales_amount'].sum()
        revenue_by_category = df.groupby('category')['sales_amount'].sum()
        revenue_by_user = df.groupby('user_id')['sales_amount'].sum()


    except KeyError as e:
        print(f"❌ ERROR: Missing expected column: {str(e)}")
        return
    except Exception as e:
        print(f"❌ ERROR while aggregating data: {str(e)}")
        return

    try:
        # File setup
        os.makedirs('Reports', exist_ok=True)
        now = datetime.now()
        report_date = now.strftime('%Y-%m-%d')
        timestamp = now.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f'Reports/report_{timestamp}.txt'

        # Build report
        report_lines = [
            "Sales Summary Report",
            f"Date: {report_date}",
            "-" * 20,
            f"\n Total Transactions: {len(df)}",
            f"\nGrand Total Revenue: {symbol}{total_revenue:.2f}",
            f"\n Max Revenue: {symbol}{df['sales_amount'].max():.2f}",
            f"\n Min Revenue: {symbol}{df['sales_amount'].min():.2f}",
            f"\n Average Revenue: {symbol}{df['sales_amount'].mean():.2f}",

        ]

        report_lines.append("\n\n--- Revenue by Category ---")
        report_lines.append(f"\nMax Revenue Category: {revenue_by_category.idxmax()} ({symbol}{revenue_by_category.max():.2f})")
        report_lines.append(f"\nMin Revenue Category: {revenue_by_category.idxmin()} ({symbol}{revenue_by_category.min():.2f})")
        # report_lines.append("\n--- List of Category: Revenue ---")
        # for category, revenue in revenue_by_category.items():
        #     report_lines.append(f"{category}: {symbol}{revenue:.2f}")

        report_lines.append("\n\n--- Revenue by User ---")
        report_lines.append(f"\nMax Revenue User: {revenue_by_user.idxmax()} ({symbol}{revenue_by_user.max():.2f})")
        report_lines.append(f"\nMin Revenue User: {revenue_by_user.idxmin()} ({symbol}{revenue_by_user.min():.2f})")
        # report_lines.append("\n--- List of User: Revenue ---")
        # for user, revenue in revenue_by_user.items():
        #     report_lines.append(f"User {user}: {symbol}{revenue:.2f}")

        report_lines.append("\n\n--- Revenue by Product ---")
        report_lines.append(f"\nMax Revenue Product: {revenue_by_product.idxmax()} ({symbol}{revenue_by_product.max():.2f})")
        report_lines.append(f"\nMin Revenue Product: {revenue_by_product.idxmin()} ({symbol}{revenue_by_product.min():.2f})")
        # report_lines.append("\n--- List of Product: Revenue ---")
        # for product, revenue in revenue_by_product.items():
        #     report_lines.append(f"{product}: {symbol}{revenue:.2f}")

        report_lines.append("-" * 20)
        report_text = "\n".join(report_lines)

        # Save to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)

        print(f"✅ Report saved as {filename}")

    except Exception as e:
        print(f"❌ ERROR while saving report: {str(e)}")
        return

    print("✅ Report generation completed successfully.")

# Run the report generation
if __name__ == "__main__":
    generate_sales_report()
