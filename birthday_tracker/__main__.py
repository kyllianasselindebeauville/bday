import argparse
import inspect


def spam(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def ham(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def eggs(args):
    print(f'{inspect.stack()[0][3]} <- {args}')


def main():
    parser = argparse.ArgumentParser(prog='bday',
                                     description='Track your birthdays.')

    subparsers = parser.add_subparsers(title='commands')

    # Default function
    parser.set_defaults(func=spam)

    # Parser for the spam command
    parser_spam = subparsers.add_parser('spam')
    parser_spam.set_defaults(func=spam)

    # Parser for the ham command
    parser_ham = subparsers.add_parser('ham')
    parser_ham.set_defaults(func=ham)

    # Parser for the eggs command
    parser_eggs = subparsers.add_parser('eggs')
    parser_eggs.set_defaults(func=eggs)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()
