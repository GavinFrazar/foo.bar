def changeBase(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and "0") or (changeBase(num // b, b, numerals).lstrip("0") + numerals[num % b])
    
def answer(n, b):
    visited = {}
    z = str(n)
    k = len(z)
    count = 1
    
    while True:
        visited[z] = count
        count += 1
        
        # y is z in ascending order of digits
        y = "".join([digit for digit in sorted(z)])

        # x is in descending order (reverse of y)
        x = y[::-1]

        # convert strings to ints in base b
        x = int(x,b)
        y = int(y,b)

        # set z as a string representation of the difference of x and y in base b
        z = str(changeBase(x - y, b))

        # pad leading zeros to maintain string length k
        if len(z) < k:
            z =  (k-len(z))*'0' + z

        # check if we've been here before
        if z in visited:
            return count - visited[z]

# -- Test cases --
ans = answer(210022,3)
assert(ans == 3)

ans = answer(1211,10)
assert(ans == 1)