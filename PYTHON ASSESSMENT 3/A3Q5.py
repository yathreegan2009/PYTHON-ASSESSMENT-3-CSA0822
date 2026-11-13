
readings = [2, 5, 8, 10, 15, 55, -60, 4, 7, 9]

# Method 1: Using for loop and append()
valid = []

for temp in readings:
    if -50 <= temp <= 50:
        valid.append(temp)

fahrenheit = []

for temp in valid:
    fahrenheit.append((temp * 9/5) + 32)

print("Valid Readings:", valid)
print("Fahrenheit:", fahrenheit)

# Method 2: Using list comprehension
valid_comp = [
    temp for temp in readings
    if -50 <= temp <= 50
]

fahrenheit_comp = [
    (temp * 9/5) + 32 for temp in valid_comp
]

print("List Comprehension:", valid_comp)
print("Fahrenheit:", fahrenheit_comp)

# Method 3: Using map(), filter() and lambda
valid_map = list(
    filter(lambda x: -50 <= x <= 50, readings)
)

fahrenheit_map = list(
    map(lambda x: (x * 9/5) + 32, valid_map)
)

print("Map and Filter:", valid_map)
print("Fahrenheit:", fahrenheit_map)

# Alarm minutes (outside 2 to 8 Celsius)
alarm_minutes = [
    i + 1 for i, temp in enumerate(readings)
    if temp < 2 or temp > 8
]

print("Alarm Minutes:", alarm_minutes)
