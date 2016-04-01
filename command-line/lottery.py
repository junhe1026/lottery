# -*- coding: utf-8 -*-
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'integers', metavar='int', nargs='+', type=int,
        help='an integer to be summed')

if __name__ == '__main__':
    print 2