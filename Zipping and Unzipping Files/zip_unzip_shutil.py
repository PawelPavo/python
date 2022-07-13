import shutil

# Zipping the entire file - "extracted_content"
dir_to_zip='C:/Users/pjaskolski/Desktop/Python/Zipping and Unzipping Files/extracted_content'

output_filename='zipped_folder_with_shutil_example'

shutil.make_archive(output_filename,'zip',dir_to_zip)


# extracting
shutil.unpack_archive('zipped_folder_with_shutil_example.zip','unzipped_with_shutil_final_unzip','zip')
