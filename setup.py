from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='telnetlib_proxy',
    version='0.3',

    # descriptions
    description='Python telnetlib with SOCKS proxy support',
    long_description=long_description,
    long_description_content_type='text/markdown',

    # author details
    author='Dave Wapstra',
    author_email='dwapstra@cisco.com',

    url='https://github.com/dwapstra/telnetlib-proxy/',

    # project licensing
    license='Apache 2.0',

    # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=['telnetlib_proxy'],

    # project directory
    package_dir={
        '': 'src',
    },

    # package dependencies
    install_requires=['pysocks'],

    # console entry point
    entry_points={'console_scripts': ['telnet5 = telnetlib_proxy:main']},
)
