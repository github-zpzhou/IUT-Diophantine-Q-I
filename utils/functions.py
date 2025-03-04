from .basic import *

def list_of_f1(n):
    # the list [0,0,f1(2), ..., f(n)]
    # sieve for prime numbers <= n
    sieve = [True] * (n+10)
    sieve[0] = False
    sieve[1] = False
    for p in trange(2, n+1):
        if (sieve[p]):
            for i in range(2*p, n+1, p):
                sieve[i] = False
    # list of related functions
    n0 = int(sqrt(n)+1) 
    list_of_prime_counting = [0] * (n0 + 1)
    list_of_prime1_sum = [0] * (n0 + 1)
    tmp_prime_counting = 0
    tmp_prime1_sum = 0
    for x in range(n0+1):
        if (sieve[x]):
            tmp_prime_counting += 1
            tmp_prime1_sum += log(x-1)
        list_of_prime_counting[x] = tmp_prime_counting
        list_of_prime1_sum[x] = tmp_prime1_sum
    # compute the values of $f1$
    res = [0] * (n+1)
    sum1, sum2, sum3 = 0, 0, 0
    for x in trange(2,n+1):
        if (sieve[x]):
            p = x
            sum1 += log(p) / (p-1)
            sum2 += log(p)
            sum3 += log(p) * p
        x0 = int(sqrt(x)+1) - int(x == pow(int(sqrt(x)),2) )
        sum4 = list_of_prime_counting[x0] * log(x) - list_of_prime1_sum[x0]
        res[x] = sum1 + (1+1/x)*sum2 - sum3/x + sum4
    return res

def list_of_f2(n):
    # the list [0,0,0,0,f2(4), ..., f2(n)]
    list_of_f1_n = list_of_f1(3*n)
    tmp = 0
    res = [0] * (n+1)
    for x1,f1 in zip(trange(3*n+1), list_of_f1_n):
        if x1%3 != 0 or x1 < 12:
            continue
        x = x1 // 3
        tmp = f1 + 10 / 3 * log(x) + 9
        tmp *= (x*x+5*x) / (x*x+x-12)
        res[x] = tmp
    return res