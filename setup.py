import os
import re

from setuptools import setup


def read(file_path):
    return open(file_path, 'r').read()


try:
    init_file_contents = read(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'invoca', '__init__.py'))
    version = re.findall(r"^__version__ = '(.*)'\r?$",
                         init_file_contents, re.M)[0]
except IndexError:
    raise RuntimeError('Unable to determine version.')

setup(
    name="invoca",
    author="David Jenkins",
    author_email="djenkins@boldmediagroup.com",
    packages=['invoca'],
    include_package_data=True,
    install_requires=['requests'],
    tests_require=['pytest', 'pytest-watch'],
    version=version,
    description='Invoca Python3 Library',
    long_description=read('README.md'),
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows'
    ],
    keywords='invoca',
    license='',
    url=''
)
