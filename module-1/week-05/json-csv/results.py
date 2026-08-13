import json

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