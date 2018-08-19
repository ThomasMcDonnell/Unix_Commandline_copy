import argparse
import os 
import re

parser = argparse.ArgumentParser(description='Rough implementation of unix\
                                 command (GREP) in python')
parser.add_argument('file', metavar='F', type=str, nargs=1)
parser.add_argument('-w', '--word', type=str, nargs=1, help='Find all\
                    instances of given word in file.')
args = parser.parse_args()

# colors for termional output
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# simple find implementation 
def find_string(_file, string):
    with open(_file) as f:
        for line in f.readlines():
            index = 0
            while index < len(line):
                index = line.find(string, index)
                if index == -1:
                    break
                print(bcolors.OKBLUE + f"\t{line}" + bcolors.ENDC, end="")
                index += len(string)

# regex text search 
def match_string(_file, string):
    pass

if __name__ == "__main__":

