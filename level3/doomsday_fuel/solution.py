"""
First, recognize that this problem is describing an absorbing Markov chain.
Then, to determine the total probablity of transitioning into a terminal state, do the following:
1.) Paritition the matrix M =   | Q R |
                                | 0 I |
where:
    Q is the n*n probablity transition matrix for the probability of transitioning from a nonterminal state into another nonterminal state,
    R is the n*t probability transition matrix for the probability of transitioning from a nonterminal state into a terminal state
    0 is the t*n matrix of zeroes
    I is the t*t identity matrix
    n = # of nonterminal states
    t = # of terminal states
    k = n + t

2.) Calculate the matrix N = (I - Q)
3.) Solve the equation N*P = R for P
4.) The first row of P will give the probability of reaching each terminal state given that you start in state 0

The difficulty of this task is in two areas:
    1.) Maintaining the calculations in quotient form
    2.) Solving the equation in step 3

Things to consider:
    -Initial state could be a terminal state
    -Sort the terminal states
    -Result will always be in the first row of P
    -Find a common denominator as the lcm of the denominators of the fractions
    -Reduce fractions by computing gcd(num,denom)
"""

from fractions import Fraction as Frac
from decimal import Decimal as Dec

def gcd(a,b):
    pass

def lcm(a,b):
    pass
    
# Return the relevant paritions of matrix M, which are Q and R, and key keeping track of what rows are mapped to in M
def partitionMatrix(M):
    # -- TODO -- implement this
    Q = None
    R = None
    key = {}
    return [Q, R, key]

def calcN(Q):
    pass

def reduceFrac(num, denom):
    pass

# solve N*P = R
def reduceMat(N, R):
    pass

def mulMats(A, B):
    pass

def answer(m):
    pass

num = 1.1
d = Dec(str(num))
f = Frac(d)
print(f)
# -- test cases --
m = [
[0,1,0,0,0,1],
[4,0,0,3,2,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]
]

wanted = [0,3,2,9,14]
print(answer(m))
print(wanted)