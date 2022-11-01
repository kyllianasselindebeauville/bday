import argparse
import inspect

from bday import birthdays


def add(args):
    print(f'{inspect.stack()[0][3]} <- {args}')
    df = birthdays.get()
    df = birthdays.add(df, name=args.name, birthdate=args.date)
    birthdays.save(df)


def rm(args):
    print(f'{inspect.stack()[0][3]} <- {args}')
    df = birthdays.get()
    df = birthdays.remove(df, id=args.id)
    birthdays.save(df)


def ls(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def today(args):
    print(f'{inspect.stack()[0][3]} <- {args}')
    df = birthdays.get()
    birthdays.list_(birthdays.today(df))
    birthdays.save(df)


def parse_args():
    parser = argparse.ArgumentParser(prog='bday',
                                     description='Track your birthdays.')

    subparsers = parser.add_subparsers(title='commands')

    # Default function
    parser.set_defaults(func=today)

    parser_add = subparsers.add_parser('add', help='add a birthday')
    parser_add.add_argument('name', type=str, help='name of the person')
    parser_add.add_argument('date', type=str, help='date of birth (dd-mm-yyyy)')
    parser_add.set_defaults(func=add)

    # Parser for the rm command
    parser_rm = subparsers.add_parser('rm', help='remove a birthday')
    parser_rm.add_argument('id', type=int, help='id to remove')
    parser_rm.set_defaults(func=rm)

    # Parser for the ls command
    parser_ls = subparsers.add_parser('ls')
    parser_ls.set_defaults(func=ls)

    args = parser.parse_args()
    return args
