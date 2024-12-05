# Course Project

This project provides a service that analyzes financial transactions and offers JSON-based reports. It supports processing data from an Excel file, generating insights, and saving results in JSON format.

## Main Functions

### Home Page
The main page of the service delivers the following information in JSON format:
- A greeting based on the current time of day.
- Data for each bank card:
  - Last 4 digits of the card.
  - Total amount of expenses.
  - Cashback (1 ruble for every 100 rubles).
  - Top 5 transactions by payment amount.
- Exchange rate.
- Values of stocks from the S&P500 index.

### Services
#### Simple Search
- **Spending by Title**: Search for transactions by their description.

#### Counts
- **Spending by Category**: Summarize spending based on transaction categories.

---

## Modules

### Module: `views`
**Functions**:
- **`welcome_message`**: Returns a greeting message based on the time of day.
- **`sum_expenses`**: Calculates the total expenses from a list of transactions.
- **`load_xlsx_data`**: Loads transaction data from an Excel file.
- **`analyze_card_usage`**: Analyzes card usage and summarizes transaction details.
- **`largest_transactions`**: Retrieves the top 5 largest transactions by amount.
- **`fetch_currency_value`**: Retrieves the exchange rate of a currency against the ruble.
- **`get_stock_currency`**: Fetches the current price of a stock.
- **`execute_main`**: Executes the primary data analysis functions.
- **`save_to_json`**: Saves analysis results to a JSON file.
- **`run_application`**: Launches the application.

### Module: `reports`
**Functions**:
- **`find_transactions`**: Searches for transactions by keyword and saves results in a JSON file.
- **`calculate_expenses`**: Computes expenses for a selected category over a specified time frame.
- **`run_analysis`**: Analyzes transactions, calculates expenses, and outputs results to the console.

### Module: `services`
**Functions**:
- **`read_transactions_xls`**: Reads transactions from an XLSX file and returns them as a list of dictionaries.
- **`search_by_description`**: Finds transactions matching a given query description.
- **`write_to_json`**: Saves data into a JSON file for easy transfer and storage.

---

## Environment Variables
Environment variables can be configured using the `api.env` file located in the project repository.

---

## Repository
The project is hosted on GitHub: [curswork_bd - dev_2 branch](https://github.com/j1nnx/curswork_bd/tree/dev_2).

---

## Getting Started
1. Clone the repository:  
   ```bash
   git clone https://github.com/j1nnx/curswork_bd.git
