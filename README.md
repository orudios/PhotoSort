# PhotoSort
PhotoSort is a simple Python script that sorts the picture and video contents of a directory into appropriate sub-directories based on file extensions, such as ```.arw```, ```.mov```, ```.jpg```. PhotoSorter supports most commonly used photo and video file extensions.

The inspiration behind this script came from having tons of unsorted pictures and videos that I took with my camera and wanting to automate the process.

## Installation
No installation of external dependencies required, script uses Python3.8 and built-in libraries.

## Usage
Currently, the script works by placing it into a main directory with all files to be sorted.

```bash
python photo_sort.py
```

## Future Work
* Add command-line arguments to accept custom directories (i.e not the one the script is located in)
* Add an ability for the script to scan sub-directories for files to sort
* Add custom sorting filters, e.g. date/name

## Contributing
Contributions, issues, and feature requests are welcome!

## License
[MIT](https://choosealicense.com/licenses/mit/)
