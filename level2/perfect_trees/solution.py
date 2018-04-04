def isPowerOfTwo(n):
    return True if n is not 0 and (n&(n-1)==0) else False

def parentOf(h, num):
    if num == 2**h - 1:
        return -1
    tmp = num
    p = 2**(h-1)-1
    while True:
        if tmp > p:
            if tmp == 2*p:
                # num is a right child
                return num+1
            # search left tree neighbor
            tmp = tmp - p
        if isPowerOfTwo(tmp+1):
            # num is a left child
            return num + tmp + 1
        p = p//2

def answer(h, q):
    ans = [parentOf(h,num) for num in q]
    return ans

"""
       15
   7        14
 3   6    10   13
1 2 4 5  8 9 11 12

This algorithm determines the parent of an elem in h steps.
For a list of n elements, it will take O(h*n) == O(n), so linear time.
"""
# test case
h = 3
q = [7,3,5,1]
expected = [-1,7,6,3]
ans = answer(h,q)
print("answered ",ans)
try:
    assert(ans == expected)
except:
    print("expected ",expected)

h = 4
q = [n for n in range(1,2**h)]
expected = [3,3,7,6,6,7,15,10,10,14,13,13,14,15,-1]
answered = answer(h,q)
print(q)
print(answered)
for i in range(len(q)):
    ans = answered[i]
    exp = expected[i]
    try:
        assert(ans == exp)
    except:
        print("answered ",ans)
        print("expected ",exp)