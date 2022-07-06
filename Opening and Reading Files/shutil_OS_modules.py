import os
import shutil

# This created a file on a directory where the script is located or
# give it a path to where you want the file to be
'''
f = open('practice.txt','w+')
f.write('This is a test string')
f.close()
'''

# List files in a given directory
'''
print(os.getcwd())
print(os.listdir())
print(os.listdir('C:/Users/pjaskolski/Desktop'))
'''

# move file to a diffrent location
'''
shutil.move('practice.txt','C:/Users/pjaskolski/Desktop')
'''
# Move back the file
'''
shutil.move('C:/Users/pjaskolski/Desktop/practice.txt','practice.txt')
'''

# Deleting a file
# Check docs for 3 diffrent methods of deleting
# ALTERNATIVELY use 'pip install send2trash'
'''
send2trash.send2trash('practice.txt')
'''

file_path='C:/Users/pjaskolski/Desktop/Python/Opening and Reading Files/Example_Top_Level'
for folder, sub_folders, files in os.walk(file_path):
    print(f'Currentlty lookig at {folder}')
    print('\n')
    print(f'The subfolders are: ')
    for sub_fold in sub_folders:
        print(f'\t Subfolders: {sub_fold}')
    print('\n')
    print(f'The files are: ')
    for f in files:
        print(f'\t Files: {f}')
    print('\n')
