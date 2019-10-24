from setuptools import setup, find_packages

setup(
    name='wtf-ftw',
    version='1.2',
    install_requires=[],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    url='https://github.com/wtf-ftw/wtf-ftw',
    description='Hello world',
)
