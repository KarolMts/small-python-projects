from pathlib import Path

def get_category(path):
    if path.suffix != '':
        return path.suffix
    return 'inne'


folder = Path(r'C:\Users\krlma\Downloads')

d = {}
for  element in folder.iterdir():
    if element.is_dir():
        continue
    d.setdefault(get_category(element), []).append(element.name)
    
print(d)