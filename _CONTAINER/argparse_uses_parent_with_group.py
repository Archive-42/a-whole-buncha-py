# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Parent with shared options
"""

# end_pymotw_header
import argparse
import argparse_parent_with_group

parser = argparse.ArgumentParser(parents=[argparse_parent_with_group.parser])

parser.add_argument("--local-arg", action="store_true", default=False)

print(parser.parse_args())
