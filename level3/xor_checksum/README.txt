The challenge was:
We need to find the XOR of integer ID numbers for the following:

Given two integers, (start,length), start is the starting ID and length is the number of consecutive numbers per "line"
For each line, find the XOR of each ID up until length - skips, until we have skipped all of the numbers on a "line" (skips == length)
i.e.:
Input:
start = 0
length = 3

0 1 2
3 4
6
checksum = 0 XOR 1 XOR 2 XOR 3 XOR 4 XOR 6
Output: 2
---------------------------------------------
Input:
start = 17
length = 4

17 18 19 20
21 22 23
25 26
29
checksum = 17 XOR 18 XOR 19 XOR 20 XOR 21 XOR 22 XOR 23 XOR 25 XOR 26 XOR 29
Output = 14
