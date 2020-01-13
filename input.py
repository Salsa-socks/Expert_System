import sys

def readfile():
    args = len(sys.argv) - 1

    if args < 1:
        print('No file given')
        exit()

    if args > 1:
        print('Too many arguments given')
        exit()

    in_put = sys.argv[1]

    if not in_put.endswith('.txt'):
        print('Wrong file type')
        exit()
    else:
        print(in_put)
        f = open(in_put, "r")
        print(f.read())