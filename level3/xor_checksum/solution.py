"""
The key to this problem is to recognize the pattern that
(4n XOR 4n+1 XOR 4n+2 XOR 4n+3) = 0, and the fact that
0 XOR n = n. It is therefore only necessary to XOR the first few ids
until we reach a multiple of 4, and then skip to the end of the line and
XOR a few ids until we reach another multiple of 4.

Checked IDs at line's start may be as far from a multiple of 4 as 3, (4n - 3).
Checked IDs near line's end may be as far from a multiple of 4 as  2, (4m + 2).
Therefore we have to XOR as many as 3 IDs from the start of the line,
and 3 IDs from the end of the line (since we have to XOR 4m, 4m+1, 4m+2), for
a worst case of 6 XOR operations per line. If there are k lines, then this
algorithm's time complexity is O(6k) == O(k), so it is linear in time.
Without skipping multiples of 4, it would take quadratic time.
"""

def answer(start, length):
    checksum = 0
    id = start
    
    # skip counts the number of IDs we skip at the line end
    for skip in range(length):
        # Keep track of where we started for this line
        start = id

        # Number of of IDs we have to check
        checks = length - skip

        # XOR line's starting IDs until we reach a
        # multiple of 4
        while (id % 4 != 0):
            checksum = checksum ^ id
            id = id + 1
        
        # Skip to one past the end of the checked IDs
        id = start + checks
        
        # XOR the necessary remaining checked IDs
        while (id % 4 != 0):
            id = id - 1
            checksum = checksum ^ id
        
        # Advance id for the next line
        id = start + length
    return checksum