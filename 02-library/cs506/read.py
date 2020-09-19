import csv

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    data = []
    with open(csv_file_path) as csvfile:
        csv_reader = csv.reader(csvfile)
        for line in csv_reader:
            data.append(line)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                data[i][j] = int(data[i][j])
    return data
