import csv

file_name = 'profiles2.csv'
with open(file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    row_list = [
        ["name", "age", "country"],
        ["Oladele Damilola", "40", "Nigeria"],
        ["Alina Hricko", "23" ,"Ukraine"],
        ["Isabel Walter", "50" ,"United Kingdom"],
    ]

    writer.writerows(row_list)
    writer.writerow(["Oladele Damilola1", "45", "Nigeria1"])


with open(file_name, 'r') as csvfile:
    # Create a reader object
    reader = csv.reader(csvfile)
    ages = []

    for row in reader:
        # Access each element in the row
        print(row)
        age=row[1]
        if (int(age)<30):
            break
        ages.append(age)
        print ("into age loop")

