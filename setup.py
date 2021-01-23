from setuptools import setup

setup(
    name='telnetlib_proxy',
    version='0.1',

    # descriptions
    description='Python telnetlib with SOCKS proxy support',

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
