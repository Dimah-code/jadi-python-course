import csv

path = "customers-100.csv"

with open(path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            if int(row["Index"]) % 2 == 0:
                print("Index", row["Index"])
        except (ValueError, KeyError):
            continue
