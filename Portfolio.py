# Stock Portfolio Tracker

# Hardcoded stock prices (you can modify as needed)
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOGL": 140,  # Google
    "MSFT": 330,   # Microsoft
    "AMZN": 175    # Amazon
}

portfolio = {}  # To store user’s stock and quantity

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available stocks and prices (USD):")
for stock, price in stock_prices.items():
    print(f" - {stock}: ${price}")

# Take user input for portfolio
while True:
    stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    
    if stock_name == "DONE":
        break
    elif stock_name not in stock_prices:
        print("❗ Invalid stock symbol. Please choose from the list above.")
        continue
    
    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity <= 0:
            print("❗ Quantity must be positive.")
            continue
        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    except ValueError:
        print("❗ Please enter a valid number for quantity.")
        continue

# Calculate total investment
total_value = 0
print("\n💼 Your Portfolio Summary:")
print("-" * 40)
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print("-" * 40)
print(f"💰 Total Investment Value: ${total_value}")

# Optional: Save to file
save_option = input("\nWould you like to save this report to a file? (yes/no): ").lower()
if save_option == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Stock Portfolio Report\n")
        file.write("-" * 40 + "\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} × ${stock_prices[stock]} = ${stock_prices[stock]*qty}\n")
        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: ${total_value}\n")
    print("✅ Portfolio report saved as 'portfolio_report.txt'.")

print("\nThank you for using the Stock Portfolio Tracker!")
