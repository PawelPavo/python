import csv

# open file
data=open('/Users/paweljaskolski/Desktop/Code Classes/python/PDFs and Spreadsheets/example.csv', encoding='utf-8')
# csv.reader
csv_data=csv.reader(data)
# reformat it into a python object list of lists
data_lines=list(csv_data)

#print(data_lines) row from csv
print(len(data_lines))

for line in data_lines[:5]:
    print(line)

print(data_lines[10])

#print(data_lines) cell from csv
print(data_lines[10][3])

# print each coloum
all_emails=[]
for line in data_lines[1:15]: #start at line 1 because 0 are table headers
    all_emails.append(line[3]) # append the desired column value - email is in colum 3

print(all_emails)

# combining two cells together
full_names=[]

for line in data_lines[1:15]:
    full_names.append(line[1]+' '+line[2])

print(full_names)