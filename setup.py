from setuptools import setup

setup(
    name='bday',
    description="Keep track of your loved ones' birthdays",
    author='Kyllian Asselin de Beauville',
    author_email='kyllianasselindebeauville@gmail.com',
    url='https://github.com/kyllianasselindebeauville/bday',
    packages=['bday'],
    license='MIT',
    install_requires=[
        'pandas>=1.5.1',
    ],
    python_requires='>=3.7',
)
