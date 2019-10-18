#!/usr/bin/env python


import argparse
import os.path

import murkle


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('--port', default=8000)
    parser.add_argument('--host', default='localhost')
    parser.add_argument('html_file')
    parser.add_argument('csv_file')
    args = parser.parse_args()

    ms = murkle.MurkleServer(
        args.host,
        args.port,
        os.path.realpath(args.html_file),
        os.path.realpath(args.csv_file))
    ms.serve()


if __name__ == '__main__':
    main()
