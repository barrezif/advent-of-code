#!/bin/sh

echo "Creating files for day $2"

DIR_NAME="./$1/$2/"
INPUT_FILE="input.txt"
PYTHON_FILE="script.py"

mkdir -p $DIR_NAME/
wget -O "$DIR_NAME/$INPUT_FILE" --no-cookies --header "Cookie: session=$3" https://adventofcode.com/$1/day/$2/input


cat > $DIR_NAME/$PYTHON_FILE << EOF
from collections import defaultdict, Counter
from enum import Enum

class InputGroup(Enum):
    COMMA = 1
    COMMA_INT = 2
    LINE = 3
    LINE_SPLIT_BY = 4
    LINE_INT = 5
    BLOCK = 6


def get_puzzle_input(groupType, splitter=None):
    file = open('input.txt')

    if groupType == InputGroup.COMMA:
        print("COMMA")
        puzzle_input = [line for line in file.read().split(',')]

    elif groupType == InputGroup.COMMA:
        print("COMMA_INT")
        puzzle_input = [int(line) for line in file.read().split(',')]
    
    elif groupType == InputGroup.BLOCK:
        print("BLOCK")
        puzzle_input = [line.strip() for line in file.read().split('\n\n')]
    
    elif groupType == InputGroup.LINE:
        print("LINE")
        puzzle_input = [line.strip() for line in file.readlines()]

    elif groupType == InputGroup.LINE_INT:
        print("LINE_INT")
        puzzle_input = [int(line) for line in file.readlines()]
    
    else:
        print("LINE_SPLIT_BY")
        puzzle_input = [line.strip().split(splitter) for line in file.readlines()]

    return puzzle_input

def part1():
    # LINE, LINE_INT, COMMA, COMMA_INT, BLOCK, LINE_SPLIT_BY
    pInput = get_puzzle_input(InputGroup.)
    print(pInput, end="\n\n\n")


    res = []

    return res


def main():
    print("           ", part1())
    print("PART 1 ^^^^^^^^^^^^^^^^^^")

if __name__ == '__main__':
    main()


EOF


cd $DIR_NAME
code -a . ./$PYTHON_FILE

