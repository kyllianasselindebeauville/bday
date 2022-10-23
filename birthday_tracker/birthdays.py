import os

import pandas as pd


def get_default_filepath() -> str:
    return os.path.join(os.getenv('HOME'), '.birthday-tracker', 'birthdays.csv')


def get_filepath(file: str = None) -> str:
    if file is None:
        return get_default_filepath()

    return os.path.join(os.getenv('HOME'), '.birthday-tracker', file)


def get(file: str = None) -> pd.DataFrame:
    filepath = get_filepath(file)

    if os.path.exists(filepath):
        df = pd.read_csv(filepath, index_col='ID')
    else:
        df = pd.DataFrame(columns=['Name', 'Birthdate'])

    return df


def save(df: pd.DataFrame, file: str = None) -> None:
    filepath = get_filepath(file)
    directory, file = os.path.split(filepath)

    os.makedirs(directory, exist_ok=True)
    df.to_csv(filepath, index_label='ID')
