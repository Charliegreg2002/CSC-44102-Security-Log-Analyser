import csv

def load_logs(filename):
    records = []

    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            records.append(row)

    return records


def main():
    print("=== Security Log Analyser ===")

    logs = load_logs("sample_logs.csv")

    for log in logs:
        print(log)


if __name__ == "__main__":
    main()