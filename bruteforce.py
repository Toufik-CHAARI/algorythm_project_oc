import csv
from itertools import combinations
import time  # Import the time module

# Read stock data from a CSV file
def read_stocks(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        stocks = [{'name': row[0], 'cost': int(row[1]), 'profit': float(row[2])} for row in reader]
    return stocks

# Calculate the profit for a combination of stocks
def calculate_profit(stocks):
    total_cost = sum(stock['cost'] for stock in stocks)
    total_profit = sum(stock['cost'] * stock['profit'] / 100 for stock in stocks)
    return total_cost, total_profit

# Find the best combination of stocks
def find_best_combination(stocks, max_budget=500):
    best_combination = None
    highest_profit = 0
    for r in range(1, len(stocks) + 1):
        for combination in combinations(stocks, r):
            cost, profit = calculate_profit(combination)
            if cost <= max_budget and profit > highest_profit:
                highest_profit = profit
                best_combination = combination
    return best_combination, highest_profit

if __name__ == "__main__":
    start_time = time.time()  # Record the start time

    stocks = read_stocks('actions.csv')
    best_combination, highest_profit = find_best_combination(stocks)
    
    if best_combination:
        print("Best combination of stocks to buy:")
        for stock in best_combination:
            print(f"{stock['name']} (Cost: {stock['cost']}€, Profit: {stock['profit']}%)")
        print(f"Total profit after 2 years: {highest_profit:.2f}€")
    else:
        print("No combination of stocks found that fits the budget.")
    
    end_time = time.time()  # Record the end time
    print(f"Time of completion: {end_time - start_time:.2f} seconds.")
