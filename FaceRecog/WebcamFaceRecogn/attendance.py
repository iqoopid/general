import csv

# Define the data to write to the CSV file
data = [
    ['Id', 'Name'],
]
def record(Id, Name):

    rec = [Id, Name]
    data.append(rec)

    # Open a new CSV file for writing
    with open('record.csv', 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)

        # Write each row of data to the CSV file
        for row in data:
            writer.writerow(row)
    

print('Data has been written to record.csv.')
