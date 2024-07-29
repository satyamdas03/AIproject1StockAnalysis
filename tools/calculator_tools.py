# to perform the necessary calculations
import pandas as pd
import numpy as np

def moving_average(data, window):
    return data.rolling(window=window).mean()

def exponential_moving_average(data, span):
    return data.ewm(span=span, adjust=False).mean()

def return_on_investment(initial_value, final_value):
    return (final_value - initial_value) / initial_value

def load_stock_data(file_path):
    return pd.read_csv(file_path, parse_dates=True, index_col='Date')

def calculate_volatility(data):
    return data.pct_change().std()

def calculate_sharpe_ratio(data, risk_free_rate=0.01):
    returns = data.pct_change()
    excess_returns = returns - risk_free_rate / 252
    return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

# Example function to calculate a simple moving average
def simple_moving_average(data, window):
    return data.rolling(window=window).mean()
def main():
    print("Welcome to the Stock Analysis Calculator")

    file_path = input("Enter the path to your stock data CSV file: ")
    data = load_stock_data(file_path)

    while True:
        print("\nChoose an option:")
        print("1. Calculate Moving Average")
        print("2. Calculate Exponential Moving Average")
        print("3. Calculate Return on Investment")
        print("4. Calculate Volatility")
        print("5. Calculate Sharpe Ratio")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            window = int(input("Enter the window size for moving average: "))
            ma = moving_average(data['Close'], window)
            print(ma.tail())
        elif choice == '2':
            span = int(input("Enter the span for exponential moving average: "))
            ema = exponential_moving_average(data['Close'], span)
            print(ema.tail())
        elif choice == '3':
            initial_value = float(input("Enter the initial value: "))
            final_value = float(input("Enter the final value: "))
            roi = return_on_investment(initial_value, final_value)
            print(f"Return on Investment: {roi * 100:.2f}%")
        elif choice == '4':
            volatility = calculate_volatility(data['Close'])
            print(f"Volatility: {volatility:.2f}")
        elif choice == '5':
            risk_free_rate = float(input("Enter the risk-free rate (default is 0.01): ") or 0.01)
            sharpe_ratio = calculate_sharpe_ratio(data['Close'], risk_free_rate)
            print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
        elif choice == '6':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

