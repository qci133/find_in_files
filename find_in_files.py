#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import re
import shutil


def is_in(f_path, regex_pattern):
    with open(f_path, 'rb') as h:
        content = h.read()
        if regex_pattern.search(content) is not None:
            return True
    return False


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print 'invalid usage.'
        print 'usage: python', sys.argv[0], 'src_dir', 'out_dir'
        sys.exit(-1)
    src_dir = sys.argv[1]
    out_dir = sys.argv[2]
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    # regex = re.compile(r'(?:\s4.*?\s1|\s1.*?\s4)', re.M | re.S)
    # regex = re.compile('JNI', re.M | re.S)
    # regex = re.compile('native', re.M | re.S)
    # regex = re.compile('4129', re.M | re.S)
    #regex = re.compile('81', re.M | re.S)
    regex = re.compile('mstshash', re.M | re.I | re.S)
    # regex = re.compile(r'(?:\^|<<|>>|~)', re.M | re.S)
    # regex = re.compile(r'(?:<<|>>)', re.M | re.S)      # ~和^出现较多，因此只使用移位
    num = 0
    needed_num = 0
    for dir_path, _, file_names in os.walk(src_dir):
        for file_name in file_names:
            file_path = os.path.join(dir_path, file_name)
            num += 1
            if is_in(file_path, regex):
                # save this file
                rel_file_path = os.path.relpath(file_path, src_dir)
                new_rel_file_path = rel_file_path.replace(os.path.sep, '_')
                new_file_path = os.path.join(out_dir, new_rel_file_path)
                shutil.copy(file_path, new_file_path)
                needed_num += 1
                print 'Found file-', needed_num

