import csv

fields = []
rows = []
with open('openrecipes.csv','r')as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Total no. of Rows: %d"%(csvreader.line_num))
print('Field names are:'+', '.join(field for field in fields))