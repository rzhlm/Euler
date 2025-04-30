def tonelli_shanks(n, p):
    assert pow(n, (p-1)//2, p) == 1, "n is not a square (mod p)"
    if p % 4 == 3:
        x = pow(n, (p+1)//4, p)
        return x
    # Find Q and S such that p-1 = Q*2^S with Q odd
    Q, S = p - 1, 0
    while Q % 2 == 0:
        Q //= 2
        S += 1
    # Find a quadratic non-residue z
    for z in range(2, p):
        if pow(z, (p-1)//2, p) == p - 1:
            break
    c = pow(z, Q, p)
    x = pow(n, (Q+1)//2, p)
    t = pow(n, Q, p)
    m = S
    while t != 1:
        temp = t
        for i in range(1, m):
            temp = pow(temp, 2, p)
            if temp == 1:
                break
        b = pow(c, 2**(m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = pow(b, 2, p)
        m = i
    return x

def get_smallest_root(q):
    p = 2 ** q - 1
    x = tonelli_shanks(q, p)
    x2 = p - x
    return min(x, x2)

# Example usage:
#q = 5
q = 74_207_281
ans = get_smallest_root(q)
print(ans)
# To get mod 10**9+7:
print(ans % (10**9 + 7))
