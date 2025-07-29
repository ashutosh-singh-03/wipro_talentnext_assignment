# Project 1: Travel recommendation based on distance
distance = float(input("How far would you like to travel in miles? "))
if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-Cycle to your destination")
else:
    print("I suggest Super-Car to your destination")

print()

# Project 2: Cloud server hosting cost calculator
cost_per_hour = 0.51

cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30

print("How much does it cost to operate one server per day?", cost_per_day)
print("How much does it cost to operate one server per week?", cost_per_week)
print("How much does it cost to operate one server per month?", cost_per_month)

budget = 918
days_with_budget = budget / cost_per_day
print("How many days can I operate one server with $918?", int(days_with_budget))
