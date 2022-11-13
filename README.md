# Bday

Bday is a birthday tracker with a CLI.

## Requirements

Make sure you have [Python 3.7+](https://www.python.org/downloads/) with [pip](https://pip.pypa.io/en/stable/installation/) installed.

```shell
python3 --version && python3 -m pip --version
```

> You may need to use `python` instead of `python3` depending on your environment.

## Installation

- Use the package manager `pip` to install `bday`.

```shell
python3 -m pip install git+https://github.com/kyllianasselindebeauville/bday.git
```

## Usage

```
usage: bday [-h] {add,rm,ls} ...

Track your birthdays.

options:
  -h, --help   show this help message and exit

commands:
  {add,rm,ls}
    add        add a birthday
    rm         remove a birthday
    ls         list birthdays
```

## Examples

- Add a birthday.

```shell
bday add epoch 01-01-1970
```

- Remove a birthday.

```shell
bday rm 42
```

> Replace `42` with the id of the birthday you want to remove.

- List today's birthdays *(default behavior)*.

```shell
bday
```

- List all birthdays.

```shell
bday ls
```

> | ID | Name  | Birthdate  | Age | Countdown |
> |---:|:------|:-----------|----:|----------:|
> |  0 | epoch | 01/01/1970 |  52 |   55 days |

## Contributing

Pull requests are welcome. Please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)
