
calls = [
    ("Chennai", "Rice seeds not received"),
    ("Madurai", "Fertiliser price high"),
    ("Chennai", "Seeds price high subsidy not received"),
    ("Salem", "Rice seeds delayed")
]

STOP = {"not", "high", "the", "is", "and"}

def frequencies(texts, stop):
    counts = {}

    for district, complaint in texts:
        words = complaint.lower().split()

        for word in words:
            word = word.strip(".,!?")

            if word and word not in stop:
                counts[word] = counts.get(word, 0) + 1

    return counts

def top(counts, k):
    return sorted(
        counts.items(),
        key=lambda x: (-x[1], x[0])
    )[:k]

# Group complaints by district
district_complaints = {}

for district, complaint in calls:
    district_complaints.setdefault(district, []).append(complaint)

print("Word Frequencies:", frequencies(calls, STOP))
print("Top 3 Words:", top(frequencies(calls, STOP), 3))
print("District Complaints:", district_complaints)
