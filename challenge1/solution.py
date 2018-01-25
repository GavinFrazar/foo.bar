def answer(s):
  # your code here
  
  if len(s) == 0:
    return 0
  ans = 1 #default answer
  for k in range(1,int(len(s)/2 + 1)):
    if len(s) % k == 0:
      smallest_pattern = s[0:k]
      comp_str = smallest_pattern * int(len(s)/k)
      if comp_str == s:
        ans = int(len(s)/k)
        break
  return ans
str = "ababab"
print(answer(str))