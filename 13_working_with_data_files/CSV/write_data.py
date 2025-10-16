import csv

fn = input("Enter a filename: (with .csv) ")

csvfile = open(fn, mode="w", newline="")

csv_write = csv.writer(csvfile, delimiter="|")

csv_write.writerow(["ID", "Name", "Age", "Gender"])

end = False
ID = 0
while not end:
    ID += 1
    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    csv_write.writerow([ID, name, age, gender])

    new_row = input("Do you want to write another line: (y/n) ")
    if new_row.lower() == "y":
        continue
    else:
        end = True

print(f"Program Closed! writed in {csvfile.name}")

csvfile.close()
