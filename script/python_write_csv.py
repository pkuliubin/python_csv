#!/usr/bin env python
# encoding:utf8

"""
python write csv file
Author: lbin1988@hotmail.com
Date: 2017-03-02
"""

import os
import os.path
import csv
import codecs
import random


def generate_test_data():
    """ docstring for generate_test_data"""
    test_data = []
    for i in range(0, 100):
        t_data = {
            'name': '姓名_{}'.format(random.randint(0, 100)),
            'age': '{}'.format(random.randint(0, 100)),
            'address': '地址_{}'.format(random.randint(0, 100))
        }
        test_data.append(t_data)
    headers = ['name', 'age', 'address']
    return headers, test_data

def write_csv_file():
    """ docstring for write_csv_file"""
    headers, test_data = generate_test_data()
    outfile = './test_data/test.csv'
    file_obj = open(outfile, 'w')
    file_obj.write(codecs.BOM_UTF8)
    writer = csv.writer(file_obj)
    writer.writerow(headers)
    for t_data in test_data:
        tlist = [t_data[key] for key in headers]
        writer.writerow(tlist)

def process():
    write_csv_file()


if __name__ == '__main__':
    process()
