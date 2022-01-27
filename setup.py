"""Setup configuration for the command line interface."""

from setuptools import setup


setup(
    name='dice',
    version='0.1.0',
    py_modules=['dice'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'dice = dice:cli',
        ],
    },
)