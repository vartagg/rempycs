# -*- coding: utf-8 -*-
"""
Simple utility for removing all .pyc files having .py analogs
from current place by walking on all subdirectories.

WARNING: Use it at your own risk.
"""
import os


class UnableToRemovePyc(Exception):
    pass


def main():
    for root, dirs, files in os.walk('.'):
        if root.startswith('./.'):
            # Ignore `hidden` files
            continue
        pyc_files = filter(lambda filename: filename.endswith('.pyc'), files)
        py_files = filter(lambda filename: filename.endswith('.py'), files)

        # Filtering for only those .pyc files that have .py analogs (which are probably more fresh versions of sources)
        excess_pyc_files = filter(lambda pyc_filename: pyc_filename[:-1] in py_files, pyc_files)

        for excess_pyc_file in excess_pyc_files:
            full_path = os.path.abspath(os.path.join(root, excess_pyc_file))
            try:
                os.remove(full_path)
            except OSError:
                raise UnableToRemovePyc('Unable to remove .pyc file {0}'.format(full_path))


if __name__ == '__main__':
    main()
