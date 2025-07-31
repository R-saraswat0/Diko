# Diko

Diko is an interactive dictionary web application that allows users to search for word definitions, pronunciations, and suggestions. It uses a Trie data structure for efficient word lookup, edit distance algorithms for close word suggestions, and fetches definitions from an external dictionary API.

## Features

- Fast word lookup using Trie data structure.
- Suggestions for misspelled or partial words.
- Fetches detailed word definitions, pronunciations, and examples.
- Interactive web UI built with Flask.
- Search history with toggle visibility.
- Audio pronunciation playback.
##Some screenshots
<img width="1890" height="892" alt="Image" src="https://github.com/user-attachments/assets/049c4340-e0d2-4bac-94a4-253393122f86" />

## Installation

1. Clone the repository:

```bash
git clone https://github.com/R-saraswat0/Diko.git
cd Diko
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r gui_app/requirements.txt
```

## Usage

1. Run the Flask web app:

```bash
python gui_app/app.py
```

2. Open your browser and navigate to:

```
http://127.0.0.1:5000
```

3. Enter a word in the search box and click "Search" to get definitions and pronunciations.

4. Use the "History" button to toggle search history visibility.

## Project Structure

- `app/` - CLI version of the dictionary app.
- `corrections/` - Edit distance and suggestion algorithms.
- `data/` - Word list file.
- `gui_app/` - Flask web app, templates, and static files.
- `scraper/` - Fetches word definitions from external API.
- `trie/` - Trie data structure implementation.
- `tests/` - Automated test scripts.

## License

This project is licensed under the MIT License.
