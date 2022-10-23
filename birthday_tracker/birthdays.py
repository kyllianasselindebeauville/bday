import os


def get_default_filepath() -> str:
    return os.path.join(os.getenv('HOME'), '.birthday-tracker', 'birthdays.csv')


def get_filepath(file: str = None) -> str:
    if file is None:
        return get_default_filepath()

    return os.path.join(os.getenv('HOME'), '.birthday-tracker', file)
