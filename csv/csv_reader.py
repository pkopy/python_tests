import csv

def csv_reader(file_object):
    '''
    Read a CSV file using csv.DictReader
    '''

    reader = csv.DictReader(file_object, delimiter=',')
    for line in reader:
        print(line["first_name"]),
        print(line["last_name"])

if __name__ == "__main__":
    with open("data.csv") as f_obj:
        csv_reader(f_obj)