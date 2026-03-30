import csv
import os

input_dir = r"d:\repos\quantium-starter-repo\data"
output_file = r"d:\repos\quantium-starter-repo\formatted_data.csv"

files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]

with open(output_file, 'w', newline='') as out_f:
    writer = csv.writer(out_f)
    writer.writerow(["Sales", "Date", "Region"])
    
    for file in files:
        file_path = os.path.join(input_dir, file)
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
            
        with open(file_path, 'r') as in_f:
            reader = csv.DictReader(in_f)
            for row in reader:
                if row['product'].strip().lower() == 'pink morsel':
                    price = float(row['price'].replace('$', ''))
                    quantity = int(row['quantity'])
                    sales = price * quantity
                    writer.writerow([sales, row['date'], row['region']])

print(f"Data successfully processed and saved to {output_file}")
