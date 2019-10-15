def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost)*(tip_percent/100)
    tax = (meal_cost)*(tax_percent/100)
    totalCost = int(round(meal_cost + tip + tax))
    print(totalCost)
solve(meal_cost = 12.00, tip_percent= 20, tax_percent= 8)
