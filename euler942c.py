from multiprocessing import Pool


def check_candidate(X, mersenne, q):
    X_square = mod(X, 2, mersenne)
    return (X_square - q) % mersenne == 0


def find_X_in_range(args):
    try:
        start, end, mersenne, q = args
        for X in range(start, end):
            if check_candidate(X, mersenne, q):
                return X
        return None
    except Exception as e:
        print("Error", e)
        return None


def parallel_search(q, num_processes=4):
    mersenne = (1 << q) - 1
    search_range = 1 << 23
    step = search_range // num_processes

    ranges = [(i * step, (i + 1) * step, mersenne, q) for i in range(num_processes)]

    with Pool(num_processes) as pool:
        results = pool.map(find_X_in_range, ranges)

    for result in results:
        if result is not None:
            return result
    return None


if __name__ == "__main__":
    from multiprocessing import freeze_support
    freeze_support()

    q = 74_207_281
    result = parallel_search(q)
    print(f"X: {result}")
    
