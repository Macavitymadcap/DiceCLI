from setuptools import setup


setup(
    name='yourscript',
    version='0.1.0',
    py_modules=['dice', 'commands'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'commands = commands:cli',
        ],
    },
)