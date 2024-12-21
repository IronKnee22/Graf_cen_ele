import os
import glob

folder_path = 'data/raw/'

files = glob.glob(os.path.join(folder_path, '*'))

for file in files:
    try:
        os.remove(file)
        print(f"File deleted: {file}")
    except Exception as e:
        print(f"Error while deleting {file}: {e}")
