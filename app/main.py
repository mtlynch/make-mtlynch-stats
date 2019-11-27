#!/usr/bin/env python3

import argparse
import logging

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
    logger.info('Started runnning')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Generate mtlynch Stats',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    main(parser.parse_args())
