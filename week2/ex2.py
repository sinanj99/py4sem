import csv
from sys import argv
import argparse


def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))
            if reader.line_num > 100:
                break


def write_list_to_file(thelist, file):
    with open(file, 'w+') as f:
        for element in thelist:
            f.write(element + "\n")
    print_file_content(file)


def write_list_to_file2(file, *strings):
    with open(file, 'w+') as f:
        for element in strings:
            f.write(element + "\n")
    print_file_content(file)


def read_csv(input_file):
    mylist = []
    with open(input_file) as f:
        reader = csv.reader(f)
        for row in reader:
            mylist.append(str(row))
            if reader.line_num > 3:
                break
    print(len(mylist))


def print_file_content_cli():
    parser = argparse.ArgumentParser(description='Print file content')
    parser.add_argument('path')
    parser.add_argument('file_name', nargs='?')
    args = parser.parse_args()
    with open(args.path) as f:
        reader = csv.reader(f)
        if args.file_name:
            with open(args.file_name, 'w') as fw:
                for row in reader:
                    fw.write(str(row))
        else:
            for row in reader:
                print(row)


# print_file_content(
#     './annual-enterprise-survey-2018-financial-year-provisional-csv.csv')

# write_list_to_file2(
#     'file.txt',
#     'a',
#     'b',
# )

# read_csv('./annual-enterprise-survey-2018-financial-year-provisional-csv.csv')

# print_file_content_cli()
