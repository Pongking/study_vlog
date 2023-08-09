# name.py
import argparse
import sys
from name_function import get_formatted_name


def parse(args):
    parser=argparse.ArgumentParser(
        description="input your name,it must contains firstname and lastname",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--first_name",type=str)
    parser.add_argument("--last_name",type=str)
    all_args=parser.parse_known_args(args)[0]
    return all_args

def main():
    all_args=parse(sys.argv[1:])
    formatted_name=get_formatted_name(all_args.first_name,all_args.last_name)
    print(f"\n Neaty formatted name:{formatted_name}")

if __name__ == '__main__':
    main()