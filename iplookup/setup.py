#!/usr/bin/env python
import iplookup
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='iplookup',
    description='simple iplookup using http://ip-api.com/docs/api:json',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='iplookup',
    version=iplookup.__version__,
    author=iplookup.__author__,
    author_email=iplookup.__author_email__,
    maintainer=iplookup.__maintainer__,
    maintainer_email=iplookup.__maintainer_email__,
    url=iplookup.__url__,
    license='MIT',
    packages=['iplookup','docopt'],
    entry_points={
        'console_scripts': [
            'iplookup = iplookup.iplookup:main',
        ]
    },
    install_requires=['requests'],
)


print "\n######################\n# command - iplookup #\n######################\n"