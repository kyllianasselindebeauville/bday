import argparse

from bday import birthdays
from bday.version import __version__


def parse_args():
    """Parses arguments from the command-line.

    Creates a parser, adds arguments to the parser, parses those arguments.

    Returns:
        An argparse.Namespace object containing the arguments as attributes.
    """
    parser = argparse.ArgumentParser(prog='bday',
                                     description='Track your birthdays.')

    parser.add_argument('-V', '--version', action='version',
                        version=f'%(prog)s {__version__}')

    subparsers = parser.add_subparsers(title='commands')

    parser.set_defaults(func=today)

    parser_add = subparsers.add_parser('add', help='add a birthday')
    parser_add.add_argument('name', type=str, help='name of the person')
    parser_add.add_argument('date', type=str, help='date of birth (dd-mm-yyyy)')
    parser_add.set_defaults(func=add)

    parser_rm = subparsers.add_parser('rm', help='remove a birthday')
    parser_rm.add_argument('id', type=int, help='id to remove')
    parser_rm.set_defaults(func=rm)

    parser_ls = subparsers.add_parser('ls', help='list birthdays')
    parser_ls.add_argument('-a', '--alphabetically',
                           action='store_const', const='alphabetically',
                           default='chronologically',
                           help='list alphabetically',
                           dest='order')
    parser_ls.add_argument('-c', '--chronologically',
                           action='store_const', const='chronologically',
                           help='list chronologically',
                           dest='order')
    parser_ls.set_defaults(func=ls)

    args = parser.parse_args()
    return args


def add(args: argparse.Namespace) -> None:
    df = birthdays.get()
    df = birthdays.add(df, name=args.name, birthdate=args.date)
    birthdays.save(df)


def rm(args: argparse.Namespace) -> None:
    df = birthdays.get()
    df = birthdays.remove(df, id=args.id)
    birthdays.save(df)


def ls(args: argparse.Namespace) -> None:
    df = birthdays.get()
    birthdays.list_(df, how=args.order)
    birthdays.save(df)


def today(args: argparse.Namespace) -> None:
    df = birthdays.get()
    birthdays.list_(birthdays.today(df))
    birthdays.save(df)
