from pathlib import Path

def get_category(path):
    if path.suffix != '':
        return path.suffix
    return '.OTHERS'


folder = Path(r'C:\Users\krlma\test_folder')

d = {}
for  element in folder.iterdir():
    if element.is_dir():
        continue
    d.setdefault(get_category(element), []).append(Path(element))
    
for category, files in d.items():
    target_dir = folder / category[1:]
    target_dir.mkdir(exist_ok=True)
    for path in files:
        path.rename(target_dir / path.name) 