# ZIPPING AND UNZIPPING FILES
import zipfile

# Creating two files
f=open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f=open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

# ZIPPING FILES
# Creating a zip file
comp_file=zipfile.ZipFile('comp_file.zip','w')

# Write to the zip file
comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)

# close the zip file
comp_file.close()


# UNZIPPING FILES

# Choosig the zip file to extract
zip_obj=zipfile.ZipFile('comp_file.zip','r')

# Extarcting the content to a folder 'extracted_content' in the same directory
# You can extract individual files as well
zip_obj.extractall('extracted_content')
