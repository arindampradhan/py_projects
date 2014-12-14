#!/usr/bin/env python
import linesofcode
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='linesofcode',
    version=linesofcode.__version__,
    description='Instant project status',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords='linesofcode py',
    author='Arindam Pradhan',
    author_email='arindampradhan@gmail.com',
    maintainer='Arindam Pradhan',
    maintainer_email='arindampradhan@gmail.com',
    url='https://github.com/arindampradhan/py_projects/linesofcode',
    license='MIT',
    packages=['linesofcode'],
    entry_points={
        'console_scripts': [
            'linesofcode = linesofcode.linesofcode:_build_scraper',
        ]
    },
    install_requires=[],
)
