nums = {}
def fib1(n):
    if n <= 2:
        return 1
    if n in nums:
        return nums[n]
    else: 
      num = fib1(n-1) + fib1(n-2)
      nums[n] = num
      return num

