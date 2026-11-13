
import random

# Generate 365 daily rainfall readings
readings = [random.randint(0, 100) for _ in range(365)]

# Weekly rainfall totals
weekly_totals = [
    sum(readings[i:i+7])
    for i in range(0, 365, 7)
]

print("Weekly Rainfall Totals:", weekly_totals)

# Maximum and minimum rainfall
print("Maximum Rainfall:", max(readings))
print("Maximum Day:", readings.index(max(readings)) + 1)

print("Minimum Rainfall:", min(readings))
print("Minimum Day:", readings.index(min(readings)) + 1)

# 7-day moving average
moving_average = [
    sum(readings[i:i+7]) / 7
    for i in range(len(readings) - 6)
]

print("7-Day Moving Average:", moving_average)

# Dry days
dry_days = [
    i + 1 for i, value in enumerate(readings)
    if value == 0
]

print("Dry Days:", dry_days)
