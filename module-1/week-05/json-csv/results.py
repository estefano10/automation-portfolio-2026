import json
import csv

results = [
    {"test": "valid_login", "result": "pass"},
    {"test": "invalid_login", "result": "fail"},
    {"test": "checkout", "result": "pass"},
    {"test": "performance_greater80%", "result": "pass"}
]

with open("results.json", mode="w") as f:
    json.dump(results, f, indent=2)

with open("results.json") as f:
    data = json.load(f)
    print(data)

with open("results.csv", newline="") as f:
    data = csv.reader(f)
    for x in data:
         print(x)

with open("results.csv", newline="") as f:
    data = list(csv.DictReader(f))
    for x in data:
         print(x)