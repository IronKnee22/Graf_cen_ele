import os
import glob

folder_path = 'data/raw/'

files = glob.glob(os.path.join(folder_path, '*'))

for file in files:
    try:
        os.remove(file)
        print(f"Smazán soubor: {file}")
    except Exception as e:
        print(f"Chyba při mazání souboru {file}: {e}")
