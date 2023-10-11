# Zip Bruteforcer

Create a python cli app, that can bruteforce a password protected zip-file with a dictionary, an optional verbose flag can be activated to print every password tried.

The app should be called like this :

`python3 zip_bruteforce.py -f <zip_file_path> -w <passwords_path> -v`

`python3 zip_bruteforce.py --file <zip_file_path> --words <passwords_path> --verbose`

- v1 : only use `sys.argv`
- v2 : use argparse
- v3 : use click
