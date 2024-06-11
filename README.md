# ImageSorter

This GUI app allows you to select a source and a target directory when you start it.
After that, all JPEG and PNG images from the source directory will be displayed and you can click on yes or no to determine if the displayed image should be moved to the target directory. There are also keyboard shortcuts (y & n).

## Project install
```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

```
pip3 install -r requirements.txt
```

## Running the app

Run the python src directly:

```
python3 main.py
```

Or build the app for MacOS:

```
./build.sh
```

Now you have a `ImageSorter.app` in the dist directory which you can install and use on MacOS.
