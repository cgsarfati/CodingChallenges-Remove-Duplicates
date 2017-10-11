"""
Test cases:

    >>> deduped([])
    []

    >>> deduped([1, 1, 1])
    [1]

    >>> deduped([1, 2, 1, 1, 3])
    [1, 2, 3]

    >>> deduped([1, 2, 3])
    [1, 2, 3]

"""


def deduped(items):
    """Return new list from items with duplicates removed."""

    # initialize empty lst to be added over time (final result)
    # initialize empty set to be added over time, then transferred to lst

    # list(set(items)) won't work because set unordered; problem needs to
    # maintain order

    remove_dup = set()

    result = []

    for item in items:
        if item not in remove_dup:
            result.append(item)
            remove_dup.add(item)

    return result

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"
