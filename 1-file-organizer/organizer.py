from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder")
args = parser.parse_args()
folder = Path(args.folder)

# funkcja tworząca klucze slownika
def get_category(path):
    # jesli jest rozszerzenie to je zwraca w lowercase
    if path.suffix != '':
        return path.suffix.lower()  
    # a jesli nie ma rozszerzenia to zwroci nazwe folderu do przechowania takich plików
    return '.NO_EXTENSION'

def get_free_name(location, path):
    new = location / path.name
    i =1
    while new.exists():
        new = location / (path.stem + f"_{i}" + path.suffix) 
        i += 1
    return new

# tworzymy obiekt Path folderu ktory chcemy uporzadkowac
# folder = Path(r'C:\Users\krlma\test_folder')


dirs = {}   # str(ext) -> [file.ext]
for  element in folder.iterdir():
    if element.is_dir():
        continue
    dirs.setdefault(get_category(element), []).append(Path(element))
    
for category, files in dirs.items():
    target_dir = folder / category[1:]
    target_dir.mkdir(exist_ok=True)
    for path in files:
        path.rename(get_free_name(target_dir, path)) 