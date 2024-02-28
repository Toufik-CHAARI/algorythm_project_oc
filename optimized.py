import csv
import time

# Read stock data from a CSV file
def read_stocks(filename):
    stocks = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        for row in reader:
            try:
                name = row[0]
                cost = float(row[1]) * 100  
                profit_percentage = float(row[2])
                profit = cost * profit_percentage / 100  
                
                if cost > 0 and profit > 0:
                    stocks.append({'name': name, 'cost': int(cost), 'profit': int(profit)})
            except ValueError:
                continue
    return stocks

# Optimize stock selection using dynamic programming
def optimize_stocks(stocks, max_budget):
    max_budget_scaled = int(max_budget * 100)  
    dp_table = [0] * (max_budget_scaled + 1)
    stock_picks = [[] for _ in range(max_budget_scaled + 1)]

    for stock in stocks:
        cost = stock['cost']
        profit = stock['profit']
        for j in range(max_budget_scaled, cost - 1, -1):
            if j >= cost and (j - cost) < len(dp_table):
                if dp_table[j - cost] + profit > dp_table[j]:
                    dp_table[j] = dp_table[j - cost] + profit
                    stock_picks[j] = stock_picks[j - cost] + [stock]

    max_profit = dp_table[-1] / 100  
    picked_stocks = stock_picks[-1]
    total_cost = sum(stock['cost'] for stock in picked_stocks) / 100 if picked_stocks else 0
    return max_profit, picked_stocks, total_cost

if __name__ == "__main__":
    start_time = time.time()
    stocks = read_stocks('dataset2_Python+P7.csv')  
    max_budget = 500  
    maximum_profit, picked_stocks, total_cost = optimize_stocks(stocks, max_budget)
    end_time = time.time()

    print(f"Maximum possible profit: {maximum_profit:.2f}€")
    print(f"Total cost: {total_cost:.2f}€")
    print("Stocks bought:")
    for stock in picked_stocks:
        print(f"- {stock['name']} (Cost: {stock['cost']/100:.2f}€, Profit: {stock['profit']/100:.2f}€)")
    print(f"Time of completion: {end_time - start_time:.4f} seconds")
