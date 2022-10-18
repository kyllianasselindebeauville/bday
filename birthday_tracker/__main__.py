import argparse


def main():
    parser = argparse.ArgumentParser(prog='bday',
                                     description='Track your birthdays.')

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
