# Your-Stocks-VS-Nifty-50

a Python-based tool designed to simulate investment in Indian stocks and compare their performance with the Nifty 50 index. This program uses Yahoo Finance data to calculate returns, portfolio value, and other key metrics, helping users make informed investment decisions.

**Features**

Fetch historical stock data for any Indian stock using its symbol (e.g., RELIANCE.NS for Reliance Industries).

Simulate an investment over a user-defined period.

Calculate and display:

Shares bought based on the initial investment amount.

Portfolio value over time.

Total returns for the selected stock and Nifty 50 index.

Compare the performance of the chosen stock against the Nifty 50 index.

Generate and display plots for:
Portfolio value comparison,
returns comparison.

**Prerequisites**

Before running the program, ensure you have the following installed:

Python 3.7 or later

Required Python libraries:

yfinance

pandas

matplotlib


**How to Use**

Clone or download this repository.

Run the program

Enter the required inputs:

Stock Symbol: Enter the Indian stock's Yahoo Finance symbol (e.g., RELIANCE.NS for Reliance Industries).

Investment Amount: The amount you wish to simulate investing (in INR).

Start Date: The date you want to start the investment simulation (format: YYYY-MM-DD).

End Date: The end date for the simulation (or enter today for the current date).

View the results:

Summary of your stock investment.

Nifty 50 comparison.

Visual plots comparing portfolio values and returns.


**Example Input:**

Enter the Indian stock symbol (e.g., RELIANCE.NS): RELIANCE.NS

Enter the investment amount in INR: 10000

Enter the start date (YYYY-MM-DD): 2023-01-01

Enter the end date (YYYY-MM-DD) or 'today' for current date: today

**Example Output:**


Investment Summary for RELIANCE.NS

Initial Investment: ₹10000.00

Shares Bought: 5.23

Initial Share Price: ₹1911.20

Final Share Price: ₹2134.45

Final Portfolio Value: ₹11162.90

Total Return: 11.63%


Nifty 50 Comparison

Nifty 50 Initial Value: ₹18102.20

Nifty 50 Final Value: ₹19345.65

Nifty 50 Total Return: 6.87%

**Example Plot:**

Portfolio Value Comparison: Shows the growth of your investment versus the Nifty 50.

Returns Comparison: Visualizes the percentage returns of your stock and Nifty 50 over time.

Project Highlights

Educational Tool: Helps users understand how their investments perform relative to the market index.

User-Friendly Interface: Input-driven console application for ease of use.

Data Visualization: Clear and informative plots to analyze portfolio performance.

**Limitations**

The program fetches data from Yahoo Finance, which might occasionally have incomplete or missing data.

Password-protected or non-Indian stocks may require different symbols.

Data accuracy depends on Yahoo Finance.

**Future Improvements**

Add support for more advanced metrics like CAGR (Compound Annual Growth Rate).

Include multiple stock portfolio simulation.

Integrate live updates for real-time investment tracking.

Build a graphical user interface (GUI).

**Contributing**

Contributions to this project are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

**License**

This project is licensed under the MIT License.
