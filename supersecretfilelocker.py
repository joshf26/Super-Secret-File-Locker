#!/usr/bin/env python3

from lib.inputparser import parse_input
from lib.filelocker import lock_file


def main():
    filename, pin, long = parse_input()
    lock_file(filename, pin, long)


if __name__ == '__main__':
    main()
