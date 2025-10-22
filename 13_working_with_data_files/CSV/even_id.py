import csv

path = "/home/dimah/Public/jadi-python-course/13_working_with_data_files/CSV/customers-100.csv"

with open(path, newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        try:
            if int(row["Index"]) % 2 == 0:
                print("Index", row["Index"], row["Company"])
        except (ValueError, KeyError):
            continue
