

def main():
    # (x² - q) % p == 0
    q = 74_207_281
    p_b = q*[True]


def find_X_square(q, target_mod):
    mersenne = (1 << q) - 1
    for X in range(1, target_mod):
        X_square = pow(X, 2, mersenne)
        if (X_square - q) % mersenne == 0:
            return X
    return None

def do():
    q = 74_207_281
    target_mod = (1 << q) - 1
    result = find_X_square(q, target_mod)
    print(f"Valid X: {result}")


do()
