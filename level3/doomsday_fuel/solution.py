"""
Thanks to PatrickJMT for his amazing math tutorials, specifically on Absorbing Markov Chains.
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

Things to consider:
    -Initial state could be a terminal state
    -Result will always be in the first row of P
    -Find a common denominator as the lcm of the denominators of the fractions
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
    
# Return the relevant paritions of matrix M, which are Q and R, and the terminal rows
def partitionMatrix(M):
    #-- TODO -- fix up notation here
    nt_rows = []
    t_rows = []
    for i in range(len(M)):
        if sum(M[i]) > 0: #indicates non terminal state
            nt_rows.append(i)
        else:
            t_rows.append(i)

    q_key = {}
    for row in nt_rows:
        q_key[row] = [col for col in nt_rows]
    
    r_key = {}
    for row in nt_rows:
        r_key[row] = [col for col in t_rows]
    
    Q = [[M[i][j] for j in q_key[i]] for i in q_key]
    R = [[M[i][j] for j in r_key[i]] for i in q_key]
    return Q, R, t_rows

def calcN(Q):
    Q = [[-num for num in row] for row in Q]
    for i in range(len(Q)):
        Q[i][i] += 1
    return Q

def createSystemOfEquations(N,R):
    rows = len(R)
    cols = len(R[0])
    A = [[0 for _ in range(rows*cols)] for i in range(rows*cols)]
    for i in range(len(N)):
        for j in range(len(N)):
            row = i*cols
            col = j*cols
            for k in range(len(R[i])):
                A[row+k][col+k] = N[i][j]
    return A

def solveSystem(A, b):
    for i in range(len(A)):
        pivot = A[i][i]
        for below in range(i+1, len(A)):
            factor = A[below][i] / pivot
            A[below] = [num1 - num2*factor for num1,num2 in zip(A[below], A[i])]
            b[below] -= b[i]*factor
        for above in range(i):
            factor = A[above][i] / pivot
            A[above] = [num1 - num2*factor for num1,num2 in zip(A[above], A[i])]
            b[above] -= b[i]*factor
        factor = 1 / pivot
        A[i] = [num*factor for num in A[i]]
        b[i] *= factor
    return b

# solve N*P = R
def solveMatEquation(N, R):
    # make system of equations Ax = b where x is a column vector of the serialized unknowns in P,
    # b is the column vector of serialized values in R
    # init A
    A = createSystemOfEquations(N,R)
    b = [num for row in R for num in row]
    x = solveSystem(A,b)

    # store solution in P
    cols = len(R[0])
    return [x[row:row+cols] for row in range(0,len(b),cols)]

def answer(m):
    # calculate number of transient states
    m = toFractionMat(m)
    m = calcProbMat(m)
    Q, R, t_rows = partitionMatrix(m)

    # Edge case where start state is terminal
    if 0 in t_rows:
        return [1] + [0 for _ in range(len(t_rows)-1)] + [1]

    N = calcN(Q)
    P = solveMatEquation(N,R)

    # P holds matrix of total probabilities of reaching terminal states
    common_denom = 1
    for num in P[0]:
        common_denom = lcm(common_denom,num.denominator)
    return [num.numerator*(common_denom//num.denominator) for num in P[0]] + [common_denom]
    
# -- test cases --
m1 = [
[0,1,0,0,0,1],
[4,0,0,3,2,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0]
]
ans = answer(m1)
assert(ans == [0,3,2,9,14])

m2 = [
    [0,2,1,0,0],
    [0,0,0,3,4],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
ans = answer(m2)
assert(ans == [7,6,8,21])