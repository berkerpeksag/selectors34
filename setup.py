# coding: utf-8

import io

from setuptools import setup

with io.open('README.rst', encoding='utf-8') as fobj:
    long_description = fobj.read()

with io.open('CHANGELOG.rst', encoding='utf-8') as fobj:
    long_description += '\n\n' + fobj.read()

setup(
    name='selectors34',
    version='1.1',
    description='Backport of the selectors module from Python 3.4.',
    long_description=long_description,
    author='Charles-François Natali',
    author_email='c.f.natali@gmail.com',
    maintainer='Berker Peksag',
    maintainer_email='berker.peksag@gmail.com',
    license='Python Software Foundation License',
    url='https://github.com/berkerpeksag/selectors34',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'License :: OSI Approved :: Python Software Foundation License',
    ],
    zip_safe=False,
    py_modules=['selectors34'],
    include_package_data=True,
    install_requires=['six'],
)
