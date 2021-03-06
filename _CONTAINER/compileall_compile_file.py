# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""

# end_pymotw_header
import compileall
import glob


def show(title):
    print(title)
    for filename in glob.glob("examples/**", recursive=True):
        print("  {}".format(filename))
    print()


show("Before")

compileall.compile_file("examples/a.py")

show("\nAfter")
