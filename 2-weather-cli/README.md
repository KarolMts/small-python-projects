# Weather CLI

A command-line tool that reports the current temperature for any city, using the
free [Open-Meteo](https://open-meteo.com/) API (no API key required).

## How it works

The tool chains two API calls:

1. **Geocoding** — converts the city name into coordinates (latitude/longitude).
2. **Forecast** — fetches the current weather for those coordinates.

## Features

- **Any city by name** — `python weather.py "New York"` (spaces are handled automatically).
- **Clean output** — e.g. `The temperature in Warsaw is 15.3 °C.`
- **Uses the API's canonical city name** rather than the raw user input.
- **Robust error handling:**
  - unknown city → friendly message,
  - bad HTTP status (404, 500, …) → reports the status code,
  - server unreachable (no network / timeout) → friendly message.
- **No API key needed** — Open-Meteo is free and keyless.

## Setup

```
python -m venv venv
source venv/Scripts/activate      # Windows (Git Bash); on Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
python weather.py <city>
```

### Examples

```
python weather.py Warsaw
python weather.py "Los Angeles"
```

## Requirements

- Python 3.x
- [`requests`](https://pypi.org/project/requests/) (see `requirements.txt`)

## Known limitations

- Reports temperature only (no wind, humidity, or forecast yet).
- Picks the first geocoding match, so ambiguous city names may resolve to a
  different place than intended.

## Inspiration

Inspired by project #3 from Babar Saad's article
["10 Python Projects That Made Me a Better Developer"](https://python.plainenglish.io/10-python-projects-that-made-me-a-better-developer-real-world-use-cases-that-strengthen-your-0522ac483fae),
reworked as a pure API-practice CLI. The implementation is my own.
