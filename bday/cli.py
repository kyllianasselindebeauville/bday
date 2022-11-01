import argparse
import inspect


def add(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def rm(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def ls(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def today(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def parse_args():
    parser = argparse.ArgumentParser(prog='bday',
                                     description='Track your birthdays.')

    subparsers = parser.add_subparsers(title='commands')

    # Default function
    parser.set_defaults(func=today)

    # Parser for the add command
    parser_add = subparsers.add_parser('add')
    parser_add.set_defaults(func=add)

    # Parser for the rm command
    parser_rm = subparsers.add_parser('rm')
    parser_rm.set_defaults(func=rm)

    # Parser for the ls command
    parser_ls = subparsers.add_parser('ls')
    parser_ls.set_defaults(func=ls)

    args = parser.parse_args()
    return args
