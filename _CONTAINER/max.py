#!/usr/bin/python
# -*- coding: utf-8 -*-

# Finds the maximum number
# in un-sorted data

# Sudo Algo:
# Iterate through data
# each time a number(say k) greater than, previous
# consideration(say p) is found, replace previous
# consideration(p) with that greater number(k)
# By this way,
# 	At last we get the maximum number from data


def max_(seq):
    max_n = seq[0]
    for item in seq[1:]:
        if item > max_n:
            max_n = item
    return max_n


# Test
# Add your tests too!
tests = [
    [9017289, 782367, 736812903, 9367821, 71256716278, 676215, 2398, 0, 1],
    [19208, 9239, 4376, 738, 78, 51, 5, 6, 12, 78, 123, 65765, 1999999999],
    [1, 2, 4, 7, 9],
]

# checking our functions results
# with python's built-in max() function
for test_i in range(len(tests)):
    m = max_(tests[test_i])
    if m == max(tests[test_i]):
        print("Max number in array({}) -> ".format(test_i + 1) + str(m))
    else:
        print("Oops! Someting went wrong!")
