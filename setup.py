#!/usr/bin/env python
from os import path
from setuptools import setup, find_packages

from SK4Me import __version__, __author__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]

setup(
    name='SK4Me',
    version=__version__,
    description='Admin ui for scrapy spider service',
    long_description=
    'Go to https://github.com/jkzleond/SK4Me/ for more information.',
    author=__author__,
    author_email='jkzleond@163.com',
    maintainer="jkzleond",
    maintainer_email="jkzleond@163.com",
    url='https://github.com/jkzleond/SK4Me/',
    license='MIT',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,

    entry_points={
        'console_scripts': {
            'sk4me = SK4Me.run:main'
        },
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
)
