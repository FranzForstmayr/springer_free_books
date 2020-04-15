## Python script to download all Springer books released for free during the 2020 COVID-19 quarantine and open Access in general

### Usage

Call the main script with a link to a csv file provided by Springer search results. Copy the link address from the "Download search results (CSV)" button or download the file and provide a path to the file as first argument. Select at least one of `--pdf` or `--epub` as format for downloading.

### Usage in a virtual environment:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python3 main.py <link> [--epub] [--pdf]
```

### On Windows:

```
python -m venv .venv
cd .venv/Scripts
activate.bat
cd ../..
pip install -r requirements.txt
python main.py <link> [--epub] [--pdf]
```

Thanks Springer!