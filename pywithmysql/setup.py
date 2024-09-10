from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pywithmysql',
    version='0.1.0',
    description='The library to work with mysql for python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='DanikBlatota777',
    author_email='danylo29bro@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pymysql',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
