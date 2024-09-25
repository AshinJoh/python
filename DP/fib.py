def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
# HELLO GITHUB
print(fib(4))