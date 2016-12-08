import csv
import sys


def multiscan(reader, f):
    next(reader)
    next(reader)
    for row in reader:
        if row != [] and row[0] != '':
            if row[0][0] == ' ' or row[0][0] == 'R':
                f.write('\n')
                f.write('\n')
            elif row[0][0] == 'K':
                break
            elif len(row[1:-1]) > 2:
                f.write("+" + "\t+".join(row[1:]) + '\n')
    f.write('\n')
    f.write('\n')
    f.close()


def biotek(reader, f):
    for row in reader:
        if row != [] and row[0] != '':
            if row[0][0] == 'r' or row[0][0] == 'K':
                f.write('\n')
            if len(row[1:-1]) > 2:
                f.write("+" + "\t+".join(row[1:-1]) + '\n')

    f.write('\n')
    f.write('')
    f.close()

if len(sys.argv) != 3:
    print("Usage: python pyextract.py <inputfile> <outputfile>")
else:
    with open(sys.argv[2], 'w') as f:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
            row1 = next(reader)
            if row1[0][0] == 'P':
                multiscan(reader, f)
            else:
                biotek(reader, f)
