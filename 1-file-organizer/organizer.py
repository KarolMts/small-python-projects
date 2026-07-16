from pathlib import Path


folder = Path(r'C:\Users\krlma\Downloads')
for  path in folder.iterdir():
    if path.is_file():
        print(path)
