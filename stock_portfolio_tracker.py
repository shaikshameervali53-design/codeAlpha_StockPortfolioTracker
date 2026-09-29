import csv



stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180,
    "META": 500,
    "NVDA": 120
}


def display_stocks():
    """Display all available stocks and their prices."""

    print("\n========== AVAILABLE STOCKS ==========")

    for stock, price in stock_prices.items():
        print(f"{stock:<8} : ${price:.2f}")

    print("======================================\n")


def get_stock_details():
    """Take stock symbol and quantity from the user."""

    while True:
        stock = input("Enter stock symbol: ").strip().upper()

        if stock not in stock_prices:
            print("Invalid stock symbol. Please choose from the available stocks.")
            continue

        break

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    price = stock_prices[stock]
    investment = price * quantity

    return stock, quantity, price, investment


def save_to_csv(portfolio, total_investment):
    """Save portfolio details to a CSV file."""

    filename = "portfolio.csv"

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        
        writer.writerow([
            "Stock",
            "Quantity",
            "Price Per Share",
            "Total Investment"
        ])

        
        for item in portfolio:
            writer.writerow([
                item["stock"],
                item["quantity"],
                f"{item['price']:.2f}",
                f"{item['investment']:.2f}"
            ])

        
        writer.writerow([])
        writer.writerow([
            "TOTAL INVESTMENT",
            "",
            "",
            f"{total_investment:.2f}"
        ])

    print(f"\nPortfolio saved successfully to {filename}")


def display_portfolio(portfolio, total_investment):
    """Display the final portfolio."""

    print("\n\n========== PORTFOLIO SUMMARY ==========")

    print(
        f"{'Stock':<10}"
        f"{'Quantity':<12}"
        f"{'Price':<15}"
        f"{'Investment':<15}"
    )

    print("-" * 52)

    for item in portfolio:

        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<12}"
            f"${item['price']:<14.2f}"
            f"${item['investment']:<14.2f}"
        )

    print("-" * 52)

    print(f"Total Investment: ${total_investment:.2f}")

    print("========================================")


def main():

    print("========================================")
    print("       STOCK PORTFOLIO TRACKER")
    print("========================================")

    display_stocks()

    portfolio = []
    total_investment = 0

    while True:

        try:
            number_of_stocks = int(
                input("How many different stocks do you want to add? ")
            )

            if number_of_stocks <= 0:
                print("Please enter a number greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    
    for i in range(number_of_stocks):

        print(f"\n--- Stock {i + 1} ---")

        stock, quantity, price, investment = get_stock_details()

        portfolio.append({
            "stock": stock,
            "quantity": quantity,
            "price": price,
            "investment": investment
        })

        total_investment += investment

    
    display_portfolio(portfolio, total_investment)
    while True:

        save_choice = input(
            "\nDo you want to save the portfolio to CSV? (yes/no): "
        ).strip().lower()

        if save_choice in ["yes", "y"]:
            save_to_csv(portfolio, total_investment)
            break

        elif save_choice in ["no", "n"]:
            print("\nPortfolio was not saved.")
            break

        else:
            print("Please enter yes or no.")


if __name__ == "__main__":
    main()