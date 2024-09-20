import csv

def open_csv(file_obj, delimiter=","):
    reader = csv.reader(file_obj, delimiter=delimiter)
    return reader


def find_line_by_column(reader: csv.reader, column_index, search_term: str, case_insensitive: bool=False):
    for row in reader:
        if column_index < len(row):
            column_word = row[column_index]
        if case_insensitive:
            if (column_word.lower() == search_term.lower()):
                return row
        else:
            if (column_word == search_term):
                return row
    return None


with open('./sample data/Wizard.csv', mode='r', newline='') as file:
    test = open_csv(file, delimiter=';')
    print(find_line_by_column(test, 1, "light", case_insensitive=True))


