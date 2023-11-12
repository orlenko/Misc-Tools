import json
import csv
from datetime import datetime


def convert_timestamp(timestamp):
    # Convert the timestamp to localized date/time string
    return datetime.utcfromtimestamp(float(timestamp)).strftime("%Y-%m-%d %H:%M:%S")


def generate_data(fname):
    with open(fname, "r") as f:
        data = json.load(f)
        length = len(data)
        print(f"data loaded: {length} entries")
    for timestamp, record in data.items():
        src_ip = record.get("src_ip")
        city = record.get("geo_info", {}).get("city")
        region = record.get("geo_info", {}).get("region")
        hostname = record.get("geo_info", {}).get("hostname")
        useragent = record.get("useragent")
        yield convert_timestamp(timestamp), src_ip, city, region, hostname, useragent


def process(fname):
    headers = ["Timestap", "IP", "City", "Region", "Hostname", "User agent"]
    rows = list(generate_data(fname))
    by_ip = {}
    by_key = {}
    for [ts, ip, c, r, h, ua] in rows:
        by_ip.setdefault(ip, []).append([ts, ip, c, r, h, ua])
        key = f"{c}-{r}-{ip}"
        by_key.setdefault(key, []).append([ts, ip, c, r, h, ua])
    for collection in [by_ip, by_key]:
        for key, rows in collection.items():
            with open(f"{key}.csv", "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(
                    [
                        dict(zip(headers, r))
                        for r in sorted(rows, key=lambda r: r[0], reverse=True)
                    ]
                )


if __name__ == "__main__":
    process("input.json")
