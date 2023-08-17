mountain_in_japan = {"jufi": 3776, "kitadake": 3193, "okuhodakadake": 3190, "dummyk": 0}

mountain_in_japan = {"fuji": 3776, "kitadake": 3193, "okuhodakadake": 3190, "dummy": 0}
mountain_in_japan_sorted = sorted(
    mountain_in_japan.items(), key=lambda s: s[1], reverse=True
)
print(mountain_in_japan_sorted)
