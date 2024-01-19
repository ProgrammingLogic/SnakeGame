from setuptools import setup, find_packages

setup(
    name='SnakeGame',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    url='https://github.com/ProgrammingLogic/SnakeGame',
    license='MIT',
    author='Jonathyn Stiverson',
    description='A simple Snake game',
    install_requires=[
        'pygame',
    ],
    author_email='jstiverson2002@gmail.com',
    entry_points={
        'console_scripts': [
            'Application = src.main:main',
        ],
    },
)
