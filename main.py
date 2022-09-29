# Tyler Wormald
# Comp390-001, Individual Programming Assignment 1
# due 10/01/22

import sys


# Initialize global indexes for important data
NAME_INDEX = 0
MASS_INDEX = 4
YEAR_INDEX = 6


# Parses each line of data, typecasting as needed.
# @param file, @return list of tuples
def parse(file):
    data_list = []
    while True:
        line = file.readline()

        # break case at end of file
        if line == '':
            return data_list

        # parse and typecast values that need to be compared, set -1 for unknown or missing information
        line = line.split('\t')
        try:
            line[MASS_INDEX] = float(line[MASS_INDEX])
        except ValueError:
            line[MASS_INDEX] = -1
        try:
            line[YEAR_INDEX] = int(line[YEAR_INDEX])
        except ValueError:
            line[YEAR_INDEX] = -1

        data_list.append(tuple(line))


# Initialize data collection from files, removes the first informatory line
# @param filename.txt, @return list
def init(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"FileNotFoundError: No such file or directory: '{filename}'")
        exit(1)
    else:
        file.readline()  # removes first line
        return parse(file)


# Format and print a table of meteorites with value at index greater than the cutoff value
# @param datalist of meteorite data, index to compare, table label :P, lower_bound and upper_bound cutoff points
def table(datalist, index, label, lower_bound):
    name_label = "NAME:"
    print(f"{name_label:<24}{label}:")
    print('=' * 44)
    for meteorite in datalist:
        if meteorite[index] > lower_bound:
            print(f"{meteorite[NAME_INDEX]:<24}{meteorite[index]}")


# Begin program, searching for command argument referencing a filename
if __name__ == '__main__':
    try:
        data = init(sys.argv[1])
    except IndexError:
        print("IndexError: Expected argument 'filename.txt', got None")
        exit(1)
    else:
        table(data, MASS_INDEX, "MASS (g)", 2900000)
        print()
        table(data, YEAR_INDEX, "YEAR", 2012)
