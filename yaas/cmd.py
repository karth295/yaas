# coding: utf-8

import argparse
import inspect
import sys
import os

from . import __version__
from . import config

YAAS_VERSION = "yaas version {0}".format(__version__)

def version(parser, args):
    """print the yaas version"""
    print YAAS_VERSION

def hello(parser, args):
    """show an elephant"""
    print "                .-.._       "
    print "          __  /`     '.     "
    print "       .-'  `/   (   a \    "
    print "      /      (    \,_   \   "
    print "     /|       '---` |\ =|   "
    print "    ` \    /__.-/  /  | |   "
    print "       |  / / \ \  \   \_\  "
    print "       |__|_|  |_|__\       "

def main():
    config.server_url = os.environ.get('YAAS_SERVER_URL', config.server_url)
    config.username = os.environ.get('YAAS_USER', config.username)
    config.password = os.environ.get('YAAS_PASSWORD', config.password)

    parser = argparse.ArgumentParser(prog="yaas")

    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version=YAAS_VERSION,
        help="print the yaas version")

    subparsers = parser.add_subparsers(dest="command")

    commands = {
        'version' : version,
        'hello' : hello
        }

    for name, fn in commands.iteritems():
        subparsers.add_parser(name, help=inspect.getdoc(fn))

    args, extra = parser.parse_known_args(sys.argv[1:])

    commands[args.command](subparsers.choices[args.command], extra)

