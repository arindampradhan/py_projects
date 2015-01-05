#!/usr/bin/env python
import weather
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup



setup(
    name='weather',
    description='simple weather using http://ip-api.com/docs/api:json',
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],

    keywords='weather',
    version=weather.__version__,
    author=weather.__author__,
    author_email=weather.__author_email__,
    maintainer=weather.__maintainer__,
    maintainer_email=weather.__maintainer_email__,
    url=weather.__url__,
    license='MIT',
    packages=['weather'],
    entry_points={
        'console_scripts': [
            'weather = weather.weather:main',
        ]
    },
    install_requires=['requests','docopt'],
)


print "\n######################\n# command - weather #\n######################\n"