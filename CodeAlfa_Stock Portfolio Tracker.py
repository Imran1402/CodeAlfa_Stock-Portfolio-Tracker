# Stock Portfolio Tracker (Optimized)

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

portfolio = {}

print("🔎 Enter your stocks (type 'done' to finish):")
while True:
    name = input("Enter stock symbol (e.g., AAPL): ").upper()
    if name == "DONE":
        break
    if name not in stock_prices:
        print(f"❌ {name} not found in stock list. Try again.")
        continue
    try:
        qty = int(input(f"Enter quantity of {name}: "))
        portfolio[name] = portfolio.get(name, 0) + qty
    except ValueError:
        print("⚠ Invalid quantity. Enter a number.")

# Calculate total
total_value = 0
print("\n📊 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares x ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_value}")

# Save to file
# Save to file
if input("Save this report to 'portfolio.txt'? (yes/no): ").lower() == 'yes':
    with open("portfolio.txt", "w", encoding="utf-8") as f:
        f.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock}: {qty} shares x ₹{price} = ₹{value}\n")
        f.write(f"\nTotal Investment Value: ₹{total_value}")
    print("✅ Portfolio saved to 'portfolio.txt'")