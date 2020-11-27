import csv


def read_csv_dict():
    file_path = "data/file.csv"

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def read_csv():

    file_path = "data/file.csv"

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

if __name__ == "__main__":
    read_csv_dict()

