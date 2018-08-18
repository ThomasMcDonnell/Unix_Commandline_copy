import argparse 
import os 
from pathlib import Path

parser = argparse.ArgumentParser(description='Rough implementation of the unix\
                                 command (FIND) in python')
parser.add_argument('path', metavar='P', type=str, nargs=1, default=os.getcwd())
parser.add_argument('-n', '--name', type=str, nargs=1, help='Find file match.')
parser.add_argument('-m', '--match', type=str, nargs=1, help='Find all\
                    files for the given pattern.')
parser.add_argument('-f', '--files', action='store_true', help='Find all files\
                    for the given path.')
parser.add_argument('-d', '--dirs', action='store_true', help='Find all\
                    directories for the given path.')
args = parser.parse_args()

# return all files in the directory (only for given path) 
def find_all_files(path):
    files = []
    for entry in os.scandir(path):
        if entry.is_file():
            files.append(entry.name)
    print(files)

# return all directories (only for given path)
def find_all_dirs(path):
    dirs = []
    for entry in os.scandir(path):
        if entry.is_dir():
            dirs.append(entry.path)
    print(dirs)

# recursive find
def find_file(path, _file):
    for f in Path(path).rglob(_file):
        print(f)

# recursive pattern match 
def match(path, pattern):
    for f in Path(path).rglob('*' + pattern):
        print(f)

if __name__ == "__main__":
    if args.files:
        find_all_files(args.path[0])
    elif args.dirs:
        find_all_dirs(args.path[0])
    elif args.name:
        find_file(args.path[0], args.name[0])
    elif args.match:
        match(args.path[0], args.match[0])
