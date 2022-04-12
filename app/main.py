#!/usr/bin/env python3

import argparse
import logging
import sys

import csv_to_yaml
import csv_to_markdown_table


logger = logging.getLogger(__name__)


def configure_logging():
    root_logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s %(name)-15s %(levelname)-4s %(message)s',
        '%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)
    root_logger.setLevel(logging.INFO)


def main(args):
    configure_logging()
    logger.info('Started stats for %s', args.project)
    if not args.to_yaml:
        print(csv_to_markdown_table.convert(sys.stdin, args.offset))
    else:
        print(csv_to_yaml.convert(args.project, sys.stdin))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Generate mtlynch Stats',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--project', type=str, required=True)
    parser.add_argument('--offset', default=-1, type=int)
    parser.add_argument('--to-yaml', action='store_true')
    main(parser.parse_args())
