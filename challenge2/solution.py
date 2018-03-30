def answer(l,t):
    start = 0
    end = 0
    subtotal = 0
    while (end < len(l)):
        subtotal = subtotal + l[end]
        if subtotal > t:
            subtotal = subtotal - l[start]
            start = start + 1
            while(subtotal > t and end > start):
                subtotal = subtotal - l[end]
                end = end - 1

        if (subtotal == t):
            return [start, end]
        end = end + 1
    return [-1,1]

l = [1,2,3,4]
t = 15
assert(answer(l,t) == [-1,1])

l = [4,3,10,2,8]
t = 12
assert(answer(l,t) == [2, 3])

l = [100, 1, 2]
t = 3
assert(answer(l,t) == [1,2])