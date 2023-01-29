# webm Converter

to use it:
- make sure python>=3.8 is installed 
- add the gifs in a folder at the root of this project
- in the project root run `python -m venv venv`
- run `"venv/Scripts/activate"`
- run `pip install -r requirements.txt`
- run `python webm_convert.py --input <input folder path> --output <output folder path>`

```
usage: python webm_convert.py [-h] [--input INPUT] [--output OUTPUT] [--rem]

options:
  -h, --help       show this help message and exit
  --input INPUT    The root input directory for gifs to be converted (defaults to 'skins')
  --output OUTPUT  The root output directory for webm videos to be saved (defaults to 'webm')
  --rem            delete converted gifs (considered False if not given)
```