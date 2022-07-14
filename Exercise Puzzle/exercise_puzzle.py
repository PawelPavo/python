import shutil
import os
import re

# EXERCISE PUZZLE
shutil.unpack_archive('unzip_me_for_instructions.zip','instructions_unzipped','zip')
file_path="C:/Users/pjaskolski/Desktop/Python/Exercise Puzzle/instructions_unzipped/extracted_content"

phone_pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')

for folder, sub_folders, files in os.walk(file_path):
    for file in files:
        f=open((f'{folder}/{file}'))
        text=f.read()
        phone=re.search(phone_pattern,text)
        if phone == None:
            continue
        else:
            print(phone.group())
            print(f)
