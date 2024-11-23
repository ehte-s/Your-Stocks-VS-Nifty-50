import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def indian_stock_simulator():
    # Get user inputs
    symbol = input("Enter the Indian stock symbol (e.g., RELIANCE.NS): ")
    investment_amount = float(input("Enter the investment amount in INR: "))
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD) or 'today' for current date: ")

    if end_date.lower() == 'today':
        end_date = datetime.today().strftime('%Y-%m-%d')

    # Download stock data
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    if stock_data.empty:
        print(f"No data available for {symbol}. Please check the symbol and date range.")
        return

    # Calculate number of shares bought
    initial_price = stock_data['Close'].iloc[0]
    shares_bought = investment_amount / initial_price

    # Calculate portfolio value over time
    stock_data['Portfolio_Value'] = stock_data['Close'] * shares_bought

    # Calculate returns
    stock_data['Returns'] = stock_data['Portfolio_Value'] / investment_amount - 1

    # Print results
    print(f"\nInvestment Summary for {symbol}")
    print(f"Initial Investment: ₹{investment_amount:.2f}")
    print(f"Shares Bought: {shares_bought:.2f}")
    print(f"Initial Share Price: ₹{initial_price:.2f}")
    print(f"Final Share Price: ₹{stock_data['Close'].iloc[-1]:.2f}")
    print(f"Final Portfolio Value: ₹{stock_data['Portfolio_Value'].iloc[-1]:.2f}")
    print(f"Total Return: {stock_data['Returns'].iloc[-1]:.2%}")
    # Download Nifty 50 data
    nifty50_symbol = "^NSEI"
    nifty50_data = yf.download(nifty50_symbol, start=start_date, end=end_date)

    if nifty50_data.empty:
        print(f"No data available for Nifty 50. Please check the date range.")
        return

    # Calculate Nifty 50 returns
    nifty50_initial_value = nifty50_data['Close'].iloc[0]
    nifty50_shares = investment_amount / nifty50_initial_value
    nifty50_data['Portfolio_Value'] = nifty50_data['Close'] * nifty50_shares
    nifty50_data['Returns'] = nifty50_data['Portfolio_Value'] / investment_amount - 1

    # Print Nifty 50 results
    print(f"\nNifty 50 Comparison")
    print(f"Nifty 50 Initial Value: {nifty50_initial_value:.2f}")
    print(f"Nifty 50 Final Value: {nifty50_data['Close'].iloc[-1]:.2f}")
    print(f"Nifty 50 Total Return: {nifty50_data['Returns'].iloc[-1]:.2%}")

    # Prepare data for plotting
    combined_returns = pd.DataFrame({
        'Stock': stock_data['Returns'],
        'Nifty50': nifty50_data['Returns']
    })

    # Plot the results
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data.index, stock_data['Portfolio_Value'], label=f'{symbol} Portfolio Value')
    plt.plot(nifty50_data.index, nifty50_data['Portfolio_Value'], label='Nifty 50 Portfolio Value')
    plt.title(f'{symbol} vs Nifty 50 Investment Performance')
    plt.xlabel('Date')
    plt.ylabel('Portfolio Value (INR)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot returns comparison
    plt.figure(figsize=(12, 6))
    combined_returns.plot()
    plt.title(f'{symbol} vs Nifty 50 Returns Comparison')
    plt.xlabel('Date')
    plt.ylabel('Returns')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    indian_stock_simulator()
