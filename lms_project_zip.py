import shutil

# Path ke folder proyek
project_folder = '/mnt/data/LMS_Project'
# Path untuk menyimpan file ZIP
zip_file_path = '/mnt/data/LMS_Project.zip'

# Membuat file ZIP
shutil.make_archive(base_name=zip_file_path.replace('.zip',''), format='zip', root_dir=project_folder)

zip_file_path
