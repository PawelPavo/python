import csv

# REMINDWE - THIS WILL OVERWRITE THE EXISITING FILE WITH THE SAME NAME - USE MODE to change!
file_to_output=open('/Users/paweljaskolski/Desktop/Code Classes/python/PDFs and Spreadsheets/to_save_file_2.csv',mode='w', newline='')

csv_writer=csv.writer(file_to_output,delimiter=',') # delimiter denotes what separates one column from the other (it can be whatever we want can be ';')

csv_writer.writerow(['a','b','c'])

csv_writer.writerows([['1','2','3'],['x','y','z'],['4','5','6']])

file_to_output.close()

# ADDING TO THE FILE WITHOUT OVERWRITING IT
f=open('/Users/paweljaskolski/Desktop/Code Classes/python/PDFs and Spreadsheets/to_save_file_2.csv',mode='a', newline='')
csv_writer=csv.writer(f)
csv_writer.writerow(['p','a','w'])
f.close()