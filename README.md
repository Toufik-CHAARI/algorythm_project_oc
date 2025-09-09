# Algorithm Project - Stock Investment Optimization

This project implements two different algorithms to solve the **0/1 Knapsack Problem** applied to stock investment optimization. The goal is to find the optimal combination of stocks to purchase within a given budget to maximize profit.

## Problem Description

Given a list of stocks with their costs and expected profit percentages, find the best combination of stocks to buy with a maximum budget of 500€ to maximize the total profit after 2 years.

## Files Overview

### Core Algorithm Files

- **`bruteforce.py`** - Brute force solution using combinatorial approach
- **`optimized.py`** - Optimized solution using dynamic programming (0/1 Knapsack algorithm)

### Data Files

- **`actions.csv`** - Small dataset with 20 stocks for testing
- **`dataset1_Python+P7.csv`** - Large dataset with 1000+ stocks
- **`dataset2_Python+P7.csv`** - Large dataset with 1000+ stocks (contains negative prices)

## Algorithm Comparison

### Brute Force Approach (`bruteforce.py`)

**Time Complexity:** O(2^n) where n is the number of stocks
**Space Complexity:** O(1)

**How it works:**
1. Generates all possible combinations of stocks using `itertools.combinations`
2. For each combination, calculates total cost and profit
3. Keeps track of the combination with highest profit within budget
4. Returns the best combination found

**Pros:**
- Guaranteed to find the optimal solution
- Simple to understand and implement

**Cons:**
- Exponential time complexity
- Impractical for large datasets (>20 stocks)

### Dynamic Programming Approach (`optimized.py`)

**Time Complexity:** O(n × W) where n is number of stocks and W is budget
**Space Complexity:** O(W)

**How it works:**
1. Uses a 1D DP table to store maximum profit for each budget amount
2. For each stock, updates the DP table in reverse order to avoid using the same stock twice
3. Tracks which stocks are selected for each budget amount
4. Returns the optimal solution for the maximum budget

**Pros:**
- Polynomial time complexity
- Efficient for large datasets
- Guaranteed optimal solution

**Cons:**
- More complex implementation
- Requires understanding of dynamic programming

## Data Format

### Input CSV Format
```csv
name,price,profit
Action-1,20,5
Action-2,30,10
...
```

Where:
- `name`: Stock identifier
- `price`: Cost of the stock in euros
- `profit`: Expected profit percentage after 2 years

### Data Processing
- Prices are converted to cents (multiplied by 100) for integer arithmetic
- Profit is calculated as: `profit_amount = cost * profit_percentage / 100`
- Negative prices and zero profits are filtered out

## Usage

### Running the Brute Force Algorithm
```bash
python bruteforce.py
```

### Running the Optimized Algorithm
```bash
python optimized.py
```

## Performance Comparison

| Dataset | Brute Force | Dynamic Programming |
|---------|-------------|-------------------|
| actions.csv (20 stocks) | ~0.01s | ~0.001s |
| dataset1 (1000+ stocks) | Impractical | ~0.01s |
| dataset2 (1000+ stocks) | Impractical | ~0.01s |

## Example Output

```
Maximum possible profit: 123.45€
Total cost: 498.50€
Stocks bought:
- Share-ABC (Cost: 25.30€, Profit: 8.50€)
- Share-XYZ (Cost: 45.20€, Profit: 12.75€)
...
Time of completion: 0.0012 seconds
```

## Technical Details

### Key Optimizations in Dynamic Programming Version

1. **Integer Scaling**: Prices converted to cents to avoid floating-point precision issues
2. **Reverse Iteration**: DP table updated in reverse to prevent using same stock multiple times
3. **Memory Efficient**: Uses 1D array instead of 2D for space optimization
4. **Stock Tracking**: Maintains list of selected stocks for each budget amount

### Error Handling

- Invalid CSV rows are skipped with error logging
- Negative prices and zero profits are filtered out
- Graceful handling of file reading errors

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Project Structure

```
algorythm_project_oc/
├── bruteforce.py          # Brute force implementation
├── optimized.py           # Dynamic programming implementation
├── actions.csv            # Small test dataset
├── dataset1_Python+P7.csv # Large dataset 1
├── dataset2_Python+P7.csv # Large dataset 2
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Algorithm Analysis

This project demonstrates the importance of algorithm choice in solving optimization problems:

- **Small datasets**: Both algorithms work, but DP is faster
- **Large datasets**: Only DP is practical due to exponential growth of brute force
- **Real-world applications**: DP approach is essential for production systems

The 0/1 Knapsack problem is a classic computer science problem with applications in:
- Resource allocation
- Investment portfolio optimization
- Resource scheduling
- Budget planning

## Future Improvements

1. Add support for fractional knapsack (greedy algorithm)
2. Implement branch and bound for exact solutions
3. Add visualization of algorithm performance
4. Support for multiple constraints
5. Add unit tests for algorithm validation