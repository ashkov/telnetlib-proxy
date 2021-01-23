
telnetlib with SOCKS proxy support
==================================

This is a python package that adds socks proxy support to `telnetlib` using PySocks.

It includes a telnet client that you can use via `telnet5` command that uses
SOCKS4, SOCKS5 or HTTP proxy set via telnet_proxy environment variable.

Installation:

    pip install telnetlib_proxy

Usage:

    export telnet_proxy=socks5://host:port

    telnet5 [-d] .. host port

    # press Ctrl-C to close the connection
