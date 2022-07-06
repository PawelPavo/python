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
