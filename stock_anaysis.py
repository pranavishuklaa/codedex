#to analyse stock data of Jan 2023

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(i):
    return stock_prices[i-1]

def max_price():
    return max(stock_prices)

def min_price():
    return min(stock_prices)    

print("Price at 5th Jan 2023: ", price_at(5))
print("Max price of Jan 2023: ", max_price())
print("Min price of Jan 2023: ", min_price())

