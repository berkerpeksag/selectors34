from setuptools import setup, find_packages

setup(
    name='selectors',
    version='1.0',

    description='Backport of the selectors module from Python 3.4.',
    author='Berker Peksag',
    author_email='berker.peksag@gmail.com',
    license='',
    url='https://github.com/berkerpeksag/selectors34',
    classifiers=[

    ],
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
)
