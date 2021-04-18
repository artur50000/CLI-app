from functools import lru_cache
import collections
import argparse


@lru_cache(maxsize=128)
def unique_letters(string_to_check):

    num_of_chars = 0
    collect = collections.Counter(string_to_check)

    for item in collect.values():
        if item == 1:
            num_of_chars += 1

    return num_of_chars


def main_parse(test_list):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--string",
        help="counts the number of unique characters",
        type=str)
    parser.add_argument(
        "--file",
        help="counts the number of unique characters",
        type=str)
    args = parser.parse_args(test_list)

    if args.file:
        with open(args.file, "r") as f:
            return (unique_letters(f.readline()))
    elif args.string:
        return (unique_letters(args.string))
