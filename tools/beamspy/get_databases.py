#!/usr/bin/python
import os
import inspect
import csv


def get_databases():
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    path = os.path.join(os.path.dirname(os.path.abspath(filename)))
    with open(os.path.join(path, 'databases.txt')) as inp:
        records = []
        for line in inp.read().splitlines()[1:]:
            line = line.split("\t")
            records.append((line[0], line[1], False))
    return records
