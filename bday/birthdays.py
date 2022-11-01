from datetime import date
import os

import pandas as pd
from prettytable import PrettyTable, SINGLE_BORDER


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

    df['Birthday'] = pd.to_datetime(df['Birthdate'].apply(_next_birthday))
    df['Countdown'] = df['Birthday'] - pd.to_datetime(date.today())

    return df


def save(df: pd.DataFrame, file: str = None) -> None:
    filepath = _get_filepath(file)
    directory, file = os.path.split(filepath)

    df.dropna(subset=['Name', 'Birthdate'], inplace=True)
    df.drop_duplicates(subset=['Name', 'Birthdate'], inplace=True)

    os.makedirs(directory, exist_ok=True)
    df.to_csv(filepath, columns=['Name', 'Birthdate'], index_label='ID')


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


def order(df: pd.DataFrame, how: str = 'chronologically') -> pd.DataFrame:
    if 'alphabetically'.startswith(how):
        return df.sort_values(['Name', 'Countdown'])
    elif 'chronologically'.startswith(how):
        return df.sort_values(['Countdown', 'Name'])
    else:
        return df


def list_(df: pd.DataFrame, how: str = 'chronologically') -> None:
    df = order(df, how)
    df['Birthdate'] = df['Birthdate'].apply(lambda x: x.strftime('%d/%m/%Y'))
    df['Countdown'] = df['Countdown'].apply(lambda x: f'{x.days} days')

    x = PrettyTable()
    x.set_style(SINGLE_BORDER)

    x.add_column('ID', df.index.to_list())
    x.add_column('Name', df['Name'].to_list())
    x.add_column('Birthdate', df['Birthdate'].to_list())
    x.add_column('Countdown', df['Countdown'].to_list())

    x.align['ID'] = 'r'
    x.align['Name'] = 'l'
    x.align['Birthdate'] = 'l'
    x.align['Countdown'] = 'r'

    print(x)


def today(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['Birthday'] == pd.to_datetime(date.today())]
