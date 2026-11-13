
trains = {
    "12601": {
        "name": "Chennai Express",
        "stops": [
            ("Chennai", "06:00", "06:15"),
            ("Vijayawada", "12:00", "12:10"),
            ("Hyderabad", "18:00", "18:15")
        ],
        "days": {"Monday", "Wednesday", "Friday"}
    },

    "12602": {
        "name": "Mumbai Express",
        "stops": [
            ("Chennai", "07:00", "07:20"),
            ("Bangalore", "12:00", "12:15"),
            ("Mumbai", "20:00", "20:30")
        ],
        "days": {"Tuesday", "Thursday", "Saturday"}
    },

    "12603": {
        "name": "Delhi Express",
        "stops": [
            ("Chennai", "08:00", "08:15"),
            ("Vijayawada", "13:00", "13:10"),
            ("Delhi", "22:00", "22:15")
        ],
        "days": {"Monday", "Tuesday", "Friday"}
    },

    "12604": {
        "name": "Coimbatore Express",
        "stops": [
            ("Chennai", "09:00", "09:15"),
            ("Salem", "13:00", "13:10"),
            ("Coimbatore", "16:00", "16:15")
        ],
        "days": {"Wednesday", "Thursday", "Sunday"}
    },

    "12605": {
        "name": "Kanyakumari Express",
        "stops": [
            ("Chennai", "10:00", "10:15"),
            ("Madurai", "16:00", "16:10"),
            ("Kanyakumari", "20:00", "20:15")
        ],
        "days": {"Monday", "Thursday", "Saturday"}
    }
}

station = "Chennai"
day = "Monday"

# Find trains stopping at the given station on a given day
result = []

for number, details in trains.items():
    if day in details["days"]:

        for stop in details["stops"]:
            if stop[0] == station:
                result.append(
                    (number, details["name"], stop[2])
                )

# Sort by departure time
result = sorted(result, key=lambda x: x[2])

print("Trains at", station, "on", day)

for number, name, departure in result:
    print(number, name, departure)

# Print complete timetable
print("\nComplete Timetable")

for number, details in trains.items():
    print("\nTrain:", number, details["name"])

    for station, arrival, departure in details["stops"]:
        print(station, arrival, departure)
