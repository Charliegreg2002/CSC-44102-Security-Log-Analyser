import csv
import ipaddress
from datetime import datetime

def load_logs(filename):
    records = []
    seen_records = set()
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        required_columns = {"timestamp", "username", "ip_address", "status"}
        actual_columns = set(reader.fieldnames or [])

        missing_columns = required_columns - actual_columns

        if missing_columns:
            print(f"Error: Missing CSV columns: {', '.join(sorted(missing_columns))}")
            return []
        for row_number, row in enumerate(reader, start=2):
            if not valid_username(row.get("username")):
                print("Rejected record: Missing or empty username")
            elif not valid_ip(row.get("ip_address")):
                print(f"Rejected row {row_number}: Invalid IP address")
            elif not valid_timestamp(row.get("timestamp")):
                print(f"Rejected row {row_number}: Invalid timestamp")
            elif not valid_status(row.get("status")):
                print(f"Rejected row {row_number}: Invalid login status")
            else:
                record_key = (
                    row["timestamp"],
                    row["username"],
                    row["ip_address"],
                    row["status"]
                )

                if record_key in seen_records:
                    print(f"Duplicate record detected at row {row_number}")
                else:
                    seen_records.add(record_key)

                records.append(row)

    if not records:
        print("Error: No valid login records were found.")
    return records

def valid_username(username):
    if username is None:
        return False

    if username.strip() == "":
        return False

    return True

def valid_ip(ip):
    if ip is None or ip.strip() == "":
        return False

    try:
        ipaddress.ip_address(ip.strip())
        return True
    except ValueError:
        return False

def valid_timestamp(timestamp):
    if timestamp is None or timestamp.strip() == "":
        return False

    try:
        datetime.strptime(timestamp.strip(), "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False

def valid_status(status):
    if status is None:
        return False

    return status.strip().upper() in ("SUCCESS", "FAILED")