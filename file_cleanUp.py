import sys
import os

filename = sys.argv[1]
new_file = os.path.join('cleaned_csv_file', filename)

with open(filename, 'r') as fp, open(new_file, 'w') as cf:
    next(fp)
    for line in fp:
        clean_line = line[:-2]
        segs = clean_line.split(";")
        cf.write(','.join(segs) + '\n')

print('Done!')