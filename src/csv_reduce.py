import csv

def open_csv(file_obj, delimiter=";"):
    reader = csv.reader(file_obj, delimiter=delimiter)
    return reader


def find_line_by_column(reader: csv.reader, column_index, search_term):
    for row in reader:
        if column_index < len(row):
            if (row[column_index]).lower() == (search_term).lower():
                return row
    return None    

with open("Wizard.csv", mode="r", newline="") as file:    
    test = open_csv(file)
    print(find_line_by_column(test, 1, "Light"))


