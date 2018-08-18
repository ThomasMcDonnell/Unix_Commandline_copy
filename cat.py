import argparse 

parser = argparse.ArgumentParser(description='Rough implementation of the unix\
                                 command (CAT) in python.')
parser.add_argument('files', metavar='F', type=str, nargs='+')
parser.add_argument('-n', '--numbers', action='store_true',
                    help='format with line numbers.') 
parser.add_argument('-w', '--write', action='store_true', 
                    help='write one file to a new file')
args = parser.parse_args()

def parsed_args(args):
    print(">>> parsed args:\n", '<<', args, '>>')

# display files, if more than one concatinate both and display 
def display_file(args):
    for file_name in args.files:
        with open(file_name) as f:
            print(f.read())

# display files with formated numbered lines
def display_formated_file(args):
    for file_name in args.files:
        with open(file_name) as f:
            line_num = 1
            for line in f.readlines():
                print(f"\t{line_num}\t{line}", end="")
                line_num += 1

# write one file to another
def write_file(args):
    lenght = len(args.files)-1
    file_out = args.files[lenght]
    for file_name in args.files[:lenght]:
        with open(file_name) as f:
            with open(file_out, 'w+') as f_out:
                for line in f:
                    f_out.write(line)


if __name__ == "__main__":
    parsed_args(args)
    if args.numbers:
        display_formated_file(args)
    elif args.write:
        write_file(args)
        print('<< contents have been copied over >>')
    else:
        display_file(args)
