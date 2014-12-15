#!/usr/bin/env python
import ftp
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='ftp',
    description='python mini ftp',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='ftp',
    version=ftp.__version__,
    author=ftp.__author__,
    author_email=ftp.__author_email__,
    maintainer=ftp.__maintainer__,
    maintainer_email=ftp.__maintainer_email__,
    url=ftp.__url__,
    license='MIT',
    packages=['ftp'],
    entry_points={
        'console_scripts': [
            'pyftp = ftp.ftp:main',
        ]
    },
    install_requires=[],
)


print "\n###################\n# command - pyftp #\n###################\n"