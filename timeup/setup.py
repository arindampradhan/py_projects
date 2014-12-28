#!/usr/bin/env python
import timeup
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='timeup',
    description='timeup',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='timeup',
    version=timeup.__version__,
    author=timeup.__author__,
    author_email=timeup.__author_email__,
    maintainer=timeup.__maintainer__,
    maintainer_email=timeup.__maintainer_email__,
    url=timeup.__url__,
    license='MIT',
    packages=['timeup'],
    entry_points={
        'console_scripts': [
            'timeup = timeup.timeup:main',
        ]
    },
    install_requires=[],
)


print "\n######################\n# command - timeup #\n######################\n"