import csv

with open('testoutput.TXT', 'w') as f:
    with open('datafiles/btinput.txt', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if row != [] and row[0] != '':
                if row[0][0] == 'r' or row[0][0] == 'K':
                    f.write('\n')
                if len(row[1:-1]) > 2:
                    f.write("+" + "\t+".join(row[1:-1]) + '\n')

    f.write('\n')
    f.write('')
    f.close()
