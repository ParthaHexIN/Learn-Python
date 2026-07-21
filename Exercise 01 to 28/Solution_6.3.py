dict1 = {
    "name": "Partha",
    "age": 21
}

dict2 = {
    "city": "Guwahati",
    "country": "India"
}

merged = {**dict1, **dict2}

print(merged)