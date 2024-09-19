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
        
spell_list = ["Alarm (Ritual)", "Light", "Magic Missile", "Vampiric Touch"]

filename = 'Wizard.csv'
file_obj = open(filename, 'r', newline='')
reader = open_csv(file_obj)
# print(find_line_by_column(reader, 1, "Light"))
for spell in spell_list:
    print(find_line_by_column(reader, 1, spell))
file_obj.close()
