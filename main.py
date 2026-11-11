from log_analyser import load_logs


def main():
    print("=== Security Log Analyser ===")

    try:
        logs = load_logs("sample_logs.csv")
    except FileNotFoundError:
        print("Error: The selected CSV file could not be found.")
        return

    for log in logs:
        print(log)


if __name__ == "__main__":
    main()