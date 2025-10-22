import csv

# Paths
outpath = "13_working_with_data_files/01_working_with_CSV/total-price.csv"
inpath = "13_working_with_data_files/01_working_with_CSV/products.csv"

with open(inpath) as infile, open(outpath, mode="w", newline="") as outfile:

    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)

    # Write header
    writer.writerow(["Product Name", "Price", "Quantity", "Total Price"])

    for row in reader:
        # Convert Price and Quantity to numbers before multiplying
        price = float(row["Price"])  # Convert to float
        quantity = int(row["Quantity"])  # Convert to integer
        total_price = price * quantity

        writer.writerow([row["Product Name"], price, quantity, total_price])

print("Done")
