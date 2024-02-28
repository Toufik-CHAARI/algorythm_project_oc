import csv
from itertools import combinations
import time  

def read_stocks(filename):
    stocks = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            try:
                name = row[0]
                cost = float(row[1]) * 100  
                profit_percentage = float(row[2])
                profit = cost * profit_percentage / 100  
                stocks.append({'name': name, 'cost': int(cost), 'profit': int(profit)})
            except ValueError as e:
                print(f"Error processing stock {row[0]}: {e}")
                continue
    return stocks


def calculate_profit(stocks):
    total_cost = sum(stock['cost'] for stock in stocks) / 100  
    total_profit = sum(stock['profit'] for stock in stocks) / 100  
    return total_cost, total_profit


def find_best_combination(stocks, max_budget=500):
    best_combination = None
    highest_profit = 0
    best_cost = 0  
    for r in range(1, len(stocks) + 1):
        for combination in combinations(stocks, r):
            cost, profit = calculate_profit(combination)
            if cost <= max_budget and profit > highest_profit:
                highest_profit = profit
                best_combination = combination
                best_cost = cost  
    return best_combination, highest_profit, best_cost

if __name__ == "__main__":
    start_time = time.time()  

    stocks = read_stocks('actions.csv')
    best_combination, highest_profit, best_cost = find_best_combination(stocks)
    
    if best_combination:
        print("Best combination of stocks to buy:")
        for stock in best_combination:
            print(f"{stock['name']} (Cost: {stock['cost']/100:.2f}€, Profit: {stock['profit']/100:.2f}%)")
        print(f"Total cost: {best_cost:.2f}€")
        print(f"Total profit after 2 years: {highest_profit:.2f}€")
        
    else:
        print("No combination of stocks found that fits the budget.")
    
    end_time = time.time()  
    print(f"Time of completion: {end_time - start_time:.2f} seconds.")
