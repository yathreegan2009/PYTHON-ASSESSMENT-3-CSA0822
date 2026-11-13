
import copy

rows, cols = 3, 4

# Aliasing problem
bad = [[0] * cols] * rows
bad[0][1] = 7

# Correct grid using list comprehension
good = [[0 for j in range(cols)] for i in range(rows)]
good[0][1] = 7

print("bad :", bad)
print("good:", good)

print(bad[0] is bad[1], good[0] is good[1])

# Tuples as dictionary keys
stops = {
    (13.0827, 80.2707): "Chennai Central",
    (13.0418, 80.2341): "T. Nagar"
}

print(stops[(13.0418, 80.2341)])

# Aliasing
a = [10, 20, 30]
b = a
b[0] = 100
print("Aliasing:", a)

# Shallow copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0][0] = 99
print("Shallow Copy:", original)

# Deep copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print("Deep Copy:", original)
print("Deep Copy Result:", deep)

# Tuple unpacking
coordinates = [(10, 20), (30, 40), (50, 60)]

for latitude, longitude in coordinates:
    print(latitude, longitude)
