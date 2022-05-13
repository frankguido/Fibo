dp = [-1 for i in range(5000)]
 
def fib(n):
    if (n <= 1):
        return n;
    global dp;

    first = 0;
    second = 0;
 
    if (dp[n - 1] != -1):
        first = dp[n - 1];
    else:
        first = fib(n - 1);
    if (dp[n - 2] != -1):
        second = dp[n - 2];
    else:
        second = fib(n - 2);
    dp[n] = first + second;
 
    # Memorizacion
    return dp[n] ;
 

if __name__ == '__main__':
    n = 33;
    print(fib(n));