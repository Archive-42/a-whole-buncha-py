#!/usr/bin/env python
"""
Solution to Project Euler Problem 44
http://projecteuler.net/

by Apalala <apalala@gmail.com>
(cc) Attribution-ShareAlike
http://creativecommons.org/licenses/by-sa/3.0/

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first
ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference,
70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
difference is pentagonal and D = |Pk − Pj| is minimised; what is the value
of D?
"""
from series import pentagonals, pentagonal, is_pentagonal


def pentagonal_sum_and_diff():
    for k in pentagonals():
        for d in pentagonals(upto=k):
            j = abs(k - d)
            if j > 0 and is_pentagonal(j) and is_pentagonal(j + k):
                return j, k


def test():
    assert is_pentagonal(pentagonal(4) + pentagonal(7))
    assert not is_pentagonal(pentagonal(70) + pentagonal(22))


def run():
    j, k = pentagonal_sum_and_diff()
    print(abs(j - k))


if __name__ == "__main__":
    test()
    run()
