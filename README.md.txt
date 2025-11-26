# 🤖 Automated Inventory Management System

A Python-based automation tool designed to streamline inventory tracking for small to medium businesses. This script reads inventory data from Excel, analyzes stock levels against minimum requirements, and automatically generates a detailed purchase report.

## 🚀 Key Features

* **Automated Analysis:** Instantly processes Excel spreadsheets (`.xlsx`) using Pandas.
* **Smart Reporting:** Identifies items below minimum stock levels.
* **Cost Calculation:** Estimates the budget required for restocking.
* **Auto-Generated Output:** Creates a formatted text file (`.txt`) ready for printing or emailing to suppliers.
* **Error Handling:** Includes robust error management for missing files or incorrect formats.

## 🛠️ Technologies Used

* **Python 3.13**
* **Pandas** (Data Manipulation)
* **OpenPyXL** (Excel I/O)

## 📋 How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/miguelmantoani/inventory-automation-py.git](https://github.com/miguelmantoani/inventory-automation-py.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pandas openpyxl
    ```
3.  Run the script:
    ```bash
    python main.py
    ```
    *(Note: If no input file is found, the script automatically generates a sample `estoque.xlsx` for testing purposes).*

## 💼 Use Case

This project demonstrates how Python can replace manual data entry tasks, reducing human error and saving hours of administrative work per week.