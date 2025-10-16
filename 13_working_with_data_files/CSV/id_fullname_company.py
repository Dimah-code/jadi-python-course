import csv

path = "/home/dimah/Public/PythonTry/13_working_with_data_files/CSV/customers-100.csv"

with open(path) as csvfile:
    csv_data = csv.reader(csvfile)
    for line in csv_data:
        print(
            f"Customer ID: {line[1]}, Company: {line[4]}, "
            f"Fullname: {line[2] + ' ' + line[3]}"
        )
