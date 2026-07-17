from pathlib import Path
import argparse




def get_category(path):
    """Return the file's extension in lowercase, or a bucket name for extensionless files."""
    if path.suffix != '':
        return path.suffix.lower()  # so .pdf and .PDF land in the same folder
    return '.NO_EXTENSION'         # bucket for files without an extension



def get_free_name(location, path):
    """Return a free path in the folder, appending _1, _2, ... if the name is taken."""
    new = location / path.name
    i = 1
    while new.exists():
        new = location / (path.stem + f"_{i}" + path.suffix) 
        i += 1
    return new


def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    args = parser.parse_args()
    folder = Path(args.folder)
    
    # mapping: extension (str) -> list of file paths
    dirs = {}   
    for  element in folder.iterdir():
        if element.is_dir():
            continue
        dirs.setdefault(get_category(element), []).append(Path(element))
    
    for category, files in dirs.items():
        target_dir = folder / category[1:]
        target_dir.mkdir(exist_ok=True)
        for path in files:
            path.rename(get_free_name(target_dir, path)) 
            
            
if __name__ == "__main__":
    main()