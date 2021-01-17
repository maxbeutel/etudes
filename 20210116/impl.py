# Substring 1: Length of the longest common substrings of two strings.

from typing import Iterable

tests = [
    ('ABC', 'XYZ', 0),
    ('abcdxyz', 'xyzabcd', 4),
    ('zxabcdezy', 'yzabcdezx', 6),
]

def longest_common_substr(A:str, B:str)-> int:
    T = dict()

    for i, a in enumerate(A):
        for j, b in enumerate(B):
            key = (i, j)

            if a == b:
                T[key] = T.get((i-1, j-1), 0) + 1
            else:
                T[key] = 0

    return max(T.values()) if len(T) > 0 else 0

for strA, strB, expected in tests:
    assert longest_common_substr(strA, strB) == expected

# * Subsequences 1: Length of the longest common subsequence of two strings.

tests = [
    ('ABC', 'XYZ', 0),
    ('BLUES', 'CLUES', 4),
    ('ABCDGH', 'AEDFHR', 3),
]

def longest_common_subseq(A:str, B:str)-> int:
    T = {}

    for i, a in enumerate(A):
        for j, b in enumerate(B):
            key = (i, j)

            if a == b:
                T[key] = T.get((i-1, j-1), 0) + 1
            else:
                T[key] = max(T.get((i-1, j), 0), T.get((i, j-1), 0))

    return T[(len(A)-1, len(B)-1)]

for strA, strB, expected in tests:
    assert longest_common_subseq(strA, strB) == expected

# * Binary Search: Find if $n$ is in a sorted array of integers in log steps

tests = [
    ([0, 2, 4, 6, 8, 10, 12, 14, 16], 3, -1),
    ([0, 2, 4, 6, 8, 10, 12, 14, 16], 16, 8),
    ([0, 2, 4, 6, 8, 10, 12, 14, 16], 0, 0),
]

def _do_bin_search(lo:int, hi:int, needle:int, L:Iterable[int])-> int:
    if lo > hi:
        return -1

    mid = (lo+hi)//2

    if L[mid] > needle:
        return _do_bin_search(lo, mid-1, needle, L)
    elif L[mid] < needle:
        return _do_bin_search(mid+1, hi, needle, L)
    else:
        return mid

def bin_search(needle:int, L:Iterable[int])-> int:
    return _do_bin_search(0, len(L)-1, needle, L)

for L, n, expected in tests:
    assert bin_search(n, L) == expected

# * Permutations: Find all permutations of a given set.

tests = [
    ([], [[]]),
    ([1], [[1]]),
    ([1, 2], [[1, 2], [2, 1]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
]

def permutations(S):
    if len(S) == 0:
        return [[]]

    return [
        perm + [a]
        for a in S
        for perm in permutations(list(filter(lambda x: x != a, S)))
    ]

for S, expected in tests:
    assert str(sorted(permutations(S))) == str(sorted(expected))

# * Count Change: Count the number of ways to make change for 100 cent if you have [1, 5, 10, 25, 50] cent coins (SICP)

tests = [
    ([1, 5, 10, 25, 50], 100, 292),
]

def count_change(coins:Iterable[int], amount:int)->int:
    if len(coins) == 0:
        return 0

    if amount < 0:
        return 0

    if amount == 0:
        return 1

    return count_change(coins, amount - coins[0]) + count_change(coins[1:], amount)

for coins, amount, expected in tests:
    assert count_change(coins, amount) == expected
