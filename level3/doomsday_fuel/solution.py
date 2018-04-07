"""
Credit to PatrickJMT for his amazing math tutorials, specifically on Absorbing Markov Chains.
==============================================================================================

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

def toFractionMat(M):
    return [[Frac(n) for n in row] for row in M]

def calcProbMat(M):
    return [[Frac(n.numerator, sum([r.numerator for r in row])) if sum([r.numerator for r in row]) > 0 else Frac(0) for n in row] for row in M]

def gcd(a,b):
    if b:
        return gcd(b,a % b)
    else:
        return a

def lcm(a,b):
    return abs(a*b)//gcd(a,b)
    
# Return the relevant paritions of matrix M, which are Q and R, and key keeping track of what rows are mapped to in M
def partitionMatrix(M):
    #-- TODO -- rotate results
    nonterminals = []
    terminals = []
    for i in range(len(M)):
        if sum(M[i]) > 0: #non terminal state detected
            nonterminals.append(i)
        else:
            terminals.append(i)

    q_key = {}
    for row in nonterminals:
        q_key[row] = [col for col in nonterminals]
    
    r_key = {}
    for row in nonterminals:
        r_key[row] = [col for col in terminals]
    
    Q = [[M[i][j] for j in q_key[i]] for i in q_key]
    R = [[M[i][j] for j in r_key[i]] for i in q_key]
    ##############-MIGHT NEED TO DECODE LATER-################
    # key = {}
    # x = terminals
    # for i in range(len(x)):
    #     key[i] = x[i]
    #########################################################
    return Q, R, terminals

def calcN(Q):
    Q = [[-num for num in row] for row in Q]
    for i in range(len(Q)):
        Q[i][i] += 1
    return Q

# solve N*P = R
def solveMatEquation(N, R):
    # make system of equations Ax = b where x is a column vector of the serialized unknowns in P,
    # b is the column vector of serialized values in R
    # init A
    A = [[0 for _ in range(len(N)**2)] for _ in range(len(N)**2)]
    for i in range(len(N)):
        for j in range(len(N)):
            row = i*len(N)
            col = j*len(N)
            for k in range(len(N)):
                A[row+k][col+k] = N[i][j]
    b = [num for row in R for num in row]

    # solve system of equations
    # -- TODO -- last thing left is to put the augmented matrix into reduced row echelon form
    
    # store solution in P
    cols = len(R[0])
    P = [b[row:row+cols] for row in range(0,len(b),cols)]
    return P

# Multiply two matrices
def mulMats(A, B):
  return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def answer(m):
    # calculate number of transient states
    m = toFractionMat(m)
    m = calcProbMat(m)
    Q, R, terminals = partitionMatrix(m)
    if 0 in terminals:
        return [0 for _ in range(len(terminals))] + [1]

    N = calcN(Q)
    P = solveMatEquation(N,R)
    # common_denom = 1
    # for num in P[0]:
    #     common_denom = lcm(common_denom,num.denominator)
    # encoded_ans = [num.numerator*(common_denom//num.denominator) for num in P[0]] + [common_denom]
    return P

# -- test cases --
m = [
[0,3,3,4],
[0,0,0,0],
[0,0,0,0],
[8,1,1,0]
]

ans = answer(m)
print(ans)
#print(answer(m))
# wanted = [0,3,2,9,14]
# print(answer(m))
# print(wanted)