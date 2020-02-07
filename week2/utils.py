from os import listdir, walk
from os.path import isfile, join
from sys import argv


def inout(folder, file_out):
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    print(onlyfiles)
    with open(file_out, 'w') as fout:
        for f in onlyfiles:
            fout.write(f)


def inout2(folder):
    allfiles = []
    for entry in walk(folder):
        for f in entry[2]:
            allfiles.append(f)
    print(allfiles)


def firstline(*files):
    for f in files:
        with open(f) as f_obj:
            print(f_obj.readlines()[0].rstrip())


def email(*files):
    for f in files:
        with open(f) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                if '@' in line:
                    print(line.rstrip())


def md(mdfiles):
    for f in mdfiles:
        with open(f) as f_obj:
            lines = f_obj.readlines()
            for line in lines:
                if '#' in line:
                    print(line.rstrip())


# inout('folder', 'file_out3.txt')
# inout2('folder', 'file_out4.txt')
# firstline('file_out2.txt', 'file_out3.txt')
if __name__ == '__main__':
    md(argv[1:])
