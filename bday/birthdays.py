from datetime import date
import os

import pandas as pd


def _get_default_directory() -> str:
    return os.path.join(os.getenv('HOME'), '.bday')


def _get_default_filepath() -> str:
    return os.path.join(_get_default_directory(), 'birthdays.csv')


def _get_filepath(file: str = None) -> str:
    if file is None:
        return _get_default_filepath()

    return os.path.join(_get_default_directory(), file)


def _next_birthday(birthday: pd._libs.tslibs.timestamps.Timestamp) -> date:
    today = date.today()
    birthday_of_the_year = date(today.year, birthday.month, birthday.day)
    next_birthday_year = today.year + int(birthday_of_the_year < today)

    return date(next_birthday_year, birthday.month, birthday.day)


def get(file: str = None) -> pd.DataFrame:
    filepath = _get_filepath(file)

    if os.path.exists(filepath):
        df = pd.read_csv(filepath, index_col='ID', parse_dates=['Birthdate'])
    else:
        df = pd.DataFrame(columns=['Name', 'Birthdate'])

    return df


def save(df: pd.DataFrame, file: str = None) -> None:
    filepath = _get_filepath(file)
    directory, file = os.path.split(filepath)

    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    os.makedirs(directory, exist_ok=True)
    df.to_csv(filepath, index_label='ID')


def add(df: pd.DataFrame, name: str, birthdate: str) -> pd.DataFrame:
    to_add = pd.DataFrame({
        'Name': [name],
        'Birthdate': [pd.to_datetime(birthdate,
                                     errors='coerce',
                                     dayfirst=True)]
    })

    return pd.concat([df, to_add], ignore_index=True)


def remove(df: pd.DataFrame, id: int) -> pd.DataFrame:
    return df.drop(index=id, errors='ignore')
