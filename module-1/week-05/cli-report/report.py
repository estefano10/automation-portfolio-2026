import csv
from collections import Counter
import json

def main() -> None:

    with open("results.csv", newline="", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))

    total = count_total(reader)
    rate = pass_rate(reader)
    failures = top_failures(reader)

    results = {"total": total, "pass_rate": rate, "top_failures": failures}

    with open("report.json", mode="w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Total: {total} | Pass rate: {rate}% | Top failures: {format_failures(failures)}")

def count_total(rows: list[dict]) -> int:
    return len(rows)

def pass_rate(rows: list[dict]) -> float:
    if not rows:
        return 0.0
    return round(sum(1 for row in rows if row["status"] == "pass") / len(rows) * 100, 2)

def top_failures(rows: list[dict]) -> list[tuple[str, int]]:
    return Counter(row["suite"] for row in rows if row["status"] == "fail").most_common()

def format_failures(failures: list[tuple[str, int]]) -> str:
    parts = [f"{suite_name} ({qty})" for suite_name, qty in failures]
    line = ", ".join(parts)
    return line

if __name__ == "__main__":
    main()