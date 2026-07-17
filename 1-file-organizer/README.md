# File Organizer

A command-line tool that tidies up a folder by sorting its files into
subfolders based on their extension.

## Features

- **Groups files by extension** — each file is moved into a matching subfolder
  (e.g. `report.pdf` → `pdf/`).
- **Case-insensitive** — `photo.PNG` and `image.png` both land in `png/`.
- **Handles extensionless files** — files without an extension go into a
  dedicated `NO_EXTENSION/` folder.
- **Never overwrites** — if a file of the same name already exists in the target
  folder, a number is appended (`report.pdf` → `report_1.pdf`, `report_2.pdf`, …).
- **Leaves subfolders alone** — only top-level files are organized.
- **Zero dependencies** — uses only the Python standard library.

## Usage

```
python organizer.py <path_to_folder>
```

### Example

```
python organizer.py C:\Users\me\Downloads
```

Given a folder containing `report.pdf`, `photo.PNG`, `notes.txt` and `README`,
the tool produces:

```
Downloads/
├── pdf/
│   └── report.pdf
├── png/
│   └── photo.PNG
├── txt/
│   └── notes.txt
└── NO_EXTENSION/
    └── README
```

## Requirements

- Python 3.x
- No third-party packages required.

## Known limitations

- Does not recurse into subfolders — only top-level files are organized.
- No dry-run / preview mode yet — files are moved immediately.

## Inspiration

Project #1 from Babar Saad's article
["10 Python Projects That Made Me a Better Developer"](https://python.plainenglish.io/10-python-projects-that-made-me-a-better-developer-real-world-use-cases-that-strengthen-your-0522ac483fae).
The implementation is my own.
