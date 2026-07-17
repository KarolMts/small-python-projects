---
tags: [python, nauka, file-organizer, postep]
ostatnia_sesja: 2026-07-16
---

# Postęp nauki — File Organizer (projekt 1/10)

Notatka do wznowienia nauki. Kontekst: powrót do programowania po przerwie
(wcześniej JS i Haskell, bez frameworków). Cel: portfolio na GitHubie z 10 małymi
projektami z Pythona, potem większy projekt.

## Główna inspiracja

- **Tytuł:** 10 Python Projects That Made Me a Better Developer
- **Autor:** Babar Saad
- **Publikacja:** Python in Plain English (Medium), lip. 2025
- **Link:** https://python.plainenglish.io/10-python-projects-that-made-me-a-better-developer-real-world-use-cases-that-strengthen-your-0522ac483fae

Artykuł podaje 10 pomysłów na projekty (z krótkimi snippetami, nie gotowe programy).
Projekt 1 = "Smart File Organizer". Pozostałe do zrobienia po kolei.

## Zasady współpracy (ważne!)

Mistrz **prowadzi i naprowadza pytaniami, ale NIE pisze kodu za mnie**.
Ja piszę cały kod sam — to ma być w 100% moja praca. Mistrz tylko:
czyta mój plik (`organizer.py`), wskazuje błędy, zadaje pytania naprowadzające,
tłumaczy pojęcia. Kod poprawiam ja.

Workflow: piszę w VS Code → zapisuję (Ctrl+S) → piszę "sprawdź" → mistrz czyta
podłączony plik i naprowadza.

## Środowisko (gotowe)

- Repo GitHub: `small-python-projects` (użytkownik: KarolMts), gałąź `main`.
- Sklonowane lokalnie: `~/small-python-projects` (= `C:\Users\krlma\small-python-projects`).
- Projekt 1 w podfolderze `1-file-organizer` (pliki: `organizer.py`, `README.md`).
- Edytor: VS Code + terminal (Git Bash). Cykl Git: `git add .` → `git commit -m "..."` → `git push`.
- Folder testowy do bezpiecznych prób: `C:\Users\krlma\test_folder` (NIE testować na prawdziwym Downloads!).

## Co już DZIAŁA

Program grupuje pliki z folderu według rozszerzenia i przenosi je do podfolderów.

Kluczowe rozwiązania, do których sam doszedłem:
- Funkcja `get_category()` — zwraca rozszerzenie albo `.OTHERS` dla plików bez rozszerzenia.
  Sprytny trik: `.OTHERS` **z kropką**, żeby `category[1:]` obcinało kropkę jednakowo dla wszystkich.
- Foldery pomijam przez `if element.is_dir(): continue`.
- Architektura "najpierw grupuj (słownik), potem działaj (przenoś)" — omija pułapkę
  ponownego skanowania nowo utworzonych folderów.
- `d.setdefault(kategoria, []).append(...)` do grupowania.
- Tworzenie folderu: `target_dir.mkdir(exist_ok=True)`; przenoszenie: `path.rename(...)`.

## NA CZYM SKOŃCZYLIŚMY — następne kroki (w tej kolejności)

1. **Obsługa konfliktu nazw** (w trakcie — to następne zadanie):
   - Problem: przy drugim uruchomieniu `rename` wywala `FileExistsError`, gdy plik
     o tej nazwie już jest w folderze docelowym.
   - Do zrobienia: wykryć kolizję (metoda `.exists()`) i zareagować.
   - Strategia do wyboru: numerowanie (`raport_1.pdf`, `raport_2.pdf`...), pominięcie,
     albo nadpisanie. Do numerowania użyć `.stem` + `.suffix`, żeby numer wstawić
     PRZED rozszerzeniem.
   - Rada: wydzielić do osobnej funkcji `find_free_name(target_dir, filename)`.
   - Test: uruchomić program, potem znów wrzucić plik o istniejącej nazwie, uruchomić ponownie.

2. **argparse** — zamienić wpisaną na sztywno ścieżkę na argument z linii poleceń:
   `python organizer.py C:\sciezka\do\folderu`. To robi z tego prawdziwe narzędzie CLI.

## Pomysły na później (nie teraz)

- Ujednolicić wielkość liter rozszerzeń przez `.lower()` (żeby `.PNG` i `.png` szły do jednego folderu).
- Obsługa podfolderów (obecnie pomijane) — dopisać jako "znane ograniczenie" w README.
- Napisać porządny README projektu (opis, jak uruchomić, czego się nauczyłem).

## Ściąga

Osobny plik: `pathlib-Path-metody-i-atrybuty.md` (do Obsidiana).
