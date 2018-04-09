# Description
* Given a list l of positive integers, define a 'lucky triple' as a 3-tuple (l_i, l_j, l_k),
where l_i divides l<sub>j</sub>, l<sub>j</sub> divides l<sub>k</sub>,
and i < j < k. Return the number of such tuples in l.

# Constraints
* 2 <= len(l) <= 2000
* 0 < n < 1000000 for all n in l

# Input: 
* A list l

# Output:
* Number of 'lucky triples'

# Example:
* Input: [1,2,3,4,5,6]
* Output: 3
* Since (1,2,4), (1,2,6), and (1,3,6) are 'lucky triples'
